using FTT.Properties;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

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
            format = format.InsertAfter("#constants", result.ToString());
        }

        public void GenerateBeginFunction()
        {
            //no-op
        }

        public void GenerateFunctionBody(MimeType mimeType)
        {
            string value = "";
            if (!string.IsNullOrEmpty(mimeType.comment))
            {
                value = value.AppendLine(GenerateComment(mimeType.comment));
            }
            value = value.AppendLine(GenerateCase(mimeType.extensions))
                .AppendLine(GenerateReturn(GetConstantFor(mimeType.type)));
            format = format.InsertAfter("#getMimeType body", value);
        }

        private string GenerateReturn(string value)
        {
            return $"{indent}{indent}return {value}";
        }

        public void GenerateEndFunction()
        {
            //no-op
        }

        public void GenerateBeginFunction2()
        {
            //no-op
        }

        public void GenerateFunctionBody2(MimeType mimeType)
        {
            string value = "";
            value = value.AppendLine(GenerateCase(new[] { mimeType.type }, "mimeType"));
            string extensions = "[ ";
            string strings = string.Join("\", \"", mimeType.extensions);
            if (strings.Length > 0)
            {
                strings = quote(strings);
            }
            extensions += strings;
            extensions += " ]";
            value = value.AppendLine(GenerateReturn(extensions));

            format = format.InsertAfter("#getMimeTypeFileExtensions body", value);
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
            string generatedFile = Path.GetFullPath(@"..\..\..\..\python\FTTLib\FTT.py");
            File.WriteAllText(generatedFile, format.ToString());
        }

        #region Private Methods

        private string GenerateCase(IEnumerable<string> values, string variable = "extension")
        {
            var joined = string.Join(", ", values.Select(e => GetConstantFor(e)));
            if (values.Count() == 1)
            {
                return $"{indent}if {variable} == {joined}:";
            }
            return string.Format($"{indent}if {variable} in ({{0}}):", joined);
        }

        private string GenerateComment(string comment)
        {
            return $"{indent}# {comment}";
        }

        private static string GenerateConstantFor(string type)
        {
            string name = GetConstantFor(type);
            return $"{name} = \"{type}\"";
        }
        
        #endregion
    }
}
