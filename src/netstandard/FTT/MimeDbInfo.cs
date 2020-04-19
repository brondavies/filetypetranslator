using System.Collections.Generic;

namespace FTT
{
    internal class MimeDbInfo
    {
        public string source { get; set; }
        public bool compressible { get; set; }
        public string[] extensions { get; set; }
    }

    internal class MimeDbInfoDict : Dictionary<string, MimeDbInfo>
    {

    }
}
