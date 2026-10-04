---
title: In this sample, we are deploying a POJO after writing a services.xml and creating an aar
nav: In this sample, we are dep...
description: In this sample, we are deploying a POJO after writing a services.xml and creating an aar
section: Imported - java2s Archive
order: 1123
source: https://web.archive.org/web/20071026050722/http://www.java2s.com:80/Code/Java/Web-Services-SOA/InthissamplewearedeployingaPOJOafterwritingaservicesxmlandcreatinganaar.htm
---
In this sample, we are deploying a POJO after writing a services.xml and creating an aar

```java title=Example.java
Axis2 Quick Start Guide- Sample 1
=================================
This sample contains source code for the xdocs/1_1/quickstartguide.html document found in
the extracted Axis2 Documents Distribution. For a more detailed description on the
source code kindly see this 'Axis2 Quick Start Guide' document.
Introduction
============
In this sample, we are deploying a POJO after writing a services.xml and
creating an aar. We also test the getPrice and update methods using a browser.
Pre-Requisites
==============
Apache Ant 1.6.2 or later
Building the Service
====================
Type "ant generate.service" or just "ant" from Axis2_HOME/samples/quickstart directory
and then deploy the Axis2_HOME/samples/quickstart/build/StockQuoteService.aar
Generate WSDL
==============
Type "ant generate.wsdl" from Axis2_HOME/samples/quickstart directory which generates a
WSDL file for the above Web service and it will be placed in Axis2_HOME/samples/quickstart/build
directory.
Running the Client
==================
- From your browser, If you point to the following URL:
http://localhost:8080/axis2/services/StockQuoteService/getPrice?symbol=IBM
You will get the following response:
<ns:getPriceResponse><ns:return>42.0</ns:return></ns:getPriceResponse>
- If you invoke the update method like so:
http://localhost:8080/axis2/services/StockQuoteService/update?symbol=IBM&price=100
And then execute the first getPrice url. You can see that the price got updated.
Help
====
Please contact axis-user list (axis-user@ws.apache.org) if you have any trouble running the sample.
```

AXIS2-quickstart.zip( 5 k)
1.  An example POJO Web service: how to expose the methods of a Java class as a Web service using Aixs2.
2.  This sample shows how to expose a Java class as a web service
3.  How to expose the getters and setters of a Service: this demo uses the Spring to initialize the property of the Service

w___w__w_._j___av___a_2___s.__c___o___m___
