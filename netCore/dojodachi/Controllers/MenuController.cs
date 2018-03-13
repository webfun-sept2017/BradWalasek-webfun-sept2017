using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace doodatchi.Controllers
{
    public class MenuController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult menu(){
            return View();
        }
    }
}
