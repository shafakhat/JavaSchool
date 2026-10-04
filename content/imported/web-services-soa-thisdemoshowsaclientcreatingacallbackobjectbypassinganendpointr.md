---
title: This demo shows a client creating a callback object by passing an EndpointReferenceType to the server
nav: This demo shows a client c...
description: This demo shows a client creating a callback object by passing an EndpointReferenceType to the server
section: Imported - java2s Archive
order: 1138
source: https://web.archive.org/web/20071105235931/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoshowsaclientcreatingacallbackobjectbypassinganEndpointReferenceTypetotheserver.htm
---
This demo shows a client creating a callback object by passing an EndpointReferenceType to the server

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
Callback Demo
=============================================
This demo shows a client creating a callback object by
passing an EndpointReferenceType to the server. The
EndpointRefrenceType is then used by the server to call
back on the callback object
Please review the README in the samples directory before
continuing.
Prerequisite
------------
If your environment already includes cxf-manifest-incubator.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory's README.  If your environment is not
properly configured, or if you are planning on using wsdl2java,
javac, and java to build and run the demos, you must set the
environment.
Building and running the demo using ant
---------------------------------------
From the samples/basic_callback directory, the ant build script
can be used to build and run the demo.
Using either UNIX or Windows:
  ant build
  ant server
  ant client
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Building the demo using wsdl2java and javac
------------------------------------------
From the samples/basic_callback directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/basic_callback.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\basic_callback.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes
  javac -d build/classes src/demo/callback/client/*.java
  javac -d build/classes src/demo/callback/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes
  javac -d build\classes src\demo\callback\client\*.java
  javac -d build\classes src\demo\callback\server\*.java
Running the demo using java
---------------------------
From the samples/basic_callback directory run the commands, entered on a
single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.callback.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.callback.client.Client ./wsdl/basic_callback.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.callback.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.callback.client.Client .\wsdl\basic_callback.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
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
package demo.callback.client;
import org.apache.callback.CallbackPortType;
@javax.jws.WebService(serviceName = "CallbackService",
                      portName = "CallbackPort",
                      endpointInterface = "org.apache.callback.CallbackPortType",
                      targetNamespace = "http://apache.org/callback")
public class CallbackImpl implements CallbackPortType  {
    /**
     * serverSayHi
     * @param: return_message (String)
     * @return: String
     */
    public String serverSayHi(String message) {
        System.out.println("Callback object invoked");
        System.out.println("Message recieved: " + message);
        return new String("Hi " + message);
    }
}
///////////////////////////////////////////////////////////////////
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
package demo.callback.client;
import java.io.File;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Endpoint;
import org.apache.callback.SOAPService;
import org.apache.callback.ServerPortType;
import org.apache.cxf.ws.addressing.EndpointReferenceType;
import org.apache.cxf.wsdl.EndpointReferenceUtils;
public final class Client {
    private static final QName SERVICE_NAME
        = new QName("http://apache.org/callback", "SOAPService");
    private static final QName SERVICE_NAME_CALLBACK
        = new QName("http://apache.org/callback", "CallbackService");
    private static final QName PORT_NAME_CALLBACK
        = new QName("http://apache.org/callback", "CallbackPort");
    private static final QName PORT_TYPE_CALLBACK
        = new QName("http://apache.org/callback", "CallbackPortType");
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        Object implementor = new CallbackImpl();
        String address = "http://localhost:9005/CallbackContext/CallbackPort";
        Endpoint.publish(address, implementor);
        if (args.length == 0) {
            System.out.println("please specify wsdl");
            System.exit(1);
        }
        URL wsdlURL;
        File wsdlFile = new File(args[0]);
        if (wsdlFile.exists()) {
            wsdlURL = wsdlFile.toURL();
        } else {
            wsdlURL = new URL(args[0]);
        }
        SOAPService ss = new SOAPService(wsdlURL, SERVICE_NAME);
        ServerPortType port = ss.getSOAPPort();
        EndpointReferenceType ref =
            EndpointReferenceUtils.getEndpointReference(wsdlURL,
                                                        SERVICE_NAME_CALLBACK,
                                                        PORT_NAME_CALLBACK.getLocalPart());
        EndpointReferenceUtils.setInterfaceName(ref, PORT_TYPE_CALLBACK);
        String resp = port.registerCallback(ref);
        System.out.println("Response from server: " + resp);
        System.exit(0);
    }
}
/////////////////////////////////////////////////////////////////
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
package demo.callback.server;
import javax.xml.ws.Endpoint;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new ServerImpl();
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
/////////////////////////////////////////////////////////////
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
package demo.callback.server;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import org.apache.callback.CallbackPortType;
import org.apache.callback.ServerPortType;
import org.apache.cxf.jaxb.JAXBUtils;
import org.apache.cxf.ws.addressing.EndpointReferenceType;
import org.apache.cxf.wsdl.EndpointReferenceUtils;
import org.apache.cxf.wsdl.WSDLManager;
import org.apache.cxf.wsdl11.WSDLManagerImpl;
@javax.jws.WebService(serviceName = "SOAPService",
                      portName = "SOAPPort",
                      targetNamespace = "http://apache.org/callback",
                      endpointInterface = "org.apache.callback.ServerPortType")
