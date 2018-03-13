using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace testing_ground
{
    public class JSONController : Controller
    {
        [HttpGet]
        [Route("JSON")]
        public IActionResult json(){

            string a = "brad";
            string b = "walasek";
            List<string> jsonList = new List<string>();
            jsonList.Add(a);
            jsonList.Add(b);
            HttpContext.Session.SetObjectAsJson("Json", JsonConvert.SerializeObject(jsonList));


            return View();
        }  

        [HttpPost("JSON")]
        public IActionResult json(Person friend){
            ViewBag.friend = friend.name;
            ViewBag.statement = friend.fullname;
            return View();
        }

        [HttpGet]
        [Route("jsontest")]
        public JsonResult Example(){
            string a = "brad";
            string b = "walasek";
            List<string> jsonList = new List<string>();
            jsonList.Add(a);
            jsonList.Add(b);
            return Json(jsonList);
        }  
    }
}