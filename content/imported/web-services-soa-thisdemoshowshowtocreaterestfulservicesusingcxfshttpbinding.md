---
title: This demo shows how to create RESTful services using CXF's HTTP binding
nav: This demo shows how to cre...
description: This demo shows how to create RESTful services using CXF's HTTP binding
section: Imported - java2s Archive
order: 1141
source: https://web.archive.org/web/20071105210638/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoshowshowtocreateRESTfulservicesusingCXFsHTTPbinding.htm
---
This demo shows how to create RESTful services using CXF's HTTP binding

```java title=Example.java
This demo shows how to create RESTful services using CXF's HTTP binding.
The server in the demo creates 3 different endpoints: a RESTful XML
endpoint, a RESTful JSON endpoint, and a SOAP endpoint.
[RUNNING THE DEMO]
The demo has a class called com.acme.customer.Main which starts up various
endpoints. To start this server run the command:
$ ant server
Once it is running try going to the following URLs:
http://localhost:8080/xml/customers
http://localhost:8080/json/customers
http://localhost:8080/xml/customers/123
http://localhost:8080/json/customers/123
These will serve out XML and JSON representation of the resources.
There is an HTML page that is served by CXF so you can try using the
JSON service via Javascript. Just go to:
http://localhost:8080/test.html
Included are some example JSON and XML files so you can add or update
customers using wget. Try the following commands and look at the results:
wget --post-file add.json http://localhost:8080/json/customers
wget --post-file add.xml http://localhost:8080/xml/customers
wget --post-file update.xml http://localhost:8080/xml/customers/123
And if you are interested in SOAP you can try the SOAP endpoint:
http://localhost:8080/soap?wsdl
[RUNNING THE CLIENT]
The demo also includes a Client class which accesses data using
HTTP. To run this demo, do:
$ ant client
```

XFire-CXF-restful_http_binding.zip( 19 k)
1.  REST based Web Services using the HTTP binding and JAX-WS Provider/Dispatch
2.  Axis2 client API has facilities to invoke REST interfaces

w___w___w.___jav___a_2__s_.___c_o__m_
