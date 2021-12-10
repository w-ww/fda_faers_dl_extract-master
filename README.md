# fda_faers_dl_extract
Downloads and extracts FDA FAERS data and generates a sql script to read the data into a MYSQL database through MYSQL shell.


fda_faers_dl_extract.py: Downloads and extracts FDA FAERS data
sql_script_gen.py: generates sql script to import data into a MYSQL database through MYSQL Shell


1, in mysql
SET GLOBAL local_infile = 1;

2, run mysqlsh
```
mysqlsh
\connect root@localhost:3306
\use faers
```

http://www.cs.sjsu.edu/~mak/tutorials/MySQLShell.pdf

3, run testfile.sql in Mysql Shell
 \connect root@127.0.0.1:3306 (No password)
 \sql
 use faers;
 \js
 执行testfile.sql

