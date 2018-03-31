using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using MySql.Data.MySqlClient;

namespace quoting_dojo.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost("quotes")]
        public IActionResult quotes(Quote quote)
        {
            if (quote.author == null || quote.text == null) {
                ViewBag.error = "Author and quote need to be more than 1 character.";
                return View("Index");
            }
            string query = $"INSERT INTO `quotesdb`.`table1` (`author`, `quote`,`created_at`) VALUES('{quote.author}', '{(string)quote.text}',NOW())";
            DbConnector.Execute(query);
            
            return RedirectToAction("quotes");
        }

        [HttpGet("quotes")]
        public IActionResult quotes(){
            List<Dictionary<string, object>> AllQuotes = DbConnector.Query("SELECT * FROM `quotesdb`.`table1` ORDER BY created_at DESC");
            ViewBag.quotes = AllQuotes;
            return View();
        }
    }
}
