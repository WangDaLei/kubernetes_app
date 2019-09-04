#!/bin/bash

echo '[mysqld]' >> /etc/mysql.my.cnf
echo 'bind-address=0.0.0.0' >> /etc/mysql.my.cnf
/etc/init.d/mysql start