using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace testing_ground
{
    public class MainController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult index(){
            return View();
        }
        
    }
}