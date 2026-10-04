---
title: JDBC Tutorial - JDBC Introduction
nav: JDBC Tutorial - JDBC Intro...
description: JDBC API is a Java API that can access a Relational Database.
section: Imported - java2s Archive
order: 50038
source: https://www.java2s.com/Tutorials/Java/JDBC/index.html
---
JDBC API is a Java API that can access a Relational Database.

JDBC stands for Java Database Connectivity It is a standard Java API for database-independent connectivity between the Java programming language and databases.

With JDBC APIs we can do the following with database:

- Making a connection to a database
- Creating SQL statements
- Executing that SQL queries in the database
- Viewing & Modifying the resulting records

The JDBC API provides the following interfaces and classes:

- DriverManager: manages a list of database drivers.
- Driver: interface handles the communications with the database server.
- Connection : interface with all methods for contacting a database.
- Statement : submits the SQL statements to the database.
- ResultSet: holds data retrieved from a database after executing an SQL query using Statement objects.
- SQLException: handles any errors that occur in a database application.

The java.sql and javax.sql are the primary packages for JDBC 4.0.
