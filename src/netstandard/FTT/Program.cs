using FTT.generators;
using System;
using System.Net;

namespace FTT
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                ServicePointManager.SecurityProtocol |= SecurityProtocolType.Tls11 | SecurityProtocolType.Tls12;

                Sources.Parse(
                    typeof(CsharpGenerator)
                    //,typeof(PythonGenerator)
                    );
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
