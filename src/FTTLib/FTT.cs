using System.Diagnostics;
using System.IO;

namespace FTT
{
    public partial class FTT
    {
        /// <summary>
        /// Returns the mime type for the given file name
        /// </summary>
        /// <param name="FileName">A file name, file extension or file path specification</param>
        [DebuggerStepThrough]
        public static string GetMimeType(string FileName)
        {
            string extension = FileName.Contains(".") ? Path.GetExtension(FileName) : FileName;

            return GetMimeTypeInternal(extension.ToLowerInvariant().Replace(".", ""));
        }
    }
}
