using System.Linq;
using System.Text.RegularExpressions;

namespace FTT.generators
{
    public class CodeGeneratorBase
    {
        private static char[] numbers = new[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
        protected static string GetConstantFor(string type)
        {
            string name = CleanExtension(type);
            if (IsKeyword(name) || numbers.Contains(name.First()))
            {
                name = "_" + name;
            }
            return name;
        }

        private static bool IsKeyword(string name)
        {
            //this is not a comprehensive list, we just add to it as needed
            switch (name)
            {
                case "as":
                case "class":
                case "for":
                case "in":
                case "is":
                    return true;
            }
            return false;
        }

        private static Regex cleanregex = new Regex("[^a-z0-9]");
        protected static string CleanExtension(string ext)
        {
            return cleanregex.Replace(ext.ToLowerInvariant().Trim(), "");
        }

        protected static string quote(string value)
        {
            return string.Format("\"{0}\"", value);
        }
    }
}
