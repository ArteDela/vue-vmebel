var mysql = require('mysql');

class VMDb
{
	connect()
	{
		let connection = mysql.createConnection({
			host     : 'localhost',
			user     : 'root',
			password : 'tiger',
			database : 'vmebel'
		});
		connection.connect();
	},

	/**
	 * product
	 */
	insertProduct(product)
	{
		let post  = {name: 'Hello MySQL', description:'test'};
		let query = connection.query('INSERT INTO products SET ?', post, function(err, result) {
			console.log(err);
		});
	}
}