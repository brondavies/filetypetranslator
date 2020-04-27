namespace FTT
{
    public static class Extensions
    {
        public static string AppendLine(this string value, string append = null)
        {
            return $"{value}\r\n{append}";
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
                return value.Insert(index + after.Length, "\r\n" + insert);
            }
            return value;
        }
    }
}
