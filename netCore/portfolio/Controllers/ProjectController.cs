using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace portfolio.Controllers{
    public class ProjectController : Controller
    {
        [HttpGet("Project")]
        public IActionResult Project()
        {
            return View();
        }
    }
}