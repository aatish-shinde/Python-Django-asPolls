Steps to install Python, Django and MySql
==================================================


python -c "import django; print(django.get_version())"

// for python 3.4
python3 -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"

// run these commands if there is an error in mysql installation
sudo su
export CFLAGS=-Qunused-arguments
export CPPFLAGS=-Qunused-arguments
pip install MySQL-python

// run this command if "libmysqlclient.18.dylib" is not found or if there is an error
ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib	

python manage.py runserver -  to run the server

python manage.py shell - interactive python shell

python manage.py syncdb - syncs the db

// for version 3.4 use migrate command instead of syncdb
python manage.py migrate - syncs the db

python manage.py sql <table_name> - creates the tables in db

 	/*********************/
 	// extra commands to validate the SQL

python manage.py validate – Checks for any errors in the construction of your models.
python manage.py sqlcustom polls – Outputs any custom SQL statements (such as table modifications or constraints) that are defined for the application.
python manage.py sqlclear polls – Outputs the necessary DROP TABLE statements for this app, according to which tables already exist in your database (if any).
python manage.py sqlindexes polls – Outputs the CREATE INDEX statements for this app.
python manage.py sqlall polls – A combination of all the SQL from the sql, sqlcustom, and sqlindexes commands.
