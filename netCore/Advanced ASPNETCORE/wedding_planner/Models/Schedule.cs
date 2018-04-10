
namespace wedding_planner.Models
{
    public class Schedule
    {
    public int id{get;set;}
    public int userid{get;set;}
    public User user{get;set;}
    public int weddingid{get;set;}
    public Wedding wedding{get;set;}
    public string status {get;set;}
    }
}