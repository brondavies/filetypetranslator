using System.Diagnostics;
using System.IO;

namespace FTTLib
{
    public partial class FTT
    {
        [DebuggerStepThrough]
        /// <summary>
        /// Returns the mime type for the given file name
        /// </summary>
        /// <param name="FileName">A file name, file extension or file path specification</param>
        /// <returns></returns>
        public static string GetMimeType(string FileName)
        {
            string extension = GetExtension(FileName);

            return GetMimeTypeInternal(extension.ToLowerInvariant().Replace(".", ""));
        }

        [DebuggerStepThrough]
        /// <summary>
        /// Returns a list of possible file extensions for the given mime type
        /// </summary>
        /// <param name="MimeType">A mime type</param>
        /// <returns></returns>
        public static string[] GetMimeTypeFileExtensions(string MimeType)
        {
            return GetMimeTypeFileExtensionsInternal(MimeType.ToLowerInvariant());
        }

        [DebuggerStepThrough]
        /// <summary>
        /// Returns a file category for the given file name
        /// </summary>
        /// <param name="FileName">A file name, file extension or file path specification</param>
        /// <returns></returns>
        public static FileCategory GetFileCategory(string FileName)
        {
            string extension = GetExtension(FileName);

            return GetFileCategoryInternal(extension.ToLowerInvariant().Replace(".", ""));
        }

        private static string GetExtension(string FileName)
        {
            return FileName.Contains(".") ? Path.GetExtension(FileName) : FileName;
        }
    }
}
