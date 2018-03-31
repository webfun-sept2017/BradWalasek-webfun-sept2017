using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using MySql.Data.MySqlClient;
using Microsoft.AspNetCore.Http;
using the_wall.Models;

namespace the_wall.Controllers
{
    public class QuotesController : Controller
    {
        [HttpGet("home")]
        public IActionResult Index()
        {
            string query = $"SELECT * FROM `c#_the_walldb`.`users` WHERE id = '{HttpContext.Session.GetString("logged")}'";
            List<Dictionary<string, object>> result = DbConnector.Query(query);
            
            // string query2 = $"SELECT users.firstname, messages.id, messages.content, messages.created_at FROM `c#_the_walldb`.`messages` JOIN users on messages.users_id = users.id WHERE users.id = '{HttpContext.Session.GetString("logged")}' order by messages.created_at desc";
            string query2 = $"SELECT users.firstname, users.id as user_id, messages.content, messages.id as message_id, messages.created_at  from messages JOIN users on messages.users_id = users_id ORDER BY messages.id desc";
            List<Dictionary<string, object>> result2 = DbConnector.Query(query2);
            string query3 = $"SELECT messages.id as message_id, users.firstname, comments.content, comments.created_at FROM comments JOIN users on comments.users_id = users.id Left Join messages on comments.messages_id = messages.id";
            List<Dictionary<string, object>> result3 = DbConnector.Query(query3);
            Bundle PagePackage = new Bundle{name = $"{result[0]["firstname"]}", messages = result2, comments = result3};
            return View(PagePackage);
            
            
            
        }
        [HttpPost("quotes")]
        public IActionResult quotes(string message)
        {
            int val = Convert.ToInt32(HttpContext.Session.GetString("logged"));
            string query = $"INSERT INTO `c#_the_walldb`.`messages` (`users_id`, `content`,`created_at`) VALUES ('{val}', '{message}',NOW())";
            
            DbConnector.Execute(query);
            
            return RedirectToAction("Index");
        }

        [HttpPost("comment")]
        
            public IActionResult comment(int id, string comment)
            {
            int val = Convert.ToInt32(HttpContext.Session.GetString("logged"));
            string query = $"INSERT INTO `c#_the_walldb`.`comments` (`users_id`, `messages_id`, `content`,`created_at`) VALUES ('{val}', {id} ,'{comment}',NOW())";
            
            DbConnector.Execute(query);
            
            return RedirectToAction("Index");
            
        }

    }
}
