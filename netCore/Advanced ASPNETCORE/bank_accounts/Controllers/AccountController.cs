using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using bank_accounts.Models;

namespace bank_accounts.Controllers
{
    public class AccountController : Controller
    {
        private Context _context;
        public AccountController(Context context)
        {
            _context = context;
        }
        [HttpGet("/user/{id}")]
        public IActionResult Index(int id)
        {
            if(HttpContext.Session.GetInt32("Logged") != id)
            {
                return RedirectToAction("Index","Login");
            }
            User user =_context.Users.Include(account => account.Transactions).Where(account=>account.userid == id).SingleOrDefault();
            user.Transactions.Reverse();
            ViewBag.Error = HttpContext.Session.GetString("Error");
            HttpContext.Session.SetString("Error", "");

            return View(user);
        }
        [HttpPost("/user/{userid}/add")]
        public IActionResult AddTransaction(int userid, float amount, int balance)
        {
            if(balance + amount < 0)
            {
                HttpContext.Session.SetString("Error","Cannot withdraw more than current balance");
                return RedirectToAction("Index", new {id = userid});
            }
            Transaction transaction = new Transaction(){userid = userid, amount = amount, created_on = DateTime.Now};
            _context.Transactions.Add(transaction);
            _context.SaveChanges();
            return RedirectToAction("Index", new {id = userid});
        }
    }
}
