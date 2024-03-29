﻿using System.Linq;
using System.Text.RegularExpressions;

namespace FTT.generators
{
    public class CodeGeneratorBase
    {
        static readonly char[] numbers = new[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
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
                case "def":
                case "for":
                case "in":
                case "is":
                case "not":
                    return true;
            }
            return false;
        }

        static readonly Regex cleanregex = new Regex(@"[^a-z0-9_]");
        protected static string CleanExtension(string ext)
        {
            return cleanregex.Replace(ext.ToLowerInvariant().Replace('+', '_').Trim(), "");
        }

        protected static string quote(string value, char c = '"')
        {
            return string.Format($"{c}{{0}}{c}", value);
        }
    }
}
