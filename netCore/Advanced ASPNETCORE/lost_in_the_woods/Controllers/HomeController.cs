using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using lost_in_the_woods.Models;
using lost_in_the_woods.Factories;


namespace lost_in_the_woods.Controllers
{
    public class HomeController : Controller
    {
        public readonly TrailFactory trailfactory;
        public HomeController(){
            trailfactory = new TrailFactory();
        }
        [HttpGet("")]
        public IActionResult Index()
        {
            List<Trail> trail = trailfactory.GetAllTrails();
            return View(trail);
        }
        [HttpGet("NewTrail")]
        public IActionResult New()
        {
            ViewBag.errors="";
            return View();
        }
        [HttpPost("Add")]
        public IActionResult Add(RegisterViewModel model)
        {
            if(ModelState.IsValid){
                Trail trail = new Trail{
                    name=model.name,
                    length=model.length,
                    description=model.description,
                    elevation=model.elevation,
                    latitude=model.latitude,
                    longitude=model.longitude
                };
                trailfactory.Add(trail);

                return RedirectToAction("Index");
                
            }
            ViewBag.errors=ModelState.Values;
            return View("New");
        }
        [HttpGet("trail/{name}")]
        public IActionResult Trail(string name){
            Trail trail = trailfactory.GetByName(name)[0];
            return View(trail);
        }
    }
}
