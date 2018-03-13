using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace quoting_dojo.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {


            List<Dictionary<string, object>> AllUsers = DbConnector.Query("SELECT * FROM people");
            foreach(Dictionary<string, object> user in AllUsers)
            {
                string name = (string)user["name"];
                Console.WriteLine(name);
            }
            return View();
        }
    }
}
