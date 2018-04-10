using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using wedding_planner.Models;
namespace wedding_planner
{
    public class LoginController : Controller
    {
        private WeddingContext _context;
        public LoginController(WeddingContext context)
        {
            _context = context;
        }
        [HttpGet("/")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("/Login")]
        public IActionResult Login(string email, string password)
        {
            User user = _context.Users.Where(target=>target.email == email).SingleOrDefault();
            if(!(user == null))
            {
                HttpContext.Session.SetString("Logged", user.email);
                return RedirectToAction("Dashboard","Home");
            }
            ViewBag.LoginError = "Invalid Email Address";
            return View("Index");
        }
        [HttpPost("/User/Create")]
        public IActionResult Register(RegisterViewModel reg)
        {
            TryValidateModel(reg);
            if(ModelState.ErrorCount >= 1)
            {
                object a = ModelState.Values;
                ViewBag.error = ModelState.Values;
                return View("Index");
            }
            User user = new User(){
                firstname = reg.firstname,
                lastname = reg.lastname,
                email = reg.email,
                password = reg.password
            };
            _context.Add(user);
            _context.SaveChanges();
            User logged = _context.Users.Where(x=>x.email == user.email).SingleOrDefault();
            List<Wedding> weddings = _context.Weddings.ToList();
            foreach(Wedding wedding in weddings)
            {
                Schedule schedule = new Schedule()
                {
                    userid = logged.id,
                    weddingid = wedding.id,
                    status = "Not attending"
                };
                _context.Add(schedule);
            }
            HttpContext.Session.SetString("Logged", user.email);

            _context.SaveChanges();
            return RedirectToAction("Dashboard","Home");
        }
    }
}