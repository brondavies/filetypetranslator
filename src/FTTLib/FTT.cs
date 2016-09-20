using System.Diagnostics;
using System.IO;

namespace FTTLib
{
    /// <summary>
    /// Methods for translating between mime-types and file extensions
    /// </summary>
    public partial class FTT
    {
        /// <summary>
        /// Returns the mime type for the given file name
        /// </summary>
        /// <param name="fileName">A file name, file extension or file path specification</param>
        /// <returns></returns>
        [DebuggerStepThrough]
        public static string GetMimeType(string fileName)
        {
            string extension = GetExtension(fileName);

            return GetMimeTypeInternal(extension.ToLowerInvariant().Replace(".", ""));
        }

        /// <summary>
        /// Returns a list of possible file extensions for the given mime type
        /// </summary>
        /// <param name="mimeType">A mime type</param>
        /// <returns></returns>
        [DebuggerStepThrough]
        public static string[] GetMimeTypeFileExtensions(string mimeType)
        {
            return GetMimeTypeFileExtensionsInternal(mimeType.ToLowerInvariant());
        }

        /// <summary>
        /// Returns a file category for the given file name
        /// </summary>
        /// <param name="fileName">A file name, file extension or file path specification</param>
        /// <returns></returns>
        [DebuggerStepThrough]
        public static FileCategory GetFileCategory(string fileName)
        {
            string extension = GetExtension(fileName);

            return GetFileCategoryInternal(extension.ToLowerInvariant().Replace(".", ""));
        }

        private static string GetExtension(string fileName)
        {
            return fileName.Contains(".") ? Path.GetExtension(fileName) : fileName;
        }
    }
}