public class ServerImpl implements ServerPortType  {
    public String registerCallback(EndpointReferenceType callback) {
        try {
            WSDLManager manager = new WSDLManagerImpl();
            QName interfaceName = EndpointReferenceUtils.getInterfaceName(callback);
            String wsdlLocation = EndpointReferenceUtils.getWSDLLocation(callback);
            QName serviceName = EndpointReferenceUtils.getServiceName(callback);
            String portString = EndpointReferenceUtils.getPortName(callback);
            QName portName = new QName(serviceName.getNamespaceURI(), portString);
            StringBuffer seiName = new StringBuffer();
            seiName.append(JAXBUtils.namespaceURIToPackage(interfaceName.getNamespaceURI()));
            seiName.append(".");
            seiName.append(JAXBUtils.nameToIdentifier(interfaceName.getLocalPart(),
                                                      JAXBUtils.IdentifierType.INTERFACE));
            System.out.println("the seiname is " + seiName.toString());
            Class<?> sei = null;
            try {
                sei = Class.forName(seiName.toString(),
                                    true, manager.getClass().getClassLoader());
            } catch (ClassNotFoundException ex) {
                ex.printStackTrace();
            }
            URL wsdlURL = new URL(wsdlLocation);
            Service service = Service.create(wsdlURL, serviceName);
            CallbackPortType port =  (CallbackPortType)service.getPort(portName, sei);
            System.out.println("Invoking on callback object");
            String resp = port.serverSayHi(System.getProperty("user.name"));
            System.out.println("Response from callback object: " + resp);
        } catch (Exception ex) {
            ex.printStackTrace();
            return null;
        }
        return "registerCallback called";
    }
}
///////////////////////////////////////////////////////////////////
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
<wsdl:definitions name="basic_callback" targetNamespace="http://apache.org/callback"
      xmlns="http://schemas.xmlsoap.org/wsdl/"
      xmlns:references="http://www.w3.org/2005/08/addressing"
      xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
      xmlns:tns="http://apache.org/callback"
      xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:jaxb="http://java.sun.com/xml/ns/jaxb" jaxb:version="2.0">
    <wsdl:types>
  <schema targetNamespace="http://apache.org/callback"
    xmlns="http://www.w3.org/2001/XMLSchema"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:jaxb="http://java.sun.com/xml/ns/jaxb"
    jaxb:version="2.0">
      <xsd:import namespace="http://www.w3.org/2005/08/addressing" schemaLocation="/schemas/wsdl/ws-addr.xsd"/>
      <element name="callback_message" type="xsd:string"/>
      <element name="RegisterCallback" type="references:EndpointReferenceType"/>
      <element name="returnType" type="xsd:string"/>
  </schema>
    </wsdl:types>
    <wsdl:message name="server_sayHi">
  <wsdl:part element="tns:callback_message" name="return_message"/>
    </wsdl:message>
    <wsdl:message name="register_callback">
  <wsdl:part element="tns:RegisterCallback" name="callback_object"/>
    </wsdl:message>
    <wsdl:message name="returnMessage">
  <wsdl:part element="tns:returnType" name="the_return"/>
    </wsdl:message>
    <wsdl:portType name="CallbackPortType">
  <wsdl:operation name="ServerSayHi">
      <wsdl:input message="tns:server_sayHi" name="ServerSayHiRequest"/>
      <wsdl:output message="tns:returnMessage" name="ServerSayHiResponse"/>
  </wsdl:operation>
    </wsdl:portType>
    <wsdl:portType name="ServerPortType">
  <wsdl:operation name="RegisterCallback">
      <wsdl:input message="tns:register_callback" name="RegisterCallbackRequest"/>
      <wsdl:output message="tns:returnMessage" name="RegisterCallbackResponse"/>
  </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="CallbackPortType_SOAPBinding" type="tns:CallbackPortType">
  <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
  <wsdl:operation name="ServerSayHi">
      <soap:operation soapAction="" style="document"/>
      <wsdl:input name="ServerSayHiRequest">
    <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ServerSayHiResponse">
    <soap:body use="literal"/>
      </wsdl:output>
  </wsdl:operation>
    </wsdl:binding>
    <wsdl:binding name="ServerPortType_SOAPBinding" type="tns:ServerPortType">
  <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
  <wsdl:operation name="RegisterCallback">
      <soap:operation soapAction="" style="document"/>
      <wsdl:input name="RegisterCallbackRequest">
    <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="RegisterCallbackResponse">
    <soap:body use="literal"/>
      </wsdl:output>
  </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="CallbackService">
  <wsdl:port binding="tns:CallbackPortType_SOAPBinding" name="CallbackPort">
      <soap:address location="http://localhost:9005/CallbackContext/CallbackPort"/>
  </wsdl:port>
    </wsdl:service>
    <wsdl:service name="SOAPService">
  <wsdl:port binding="tns:ServerPortType_SOAPBinding" name="SOAPPort">
      <soap:address location="http://localhost:9000/SoapContext/SoapPort"/>
  </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-callback.zip( 12 k)
1.  This demo shows how JAX-WS handlers are used
2.  This demo illustrates the use of the JAX-WS APIs to run a simple client against a standalone server using SOAP 1.1 over HTTP
3.  This demo illustrates the use of the JAX-WS asynchronous invocation model
4.  MTOSI 1.1 Samples
5.  This demo shows how to develope an user interceptor and add the interceptor into the interceptor chain through configuration

ww__w___._j_av_a___2_s__.co__m
