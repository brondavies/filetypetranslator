using System;
using System.IO;

namespace FTT
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string generatedFile = Path.GetFullPath(@"..\..\..\FTTLib\FTT.generated.cs");
                File.WriteAllText(generatedFile, Sources.Parse());
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                Console.WriteLine(e.StackTrace);
                Environment.ExitCode = 1;
            }
        }
    }
}
