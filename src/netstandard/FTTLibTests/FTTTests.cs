using FTTLib;

namespace FTTLibTests;

[TestClass]
public class FTTTests
{
    [TestMethod]
    public void GetMimeType_ValidFileName_ReturnsMimeType()
    {
        string fileName = "example.txt";
        string mimeType = FTT.GetMimeType(fileName);
        Assert.AreEqual("text/plain", mimeType);
    }

    [TestMethod]
    public void GetMimeType_InvalidFileName_ReturnsNoMimeType()
    {
        string fileName = "example.unknown";
        string mimeType = FTT.GetMimeType(fileName);
        Assert.AreEqual("", mimeType);
    }

    [TestMethod]
    public void GetMimeTypeFileExtensions_ValidMimeType_ReturnsExtensions()
    {
        string mimeType = "text/plain";
        string[] extensions = FTT.GetMimeTypeFileExtensions(mimeType);
        CollectionAssert.Contains(extensions, "txt");
    }

    [TestMethod]
    public void GetMimeTypeFileExtensions_InvalidMimeType_ReturnsEmptyArray()
    {
        string mimeType = "invalid/mime";
        string[] extensions = FTT.GetMimeTypeFileExtensions(mimeType);
        Assert.AreEqual(0, extensions.Length);
    }

    [TestMethod]
    public void GetFileCategory_ValidFileName_ReturnsFileCategory()
    {
        string fileName = "example.jpg";
        FileCategory category = FTT.GetFileCategory(fileName);
        Assert.AreEqual(FileCategory.Image, category);
    }

    [TestMethod]
    public void GetFileCategory_InvalidFileName_ReturnsBinaryCategory()
    {
        string fileName = "example.unknown";
        FileCategory category = FTT.GetFileCategory(fileName);
        Assert.AreEqual(FileCategory.Binary, category);
    }
}
