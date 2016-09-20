namespace FTTLib
{
    /// <summary>
    /// File Category enumerator for generalized file type identification
    /// </summary>
    public enum FileCategory
    {
        /// <summary>
        /// Any file that can be extracted into several files
        /// </summary>
        Archive,
        /// <summary>
        /// Any file that can only contain an audio stream
        /// </summary>
        Audio,
        /// <summary>
        /// Any file that is unclassified or does not have a text representation
        /// </summary>
        Binary,
        /// <summary>
        /// Any file that contains instructions that are compilable or machine-readable
        /// </summary>
        Code,
        /// <summary>
        /// Any file that is designed for conveying structured information between people
        /// </summary>
        Document,
        /// <summary>
        /// Any file that can only contain a single image or series of images
        /// </summary>
        Image,
        /// <summary>
        /// Any file that is not classified under another category and is not binary
        /// </summary>
        Text,
        /// <summary>
        /// Any file that is designed to be a container for a video stream
        /// </summary>
        Video,
    }
}
