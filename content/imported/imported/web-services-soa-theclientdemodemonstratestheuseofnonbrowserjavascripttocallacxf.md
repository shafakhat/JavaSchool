---
title: The client demo demonstrates the use of (non-browser) JavaScript to call a CXF server
nav: The client demo demonstrat...
description: The client demo demonstrates the use of (non-browser) JavaScript to call a CXF server
section: Imported - java2s Archive
order: 1129
source: https://web.archive.org/web/20080513030309/http://www.java2s.com/Code/Java/Web-Services-SOA/TheclientdemodemonstratestheuseofnonbrowserJavaScripttocallaCXFserver.htm
---
```java title=Example.java
Hello World Client Demo using JavaScript
=========================================================
The client demo demonstrates the use of (non-browser)
JavaScript to call a CXF server.
The client side makes call by JAXWS. It uses the Mozilla Rhino library
to read the JavaScript file and run it.
Building and running the demo server using ant
---------------------------------------
From the samples/hello_world directory, the ant build script
can be used to build and run the demo.
Using either UNIX or Windows:
  ant build
  ant server  (in the background or another window)
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Running the JavaScript client
-----------------------------
In another command line window, run the ant "client" target from
the build.xml file located in the same directory as this README.
Using either UNIX or Windows:
  ant client
When running the client, you can terminate the server process by issuing
Ctrl-C in its command window.
The client will show this output:
invoke sayHi().   return Bonjour
invoke greetMe(String).   return Hello Jeff
The same time, the server will give this output:
     [java] Executing operation sayHi
     [java] Executing operation greetMe
     [java] Message received: Jeff
////////////////////////////////////////////////////////////////
/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
importPackage(Packages.java.io);
importPackage(Packages.javax.xml.namespace);
importPackage(Packages.org.apache.hello_world_soap_http);
var qname=new Packages.javax.xml.namespace.QName("http://apache.org/hello_world_soap_http", "SOAPService");
var curpath=new File("..");
var sepa=File.separator;
var hwpath=curpath.getAbsolutePath()+sepa+"hello_world"+sepa+"wsdl"+sepa+"hello_world.wsdl";
var url = new File(hwpath).toURL();
var ss=new SOAPService(url,qname);
var port = ss.getSoapPort();
var resp=port.sayHi();
print("invoke sayHi().   return " + resp);
resp=port.greetMe("Jeff");
print("invoke greetMe(String).   return " + resp);
```

XFire-CXF-js_client.zip( 5 k)
1.  The demo demonstrates the use of the JavaScript and E4X dynamic languages to implement JAX-WS Providers
2.  Axis2 client API has facilities to accept responses in JSON
