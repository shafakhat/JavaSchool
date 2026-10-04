---
title: The use of Apache CXF's xml binding
nav: The use of Apache CXF's xm...
description: The use of Apache CXF's xml binding: how xml binding works with the doc-lit bare style
section: Imported - java2s Archive
order: 1133
source: https://web.archive.org/web/20071104194300/http://www.java2s.com:80/Code/Java/Web-Services-SOA/TheuseofApacheCXFsxmlbindinghowxmlbindingworkswiththedoclitbarestyle.htm
---
The use of Apache CXF's xml binding: how xml binding works with the doc-lit bare style

```java title=Example.java
Hello World Demo using BARE Style in XML Binding
=============================================
This demo illustrates the use of Apache CXF's xml binding. This
specific demo shows you how xml binding works with the
doc-lit bare style
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
From the samples/hello_world_xml_bare directory, the ant build script
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
From the samples/hello_world_xml_bare directory, first create the target
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
From the samples/hello_world_xml_bare directory run the following
commands. They are entered on a single command line.
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
From the samples/hello_world_xml_bare directory, the ant build script
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
import org.apache.hello_world_xml_http.bare.Greeter;
import org.apache.hello_world_xml_http.bare.XMLService;
import org.apache.hello_world_xml_http.bare.types.MyComplexStructType;
// import org.apache.hello_world_xml_http.bare.PingMeFault;
public final class Client {
    private static final QName SERVICE_NAME = new QName("http://apache.org/hello_world_xml_http/bare",
            "XMLService");
    private static final QName PORT_NAME =
        new QName("http://apache.org/hello_world_xml_http/bare", "XMLPort");
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
        XMLService service = new XMLService(wsdlURL, SERVICE_NAME);
        Greeter greeter = (Greeter) service.getPort(PORT_NAME, Greeter.class);
        System.out.println("Invoking sayHi...");
        System.out.println("server responded with: " + greeter.sayHi());
        System.out.println();
        System.out.println("Invoking greetMe...");
        System.out.println("server responded with: " + greeter.greetMe(System.getProperty("user.name")));
        System.out.println();
        MyComplexStructType argument = new MyComplexStructType();
        MyComplexStructType retVal = null;
        String str1 = "this is element 1";
        String str2 = "this is element 2";
        int int1 = 42;
        argument.setElem1(str1);
        argument.setElem2(str2);
        argument.setElem3(int1);
        System.out.println("Invoking sendReceiveData...");
        retVal = greeter.sendReceiveData(argument);
        System.out.println("Response from sendReceiveData operation :");
        System.out.println("Element-1 : " + retVal.getElem1());
        System.out.println("Element-2 : " + retVal.getElem2());
        System.out.println("Element-3 : " + retVal.getElem3());
        System.out.println();
        /*
         * try { System.out.println("Invoking pingMe, expecting exception...");
         * port.pingMe(); } catch (PingMeFault ex) {
         * System.out.println("Expected exception: PingMeFault has occurred: " +
         * ex.getMessage()); }
         */
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
import org.apache.hello_world_xml_http.bare.Greeter;
import org.apache.hello_world_xml_http.bare.types.MyComplexStructType;
@javax.jws.WebService(serviceName = "XMLService",
                portName = "XMLPort",
                endpointInterface = "org.apache.hello_world_xml_http.bare.Greeter",
                targetNamespace = "http://apache.org/hello_world_xml_http/bare")
@javax.xml.ws.BindingType(value = "http://cxf.apache.org/bindings/xformat")
public class GreeterImpl implements Greeter {
    public String greetMe(String me) {
        // TODO Auto-generated method stub
        System.out.println("received calling greetMe!");
        return "Hello " + me;
    }
    public String sayHi() {
        // TODO Auto-generated method stub
        System.out.println("received calling sayHi!");
        return "Bonjour";
    }
    public MyComplexStructType sendReceiveData(MyComplexStructType in) {
        // TODO Auto-generated method stub
        System.out.println("received calling sendReceiveData!");
        return in;
    }
    public String testMultiParamPart(MyComplexStructType in2, String in1) {
        // TODO Auto-generated method stub
        in2.setElem1(in1);
        return "Bonjour";
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
<wsdl:definitions name="HelloWorld" targetNamespace="http://apache.org/hello_world_xml_http/bare"
      xmlns="http://schemas.xmlsoap.org/wsdl/"
      xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
      xmlns:xformat="http://cxf.apache.org/bindings/xformat"
      xmlns:tns="http://apache.org/hello_world_xml_http/bare"
      xmlns:x1="http://apache.org/hello_world_xml_http/bare/types"
      xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:types>
  <schema targetNamespace="http://apache.org/hello_world_xml_http/bare/types"
    xmlns="http://www.w3.org/2001/XMLSchema"
    elementFormDefault="qualified">
      <element name="responseType" type="xsd:string"/>
      <element name="requestType" type="xsd:string"/>
      <element name="myComplexStruct" type="x1:myComplexStructType"/>
      <complexType name="myComplexStructType">
    <sequence>
        <element name="elem1" type="xsd:string"/>
        <element name="elem2" type="xsd:string"/>
        <element name="elem3" type="xsd:int"/>
    </sequence>
      </complexType>
  </schema>
    </wsdl:types>
    <wsdl:message name="sayHiRequest"/>
    <wsdl:message name="sayHiResponse">
  <wsdl:part type="xsd:string" name="out"/>
    </wsdl:message>
    <wsdl:message name="greetMeRequest">
  <wsdl:part element="x1:requestType" name="me"/>
    </wsdl:message>
    <wsdl:message name="greetMeResponse">
  <wsdl:part element="x1:responseType" name="theResponse"/>
    </wsdl:message>
    <wsdl:message name="sendReceiveDataRequest">
  <wsdl:part type="x1:myComplexStructType" name="in"/>
    </wsdl:message>
    <wsdl:message name="sendReceiveDataResponse">
  <wsdl:part type="x1:myComplexStructType" name="out"/>
    </wsdl:message>
    <wsdl:message name="multiParamPartRequest">
  <wsdl:part element="x1:requestType" name="in1"/>
  <wsdl:part element="x1:myComplexStruct" name="in2"/>
    </wsdl:message>
    <wsdl:message name="multiParamPartResponse">
  <wsdl:part element="x1:responseType" name="out1"/>
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
  <wsdl:operation name="sendReceiveData">
      <wsdl:input message="tns:sendReceiveDataRequest" name="SendReceiveDataRequest"/>
      <wsdl:output message="tns:sendReceiveDataResponse" name="SendReceiveDataResponse"/>
  </wsdl:operation>
  <wsdl:operation name="testMultiParamPart" parameterOrder="in2 in1">
      <wsdl:input message="tns:multiParamPartRequest" name="multiParamPartRequest"/>
      <wsdl:output message="tns:multiParamPartResponse" name="multiParamPartResponse"/>
  </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="Greeter_XMLBinding" type="tns:Greeter">
  <xformat:binding/>
  <wsdl:operation name="sayHi">
      <wsdl:input>
    <xformat:body rootNode="tns:sayHi"/>
      </wsdl:input>
      <wsdl:output/>
  </wsdl:operation>
  <wsdl:operation name="greetMe">
      <wsdl:input/>
      <wsdl:output/>
  </wsdl:operation>
  <wsdl:operation name="sendReceiveData">
      <wsdl:input/>
      <wsdl:output/>
  </wsdl:operation>
  <wsdl:operation name="testMultiParamPart">
      <wsdl:input>
    <xformat:body rootNode="tns:multiParamRootReq"/>
      </wsdl:input>
      <wsdl:output/>
  </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="XMLService">
  <wsdl:port binding="tns:Greeter_XMLBinding" name="XMLPort">
      <http:address location="http://localhost:9000/XMLService/XMLPort"/>
  </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-hello_world_xml_bare.zip( 14 k)
1.  Colocated Demo using Document/Literal Style
2.  Hello World Dispatch Demo using Document/Literal Style
3.  Apache CXF's xml binding: how xml binding works with the doc-lit wrapped style
4.  XFire CXF integration

www.j__a___v___a___2__s_.___c_om
