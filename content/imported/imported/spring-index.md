---
title: Spring Tutorial - Spring Introduction
nav: Spring Tutorial - Spring I...
description: Spring is a framework for building Java applications. We can use Spring to build any application in Java, for example, stand-alone, web, or Java Enterprise Edition (JEE)
section: Imported - java2s Archive
order: 50037
source: https://www.java2s.com/Tutorials/Java/Spring/index.html
---
- Next »

Spring is a framework for building Java applications. We can use Spring to build any application in Java, for example, stand-alone, web, or Java Enterprise Edition (JEE) applications).

Spring's philosophy is minimal impact.

Spring is lightweight in the sense that we have to make few, if any, changes to your application code to gain the benefits of the Spring core.

## Inverting Control or Injecting Dependencies

The core of the Spring Framework is based on the principle of Inversion of Control (IoC).

IoC is a technique that externalizes the creation and management of component dependencies.

Spring's Injecting Dependencies implementation is based on two core Java concepts:

- JavaBeans
- interfaces

The benefits of using DI rather than a more traditional approach:

- Reduce glue code
- Simplified application configuration
- Manage common dependencies in a single repository
- Improve testability
- Promote good application design

## Spring Features

Spring offers many modules, features and functions.

- Aspect-Oriented Programming with Spring. AOP provides the ability to implement crosscutting logic, which applies to many parts of your application, in a single place.
- Spring Expression Language. Expression Language (EL) allows us to manipulate Java objects at runtime.
- Validation in Spring. Spring provides a built-in validation API by way of the Validator interface.
- Accessing Data in Spring. Spring provides integration with a choice selection of these data access tools. In addition, Spring makes plain vanilla JDBC a viable option for many projects, with its simplified wrapper APIs around the standard API. Spring's data access module provides out-of-the-box support for JDBC, Hibernate, JDO, and the JPA.
- Object/XML Mapping in Spring. Spring supports many common Java-to-XML mapping frameworks and, as usual, eliminates the need for directly coupling to any specific implementation.
- Managing Transactions. Spring provides an abstraction layer for transaction management, allowing for programmatic and declarative transaction control.
- Simplifying and Integrating with JEE
- MVC in the Web Tier
- WebSocket Support
- Remoting Support
- Mail Support
- Job Scheduling Support
- Dynamic Scripting Support
- Simplified Exception Handling

## Spring Modules

Spring version 4.0.2.RELEASE comes with 20 modules, packaged into 20 JAR files.

The following table describes these JAR files and their corresponding modules.

JAR File  Description
---  ---
aop  Spring's AOP features
aspects  For Advanced integration with the AspectJ AOP library.
beans  For Spring's manipulation of Spring beans.
context  Provide many extensions to the Spring core.
context-support  Further extensions to the spring-context module.
core  Core module for every Spring application.
expression  Support for Spring Expression Language (SpEL).
instrument  Spring's instrumentation agent for Java Virtual Machine (JVM) bootstrapping.
instrument-tomcat  Spring's instrumentation agent for JVM bootstrapping in the Tomcat server.
jdbc  For JDBC support.
jms  For JMS support.
messaging  For message-based applications and adds support for STOMP messages.
orm  Spring's standard JDBC feature set with support for popular ORM tools including Hibernate, JDO, JPA.
oxm  Support for Object/XML Mapping (OXM).
test  Mock classes to aid in testing your applications.
tx  For supporting Spring's transaction infrastructure.
web  For using Spring in your web applications
webmvc  For Spring's own MVC framework.
web-portlet  For using Spring MVC in developing portlets for deployment to a portal server environment.
websocket  For the Java API for WebSocket (JSR-356).

- Next »
