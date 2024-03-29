﻿namespace FTT
{
    public static class Extensions
    {
        public static string AppendLine(this string value, string append = null)
        {
            return $"{value}\n{append}";
        }

        public static string Append(this string value, string append)
        {
            return $"{value}{append}";
        }

        public static string InsertAfter(this string value, string after, string insert)
        {
            int index = value.IndexOf(after);
            if (index >= 0)
            {
                return value.Insert(index + after.Length, "\n" + insert);
            }
            return value;
        }

        public static string InsertBefore(this string value, string before, string insert)
        {
            int index = value.IndexOf(before);
            if (index >= 0)
            {
                return value.Insert(index, "\n" + insert);
            }
            return value;
        }
    }
}
