using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using restraunter.Models;
using Microsoft.EntityFrameworkCore;

namespace restraunter.Controllers
{
    public class HomeController : Controller
    {
        private Context _context;
        public HomeController(Context context)
        {
            _context = context;
        }

        [HttpGet("/")]
        public IActionResult Index()
        {
            ViewBag.Errors="";
            return View();
        }
        [HttpGet("/Reviews")]
        public IActionResult Reviews()
        {
            List<Review> reviews = _context.reviews.ToList();
            reviews.Reverse();
                                    
            return View(reviews);
        }
        [HttpPost("/verify")]
        public IActionResult Add(Review review)
        {
            TryValidateModel(review);
            if(ModelState.ErrorCount >= 1)
            {
                ViewBag.errors=ModelState.Values;
                object a = ModelState.Values;
                return View("Index");
            }
            _context.Add(review);
            _context.SaveChanges();
            return RedirectToAction("Reviews");
        }
    }
}
