using MySql.Data.MySqlClient;
using Dapper;
using dojo_league.Models;
using System.Data;
using System.Collections.Generic;
using System.Linq;
namespace dojo_league.Factory
{
    public class DojoFactory : IFactory<Dojo> 
    {
        private string connectionString;
        public DojoFactory()
        {
            connectionString = "server=localhost;userid=root;password=root;port=3306;database=dojo_leaguedb;SslMode=None";
        }
        internal IDbConnection Connection
        {
            get
            {
                return new MySqlConnection(connectionString);
            }
        }

        public List<Dojo> ViewAll()
        {
            using(IDbConnection dbConnection = Connection)
            {
            string query = "SELECT * FROM `dojo_leaguedb`.`dojos`";
            dbConnection.Open();
            return dbConnection.Query<Dojo>(query).ToList();
            }
        }
        public void AddDojo(Dojo dojo)
        {
            using(IDbConnection dbConnection = Connection)
            {
                string query = $"INSERT INTO `dojo_leaguedb`.`dojos` (`name`,`location`,`description`) VALUES ('{dojo.name}','{dojo.location}','{dojo.description}')";
                dbConnection.Open();
                dbConnection.Execute(query);
            }
        }
        //add dojo
        //view all dojos

    }
    

}