namespace FTTLib
{
    public enum FileCategory
    {
        Archive, // any file that can be extracted into several files
        Audio, // any file that can only contain an audio stream
        Binary, // any file that is unclassified or does not have a text representation
        Code, // any file that contains instructions that are compilable or machine-readable
        Document, // any file that is designed for conveying structured information between people
        Image, // any file that can only contain a single image or series of images
        Text, // any file that is not classified under another category and is not binary
        Video, // any file that is designed to be a container for a video stream
    }
}
