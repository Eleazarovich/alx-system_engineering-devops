# puppet script to fix error 500 in Apache server
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
