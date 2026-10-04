---
title: This demo illustrates Apache CXF's support for SOAP headers
nav: This demo illustrates Apac...
description: This demo illustrates Apache CXF's support for SOAP headers. In the
section: Imported - java2s Archive
order: 1134
source: https://web.archive.org/web/20071013163104/http://java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoillustratesApacheCXFssupportforSOAPheaders.htm
---
This demo illustrates Apache CXF's support for SOAP headers

```java title=Example.java
SOAP Headers
============
This demo illustrates Apache CXF's support for SOAP headers.  In the
WSDL file, the SOAP header is included as an additional part within
the message and binding definitions.  Using this approach to defining a
SOAP header, Apache CXF treats the header content as another parameter
to the operation.  Consequently, the header content is simply
manipulated within the method body.
The client application creates the header content, which is simply
a string value.  The server application views the supplied values
and may set these values into the operation's return values or
out/inout headers.
Please review the README in the samples directory before
continuing.
Prerequisites
-------------
If your environment already includes cxf.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory's README.  If your environment is not
properly configured, or if you are planning on using wsdl2java,
javac, and java to build and run the demos, you must set the
environment.
Building and running the demo using ant
---------------------------------------
From the samples/soap_header directory, the ant build script
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
From the samples/soap_header directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/soap_header.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\soap_header.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf.jar:./build/classes
  javac -d build/classes src/demo/soap_header/client/*.java
  javac -d build/classes src/demo/soap_header/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf.jar;.\build\classes
  javac -d build\classes src\demo\soap_header\client\*.java
  javac -d build\classes src\demo\soap_header\server\*.java
Running the demo using java
---------------------------
From the samples/soap_header directory run the following commands.
They are entered on a single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.soap_header.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.soap_header.client.Client ./wsdl/soap_header.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.soap_header.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.soap_header.client.Client .\wsdl\soap_header.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
Building and running the demo in a servlet container
----------------------------------------------------
From the samples/soap_header directory, the ant build script
can be used to create the war file that is deployed into the
servlet container.
Build the war file with the command:
  ant war
Preparing deploy to APACHE TOMCAT
* set CATALINA_HOME environment to your TOMCAT home directory
Deploy the war file into APACHE TOMCAT with the commond:
[NOTE] This step will check if the cxf jars present in Tomcat,
       if not, it will automatically copy all the jars into CATALINA_HOME/shared/lib
  ant deploy -Dtomcat=true
The servlet container will extract the war and deploy the application.
Using ant, run the client application with the command:
  ant client-servlet -Dbase.url=http://localhost:#
Where # is the TCP/IP port used by the servlet container,
e.g., 8080.
Or
  ant client-servlet -Dhost=localhost -Dport=8080
You can ignore the -Dhost and -Dport if your tomcat setup is same, i.e ant client-servlet
Using java, run the client application with the command:
  For UNIX:
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.soap_header.client.Client http://localhost:#/soapheader/services/soap_header?wsdl
  For Windows:
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.soap_header.client.Client http://localhost:#/soapheader/services/soap_header?wsdl
Where # is the TCP/IP port used by the servlet container,
e.g., 8080.
Undeploy the application from the APACHE TOMCAT with the command:
   ant undeploy -Dtomcat=true
/////////////////////////////////////////////////////////////////////////
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
package demo.soap_header.client;
import java.io.File;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Holder;
import org.apache.headers.HeaderService;
import org.apache.headers.HeaderTester;
import org.apache.headers.InHeader;
import org.apache.headers.InHeaderResponse;
import org.apache.headers.InoutHeader;
import org.apache.headers.InoutHeaderResponse;
import org.apache.headers.OutHeader;
import org.apache.headers.OutHeaderResponse;
import org.apache.headers.SOAPHeaderData;
public final class Client {
    private static final QName SERVICE_NAME
        = new QName("http://apache.org/headers", "HeaderService");
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
        HeaderService hs = new HeaderService(wsdlURL, SERVICE_NAME);
        HeaderTester proxy = hs.getSoapPort();
        invokeInHeader(proxy);
        invokeOutHeader(proxy);
        invokeInOutHeader(proxy);
    }
    private static void invokeInHeader(HeaderTester proxy) {
        // invoke inHeader operation
        System.out.println("Invoking inHeader operation");
        InHeader me = new InHeader();
        me.setRequestType("CXF user");
        SOAPHeaderData headerInfo = new SOAPHeaderData();
        headerInfo.setOriginator("CXF client");
        headerInfo.setMessage("Invoking inHeader operation");
        InHeaderResponse response = proxy.inHeader(me, headerInfo);
        System.out.println("\tinHeader invocation returned: ");
        System.out.println("\t\tResult: " + response.getResponseType());
    }
    private static void invokeOutHeader(HeaderTester proxy) {
        // invoke outHeaderoperation
        System.out.println("Invoking outHeader operation");
        OutHeader me = new OutHeader();
        me.setRequestType("CXF user");
        Holder<OutHeaderResponse> theResponse = new Holder<OutHeaderResponse>();
        Holder<SOAPHeaderData> headerInfo = new Holder<SOAPHeaderData>();
        proxy.outHeader(me, theResponse, headerInfo);
        System.out.println("\toutHeader invocation returned: ");
        System.out.println("\t\tOut parameter: " + theResponse.value.getResponseType());
        System.out.println("\t\tHeader content:");
        System.out.println("\t\t\tOriginator: " + headerInfo.value.getOriginator());
        System.out.println("\t\t\tMessage: " + headerInfo.value.getMessage());
    }
    private static void invokeInOutHeader(HeaderTester proxy) {
        System.out.println("Invoking inoutHeader operation");
        InoutHeader me = new InoutHeader();
        me.setRequestType("CXF user");
        Holder<SOAPHeaderData> headerInfo = new Holder<SOAPHeaderData>();
        SOAPHeaderData shd = new SOAPHeaderData();
        shd.setOriginator("CXF client");
        shd.setMessage("Invoking inoutHeader operation");
        headerInfo.value = shd;
        InoutHeaderResponse response = proxy.inoutHeader(me, headerInfo);
        System.out.println("\tinoutHeader invocation returned: ");
        System.out.println("\t\tResult: " + response.getResponseType());
        System.out.println("\t\tHeader content:");
        System.out.println("\t\t\tOriginator: " + headerInfo.value.getOriginator());
        System.out.println("\t\t\tMessage: " + headerInfo.value.getMessage());
        System.exit(0);
    }
}
//////////////////////////////////////////////////////////////////////////////
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
package demo.soap_header.server;
import javax.xml.ws.Holder;
import org.apache.headers.HeaderTester;
import org.apache.headers.InHeader;
import org.apache.headers.InHeaderResponse;
import org.apache.headers.InoutHeader;
import org.apache.headers.InoutHeaderResponse;
import org.apache.headers.OutHeader;
import org.apache.headers.OutHeaderResponse;
import org.apache.headers.SOAPHeaderData;
@javax.jws.WebService(serviceName = "HeaderService",
            portName = "SoapPort",
            endpointInterface = "org.apache.headers.HeaderTester",
            targetNamespace = "http://apache.org/headers")
public class HeaderTesterImpl implements HeaderTester {
    public InHeaderResponse inHeader(InHeader me,
                                     SOAPHeaderData headerInfo) {
        System.out.println("inHeader invoked");
        System.out.println("\tGetting Originator: " + headerInfo.getOriginator());
        System.out.println("\tGetting Message: " + headerInfo.getMessage());
        InHeaderResponse ihr = new InHeaderResponse();
        ihr.setResponseType("Hello " + me.getRequestType());
        return ihr;
    }
    public void outHeader(OutHeader me,
                          Holder<OutHeaderResponse> theResponse,
                          Holder<SOAPHeaderData> headerInfo) {
        System.out.println("outHeader invoked");
        System.out.println("\tSetting originator: CXF server");
        System.out.println("\tSetting message: outHeader invocation succeeded");
        SOAPHeaderData sh = new SOAPHeaderData();
        sh.setOriginator("CXF server");
        sh.setMessage("outHeader invocation succeeded");
        headerInfo.value = sh;
        OutHeaderResponse ohr = new OutHeaderResponse();
        ohr.setResponseType("Hello " + me.getRequestType());
        theResponse.value = ohr;
    }
    public InoutHeaderResponse inoutHeader(InoutHeader me,
                                           Holder<SOAPHeaderData> headerInfo) {
        System.out.println("inoutHeader invoked");
        System.out.println("\tGetting Originator: " + headerInfo.value.getOriginator());
        System.out.println("\tGetting Message: " + headerInfo.value.getMessage());
        System.out.println("\tSetting originator: CXF server");
        System.out.println("\tSetting message: inoutHeader invocation succeeded");
        headerInfo.value.setOriginator("CXF server");
        headerInfo.value.setMessage("inoutHeader invocation succeeded");
        InoutHeaderResponse iohr = new InoutHeaderResponse();
        iohr.setResponseType("Hello " + me.getRequestType());
        return iohr;
    }
}
//////////////////////////////////////////////////////////////////////////////
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
package demo.soap_header.server;
import javax.xml.ws.Endpoint;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new HeaderTesterImpl();
        String address = "http://localhost:9000/headers";
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
//////////////////////////////////////////////////////////////////////////////
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
<definitions name="soap_header" targetNamespace="http://apache.org/headers"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://apache.org/headers"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <types>
        <schema targetNamespace="http://apache.org/headers"
            xmlns="http://www.w3.org/2001/XMLSchema"
            xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
            <complexType name="SOAPHeaderData">
                <sequence>
                    <element maxOccurs="1" minOccurs="1" name="originator" type="string"/>
                    <element maxOccurs="1" minOccurs="1" name="message" type="string"/>
                </sequence>
            </complexType>
            <element name="SOAPHeaderInfo" type="tns:SOAPHeaderData"/>
        <element name="inHeader">
           <complexType>
                    <sequence>
                        <element name="requestType" type="xsd:string"/>
                    </sequence>
                </complexType>
        </element>
        <element name="inHeaderResponse">
           <complexType>
                    <sequence>
                        <element name="responseType" type="xsd:string"/>
                    </sequence>
                </complexType>
        </element>
        <element name="outHeader">
           <complexType>
                    <sequence>
                        <element name="requestType" type="xsd:string"/>
                    </sequence>
                </complexType>
        </element>
        <element name="outHeaderResponse">
           <complexType>
                    <sequence>
                        <element name="responseType" type="xsd:string"/>
                    </sequence>
                </complexType>
        </element>
        <element name="inoutHeader">
           <complexType>
                    <sequence>
                        <element name="requestType" type="xsd:string"/>
                    </sequence>
                </complexType>
        </element>
        <element name="inoutHeaderResponse">
           <complexType>
                    <sequence>
                        <element name="responseType" type="xsd:string"/>
                    </sequence>
                </complexType>
        </element>
        </schema>
    </types>
    <message name="inHeaderRequest">
        <part element="tns:inHeader" name="me"/>
        <part element="tns:SOAPHeaderInfo" name="header_info"/>
    </message>
    <message name="inHeaderResponse">
        <part element="tns:inHeaderResponse" name="the_response"/>
    </message>
    <message name="outHeaderRequest">
        <part element="tns:outHeader" name="me"/>
    </message>
    <message name="outHeaderResponse">
        <part element="tns:outHeaderResponse" name="the_response"/>
        <part element="tns:SOAPHeaderInfo" name="header_info"/>
    </message>
    <message name="inoutHeaderRequest">
        <part element="tns:inoutHeader" name="me"/>
        <part element="tns:SOAPHeaderInfo" name="header_info"/>
    </message>
    <message name="inoutHeaderResponse">
        <part element="tns:inoutHeaderResponse" name="the_response"/>
        <part element="tns:SOAPHeaderInfo" name="header_info"/>
    </message>
    <portType name="headerTester">
        <operation name="inHeader">
            <input message="tns:inHeaderRequest" name="inHeaderRequest"/>
            <output message="tns:inHeaderResponse" name="inHeaderResponse"/>
        </operation>
        <operation name="outHeader">
            <input message="tns:outHeaderRequest" name="outHeaderRequest"/>
            <output message="tns:outHeaderResponse" name="outHeaderResponse"/>
        </operation>
        <operation name="inoutHeader">
            <input message="tns:inoutHeaderRequest" name="inoutHeaderRequest"/>
            <output message="tns:inoutHeaderResponse" name="inoutHeaderResponse"/>
        </operation>
    </portType>
    <binding name="headerTesterSOAPBinding" type="tns:headerTester">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="inHeader">
            <soap:operation soapAction="" style="document"/>
            <input name="inHeaderRequest">
                <soap:body parts="me" use="literal"/>
                <soap:header message="tns:inHeaderRequest" part="header_info"
                    use="literal"/>
            </input>
            <output name="inHeaderResponse">
                <soap:body use="literal"/>
            </output>
        </operation>
        <operation name="outHeader">
            <soap:operation soapAction="" style="document"/>
            <input name="outHeaderRequest">
                <soap:body use="literal"/>
            </input>
            <output name="outHeaderResponse">
                <soap:body parts="the_response" use="literal"/>
                <soap:header message="tns:outHeaderResponse" part="header_info"
                    use="literal"/>
            </output>
        </operation>
        <operation name="inoutHeader">
            <soap:operation soapAction="" style="document"/>
            <input name="inoutHeaderRequest">
                <soap:body parts="me" use="literal"/>
                <soap:header message="tns:inoutHeaderRequest" part="header_info"
                    use="literal"/>
            </input>
            <output name="inoutHeaderResponse">
                <soap:body parts="the_response" use="literal"/>
                <soap:header message="tns:inoutHeaderResponse" part="header_info"
                    use="literal"/>
            </output>
        </operation>
    </binding>
    <service name="HeaderService">
        <port binding="tns:headerTesterSOAPBinding" name="SoapPort">
            <soap:address location="http://localhost:9000/headers"/>
        </port>
    </service>
</definitions>
```

XFire-CXF-soap_header.zip( 12 k)
1.  JAX-WS: SOAP Element Any Type
2.  JAX-WS: SOAP Element
3.  A SOAP message with an attachment and XML-binary Optimized Packaging
4.  Hello World SOAP12 Demo using Document/Literal Style: the use of Apache CXF's SOAP 1.2 capabilities
5.  Demonstrates the capabilities and power of SOAP with Attachment support and the Attachment API of AXIS2

w__w_w___._j___a___v___a2__s___._com
