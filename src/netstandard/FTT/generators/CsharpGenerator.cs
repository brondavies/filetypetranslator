using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace FTT.generators
{
    public class CsharpGenerator : CodeGeneratorBase, ICodeGenerator
    {
        const string indent = "                ";
        StringBuilder format = new StringBuilder();

        public void GenerateFileStart()
        {
            format.Append(
            @"namespace FTTLib
{
    public sealed partial class FTT
    {
");
        }

        public void GenerateConstants(List<MimeType> mimetypes)
        {
            var list = new List<string>();
            foreach (var mimetype in mimetypes)
            {
                list.Add(GenerateConstantFor(mimetype.type));
                foreach (string ext in mimetype.extensions)
                {
                    list.Add(GenerateConstantFor(ext));
                }
            }
            var text = File.ReadAllText(@"..\..\..\..\netstandard\FTTLib\FTT.categories.cs");
            foreach(var pair in AllConstants)
            {
                text = text.Replace(string.Format("\"{0}\"", pair.Value), pair.Key);
            }
            File.WriteAllText(@"..\..\..\..\netstandard\FTTLib\FTT.categories.cs", text, Encoding.UTF8);
            foreach (var item in list.OrderBy(s => s))
            {
                format.AppendLine(item);
            }
        }

        public void GenerateBeginFunction()
        {
            format.Append(@"
        private static string GetMimeTypeInternal(string extension)
        {
            switch (extension)
            {
");
        }

        public void GenerateFunctionBody(MimeType mimeType)
        {
            if (!string.IsNullOrEmpty(mimeType.comment))
            {
                format.AppendLine(GenerateComment(mimeType.comment));
            }
            foreach (string extension in mimeType.extensions)
            {
                format.AppendLine(GenerateCase(extension));
            }
            format.AppendLine(GenerateReturn(GetConstantFor(mimeType.type)));
        }

        public void GenerateEndFunction()
        {
            format.Append(@"            }
            return """";
        }");
        }

        public void GenerateBeginFunction2()
        {
            format.Append(@"
        private static string[] GetMimeTypeFileExtensionsInternal(string mimeType)
        {
            switch(mimeType)
            {
");
        }

        public void GenerateFunctionBody2(MimeType mimeType)
        {
            format.AppendLine(GenerateCase(mimeType.type));
            string extensions = @"new string[] { ";
            string strings = string.Join("\", \"", mimeType.extensions);
            if (strings.Length > 0)
            {
                strings = quote(strings) + " ";
            }
            extensions += strings;
            extensions += "}";
            format.AppendLine(GenerateReturn(extensions));
        }

        public void GenerateEndFunction2()
        {
            format.Append(@"            }

            return new string[] { };
        }");
        }

        public void GenerateFileEnd()
        {
            format.Append(@"
    }
}");
        }

        public void Finish()
        {
            string generatedFile = Path.GetFullPath(@"..\..\..\FTTLib\FTT.generated.cs");
            File.WriteAllText(generatedFile, format.ToString());
        }

        static Dictionary<string, string> AllConstants = new Dictionary<string, string>();
        private static string GenerateConstantFor(string type)
        {
            string name = GetConstantFor(type);
            if (!AllConstants.ContainsKey(name)) AllConstants.Add(name, type);
            return string.Format("        const string {0} = \"{1}\";", name, type);
        }

        private static string GenerateReturn(string type)
        {
            return string.Format("{0}    return {1};", indent, type);
        }

        private static string GenerateComment(string comment)
        {
            return string.Format("{0}// {1}", indent, comment);
        }

        private static string GenerateCase(string extension)
        {
            return string.Format("{0}case {1}:", indent, GetConstantFor(extension));
        }
    }
}
