using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Xml.Serialization;

namespace FTT
{
    class Sources
    {
        const string freedesktopUrl = "https://cgit.freedesktop.org/xdg/shared-mime-info/plain/freedesktop.org.xml.in";
        const string stdiconJsonUrl = "http://www.stdicon.com/mimetypes";

        const string indent = "                ";


        public static string Parse()
        {
            MimeInfo info = null;
            JsonDict stdicon = null;
            using (WebClient client = new WebClient())
            {
                XmlSerializer serializer = new XmlSerializer(typeof(MimeInfo));
                info = (MimeInfo)serializer.Deserialize(client.OpenRead(freedesktopUrl));
                stdicon = JsonConvert.DeserializeObject<JsonDict>(client.DownloadString(stdiconJsonUrl));
            }

            Console.Write(stdicon);

            List<MimeType> mimetypes = new List<MimeType>();
            ParseMimeInfo(info, mimetypes);
            ParseStdIcon(stdicon, mimetypes);

            mimetypes = mimetypes.OrderBy(m => m.extensions.First()).ToList();

            StringBuilder format = new StringBuilder(GenerateFileStart());

            foreach (MimeType mt in mimetypes)
            {
                if (!string.IsNullOrEmpty(mt.comment))
                {
                    format.AppendLine(GenerateComment(mt.comment));
                }
                foreach (string extension in mt.extensions)
                {
                    format.AppendLine(GenerateCase(extension));
                }
                format.AppendLine(GenerateReturn(mt.type));
            }

            format.Append(GenerateFileEnd());
            return format.ToString();
        }

        private static void ParseStdIcon(JsonDict dict, List<MimeType> mimetypes)
        {
            foreach (var entry in dict)
            {
                string extension = CleanExtension(entry.Keys.First());
                string type = entry.Values.First().Trim();
                if (!string.IsNullOrEmpty(type) && !string.IsNullOrEmpty(extension))
                {
                    MimeType mimeType = mimetypes.Find(t => t.type == type) ?? new MimeType();

                    if (!mimetypes.Exists(m => m.extensions.Contains(extension)))
                    {
                        mimeType.extensions.Add(extension);
                        if (string.IsNullOrEmpty(mimeType.type))
                        {
                            mimeType.type = type;
                            mimetypes.Add(mimeType);
                        }
                    }
                }
            }
        }

        private static void ParseMimeInfo(MimeInfo info, List<MimeType> mimetypes)
        {
            StringBuilder format = new StringBuilder(GenerateFileStart());
            foreach (mimeinfoMimetype item in info.Items)
            {
                if (item.glob != null && !string.IsNullOrEmpty(item.type))
                {
                    bool added = false;
                    item.type = item.type.ToLowerInvariant().Trim();
                    MimeType mimeType = mimetypes.Find(t => t.type == item.type) ?? new MimeType();
                    foreach (var glob in item.glob)
                    {
                        string extension = CleanExtension(glob.pattern);
                        if (!mimetypes.Exists(m => m.extensions.Contains(extension)) && !mimeType.extensions.Contains(extension))
                        {
                            added = mimeType.type == null;
                            mimeType.extensions.Add(extension);
                        }
                    }
                    if (added)
                    {
                        mimeType.type = item.type;
                        mimeType.comment = item._comment;
                        mimetypes.Add(mimeType);
                    }
                }
            }
        }

        private static string CleanExtension(string ext)
        {
            return ext.Replace("*", "").Replace(".", "").ToLowerInvariant().Trim();
        }

        private static string GenerateReturn(string type)
        {
            return string.Format("{0}    return \"{1}\";", indent, type);
        }

        private static string GenerateComment(string comment)
        {
            return string.Format("{0}// {1}", indent, comment);
        }

        private static string GenerateCase(string extension)
        {
            return string.Format("{0}case \"{1}\":", indent, extension);
        }

        private static string GenerateFileStart()
        {
            return @"namespace FTT
{
    public partial class FTT
    {
        private static string GetMimeTypeInternal(string extension)
        {
            switch (extension)
            {
";
        }

        private static string GenerateFileEnd()
        {
            return @"            }
            return """";
        }
    }
}";
        }

    }
}
