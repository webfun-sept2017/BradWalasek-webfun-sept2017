using System;
using System.Collections.Generic;
using System.Data;
using MySql.Data.MySqlClient;
using lost_in_the_woods.Models;
using Dapper;
using System.Linq;
namespace lost_in_the_woods.Factories
{
    public class TrailFactory
    {
        private string connectionString;
        public TrailFactory()
        {
            connectionString="server=localhost;userid=root;password=root;port=3306;database=trailsdb;SslMode=None";
        }
        internal IDbConnection Connection
        {
            get {
                return new MySqlConnection(connectionString);
            }
        }

        public void Add(Trail trail)
        {
            using (IDbConnection dbConnection = Connection)
            {
                string query = "INSERT INTO `trailsdb`.`trails` (`name`, `length`,`elevation`,`description`,`latitude`,`longitude`) VALUES (@name, @length, @elevation, @description, @latitude, @longitude) ";
                dbConnection.Open();
                dbConnection.Execute(query, trail);
            }
        }
        public List<Trail> GetAllTrails()
        {
            using (IDbConnection dbConnection = Connection){
               string query = "SELECT * FROM `trailsdb`.`trails`";
               dbConnection.Open();
               return dbConnection.Query<Trail>(query).ToList();
            }
            
        }
        public List<Trail> GetByName(string name)
        {
            using(IDbConnection dbConnection = Connection){
                string query = $"SELECT * from `trailsdb`.`trails` WHERE name = '{name}'";
                dbConnection.Open();
                return dbConnection.Query<Trail>(query).ToList();
            }
        }
        //get trails
        //add new trails

    }
    
}