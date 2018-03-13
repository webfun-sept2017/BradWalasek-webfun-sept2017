using System;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace dojo_survey.Controllers
{
    
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Home()
        {
            return View();
        }




        [HttpPost("result")]
        
        public IActionResult Result(string location, string language, string name, string comment)
        {
            ViewBag.loc = location;
            ViewBag.lan = language;
            ViewBag.name = name;
            ViewBag.com = comment;
            return View();
        }






    }
}