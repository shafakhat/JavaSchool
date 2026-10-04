---
title: log4j Tutorial - Log4j Introduction
nav: log4j Tutorial - Log4j Int...
description: Log4j is a Reliable, Fast and Flexible Logging Framework (APIs) written in Java and distributed under the Apache Software License.
section: Imported - java2s Archive
order: 50041
source: https://www.java2s.com/Tutorials/Java/log4j/index.html
---
- Next »

Log4j is a Reliable, Fast and Flexible Logging Framework (APIs) written in Java and distributed under the Apache Software License.

Log4j is configurable via external configuration files at runtime. It controls the logging process in levels of priorities and has abilities to log information to a variety of destinations, such as a database, file, console, UNIX Syslog etc.

Log4j has three main components:

- loggers: capture logging information.
- appenders: publish logging information to various destinations.
- layouts: format logging information in different styles.

## log4j - Architecture

Log4j API is designed in layered where each layer is different tasks.

There are two type of objects in Log4j framework.

**Core Objects:** are mandatory objects of the framework and required to use the framework.

**Support Objects:** are optional and used by core objects to perform additional tasks.

The Logger object captures logging information.

The layer objects formats logging information in different styles.

The Appender object publishes logging information to various preferred destinations such as a database, file, console, UNIX Syslog etc.

The Level object defines the granularity and priority for logging information. There are seven levels of logging: OFF, DEBUG, INFO, ERROR, WARN, FATAL, and ALL.

The Filter object does the filtering for the information and decides if to log or not.

An Appender objects can have several Filter objects.

The ObjectRenderer object provides a String representation of different objects passed to the logging framework.

The LogManager object manages the logging framework. It reads the initial configuration parameters from a configuration file or a configuration class.

- Next »
