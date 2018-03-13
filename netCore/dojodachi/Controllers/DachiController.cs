using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Newtonsoft.Json;
using System;

namespace dojodachi.Controllers
{
    public class DachiController : Controller
    {
        [HttpPost]
        [Route("dachi")]
        public IActionResult generate(string name){
            List<object> stats = new List<object>();
            stats.Add(name); //0
            stats.Add(20); //1
            stats.Add(20); //2
            stats.Add(50); //3
            stats.Add(3); //4
            stats.Add(""); //5
            HttpContext.Session.SetObjectAsJson("dachi", stats);
            return RedirectToAction("dachi");
        }
        [HttpGet]
        [Route("dachi")]
        public IActionResult dachi(){
            List<object> stats = HttpContext.Session.GetObjectFromJson<List<object>>("dachi");
            if((Int64)stats[1]>100 && (Int64)stats[2]>100 && (Int64)stats[3] > 100){
                return RedirectToAction("victory");
            }
            if((Int64)stats[1]<0 || (Int64)stats[2]<0 || (Int64)stats[3]<0){
                return RedirectToAction("lost");
            }
            ViewBag.Name = stats[0];
            ViewBag.Happiness = stats[1];
            ViewBag.Fullness = stats[2];
            ViewBag.Energy = stats[3];
            ViewBag.Meals = stats[4];
            ViewBag.Response = stats[5];
            return View();
        }
        [HttpGet]
        [Route("victory")]
        public IActionResult victory(){
            return View();
        }
        [HttpGet]
        [Route("lost")]
        public IActionResult lost(){
            return View();
        }

        [HttpPost]
        [Route("activity/eat")]
        public IActionResult eat()
        {
            List<object> stats = HttpContext.Session.GetObjectFromJson<List<object>>("dachi");
            if ((Int64)stats[4] > 0){
                Random chance = new Random();
                stats[4] = (Int64)stats[4] - 1;
                int gain = 0;
                string mood = "upset";
                if(chance.Next(1,5)> 1){
                    gain = chance.Next(1,6);
                    stats[2] = (Int64)stats[2] + gain;
                    mood = "happy";      
                }
                
                stats[5]=String.Format("{0} was {1} and gained {2} fullness",stats[0],mood,gain);
                HttpContext.Session.SetObjectAsJson("dachi", stats);
                return RedirectToAction("dachi");
            }
            stats[5]="No food left!";
            HttpContext.Session.SetObjectAsJson("dachi", stats);
            return RedirectToAction("dachi");
        }

        [HttpPost]
        [Route("activity/play")]
        public IActionResult play()
        {
            List<object> stats = HttpContext.Session.GetObjectFromJson<List<object>>("dachi");
            if ((Int64)stats[3] > 0){
                Random chance = new Random();
                stats[3] = (Int64)stats[3] - 5;
                int gain = 0;
                string mood = "upset";
                if(chance.Next(1,5)> 1){
                    gain = chance.Next(5,11);
                    stats[1] = (Int64)stats[1] + gain;
                    mood = "happy";      
                }
                
                stats[5]=String.Format("{0} was {1} and gained {2} happiness",stats[0],mood,gain);
                HttpContext.Session.SetObjectAsJson("dachi", stats);
                return RedirectToAction("dachi");
            }
            stats[5]= "No energy left!";
            HttpContext.Session.SetObjectAsJson("dachi", stats);
            return RedirectToAction("dachi");
            
        }

        [HttpPost]
        [Route("activity/work")]
        public IActionResult work()
        {
            List<object> stats = HttpContext.Session.GetObjectFromJson<List<object>>("dachi");
            Random chance = new Random();
            stats[3] = (Int64)stats[3] - 5;
            int gain = chance.Next(1,4);
            stats[4] = (Int64)stats[4] + gain;
            stats[5] = String.Format("You worked and gained {0}",gain);
            HttpContext.Session.SetObjectAsJson("dachi", stats);
            return RedirectToAction("dachi");
        }
        [HttpPost]
        [Route("activity/sleep")]
        public IActionResult sleep(){
            List<object> stats = HttpContext.Session.GetObjectFromJson<List<object>>("dachi");
            stats[3] = (Int64)stats[3] + 15;
            stats[1] = (Int64)stats[1] - 5;
            stats[2] = (Int64)stats[2] - 5;
            stats[5] = String.Format("{0} slept, losing 5 happiness, 5 fullness and gaining 15 energy.",stats[0]);
            HttpContext.Session.SetObjectAsJson("dachi", stats);
            return RedirectToAction("dachi");
        }



    }
    public static class SessionExtensions
    {
        // We can call ".SetObjectAsJson" just like our other session set methods, by passing a key and a value
        public static void SetObjectAsJson(this ISession session, string key, object value)
        {
            // This helper function simply serializes theobject to JSON and stores it as a string in session
            session.SetString(key, JsonConvert.SerializeObject(value));
        }
        
        // generic type T is a stand-in indicating that we need to specify the type on retrieval
        public static T GetObjectFromJson<T>(this ISession session, string key)
        {
            string value = session.GetString(key);
            // Upon retrieval the object is deserialized based on the type we specified
            return value == null ? default(T) : JsonConvert.DeserializeObject<T>(value);
        }
    }
}
