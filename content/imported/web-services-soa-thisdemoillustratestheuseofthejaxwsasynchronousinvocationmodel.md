---
title: This demo illustrates the use of the JAX-WS asynchronous invocation model
nav: This demo illustrates the ...
description: This demo illustrates the use of the JAX-WS asynchronous invocation model
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20071105012737/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoillustratestheuseoftheJAXWSasynchronousinvocationmodel.htm
---
```java title=Example.java
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
Hello World Asynchronous Demo using Document/Literal Style
==========================================================
This demo illustrates the use of the JAX-WS asynchronous
invocation model. Please refer to the JAX-WS 2.0 specification
(http://jcp.org/aboutJava/communityProcess/pfd/jsr224/index.html)
for background.
The asynchronous model allows the client thread to continue after
making a two-way invocation without being blocked while awaiting a
response from the server. Once the response is available, it is
delivered to the client application asynchronously using one
of two alternative approaches:
- Callback: the client application implements the
javax.xml.ws.AsyncHandler interface to accept notification
of the response availability
- Polling: the client application periodically polls a
javax.xml.ws.Response instance to check if the response
is available
This demo illustrates both approaches.
Additional methods are generated on the Service Endpoint
Interface (SEI) to provide this asynchrony, named by
convention with the suffix "Async".
As many applications will not require this functionality,
the asynchronous variants of the SEI methods are omitted
by default to avoid polluting the SEI with unnecessary
baggage. In order to enable generation of these methods,
a bindings file (wsdl/async_bindings.xml) is passed
to the wsdl2java generator.
Please review the README in the samples directory before
continuing.
Prerequisite
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
From the samples/hello_world_async directory, the ant build script
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
From the samples/hello_world_async directory, run the following wsdl2java
command to generate classes required in the async case.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -b ./wsdl/async_binding.xml -compile ./wsdl/hello_world_async.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -b .\wsdl\async_binding.xml -compile .\wsdl\hello_world_async.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes
  javac -d build/classes src/demo/hw/client/*.java
  javac -d build/classes src/demo/hw/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes
  javac -d build\classes src\demo\hw\client\*.java
  javac -d build\classes src\demo\hw\server\*.java
Running the demo using java
---------------------------
From the samples/hello_world_async directory run the commands, entered on a
single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.client.Client ./wsdl/hello_world_async.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.hw.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hw.client.Client .\wsdl\hello_world_async.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
///////////////////////////////////////////////////////////////////////////////
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
package demo.hw.client;
import java.io.File;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import javax.xml.namespace.QName;
import javax.xml.ws.Response;
import org.apache.hello_world_async_soap_http.GreeterAsync;
import org.apache.hello_world_async_soap_http.SOAPService;
import org.apache.hello_world_async_soap_http.types.GreetMeSometimeResponse;
public final class Client {
    private static final QName SERVICE_NAME
        = new QName("http://apache.org/hello_world_async_soap_http", "SOAPService");
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        if (args.length == 0) {
            System.out.println("please specify wsdl");
            System.exit(1);
        }
        File wsdl = new File(args[0]);
        SOAPService ss = new SOAPService(wsdl.toURL(), SERVICE_NAME);
        ExecutorService executor = Executors.newFixedThreadPool(5);
        ss.setExecutor(executor);
        GreeterAsync port = ss.getSoapPort();
        String resp;
        // callback method
        TestAsyncHandler testAsyncHandler = new TestAsyncHandler();
        System.out.println("Invoking greetMeSometimeAsync using callback object...");
        Future<?> response = port.greetMeSometimeAsync(System.getProperty("user.name"), testAsyncHandler);
        while (!response.isDone()) {
            Thread.sleep(100);
        }
        resp = testAsyncHandler.getResponse();
        System.out.println();
        System.out.println("Server responded through callback with: " + resp);
        System.out.println();
        //polling method
        System.out.println("Invoking greetMeSometimeAsync using polling...");
        Response<GreetMeSometimeResponse> greetMeSomeTimeResp =
            port.greetMeSometimeAsync(System.getProperty("user.name"));
        while (!greetMeSomeTimeResp.isDone()) {
            Thread.sleep(100);
        }
        GreetMeSometimeResponse reply = greetMeSomeTimeResp.get();
        System.out.println("Server responded through polling with: " + reply.getResponseType());
        System.exit(0);
    }
}
///////////////////////////////////////////////////////////////////////////////
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
package demo.hw.client;
import javax.xml.ws.AsyncHandler;
import javax.xml.ws.Response;
import org.apache.hello_world_async_soap_http.types.GreetMeSometimeResponse;
public class TestAsyncHandler implements AsyncHandler<GreetMeSometimeResponse> {
    private GreetMeSometimeResponse reply;
    public void handleResponse(Response<GreetMeSometimeResponse> response) {
        try {
            System.err.println("handleResponse called");
            reply = response.get();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
    public String getResponse() {
        return reply.getResponseType();
    }
}
///////////////////////////////////////////////////////////////////////////////
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
package demo.hw.server;
import java.util.concurrent.Future;
import java.util.logging.Logger;
import javax.jws.WebService;
import javax.xml.ws.AsyncHandler;
import javax.xml.ws.Response;
import org.apache.hello_world_async_soap_http.GreeterAsync;
import org.apache.hello_world_async_soap_http.types.GreetMeSometimeResponse;
@WebService(serviceName = "SOAPService",
            portName = "SoapPort",
            endpointInterface = "org.apache.hello_world_async_soap_http.GreeterAsync",
            targetNamespace = "http://apache.org/hello_world_async_soap_http")
public class GreeterImpl implements GreeterAsync {
    private static final Logger LOG =
        Logger.getLogger(GreeterImpl.class.getPackage().getName());
     /* (non-Javadoc)
     * @see org.apache.hello_world_soap_http.Greeter#greetMeSometime(java.lang.String)
     */
    public String greetMeSometime(String me) {
        LOG.info("Executing operation greetMeSometime");
        System.out.println("Executing operation greetMeSometime\n");
        return "How are you " + me;
    }
    public Future<?>  greetMeSometimeAsync(String requestType,
                                           AsyncHandler<GreetMeSometimeResponse> asyncHandler) {
        return null;
        /*not called */
    }
    public Response<GreetMeSometimeResponse> greetMeSometimeAsync(String requestType) {
        return null;
        /*not called */
    }
}
///////////////////////////////////////////////////////////////////////////////
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
package demo.hw.server;
import javax.xml.ws.Endpoint;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new GreeterImpl();
        String address = "http://localhost:9000/SoapContext/SoapPort";
        Endpoint.publish(address, implementor);
    }
    public static void main(String args[]) throws Exception {
        new Server();
        System.out.println("Server ready...");
        Thread.sleep(5 * 60 * 1000);
        System.out.println("Server exiting");
        System.exit(0);
    }
}
///////////////////////////////////////////////////////////////////////////////
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements. See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership. The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License. You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied. See the License for the
  specific language governing permissions and limitations
  under the License.
-->
<bindings
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    wsdlLocation="hello_world_async.wsdl"
    xmlns="http://java.sun.com/xml/ns/jaxws">
    <bindings node="wsdl:definitions">
        <enableAsyncMapping>true</enableAsyncMapping>
    </bindings>
</bindings>
///////////////////////////////////////////////////////////////////////////////
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements. See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership. The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License. You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied. See the License for the
  specific language governing permissions and limitations
  under the License.
-->
<wsdl:definitions xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://apache.org/hello_world_async_soap_http" xmlns:x1="http://apache.org/hello_world_async_soap_http/types" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://apache.org/hello_world_async_soap_http" name="HelloWorld">
    <wsdl:types>
        <schema targetNamespace="http://apache.org/hello_world_async_soap_http/types" xmlns="http://www.w3.org/2001/XMLSchema" xmlns:x1="http://apache.org/hello_world_async_soap_http/types" elementFormDefault="qualified">
            <element name="greetMeSometime">
                <complexType>
                    <sequence>
                        <element name="requestType" type="xsd:string"/>
                    </sequence>
                </complexType>
            </element>
            <element name="greetMeSometimeResponse">
                <complexType>
                    <sequence>
                        <element name="responseType" type="xsd:string"/>
                    </sequence>
                </complexType>
            </element>
        </schema>
    </wsdl:types>
    <wsdl:message name="greetMeSometimeRequest">
        <wsdl:part name="in" element="x1:greetMeSometime"/>
    </wsdl:message>
    <wsdl:message name="greetMeSometimeResponse">
        <wsdl:part name="out" element="x1:greetMeSometimeResponse"/>
    </wsdl:message>
    <wsdl:portType name="GreeterAsync">
        <wsdl:operation name="greetMeSometime">
            <wsdl:input name="greetMeSometimeRequest" message="tns:greetMeSometimeRequest"/>
            <wsdl:output name="greetMeSometimeResponse" message="tns:greetMeSometimeResponse"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="GreeterAsync_SOAPBinding" type="tns:GreeterAsync">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="greetMeSometime">
            <soap:operation style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="SOAPService">
        <wsdl:port name="SoapPort" binding="tns:GreeterAsync_SOAPBinding">
            <soap:address location="http://localhost:9000/SoapContext/SoapPort"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-hello_world_async.zip( 13 k)
1.  This demo shows a client creating a callback object by passing an EndpointReferenceType to the server
2.  This demo shows how JAX-WS handlers are used
3.  This demo illustrates the use of the JAX-WS APIs to run a simple client against a standalone server using SOAP 1.1 over HTTP
4.  MTOSI 1.1 Samples
5.  This demo shows how to develope an user interceptor and add the interceptor into the interceptor chain through configuration

w_ww.ja_va2_s__._c__o_m_
