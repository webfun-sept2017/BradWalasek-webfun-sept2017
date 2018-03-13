using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace portfolio.Controllers{
    public class ContactController : Controller
    {
        [HttpGet("Contact")]
        public IActionResult Contact()
        {
            return View();
        }
    }
}