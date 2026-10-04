---
title: Apache CXF's xml binding
nav: Apache CXF's xml binding
description: Apache CXF's xml binding: how xml binding works with the doc-lit wrapped style
section: Imported - java2s Archive
order: 1104
source: https://web.archive.org/web/20071105235906/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ApacheCXFsxmlbindinghowxmlbindingworkswiththedoclitwrappedstyle.htm
---
Apache CXF's xml binding: how xml binding works with the doc-lit wrapped style

```java title=Example.java
Hello World Demo using WRAPPED Style in XML Binding
=============================================
This demo illustrates the use of Apache CXF's xml binding. This
specific demo shows you how xml binding works with the
doc-lit wrapped style.
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
From the samples/hello_world_xml_wrapped directory, the ant build script
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
From the samples/hello_world_xml_wrapped directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/hello_world.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\hello_world.wsdl
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
From the samples/hello_world_xml_wrapped directory run the commands, entered
on a single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.client.Client ./wsdl/hello_world.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.hw.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hw.client.Client .\wsdl\hello_world.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
Building and running the demo in a servlet container
----------------------------------------------------
From the samples/hello_world_xml_wrapped directory, the ant build script
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
Using java, run the client application with the command:
  For UNIX:
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hw.client.Client http://localhost:#/helloworld/services/hello_world?wsdl
  For Windows:
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hw.client.Client http://localhost:#/helloworld/services/hello_world?wsdl
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
use your favoriate browser to get the results back.
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
package demo.hw.client;
import java.io.File;
import java.net.URL;
import javax.xml.namespace.QName;
import org.apache.hello_world_xml_http.wrapped.Greeter;
import org.apache.hello_world_xml_http.wrapped.PingMeFault;
import org.apache.hello_world_xml_http.wrapped.XMLService;
public final class Client {
    public static final QName SERVICE_NAME = new QName("http://apache.org/hello_world_xml_http/wrapped",
            "XMLService");
    public static final QName PORT_NAME =
        new QName("http://apache.org/hello_world_xml_http/wrapped", "XMLPort");
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
        XMLService ss = new XMLService(wsdlURL, SERVICE_NAME);
        Greeter port = ss.getXMLPort();
        String resp;
        System.out.println("Invoking sayHi...");
        resp = port.sayHi();
        System.out.println("Server responded with: " + resp);
        System.out.println();
        System.out.println("Invoking greetMe...");
        resp = port.greetMe(System.getProperty("user.name"));
        System.out.println("Server responded with: " + resp);
        System.out.println();
        System.out.println("Invoking greetMeOneWay...");
        port.greetMeOneWay(System.getProperty("user.name"));
        System.out.println("No response from server as method is OneWay");
        System.out.println();
        try {
            System.out.println("Invoking pingMe, expecting exception...");
            port.pingMe();
        } catch (PingMeFault ex) {
            System.out.println("Expected exception: " + ex.getMessage());
        }
        System.exit(0);
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
        String target = "http://localhost:9000/XMLService/XMLPort/sayHi";
        URL url = new URL(target);
        HttpURLConnection httpConnection = (HttpURLConnection) url.openConnection();
        httpConnection.connect();
        System.out.println("Invoking server through HTTP GET to invoke sayHi");
        InputStream in = httpConnection.getInputStream();
        StreamSource source = new StreamSource(in);
        printSource(source);
        // Sent HTTP GET request to invoke greetMe FAULT
        target = "http://localhost:9000/XMLService/XMLPort/greetMe/me/CXF";
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
        target = "http://localhost:9000/XMLService/XMLPort/greetMe/requestType/CXF";
        url = new URL(target);
        httpConnection = (HttpURLConnection) url.openConnection();
        httpConnection.connect();
        System.out.println("Invoking server through HTTP GET to invoke greetMe");
        in = httpConnection.getInputStream();
        source = new StreamSource(in);
        printSource(source);
        // Sent HTTP GET request to invoke pingMe
        target = "http://localhost:9000/XMLService/XMLPort/pingMe";
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
package demo.hw.server;
import org.apache.hello_world_xml_http.wrapped.Greeter;
import org.apache.hello_world_xml_http.wrapped.PingMeFault;
import org.apache.hello_world_xml_http.wrapped.types.FaultDetail;
@javax.jws.WebService(serviceName = "XMLService",
                      portName = "XMLPort",
                      endpointInterface = "org.apache.hello_world_xml_http.wrapped.Greeter",
                      targetNamespace = "http://apache.org/hello_world_xml_http/wrapped")
@javax.xml.ws.BindingType(value = "http://cxf.apache.org/bindings/xformat")
public class GreeterImpl implements Greeter {
    public String greetMe(String me) {
        System.out.println("received calling greetMe!");
        return "Hello " + me;
    }
    public void greetMeOneWay(String me) {
        System.out.println("Executing operation greetMeOneWay\n");
        System.out.println("Hello there " + me);
    }
    public String sayHi() {
        System.out.println("received calling sayHi!");
        return "Bonjour";
    }
    public void pingMe() throws PingMeFault {
        System.out.println("received calling PingMeFault!");
        FaultDetail faultDetail = new FaultDetail();
        faultDetail.setMajor((short)2);
        faultDetail.setMinor((short)1);
        throw new PingMeFault("PingMeFault raised by server", faultDetail);
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
package demo.hw.server;
import javax.xml.ws.Endpoint;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new GreeterImpl();
        String address = "http://localhost:9000/XMLService/XMLPort";
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
<wsdl:definitions name="HelloWorld"
  targetNamespace="http://apache.org/hello_world_xml_http/wrapped"
  xmlns="http://schemas.xmlsoap.org/wsdl/"
  xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
  xmlns:tns="http://apache.org/hello_world_xml_http/wrapped"
  xmlns:x1="http://apache.org/hello_world_xml_http/wrapped/types"
  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
  xmlns:xformat="http://cxf.apache.org/bindings/xformat"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <wsdl:types>
    <schema
      targetNamespace="http://apache.org/hello_world_xml_http/wrapped/types"
      xmlns="http://www.w3.org/2001/XMLSchema"
      elementFormDefault="qualified">
      <element name="sayHi">
        <complexType />
      </element>
      <element name="sayHiResponse">
        <complexType>
          <sequence>
            <element name="responseType" type="xsd:string" />
          </sequence>
        </complexType>
      </element>
      <element name="greetMe">
        <complexType>
          <sequence>
            <element name="requestType" type="xsd:string" />
          </sequence>
        </complexType>
      </element>
      <element name="greetMeResponse">
        <complexType>
          <sequence>
            <element name="responseType" type="xsd:string" />
          </sequence>
        </complexType>
      </element>
      <element name="greetMeOneWay">
        <complexType>
          <sequence>
            <element name="requestType" type="xsd:string" />
          </sequence>
        </complexType>
      </element>
      <element name="pingMe">
        <complexType />
      </element>
      <element name="pingMeResponse">
        <complexType />
      </element>
      <element name="faultDetail">
        <complexType>
          <sequence>
            <element name="minor" type="xsd:short" />
            <element name="major" type="xsd:short" />
          </sequence>
        </complexType>
      </element>
    </schema>
  </wsdl:types>
  <wsdl:message name="sayHiRequest">
    <wsdl:part element="x1:sayHi" name="in" />
  </wsdl:message>
  <wsdl:message name="sayHiResponse">
    <wsdl:part element="x1:sayHiResponse" name="out" />
  </wsdl:message>
  <wsdl:message name="greetMeRequest">
    <wsdl:part element="x1:greetMe" name="in" />
  </wsdl:message>
  <wsdl:message name="greetMeResponse">
    <wsdl:part element="x1:greetMeResponse" name="out" />
  </wsdl:message>
  <wsdl:message name="greetMeOneWayRequest">
    <wsdl:part element="x1:greetMeOneWay" name="in" />
  </wsdl:message>
  <wsdl:message name="pingMeRequest">
    <wsdl:part name="in" element="x1:pingMe" />
  </wsdl:message>
  <wsdl:message name="pingMeResponse">
    <wsdl:part name="out" element="x1:pingMeResponse" />
  </wsdl:message>
  <wsdl:message name="pingMeFault">
    <wsdl:part name="faultDetail" element="x1:faultDetail" />
  </wsdl:message>
  <wsdl:portType name="Greeter">
    <wsdl:operation name="sayHi">
      <wsdl:input message="tns:sayHiRequest" name="sayHiRequest" />
      <wsdl:output message="tns:sayHiResponse"
        name="sayHiResponse" />
    </wsdl:operation>
    <wsdl:operation name="greetMe">
      <wsdl:input message="tns:greetMeRequest"
        name="greetMeRequest" />
      <wsdl:output message="tns:greetMeResponse"
        name="greetMeResponse" />
    </wsdl:operation>
    <wsdl:operation name="greetMeOneWay">
      <wsdl:input message="tns:greetMeOneWayRequest"
        name="greetMeOneWayRequest" />
    </wsdl:operation>
    <wsdl:operation name="pingMe">
      <wsdl:input name="pingMeRequest"
        message="tns:pingMeRequest" />
      <wsdl:output name="pingMeResponse"
        message="tns:pingMeResponse" />
      <wsdl:fault name="pingMeFault" message="tns:pingMeFault" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="Greeter_XMLBinding" type="tns:Greeter">
    <xformat:binding />
    <wsdl:operation name="sayHi">
      <wsdl:input name="sayHiRequest" />
      <wsdl:output name="sayHiResponse" />
    </wsdl:operation>
    <wsdl:operation name="greetMe">
      <wsdl:input name="greetMeRequest" />
      <wsdl:output name="greetMeResponse" />
    </wsdl:operation>
    <wsdl:operation name="greetMeOneWay">
      <wsdl:input name="greetMeOneWayRequest" />
    </wsdl:operation>
    <wsdl:operation name="pingMe">
      <wsdl:input />
      <wsdl:output />
      <wsdl:fault name="pingMeFault" />
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="XMLService">
    <wsdl:port binding="tns:Greeter_XMLBinding" name="XMLPort">
      <http:address
        location="http://localhost:9000/XMLService/XMLPort" />
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-hello_world_xml_wrapped.zip( 14 k)
1.  Colocated Demo using Document/Literal Style
2.  Hello World Dispatch Demo using Document/Literal Style
3.  The use of Apache CXF's xml binding: how xml binding works with the doc-lit bare style
4.  XFire CXF integration

w___ww_.j___a_va_2___s___.co_m
