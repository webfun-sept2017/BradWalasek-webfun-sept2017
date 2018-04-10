using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using wedding_planner.Models;

namespace wedding_planner.Controllers
{
    public class HomeController : Controller
    {
        private WeddingContext _context;
        public HomeController(WeddingContext context)
        {
            _context = context; 
        }
        [HttpGet("/Dashboard")]
        public IActionResult Dashboard()
        {
            string email = HttpContext.Session.GetString("Logged");
            List<Schedule> Schedule = _context.Schedules
                                                .Include(schedule=>schedule.user)
                                                .Include(schedule => schedule.wedding)
                                                .Where(schedule=> schedule.user.email == email)
                                                .ToList();
            
            return View(Schedule);
        }
        [HttpGet("/Wedding/New")]
        public IActionResult Plan()
        {
            return View();
        }
        [HttpPost("/Wedding/Create")]
        public IActionResult Create(string wedderone, string weddertwo, string address, DateTime date)
        {
            Wedding wedding = new Wedding(){
                name = $"{wedderone} + {weddertwo}",
                address = address,
                date = date
            };
            _context.Add(wedding);
            _context.SaveChanges();
            List<User> users = _context.Users.ToList();
            Wedding added = _context.Weddings.Where(id=>id.name == wedding.name).SingleOrDefault();
            foreach(User user in users)
            {
                Schedule schedule = new Schedule()
                {
                    userid = user.id,
                    weddingid = added.id,
                    status = "Not attending"
                };
                _context.Add(schedule);
            }
            _context.SaveChanges();
            return RedirectToAction("Dashboard");
        }
        [HttpPost("/Schedule/Update")]
        public IActionResult Update(int id, string status)          
        {
            Schedule updating = _context.Schedules.Where(schedule=>schedule.id == id).SingleOrDefault();
            if (status == "Not attending")
                {
                    updating.status = "Attending";
                }
                else
                {
                    updating.status = "Not attending";
                }
            _context.SaveChanges();
            return RedirectToAction("Dashboard");
        }
        [HttpGet("/Wedding/{id}")]
        public IActionResult View(int id)
        {
            Wedding wedding = _context.Weddings.Include(w=>w.schedules)
                                                .ThenInclude(w=>w.user)
                                                .Where(w=>w.id == id).SingleOrDefault();
            if(!(wedding is null))
            {
                return View(wedding);
            }
            return RedirectToAction("Dashboard");
        }

    }
}
