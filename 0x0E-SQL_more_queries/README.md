# 0x0E. SQL - More queries
* <code> sudo mysql </code>
* <code> mysql -u root -p </code>
* <code> CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';</code
 * authentication_plugin
  * caching_sha2_password - <i>If you plan to use this database with a PHP application — phpMyAdmin, for example — you may want to create a user that will authenticate with the older, though still secure,this plugin instead</i>
  * mysql_native_password - <i>you can leave out the <code> WITH authentication_plugin </code> portion of the syntax entirely to have the user authenticate with MySQL’s default plugin</i>
  * auth_socket - <i>provides strong security without requiring valid users to enter a password to access the database. But it also prevents remote connections, which can complicate things when external programs need to interact with MySQL.</i>
* <code>ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';</code>
