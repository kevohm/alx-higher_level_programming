# 0x0E. SQL - More queries
# syntax
* <code> CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';</code>
  * authentication_plugin
    * caching_sha2_password - <i>If you plan to use this database with a PHP application — phpMyAdmin, for example — you may want to create a user that will authenticate with the older, though still secure,this plugin instead</i>
    * mysql_native_password - <i>you can leave out the <code> WITH authentication_plugin </code> portion of the syntax entirely to have the user authenticate with MySQL’s default plugin</i>
    * auth_socket - <i>provides strong security without requiring valid users to enter a password to access the database. But it also prevents remote connections, which can complicate things when external programs need to interact with MySQL.</i>
* <code>GRANT PRIVILEGE ON database.table TO 'username'@'host';</code> - <i>
The <code> PRIVILEGE </code> value in this example syntax defines what actions the user is allowed to perform on the specified database and table. You can grant multiple privileges to the same user in one command by separating each with a comma.You can also grant a user privileges globally by entering asterisks (*) in place of the database and table names. In SQL, asterisks are special characters used to represent “all” databases or tables</i>
* <code> REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';</code><i>If you need to revoke a permission, the structure is almost identical to granting it</i?
# examples
* <code> sudo mysql </code>
* <code> mysql -u root -p </code>
* <code>ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';</code>
* <code>GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;</code>
* <code>GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;</code>
* <code>FLUSH PRIVILEGES;</code><i>Many guides suggest running the FLUSH PRIVILEGES command immediately after a CREATE USER or GRANT statement in order to reload the grant tables to ensure that the new privileges are put into effect</i>
* <code>SHOW GRANTS FOR 'username'@'host';</code>
* <code>DROP USER 'username'@'localhost';</code>
* <code>exit</code><i>After creating your MySQL user and granting them privileges, you can exit the MySQL client,In the future, to log in as your new MySQL user, you’d use a command like the following</i>
* <code>mysql -u sammy -p</code><i>The <code>-p</code> flag will cause the MySQL client to prompt you for your MySQL user’s password in order to authenticate.<i>
