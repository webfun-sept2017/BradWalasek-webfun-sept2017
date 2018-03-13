using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using Newtonsoft.Json;

namespace PokeInfo.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost]
        public IActionResult Search(int request)
        {
            
            return View();
        }



        [HttpGet]
        [Route("pokemon")]
        public IActionResult QueryPoke(int pokeid)
        {
            var PokeInfo = new Dictionary<string, object>();
            WebRequest.GetPokemonDataAsync(pokeid, ApiResponse =>
            {PokeInfo = ApiResponse;}).Wait();
            string name = PokeInfo["name"].ToString();
            Int64 weight = (Int64)PokeInfo["weight"];
            string type = PokeInfo["types"].ToString();
            // string test = JsonConvert.SerializeObject(searched, Formatting.Indented);
            // Console.WriteLine(test);
            ViewBag.Name=name;
            ViewBag.Weight = weight;
            ViewBag.Type = type;
            return View();
        }



    }
}
