---
title: Hello World SOAP12 Demo using Document/Literal Style
nav: Hello World SOAP12 Demo us...
description: Hello World SOAP12 Demo using Document/Literal Style: the use of Apache CXF's SOAP 1.2 capabilities
section: Imported - java2s Archive
order: 1119
source: https://web.archive.org/web/20071013163054/http://java2s.com:80/Code/Java/Web-Services-SOA/HelloWorldSOAP12DemousingDocumentLiteralStyletheuseofApacheCXFsSOAP12capabilities.htm
---
Hello World SOAP12 Demo using Document/Literal Style: the use of Apache CXF's SOAP 1.2 capabilities

```java title=Example.java
====================================================
This demo shows the use of Apache CXF's SOAP 1.2 capabilities.
Please review the README in the samples directory before
continuing.
Prerequisites
-------------
If your environment already includes cxf-manifest-incubator.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory's README.  If your environment is not
properly configured, or if you are planning on using wsdl2java,
javac, and java to build and run the demos, you must set the
environment.
Building and running the demo using ant
---------------------------------------
From the samples/hello_world directory, the ant build script
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
From the samples/hello_world directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/hello_world_soap12.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\hello_world_soap12.wsdl
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
From the samples/hello_world directory run the following commands.
They are entered on a single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.client.Client ./wsdl/hello_world_soap12.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.hw.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hw.client.Client .\wsdl\hello_world_soap12.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
Building and running the demo in a servlet container
----------------------------------------------------
From the samples/hello_world directory, the ant build script
can be used to create the war file that is deployed into the
servlet container.
Build the war file with the command:
  ant war
Preparing deploy to APACHE TOMCAT
* set CATALINA_HOME environment to your TOMCAT home directory
Deploy the application into APACHE TOMCAT with the commond:
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
         demo.hw.client.Client http://localhost:#/helloworld/services/hello_world_soap12?wsdl
  For Windows:
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hw.client.Client http://localhost:#/helloworld/services/hello_world_soap12?wsdl
Where # is the TCP/IP port used by the servlet container,
e.g., 8080.
Undeploy the application from the APACHE TOMCAT with the command:
   ant undeploy -Dtomcat=true
Running demo with HTTP GET
----------------------------------------------------
APACHE CXF support HTTP GET to invoke the service, instead of running
   ant client
you can use
   ant client.get
to invoke the service with simple HttpURLConnection, or you can even
use your favorite browser to get the results back.
////////////////////////////////////////////////////////////////////////////
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
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.ProtocolException;
import org.apache.hello_world_soap12_http.Greeter;
import org.apache.hello_world_soap12_http.PingMeFault;
import org.apache.hello_world_soap12_http.SOAPService;
import org.apache.hello_world_soap12_http.types.FaultDetail;
public final class Client {
    private static final QName SERVICE_NAME
        = new QName("http://apache.org/hello_world_soap12_http", "SOAPService");
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
        System.out.println(wsdlURL);
        SOAPService ss = new SOAPService(wsdlURL, SERVICE_NAME);
        Greeter port = ss.getSoapPort();
        String resp;
        System.out.println("Invoking sayHi...");
        resp = port.sayHi();
        System.out.println("Server responded with: " + resp);
        System.out.println();
        System.out.println("Invoking greetMe...");
        resp = port.greetMe(System.getProperty("user.name"));
        System.out.println("Server responded with: " + resp);
        System.out.println();
        System.out.println("Invoking greetMe with invalid length string, expecting exception...");
        try {
            resp = port.greetMe("Invoking greetMe with invalid length string, expecting exception...");
        } catch (ProtocolException e) {
            System.out.println("Expected exception has occurred: " + e.getClass().getName());
        }
        System.out.println();
        System.out.println("Invoking greetMeOneWay...");
        port.greetMeOneWay(System.getProperty("user.name"));
        System.out.println("No response from server as method is OneWay");
        System.out.println();
        try {
            System.out.println("Invoking pingMe, expecting exception...");
            port.pingMe();
        } catch (PingMeFault ex) {
            System.out.println("Expected exception: PingMeFault has occurred: " + ex.getMessage());
            FaultDetail detail = ex.getFaultInfo();
            System.out.println("FaultDetail major:" + detail.getMajor());
            System.out.println("FaultDetail minor:" + detail.getMinor());
        }
        System.exit(0);
    }
}
/////////////////////////////////////////////////////////////////////////////
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
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Properties;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
public final class Get {
    private Get() {
    }
    public static void main(String args[]) throws Exception {
        // Sent HTTP GET request to invoke sayHi
        String target = "http://localhost:9000/SoapContext/SoapPort/sayHi";
        URL url = new URL(target);
        HttpURLConnection httpConnection = (HttpURLConnection) url.openConnection();
        httpConnection.connect();
        System.out.println("Invoking server through HTTP GET to invoke sayHi");
        InputStream in = httpConnection.getInputStream();
        StreamSource source = new StreamSource(in);
        printSource(source);
        // Sent HTTP GET request to invoke greetMe FAULT
        target = "http://localhost:9000/SoapContext/SoapPort/greetMe/me/CXF";
        url = new URL(target);
        httpConnection = (HttpURLConnection) url.openConnection();
        httpConnection.connect();
        System.out.println("Invoking server through HTTP GET to invoke greetMe");
        try {
            in = httpConnection.getInputStream();
            source = new StreamSource(in);
            printSource(source);
        } catch (Exception e) {
            System.err.println("GreetMe Fault: " + e.getMessage());
        }
        InputStream err = httpConnection.getErrorStream();
        source = new StreamSource(err);
        printSource(source);
        // Sent HTTP GET request to invoke greetMe
        target = "http://localhost:9000/SoapContext/SoapPort/greetMe/requestType/CXF";
        url = new URL(target);
        httpConnection = (HttpURLConnection) url.openConnection();
        httpConnection.connect();
        System.out.println("Invoking server through HTTP GET to invoke greetMe");
        in = httpConnection.getInputStream();
        source = new StreamSource(in);
        printSource(source);
        // Sent HTTP GET request to invoke pingMe
        target = "http://localhost:9000/SoapContext/SoapPort/pingMe";
        url = new URL(target);
        httpConnection = (HttpURLConnection) url.openConnection();
        httpConnection.connect();
        System.out.println("Invoking server through HTTP GET to invoke pingMe");
        try {
            in = httpConnection.getInputStream();
        } catch (Exception e) {
            System.out.println("PingMe fault raised");
        }
        err = httpConnection.getErrorStream();
        source = new StreamSource(err);
        printSource(source);
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
            System.out.println();
            System.out.println("**** Response ******");
            System.out.println();
            System.out.println(bos.toString());
            bos.close();
            System.out.println();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
/////////////////////////////////////////////////////////////////////////////
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
import java.util.logging.Logger;
import org.apache.hello_world_soap12_http.Greeter;
import org.apache.hello_world_soap12_http.PingMeFault;
import org.apache.hello_world_soap12_http.types.FaultDetail;
@javax.jws.WebService(portName = "SoapPort", serviceName = "SOAPService",
                      targetNamespace = "http://apache.org/hello_world_soap12_http",
                      endpointInterface = "org.apache.hello_world_soap12_http.Greeter")
@javax.xml.ws.BindingType(value = "http://www.w3.org/2003/05/soap/bindings/HTTP/")
public class GreeterImpl implements Greeter {
    private static final Logger LOG =
        Logger.getLogger(GreeterImpl.class.getPackage().getName());
    public String greetMe(String me) {
        LOG.info("Executing operation greetMe");
        System.out.println("Executing operation greetMe");
        System.out.println("Message received: " + me + "\n");
        return "Hello " + me;
    }
    public void greetMeOneWay(String me) {
        LOG.info("Executing operation greetMeOneWay");
        System.out.println("Executing operation greetMeOneWay\n");
        System.out.println("Hello there " + me);
    }
    public String sayHi() {
        LOG.info("Executing operation sayHi");
        System.out.println("Executing operation sayHi\n");
        return "Bonjour";
    }
    public void pingMe() throws PingMeFault {
        FaultDetail faultDetail = new FaultDetail();
        faultDetail.setMajor((short)2);
        faultDetail.setMinor((short)1);
        LOG.info("Executing operation pingMe, throwing PingMeFault exception");
        System.out.println("Executing operation pingMe, throwing PingMeFault exception\n");
        throw new PingMeFault("PingMeFault raised by server", faultDetail);
    }
}
/////////////////////////////////////////////////////////////////////////////
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
<definitions name="HelloWorld"
       xmlns="http://schemas.xmlsoap.org/wsdl/"
       xmlns:tns="http://apache.org/hello_world_soap12_http"
       xmlns:x1="http://apache.org/hello_world_soap12_http/types"
       xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
       xmlns:xsd="http://www.w3.org/2001/XMLSchema"
       targetNamespace="http://apache.org/hello_world_soap12_http"
       xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/">
    <wsdl:types>
  <schema targetNamespace="http://apache.org/hello_world_soap12_http/types"
    xmlns="http://www.w3.org/2001/XMLSchema"
    xmlns:x1="http://apache.org/hello_world_soap12_http/types"
    elementFormDefault="qualified">
      <simpleType name="MyStringType">
    <restriction base="string">
        <maxLength value="30" />
    </restriction>
      </simpleType>
      <element name="sayHi">
    <complexType/>
      </element>
      <element name="sayHiResponse">
    <complexType>
        <sequence>
      <element name="responseType" type="string"/>
        </sequence>
    </complexType>
      </element>
            <element name="greetMe">
                <complexType>
                    <sequence>
                        <element name="requestType" type="x1:MyStringType"/>
                    </sequence>
                </complexType>
            </element>
            <element name="greetMeResponse">
                <complexType>
                    <sequence>
                        <element name="responseType" type="string"/>
                    </sequence>
                </complexType>
            </element>
            <element name="greetMeOneWay">
                <complexType>
                    <sequence>
                        <element name="requestType" type="string"/>
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
      <element name="minor" type="short"/>
      <element name="major" type="short"/>
        </sequence>
                </complexType>
      </element>
        </schema>
    </wsdl:types>
    <wsdl:message name="sayHiRequest">
        <wsdl:part name="in" element="x1:sayHi"/>
    </wsdl:message>
    <wsdl:message name="sayHiResponse">
        <wsdl:part name="out" element="x1:sayHiResponse"/>
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
    <wsdl:message name="pingMeRequest">
  <wsdl:part name="in" element="x1:pingMe"/>
    </wsdl:message>
    <wsdl:message name="pingMeResponse">
        <wsdl:part name="out" element="x1:pingMeResponse"/>
    </wsdl:message>
    <wsdl:message name="pingMeFault">
  <wsdl:part name="faultDetail" element="x1:faultDetail"/>
    </wsdl:message>
    <wsdl:portType name="Greeter">
        <wsdl:operation name="sayHi">
            <wsdl:input name="sayHiRequest" message="tns:sayHiRequest"/>
            <wsdl:output name="sayHiResponse" message="tns:sayHiResponse"/>
        </wsdl:operation>
        <wsdl:operation name="greetMe">
            <wsdl:input message="tns:greetMeRequest" name="greetMeRequest"/>
            <wsdl:output message="tns:greetMeResponse" name="greetMeResponse"/>
        </wsdl:operation>
        <wsdl:operation name="greetMeOneWay">
            <wsdl:input message="tns:greetMeOneWayRequest" name="greetMeOneWayRequest"/>
        </wsdl:operation>
  <wsdl:operation name="pingMe">
      <wsdl:input name="pingMeRequest" message="tns:pingMeRequest"/>
      <wsdl:output name="pingMeResponse" message="tns:pingMeResponse"/>
      <wsdl:fault name="pingMeFault" message="tns:pingMeFault"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="Greeter_SOAPBinding" type="tns:Greeter">
  <soap12:binding transport="http://www.w3.org/2003/05/soap/bindings/HTTP/" style="document" />
  <operation name="sayHi">
      <soap12:operation style="document" soapAction=""/>
      <input>
    <soap12:body use="literal" />
      </input>
      <output>
    <soap12:body use="literal" />
      </output>
  </operation>
        <wsdl:operation name="greetMe">
            <soap12:operation soapAction="" style="document"/>
            <wsdl:input name="greetMeRequest">
                <soap12:body use="literal"/>
            </wsdl:input>
            <wsdl:output name="greetMeResponse">
                <soap12:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="greetMeOneWay">
            <soap12:operation soapAction="" style="document"/>
            <wsdl:input name="greetMeOneWayRequest">
                <soap12:body use="literal"/>
            </wsdl:input>
        </wsdl:operation>
  <operation name="pingMe">
      <soap12:operation style="document"/>
      <input>
                <soap12:body use="literal"/>
            </input>
            <output>
                <soap12:body use="literal"/>
            </output>
            <fault name="pingMeFault">
                <soap12:fault name="pingMeFault" use="literal"/>
            </fault>
        </operation>
    </wsdl:binding>
    <wsdl:service name="SOAPService">
        <wsdl:port name="SoapPort" binding="tns:Greeter_SOAPBinding">
            <soap12:address location="http://localhost:9000/SoapContext/SoapPort"/>
        </wsdl:port>
    </wsdl:service>
</definitions>
```

XFire-CXF-soap12.zip( 14 k)
1.  JAX-WS: SOAP Element Any Type
2.  JAX-WS: SOAP Element
3.  A SOAP message with an attachment and XML-binary Optimized Packaging
4.  This demo illustrates Apache CXF's support for SOAP headers
5.  Demonstrates the capabilities and power of SOAP with Attachment support and the Attachment API of AXIS2

w___w___w.__j__a___v_a2__s._c_o___m
