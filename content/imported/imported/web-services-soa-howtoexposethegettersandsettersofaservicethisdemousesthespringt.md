---
title: How to expose the getters and setters of a Service
nav: How to expose the getters ...
description: How to expose the getters and setters of a Service: this demo uses the Spring to initialize the property of the Service
section: Imported - java2s Archive
order: 1120
source: https://web.archive.org/web/20071026050227/http://www.java2s.com:80/Code/Java/Web-Services-SOA/HowtoexposethegettersandsettersofaServicethisdemousestheSpringtoinitializethepropertyoftheService.htm
---
How to expose the getters and setters of a Service: this demo uses the Spring to initialize the property of the Service

```java title=Example.java
POJO Web Services using Apache Axis2- Sample 2
==============================================
This sample contains source code for the xdocs/1_1/pojoguide.html document found in
the extracted Axis2 Documents Distribution. For a more detailed description on the
source code kindly see this 'POJO Web Services using Apache Axis2' document.
In this specific sample you'll be shown how to take a POJO  (Plain Old Java Object)
based on the Spring Framework, and deploy that as an AAR packaged Web service on Tomcat.
This is a quick way to get a Web service up and running in no time.
Introduction
============
This sample shows how to expose the getters and setters of WeatherSpringService that
takes Weather type Java Object as the argument and the return type. It uses the Spring
framework to initialize the weather property of the WeatherSpringService.
Pre-Requisites
==============
Apache Ant 1.6.2 or later
Spring-1.2.6.jar or later
You need to have this jar in your build and runtime class path. The easiest way to do this
is to copy it to Axis2_HOME/lib directory.
Building the Service
====================
Type $ant from Axis2_HOME/samples/pojoguidespring
Running the Client
==================
Type $ant rpc.client from from Axis2_HOME/samples/pojoguidespring
Help
====
Please contact axis-user list (axis-user@ws.apache.org) if you have any trouble running the sample.
```

AXIS2-pojoguidespring.zip( 9 k)
1.  An example POJO Web service: how to expose the methods of a Java class as a Web service using Aixs2.
2.  This sample shows how to expose a Java class as a web service
3.  In this sample, we are deploying a POJO after writing a services.xml and creating an aar

w___w___w__.___j__a__v_a2s.___c__o__m
