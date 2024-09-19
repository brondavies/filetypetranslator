using FTT.Properties;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace FTT.generators
{
    public class JavascriptGenerator : CodeGeneratorBase, ICodeGenerator
    {
        static string indent = "  ";
        string format = Resources.JavascriptClass;

        public void GenerateFileStart()
        {
            //no-op
        }

        public void GenerateConstants(List<MimeType> mimetypes)
        {
            StringBuilder result = new StringBuilder();
            var list = new List<string>();
            foreach (var mimetype in mimetypes)
            {
                list.Add(GenerateConstantFor(mimetype.type));
                foreach (string ext in mimetype.extensions)
                {
                    list.Add(GenerateConstantFor(ext));
                }
            }
            foreach(var item in list.OrderBy(s => s))
            {
                result.AppendLine(item);
            }

            foreach (var pair in AllConstants)
            {
                format = format.Replace(string.Format("'{0}'", pair.Value), pair.Key);
            }
            File.WriteAllText(@"..\..\..\..\netstandard\FTT\Properties\JavascriptClass.js", format, Encoding.UTF8);
            format = format.InsertAfter("//constants", result.ToString());
        }

        public void GenerateBeginFunction()
        {
            format = format.InsertBefore("//getMimeType body", $"{indent}switch(extension) {{");
            format = format.InsertAfter("//getMimeType body", $"{indent}}}");
        }

        public void GenerateFunctionBody(MimeType mimeType)
        {
            string value = "";
            if (!string.IsNullOrEmpty(mimeType.comment))
            {
                value = value.AppendLine(indent + GenerateComment(mimeType.comment));
            }
            
            foreach (string extension in mimeType.extensions)
            {
                value = value.AppendLine(GenerateCase(extension));
            }
            value = value.AppendLine(GenerateReturn(GetConstantFor(mimeType.type)));

            //value = value.AppendLine(GenerateCase(mimeType.extensions))
            //    .AppendLine(GenerateReturn(GetConstantFor(mimeType.type)));
            format = format.InsertAfter("//getMimeType body", value);
        }

        private string GenerateReturn(string value)
        {
            return $"{indent}{indent}return {value};";
        }

        public void GenerateEndFunction()
        {
            //no-op
        }

        public void GenerateBeginFunction2()
        {
            format = format.InsertBefore("//getMimeTypeFileExtensions body", $"{indent}switch(mimeType) {{");
            format = format.InsertAfter("//getMimeTypeFileExtensions body", $"{indent}}}");
        }

        public void GenerateFunctionBody2(MimeType mimeType)
        {
            string value = "";
            value = value.AppendLine(GenerateCase(GetConstantFor(mimeType.type)));
            string extensions = "[ ";
            string strings = string.Join(", ", mimeType.extensions.Select(e => GetConstantFor(e)));
            extensions += strings;
            extensions += " ]";
            value = value.AppendLine(GenerateReturn(extensions));

            format = format.InsertAfter("//getMimeTypeFileExtensions body", value);
        }

        public void GenerateEndFunction2()
        {
            //no-op
        }

        public void GenerateFileEnd()
        {
            //no-op
        }

        public void Finish()
        {
            string generatedFile = Path.GetFullPath(@"..\..\..\..\node\dist\FTT.js");
            File.WriteAllText(generatedFile, format.ToString());
        }

        #region Private Methods

        private string GenerateCase(string value)
        {
            return $"{indent}{indent}case {GetConstantFor(value)}:";
        }

        private string GenerateCase(IEnumerable<string> values, string variable = "extension")
        {
            var joined = string.Join(", ", values.Select(e => GetConstantFor(e)));
            if (values.Count() == 1)
            {
                return $"{indent}if ({variable} === {joined})";
            }
            return string.Format($"{indent}if ([{{0}}].includes({variable}))", joined);
        }

        private string GenerateComment(string comment)
        {
            return $"{indent}// {comment}";
        }

        static Dictionary<string, string> AllConstants = new Dictionary<string, string>();
        private static string GenerateConstantFor(string type)
        {
            string name = GetConstantFor(type);
            if (!AllConstants.ContainsKey(name)) AllConstants.Add(name, type);
            return $"const {name} = '{type}';";
        }
        
        #endregion
    }
}
