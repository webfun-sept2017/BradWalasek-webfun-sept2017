using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace calling_card.Controllers
{
    public class dummyinformation : Controller
    {
        [HttpGet]
        [Route("")]
        public string Index()
        {
            return "Hello World!";
        }
        [HttpGet]
        [Route("{first}/{last}/{age}/{color}")]
        public JsonResult Information(string first, string last, int years, string color)
        {
            var result = new {
                FirstName = first,
                LastName = last,
                Age = years,
                Fcolor = color
            };
            return Json(result);
        }
    }

}
