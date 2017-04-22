# movieDatabase


- This web application is designed to allow a superuser add, change, and delete a movie database.
- Users will first register and then are able to filter the database with a faceted search.


### Prerequisites

```
* Python version 2.7, 3.3, 3.4 and 3.5. Python 3+ is recommended.
* Python virtual environment
* Django 1.10+
* MySQL
```

### Installing

* If you’re on Linux or Mac OS X, you probably have Python already installed. Type python at a command prompt (or in Applications/Utilities/Terminal, in OS X).
* Assuming Python is not installed in your system, we first need to get the installer. Go to https://www.python.org/downloads/ and click the big yellow button that says “Download Python 3.x.x”
```
* python -m pip install -U pip 
```
Install virtual environment
```
* pip install virtualenv 
* virtualenv env_mysite 
* env_mysite\scripts\activate 
```
Install MySQL. We are assuming you're using Linux or Mac OS X. If not, check out how to install MySQL on this page: https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html
To install and use a MySQL binary distribution, the command sequence looks like this:
```
shell> groupadd mysql
shell> useradd -r -g mysql -s /bin/false mysql
shell> cd /usr/local
shell> tar zxvf /path/to/mysql-VERSION-OS.tar.gz
shell> ln -s full-path-to-mysql-VERSION-OS mysql
shell> cd mysql
shell> mkdir mysql-files
shell> chmod 750 mysql-files
shell> chown -R mysql .
shell> chgrp -R mysql .
shell> bin/mysql_install_db --user=mysql    # MySQL 5.7.5
shell> bin/mysqld --initialize --user=mysql # MySQL 5.7.6 and up
shell> bin/mysql_ssl_rsa_setup              # MySQL 5.7.6 and up
shell> chown -R root .
shell> chown -R mysql data mysql-files
shell> bin/mysqld_safe --user=mysql &
# Next command is optional
shell> cp support-files/mysql.server /etc/init.d/mysql.server
```
Finally, install Django.
```
* pip install django
```

## Built With

* [Python](https://www.python.org/) - The programming language used.
* [Django](https://www.djangoproject.com/) - The web framework used.
* [Virtual Environment](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) - a tool to keep the dependencies required by different projects in separate places
* [Bootstrap](http://getbootstrap.com/) -  HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.
* [MySQL}(https://www.mysql.com/) - Open source database used to handle and store our data.




## Authors

* **Daniel Ng** - [mdng223](https://github.com/mdng223)
* **Lucian Hymer** - [lucianhymer](https://github.com/lucianhymer)
* **Tristan Basil** - [Immaculato](https://github.com/Immaculato)
* **Katie Long** - [katrinamo](https://github.com/katrinamo)


## Acknowledgments


* This assumes you are using MySQL. You can change what database you use by altering settings.py
* Go to mysite/settings.py and go to lines 93-94 and change the MySQL username/password. 
* This was a good learning process on the use of a MVC framework. 
