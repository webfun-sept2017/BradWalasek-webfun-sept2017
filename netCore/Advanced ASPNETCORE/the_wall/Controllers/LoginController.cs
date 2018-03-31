using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using the_wall.Models;

namespace the_wall.Controllers
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
                string query = $"SELECT * FROM `c#_the_walldb`.`users` WHERE email = '{email}'";
                List<Dictionary<string, object>> result = DbConnector.Query(query);
                
                if((string)result[0]["password"] == password)
                {
                    HttpContext.Session.SetString("logged",$"{(result[0]["id"])}" );
                    return RedirectToAction("Index", "Quotes");
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
            string query = $"INSERT INTO `c#_the_walldb`.`users` (`firstname`, `lastname`, `email`,`password`,`created_at`) VALUES ('{user.firstName}', '{user.lastName}', '{user.email}', '{user.password}', NOW())";
            DbConnector.Execute(query);
            return RedirectToAction("Index","Quotes");
        }
    }
}
