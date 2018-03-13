using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;

namespace portfolio.Controllers{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Home()
        {    
            return View();
        }
    }
}