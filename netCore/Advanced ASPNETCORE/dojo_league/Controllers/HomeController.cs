using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using dojo_league.Factory;
using dojo_league.Models;

namespace dojo_league.Controllers
{
    public class HomeController : Controller
    {
        private NinjaFactory ninjaFactory;
        private DojoFactory dojoFactory;
        [HttpGet("")]
        public IActionResult Dojos()
        {
            return View();
        }
        [HttpGet("Ninjas")]
        public IActionResult Ninjas()
        {
            ninjaFactory = new NinjaFactory();
            List<Dictionary<string,object>> data = ninjaFactory.ViewAll();
            return View(data);
        }
        [HttpGet("Ninja/{id}")]
        public IActionResult ViewNinja(int id)
        {
            return View();
        }
        [HttpGet("Dojo/{id}")]
        public IActionResult ViewDojo(int id)
        {
            return View();
        }
        [HttpPost("/Ninja/Add")]
        public IActionResult AddNinja(Ninja ninja)
        {
            ninjaFactory = new NinjaFactory();
            TryValidateModel(ninja);
            ViewBag.Error = ModelState;
            ninjaFactory.AddNinja(ninja);
            
            return RedirectToAction("Ninjas");
        }
        [HttpPost("/Dojo/Add")]
        public IActionResult AddDojo(Dojo dojo)
        {
            dojoFactory = new DojoFactory();
            TryValidateModel(dojo);
            ViewBag.Error=ModelState;
            dojoFactory.AddDojo(dojo);

            return RedirectToAction("Dojos");
        }
        
    }
}

