using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using form_submission.Models;

namespace form_submission.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("validation")]
        public IActionResult validation(string first, string last, int age, string email, string password){
            User NewUser = new User{
                firstName = first,
                lastName = last,
                age = age,
                email = email,
                password = password
            };
            TryValidateModel(NewUser);
            ViewBag.error= ModelState.Values;
            return View();
        }
    }
}
