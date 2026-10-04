---
title: The demo demonstrates the use of the JavaScript and E4X dynamic languages to implement JAX-WS Providers
nav: The demo demonstrates the ...
description: The demo demonstrates the use of the JavaScript and E4X dynamic languages to implement JAX-WS Providers
section: Imported - java2s Archive
order: 1130
source: https://web.archive.org/web/20080513031103/http://www.java2s.com/Code/Java/Web-Services-SOA/ThedemodemonstratestheuseoftheJavaScriptandE4XdynamiclanguagestoimplementJAXWSProviders.htm
---
```java title=Example.java
Hello World Demo using JavaScript and E4X Implementations
=========================================================
The demo demonstrates the use of the JavaScript and E4X dynamic
languages to implement JAX-WS Providers.
The client side makes two Dispatch-based invocations. The first uses
SOAPMessage data in MESSAGE mode, and the second uses DOMSource in
PAYLOAD mode. The first service is implemented using E4X, the second
using JavaScript.
The two messages are constructed by reading in the XML files found in
the demo/hwDispatch/client directory.
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
From the samples/js_provider directory, the ant build script
can be used to build and run the demo.
Using either UNIX or Windows:
  ant build
  ant server  (in the background or another window)
  ant client
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Building the demo using wsdl2java and javac
-------------------------------------------
From the samples/dispatch_provider directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes ./wsdl/hello_world.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes .\wsdl\hello_world.wsdl
    May use either forward or back slashes.
Now compile both the generated code and the provided client
application with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:
  $CXF_HOME/lib/js-1.6R5.jar:$CXF_HOME/lib/xbean-2.2.0.jar:
  build/classes
  javac -d build/classes src/demo/hwDispatch/client/*.java
For Windows:
  set CLASSPATH=%CLASSPATH%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;
  %CXF_HOME%\lib\js-1.6R5.jar;%CXF_HOME%\lib\xbean-2.2.0.jar;
  build\classes
  javac -d build\classes src\demo\hwDispatch\client\*.java
Windows may use either forward or back slashes.
Since JavaScript and E4X are interpreted at runtime and do not require
compilation, there is no server-side java code requiring compilation.
Finally, copy resource files into the build/classes directory with the commands:
For UNIX:
  cp ./src/demo/hwDispatch/client/*.xml ./build/classes/demo/hwDispatch/client
For Windows:
  copy src\demo\hwDispatch\client\*.xml build\classes\demo\hwDispatch\client
Running the demo using java
---------------------------
From the samples/js_dispatch directory run the commands, entered on a
single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         org.apache.cxf.js.rhino.ServerApp -v
         -b http://localhost:9000/SoapContext impl.jsx impl.js
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hwDispatch.client.Client ./wsdl/hello_world.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         org.apache.cxf.js.rhino.ServerApp -v
         -b http://localhost:9000/SoapContext impl.jsx impl.js
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hwDispatch.client.Client .\wsdl\hello_world.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
///////////////////////////////////////////////////////////////////////
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
package demo.hwDispatch.client;
import java.io.File;
import java.io.InputStream;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.soap.MessageFactory;
import javax.xml.soap.SOAPMessage;
import javax.xml.transform.dom.DOMSource;
import javax.xml.ws.Dispatch;
import javax.xml.ws.Service.Mode;
import org.apache.hello_world_soap_http.SOAPService1;
import org.apache.hello_world_soap_http.SOAPService3;
public final class Client {
    private Client() {
    }
    public static void main(String args[]) throws Exception {
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
        MessageFactory factory = MessageFactory.newInstance();
        System.out.println(wsdlURL + "\n\n");
        final String ns = "http://apache.org/hello_world_soap_http";
        QName serviceName1 = new QName(ns, "SOAPService1");
        QName portName1 = new QName(ns, "SoapPort1");
        SOAPService1 service1 = new SOAPService1(wsdlURL, serviceName1);
        InputStream is1 =  Client.class.getResourceAsStream("GreetMeDocLiteralReq1.xml");
        SOAPMessage soapReq1 = factory.createMessage(null, is1);
        Dispatch<SOAPMessage> dispSOAPMsg = service1.createDispatch(portName1,
                                                                    SOAPMessage.class, Mode.MESSAGE);
        System.out.println("Invoking server through Dispatch interface using SOAPMessage");
        SOAPMessage soapResp = dispSOAPMsg.invoke(soapReq1);
        System.out.println("Response from server: " + soapResp.getSOAPBody().getTextContent());
        QName serviceName3 = new QName(ns, "SOAPService3");
        QName portName3 = new QName(ns, "SoapPort3");
        SOAPService3 service3 = new SOAPService3(wsdlURL, serviceName3);
        InputStream is3 =  Client.class.getResourceAsStream("GreetMeDocLiteralReq3.xml");
        SOAPMessage soapReq3 = MessageFactory.newInstance().createMessage(null, is3);
        DOMSource domReqPayload = new DOMSource(soapReq3.getSOAPBody().extractContentAsDocument());
        Dispatch<DOMSource> dispDOMSrcPayload = service3.createDispatch(portName3,
                                                                        DOMSource.class, Mode.PAYLOAD);
        System.out.println("Invoking server through Dispatch interface using DOMSource in PAYLOAD Mode");
        DOMSource domRespPayload = dispDOMSrcPayload.invoke(domReqPayload);
        System.out.println("Response from server: "
                           + domRespPayload.getNode().getFirstChild().getTextContent());
        System.exit(0);
    }
}
////////////////////////////////////////////////////////////////////////////////
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
<wsdl:definitions name="HelloWorld" targetNamespace="http://apache.org/hello_world_soap_http"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://apache.org/hello_world_soap_http"
    xmlns:x1="http://apache.org/hello_world_soap_http/types"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:types>
        <schema targetNamespace="http://apache.org/hello_world_soap_http/types"
            xmlns="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
            <element name="sayHi">
                <complexType/>
            </element>
            <element name="sayHiResponse">
                <complexType>
                    <sequence>
                        <element name="responseType" type="xsd:string"/>
                    </sequence>
                </complexType>
            </element>
            <element name="greetMe">
                <complexType>
                    <sequence>
                        <element name="requestType" type="xsd:string"/>
                    </sequence>
                </complexType>
            </element>
            <element name="greetMeResponse">
                <complexType>
                    <sequence>
                        <element name="responseType" type="xsd:string"/>
                    </sequence>
                </complexType>
            </element>
            <element name="greetMeOneWay">
                <complexType>
                    <sequence>
                        <element name="requestType" type="xsd:string"/>
                    </sequence>
                </complexType>
            </element>
          <element name="pingMe">
        <complexType/>
      </element>
      <element name="pingMeResponse">
        <complexType/>
      </element>
      <element name="faultDetail">
        <complexType>
          <sequence>
            <element name="minor" type="xsd:short"/>
            <element name="major" type="xsd:short"/>
          </sequence>
        </complexType>
      </element>
        </schema>
    </wsdl:types>
    <wsdl:message name="sayHiRequest">
        <wsdl:part element="x1:sayHi" name="in"/>
    </wsdl:message>
    <wsdl:message name="sayHiResponse">
        <wsdl:part element="x1:sayHiResponse" name="out"/>
    </wsdl:message>
    <wsdl:message name="greetMeRequest">
        <wsdl:part element="x1:greetMe" name="in"/>
    </wsdl:message>
    <wsdl:message name="greetMeResponse">
        <wsdl:part element="x1:greetMeResponse" name="out"/>
    </wsdl:message>
    <wsdl:message name="greetMeOneWayRequest">
        <wsdl:part element="x1:greetMeOneWay" name="in"/>
    </wsdl:message>
    <wsdl:portType name="Greeter">
        <wsdl:operation name="sayHi">
            <wsdl:input message="tns:sayHiRequest" name="sayHiRequest"/>
            <wsdl:output message="tns:sayHiResponse" name="sayHiResponse"/>
        </wsdl:operation>
        <wsdl:operation name="greetMe">
            <wsdl:input message="tns:greetMeRequest" name="greetMeRequest"/>
            <wsdl:output message="tns:greetMeResponse" name="greetMeResponse"/>
        </wsdl:operation>
        <wsdl:operation name="greetMeOneWay">
            <wsdl:input message="tns:greetMeOneWayRequest" name="greetMeOneWayRequest"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="Greeter_SOAPBinding" type="tns:Greeter">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="sayHi">
            <soap:operation soapAction="" style="document"/>
            <wsdl:input name="sayHiRequest">
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output name="sayHiResponse">
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="greetMe">
            <soap:operation soapAction="" style="document"/>
            <wsdl:input name="greetMeRequest">
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output name="greetMeResponse">
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="greetMeOneWay">
            <soap:operation soapAction="" style="document"/>
            <wsdl:input name="greetMeOneWayRequest">
                <soap:body use="literal"/>
            </wsdl:input>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="SOAPService1">
        <wsdl:port binding="tns:Greeter_SOAPBinding" name="SoapPort1">
            <soap:address location="http://localhost:9000/SoapContext/SoapPort1"/>
        </wsdl:port>
    </wsdl:service>
    <wsdl:service name="SOAPService2">
        <wsdl:port binding="tns:Greeter_SOAPBinding" name="SoapPort2">
            <soap:address location="http://localhost:9000/SoapContext/SoapPort2"/>
        </wsdl:port>
    </wsdl:service>
    <wsdl:service name="SOAPService3">
        <wsdl:port binding="tns:Greeter_SOAPBinding" name="SoapPort3">
            <soap:address location="http://localhost:9000/SoapContext/SoapPort3"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-js_provider.zip( 13 k)
1.  The client demo demonstrates the use of (non-browser) JavaScript to call a CXF server
2.  Axis2 client API has facilities to accept responses in JSON
