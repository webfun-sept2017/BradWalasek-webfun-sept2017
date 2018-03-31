using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using login_and_registration.Models;

namespace login_and_registration.Controllers
{
    public class LoginController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("verify")]
        public IActionResult verify(string email, string password)
        {
            try
            {
                string query = $"Select * FROM `logindb`.`users` WHERE email = '{email}'";
                List<Dictionary<string, object>> result = DbConnector.Query(query);
                string test = (string)result[0]["firstname"];
                if((string)result[0]["password"] == password)
                {
                    ViewBag.user = result[0]["firstname"];
                    return View("success");
                }
                else{
                    ViewBag.login = "Incorrect password";
                }
            }
            catch
            {
                ViewBag.login = "Invalid login credentials";
            }
            return View("Index");
        }
        [HttpPost("new")]
        public IActionResult create(User user)
        {
            TryValidateModel(user);
            int n = 0;
            foreach(var error in ModelState.Values)
            {
                n += error.Errors.Count;
            }
            if(n>0){
                ViewBag.error = ModelState.Values;
                return View("Index");
            }
            string query = $"INSERT INTO `logindb`.`users` (`firstname`, `lastname`, `email`,`password`,`created_at`) VALUES ('{user.firstName}', '{user.lastName}', '{user.email}', '{user.password}', NOW())";
            DbConnector.Execute(query);
            ViewBag.user = user.firstName;
            return View("success");
        }
    }
}
