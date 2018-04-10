using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Linq;
using bank_accounts.Models;

namespace bank_accounts.Controllers
{
    public class LoginController : Controller
    {
        private Context _context;
        public LoginController(Context context)
        {
            _context = context;
        }
        [HttpGet("/")]
        public IActionResult Index()
        {
            var logged = HttpContext.Session.GetInt32("Logged");
            if(logged != null)
            {
                return RedirectToAction("Index","Account", new {id = logged});
            }
            ViewBag.error="";
            return View();
        }
        [HttpPost("/user/verify")]
        public IActionResult Add(RegisterViewModel reg)
        {
            TryValidateModel(reg);
            foreach(var item in ModelState.Values)
            {
                if((int)item.ValidationState != 2)
                {
                    ViewBag.error = ModelState.Values;
                    return View("Index");
                }
            }
            User user = new User()
            {
                firstname = reg.firstname,
                lastname = reg.lastname,
                email = reg.email,
                password = reg.password
            }
            ;
            _context.Add(user);
            _context.SaveChanges();
            HttpContext.Session.SetInt32("Logged", user.userid);
            return RedirectToAction("Index","Account",new{id=user.userid});
        }
        [HttpPost("/login")]
        public IActionResult LogIn(string email, string password)
        {
            try{
                User account = _context.Users.Where(user=>user.email == email).SingleOrDefault();
                if(password == account.password)
                {
                    HttpContext.Session.SetInt32("Logged", account.userid);
                    return RedirectToAction("Index");
                }
                ViewBag.LoginError = "Invalid Login Credentials";
                return View("Index");
            }
            catch{
                ViewBag.LoginError = "Invalid Login Credentials";
                return View("Index");
            }
        }
        [HttpGet("/logout")]
        public IActionResult LogOut()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}