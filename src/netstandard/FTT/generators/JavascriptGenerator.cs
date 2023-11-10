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
            foreach (var mimetype in mimetypes)
            {
                result.AppendLine(GenerateConstantFor(mimetype.type));
                foreach (string ext in mimetype.extensions)
                {
                    result.AppendLine(GenerateConstantFor(ext));
                }
            }
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

        private static string GenerateConstantFor(string type)
        {
            string name = GetConstantFor(type);
            return $"const {name} = '{type}';";
        }
        
        #endregion
    }
}
