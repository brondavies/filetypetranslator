using FTT.Properties;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FTT.generators
{
    public class PythonGenerator : CodeGeneratorBase, ICodeGenerator
    {
        static string indent = "    ";
        string format = Resources.PythonClass;

        public void GenerateFileStart()
        {
            //no-op
        }

        public void GenerateConstants(List<MimeType> mimetypes)
        {
            StringBuilder result = new StringBuilder();
            foreach (var mimetype in mimetypes)
            {
                result.AppendLine(GenerateConstantFor(mimetype.type));
                foreach (string ext in mimetype.extensions)
                {
                    result.AppendLine(GenerateConstantFor(ext));
                }
            }
            format.Replace("# constants", result.ToString());
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
            string generatedFile = Path.GetFullPath(@"..\..\..\..\src\python\FTTLib\FTT.py");
            File.WriteAllText(generatedFile, format.ToString());
        }

        private static string GenerateConstantFor(string type)
        {
            string name = GetConstantFor(type);
            return $"{indent}{name} = \"{type}\"";
        }
    }
}
