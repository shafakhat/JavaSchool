---
title: REST based Web Services using the HTTP binding and JAX-WS Provider/Dispatch
nav: REST based Web Services us...
description: REST based Web Services using the HTTP binding and JAX-WS Provider/Dispatch
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/20071105054012/http://www.java2s.com:80/Code/Java/Web-Services-SOA/RESTbasedWebServicesusingtheHTTPbindingandJAXWSProviderDispatch.htm
---
```java title=Example.java
RESTful Hello World Demo
========================
The demo shows REST based Web Services using the HTTP binding and
JAX-WS Provider/Dispatch. The REST server provides the following services:
A RESTful customer service is provided on URL http://localhost:9000/customerservice/customer.
Users access this URI to query or update customer info.
A HTTP GET request to URL http://localhost:9000/customerservice/customer returns
a list of customer hyperlinks. This allows client navigates through the
application states. The XML document returned:
<Customers>
  <Customer href="http://localhost/customerservice/customer?id=1234">
      <id>1234</id>
  </Customer>
  <Customer href="http://localhost/customerservice/customer?id=1235">
      <id>1235</id>
  </Customer>
  <Customer href="http://localhost/customerservice/customer?id=1236">
      <id>1236</id>
  </Customer>
</Customers>
A HTTP GET request to URL http://localhost:9000/customerservice/customer?id=1234
returns a customer instance whose id is 1234. The XML document returned:
<Customer>
  <id>1234</id>
  <name>John</name>
  <phoneNumber>123456</phoneNumber>
</Customer>
A HTTP POST request to URL http://localhost:9000/customerservice/customer
with the data:
<Customer>
  <id>1234</id>
  <name>John</name>
  <phoneNumber>123456</phoneNumber>
</Customer>
updates customer 1234 with the data provided.
The client code demonstrates how to send HTTP POST with XML data using
JAX-WS Dispatch and how to send HTTP GET using URL.openStream(). The
server code demonstrates how to build a RESTful endpoints through
JAX-WS Provider interface.
Please review the README in the samples directory before
continuing.
Prerequisites
------------
If your environment already includes cxf-manifest-incubator.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory README.  If your environment is not
properly configured, or if you are planning on using wsdl2java,
javac, and java to build and run the demos, you must set the
environment.
Building and running the demo using ant
---------------------------------------
From the samples/restful directory, the ant build script
can be used to build and run the demo.
Using either UNIX or Windows:
  ant build
  ant server
  ant client
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Building the demo using wsdl2java and javac
-------------------------------------------
From the samples/restful directory, first create the target
directory build/classes and then compile the provided client
and server applications with the commands:
For UNIX:
  mkdir -p build/classes
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes
  javac -d build/classes src/demo/restful/client/*.java
  javac -d build/classes src/demo/restful/server/*.java
For Windows:
  mkdir build\classes
    Must use back slashes.
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes
  javac -d build\classes src\demo\restful\client\*.java
  javac -d build\classes src\demo\restful\server\*.java
Finally, copy resource files into the build/classes directory with the commands:
For UNIX:
  cp ./src/demo/restful/client/*.xml ./build/classes/demo/restful/client
  cp ./src/demo/restful/server/*.xml ./build/classes/demo/restful/server
For Windows:
  copy src\demo\restful\client\*.xml build\classes\demo\restful\client
  copy src\demo\restful\server\*.xml build\classes\demo\restful\server
Running the demo using java
---------------------------
From the samples/restful directory run the following commands. They
are entered on a single command line.
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.restful.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.restful.client.Client
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.restful.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.restful.client.Client
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
//////////////////////////////////////////////////////////////////////////
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
package demo.restful.client;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.net.URI;
import java.net.URL;
import java.util.Map;
import java.util.Properties;
import javax.xml.namespace.QName;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import javax.xml.ws.Dispatch;
import javax.xml.ws.Service;
import javax.xml.ws.handler.MessageContext;
import javax.xml.ws.http.HTTPBinding;
import org.w3c.dom.Document;
import org.apache.cxf.helpers.XMLUtils;
public final class Client {
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        QName serviceName = new QName("http://apache.org/hello_world_xml_http/wrapped",
                                                "cutomerservice");
        QName portName = new QName("http://apache.org/hello_world_xml_http/wrapped",
                                             "RestProviderPort");
        String endpointAddress = "http://localhost:9000/customerservice/customer";
        // Sent HTTP GET request to query all customer info
        URL url = new URL(endpointAddress);
        System.out.println("Invoking server through HTTP GET to query all customer info");
        InputStream in = url.openStream();
        StreamSource source = new StreamSource(in);
        printSource(source);
        // Sent HTTP GET request to query customer info
        url = new URL(endpointAddress + "?id=1234");
        System.out.println("Invoking server through HTTP GET to query customer info");
        in = url.openStream();
        source = new StreamSource(in);
        printSource(source);
        // Sent HTTP POST request to update customer info using JAX-WS Dispatch
        URI endpointURI = new URI(endpointAddress.toString());
        String path = null;
        if (endpointURI != null) {
            path = endpointURI.getPath();
        }
        Service service = Service.create(serviceName);
        service.addPort(portName, HTTPBinding.HTTP_BINDING,  endpointAddress);
        Dispatch<DOMSource> dispatcher = service.createDispatch(portName,
                                                                DOMSource.class, Service.Mode.PAYLOAD);
        Map<String, Object> requestContext = dispatcher.getRequestContext();
        Client client = new Client();
        InputStream is = client.getClass().getResourceAsStream("CustomerJohnReq.xml");
        Document doc = XMLUtils.parse(is);
        DOMSource reqMsg = new DOMSource(doc);
        requestContext.put(MessageContext.HTTP_REQUEST_METHOD, "POST");
        System.out.println("Invoking through HTTP POST to update customer using JAX-WS Dispatch");
        DOMSource result = dispatcher.invoke(reqMsg);
        printSource(result);
        System.out.println("Client Invoking is succeeded!");
        System.exit(0);
    }
    private static void printSource(Source source) {
        try {
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            StreamResult sr = new StreamResult(bos);
            Transformer trans = TransformerFactory.newInstance().newTransformer();
            Properties oprops = new Properties();
            oprops.put(OutputKeys.OMIT_XML_DECLARATION, "yes");
            trans.setOutputProperties(oprops);
            trans.transform(source, sr);
            System.out.println("**** Response ******");
            System.out.println(bos.toString());
            bos.close();
            System.out.println();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
//////////////////////////////////////////////////////////////////////////
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
package demo.restful.server;
import java.io.InputStream;
import javax.annotation.Resource;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.ws.Provider;
import javax.xml.ws.Service;
import javax.xml.ws.ServiceMode;
import javax.xml.ws.WebServiceContext;
import javax.xml.ws.WebServiceProvider;
import javax.xml.ws.handler.MessageContext;
import org.w3c.dom.Document;
import org.apache.cxf.message.Message;
@WebServiceProvider()
@ServiceMode(value = Service.Mode.PAYLOAD)
public class RestSourcePayloadProvider implements Provider<DOMSource> {
    @Resource
    protected WebServiceContext wsContext;
    public RestSourcePayloadProvider() {
    }
    public DOMSource invoke(DOMSource request) {
        MessageContext mc = wsContext.getMessageContext();
        String path = (String)mc.get(Message.PATH_INFO);
        String query = (String)mc.get(Message.QUERY_STRING);
        String httpMethod = (String)mc.get(Message.HTTP_REQUEST_METHOD);
        System.out.println("--path--- " + path);
        System.out.println("--query--- " + query);
        System.out.println("--httpMethod--- " + httpMethod);
        if (httpMethod.equalsIgnoreCase("POST")) {
            // TBD: parse query info from DOMSource
            System.out.println("---Invoking updateCustomer---");
            return updateCustomer(request);
        } else if (httpMethod.equalsIgnoreCase("GET")) {
            if (path.equals("/customerservice/customer") && query == null) {
                System.out.println("---Invoking getAllCustomers---");
                return getAllCustomers();
            } else if (path.equals("/customerservice/customer") && query != null) {
                System.out.println("---Invoking getCustomer---");
                return getCustomer(query);
            }
        }
        return null;
    }
    private DOMSource getAllCustomers() {
        return createDOMSource("CustomerAllResp.xml");
    }
    private DOMSource getCustomer(String customerID) {
        return createDOMSource("CustomerJohnResp.xml");
    }
    private DOMSource updateCustomer(DOMSource request) {
        // TBD: returned update customer info
        return createDOMSource("CustomerJohnResp.xml");
    }
    private DOMSource createDOMSource(String fileName) {
        DocumentBuilderFactory factory;
        DocumentBuilder builder;
        Document document = null;
        DOMSource response = null;
        try {
            factory = DocumentBuilderFactory.newInstance();
            //factory.setValidating(true);
            builder = factory.newDocumentBuilder();
            InputStream greetMeResponse = getClass().getResourceAsStream(fileName);
            document = builder.parse(greetMeResponse);
            response = new DOMSource(document);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return response;
    }
}
//////////////////////////////////////////////////////////////////////////
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
package demo.restful.server;
import javax.xml.ws.Endpoint;
import javax.xml.ws.http.HTTPBinding;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Endpoint e = Endpoint.create(HTTPBinding.HTTP_BINDING, new RestSourcePayloadProvider());
        String address = "http://localhost:9000/customerservice/customer";
        e.publish(address);
    }
    public static void main(String args[]) throws Exception {
        new Server();
        System.out.println("Server ready...");
        Thread.sleep(5 * 60 * 1000);
        System.out.println("Server exiting");
        System.exit(0);
    }
}
```

XFire-CXF-restful_dispatch.zip( 13 k)
1.  This demo shows how to create RESTful services using CXF's HTTP binding
2.  Axis2 client API has facilities to invoke REST interfaces

w__w___w.j_a_v__a2_s_.co_m___
