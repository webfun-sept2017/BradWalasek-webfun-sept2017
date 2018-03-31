using System.Collections.Generic;
using System.Linq;
using Dapper;
using MySql.Data.MySqlClient;
using dojo_league.Models;
using System.Data;
namespace dojo_league.Factory
{
    public class NinjaFactory : IFactory<Ninja>
    {
        private string connectionString;
        public NinjaFactory()
        {
            connectionString = "server=localhost; userid=root; password=root; port = 3306; database=dojo_leaguedb; SslMode=None";
        }
        internal IDbConnection Connection
        {
            get
            {
                return new MySqlConnection(connectionString);
            }
        }
        public List<Dictionary<string, object>> ViewAll()
        {

            using (IDbConnection dbConnection = Connection)
            {
                dbConnection.Open();
                var query=
                @"
                SELECT * FROM `dojos`;
                SELECT * FROM `ninjas`;
                ";
            }






            // using(IDbConnection dbConnection = Connection)
            // {
            // string query = "SELECT `dojos`.`name` as 'dojo', `dojos`.`id` as 'dojo_id', `ninjas`.`name`, `ninjas`.`id` as 'ninja_id' FROM `dojo_leaguedb`.`dojos` LEFT JOIN `ninjas` on `dojos`.`id` = `ninjas`.`dojo_id`;";
            // dbConnection.Open();
            // List<Ninja> list = dbConnection.Query<Ninja>("SELECT * FROM `dojo_leaguedb`.`ninjas`").ToList();
            // List<Dictionary<string, object>> listnumber2 = dbConnection.Query<Dictionary<string, object>>(query).ToList();
            // return listnumber2;
            // }
        }
        public void AddNinja(Ninja ninja)
        {
            using(IDbConnection dbConnection = Connection)
            {
                string query = $"INSERT INTO `dojo_leaguedb`.`ninjas` (`name`,`level`,`description`, `dojo_id`) VALUES ('{ninja.name}','{ninja.level}','{ninja.description}','{ninja.dojo}')";
                dbConnection.Open();
                dbConnection.Execute(query);
            }
        }
    }
    //add ninja
    //update ninja (banish and recruit)
    //view all ninjas

}