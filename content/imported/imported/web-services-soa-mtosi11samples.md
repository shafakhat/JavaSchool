---
title: MTOSI 1.1 Samples
nav: MTOSI 1.1 Samples
description: alarm_retrieval - contains a simple sample implementation of the
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/20071105161255/http://www.java2s.com:80/Code/Java/Web-Services-SOA/MTOSI11Samples.htm
---
```java title=Example.java
=================
mtosi_1.1 contains the following subdirectories:
wsdl            - contains the mtosi 1.1 wsdls
xsd             - contains the mtosi 1.1 schemas
alarm_retrieval - contains a simple sample implementation of the
                  alarm_retrieval mtosi interface.  Please refer to
                  the alarm_retrieval/README.txt for instructions to
                  run that demo.
code_gen        - contains targets for generating code for mtosi
                  interfaces which do not have a sample implementation
Going beyond the basic sample
=============================
You can use the alarm_retrieval demo as a template for implementing
any of the other mtosi interfaces.  The code_gen directory
demonstrates the wsdl2java targets needed to generate code for the
remaining mtosi interfaces.
```

XFire-CXF-mtosi_1.1.zip( 152 k)
1.  This demo shows a client creating a callback object by passing an EndpointReferenceType to the server
2.  This demo shows how JAX-WS handlers are used
3.  This demo illustrates the use of the JAX-WS APIs to run a simple client against a standalone server using SOAP 1.1 over HTTP
4.  This demo illustrates the use of the JAX-WS asynchronous invocation model
5.  This demo shows how to develope an user interceptor and add the interceptor into the interceptor chain through configuration

w_w___w___._ja_v_a_2___s.c_o_m__
