---
title: The RPC-Literal style binding
nav: The RPC-Literal style bind...
description: If your environment already includes cxf-manifest-incubator.jar on the
section: Imported - java2s Archive
order: 1132
source: https://web.archive.org/web/20071105210633/http://www.java2s.com:80/Code/Java/Web-Services-SOA/TheRPCLiteralstylebinding.htm
---
The RPC-Literal style binding

```java title=Example.java
Hello World Demo using RPC-Literal Style
========================================
This version of Helloe World demonstrates the use
of the RPC-Literal style binding.
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
From the samples/hello_world_RPCLit directory, the ant build script
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
From the samples/hello_world_RPCLit directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/hello_world_RPCLit.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\hello_world_RPCLit.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes
  javac -d build/classes src/demo/hwRPCLit/client/*.java
  javac -d build/classes src/demo/hwRPCLit/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes
  javac -d build\classes src\demo\hwRPCLit\client\*.java
  javac -d build\classes src\demo\hwRPCLit\server\*.java
Running the demo using java
---------------------------
From the samples/hello_world_RPCLit directory run the following
commands. They are entered on a single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hwRPCLit.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.hwRPCLit.client.Client ./wsdl/hello_world_RPCLit.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.hwRPCLit.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hwRPCLit.client.Client .\wsdl\hello_world_RPCLit.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
Building and running the demo in a servlet container
----------------------------------------------------
From the samples/hello_world_RPCLit directory, the ant build script
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
         demo.hwRPCLit.client.Client http://localhost:#/helloworld/services/hello_world_rpclit?wsdl
  For Windows:
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.hwRPCLit.client.Client http://localhost:#/helloworld/services/hello_world_rpclit?wsdl
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
package demo.hwRPCLit.client;
import java.io.File;
import java.net.URL;
import javax.xml.namespace.QName;
import org.apache.hello_world_rpclit.GreeterRPCLit;
import org.apache.hello_world_rpclit.SOAPServiceRPCLit;
import org.apache.hello_world_rpclit.types.MyComplexStruct;
public final class Client {
    private static final QName SERVICE_NAME =
        new QName("http://apache.org/hello_world_rpclit", "SOAPServiceRPCLit");
    private static final QName PORT_NAME =
        new QName("http://apache.org/hello_world_rpclit", "SoapPortRPCLit");
    private Client() {
    }
    public static void main(String[] args) throws Exception {
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
        SOAPServiceRPCLit service = new SOAPServiceRPCLit(wsdlURL, SERVICE_NAME);
        GreeterRPCLit greeter = (GreeterRPCLit)service.getPort(PORT_NAME, GreeterRPCLit.class);
        System.out.println("Invoking sayHi...");
        System.out.println("server responded with: " + greeter.sayHi());
        System.out.println();
        System.out.println("Invoking greetMe...");
        System.out.println("server responded with: " + greeter.greetMe(System.getProperty("user.name")));
        System.out.println();
        MyComplexStruct argument = new MyComplexStruct();
        MyComplexStruct retVal = null;
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
        System.exit(0);
    }
}
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
package demo.hwRPCLit.client;
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
        target = "http://localhost:9000/SoapContext/SoapPort/greetMe/in/CXF";
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
package demo.hwRPCLit.server;
import java.util.logging.Logger;
import org.apache.hello_world_rpclit.GreeterRPCLit;
import org.apache.hello_world_rpclit.types.MyComplexStruct;
@javax.jws.WebService(portName = "SoapPortRPCLit", serviceName = "SOAPServiceRPCLit",
                      targetNamespace = "http://apache.org/hello_world_rpclit",
                      endpointInterface = "org.apache.hello_world_rpclit.GreeterRPCLit")
public class GreeterRPCLitImpl implements GreeterRPCLit {
    private static final Logger LOG = Logger.getLogger(GreeterRPCLitImpl.class.getPackage().getName());
    public String greetMe(String me) {
        LOG.info("Executing operation greetMe");
        System.out.println("Executing operation greetMe");
        System.out.println("Message received: " + me + "\n");
        return "Hello " + me;
    }
    public String sayHi() {
        LOG.info("Executing operation sayHi");
        System.out.println("Executing operation sayHi" + "\n");
        return "Bonjour";
    }
    public MyComplexStruct sendReceiveData(MyComplexStruct in) {
        LOG.info("Executing operation sendReceiveData");
        System.out.println("Executing operation sendReceiveData");
        System.out.println("Received struct with values :\nElement-1 : " + in.getElem1() + "\nElement-2 : "
                           + in.getElem2() + "\nElement-3 : " + in.getElem3() + "\n");
        return in;
    }
}
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
package demo.hwRPCLit.server;
import javax.xml.ws.Endpoint;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new GreeterRPCLitImpl();
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
///////////////////////////////////////////////////////////////////////
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
<wsdl:definitions name="HelloWorld" targetNamespace="http://apache.org/hello_world_rpclit"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://apache.org/hello_world_rpclit"
    xmlns:x1="http://apache.org/hello_world_rpclit/types"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:types>
        <schema targetNamespace="http://apache.org/hello_world_rpclit/types"
            xmlns="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
            <complexType name="myComplexStruct">
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
        <wsdl:part type="xsd:string" name="in"/>
    </wsdl:message>
    <wsdl:message name="greetMeResponse">
        <wsdl:part type="xsd:string" name="out"/>
    </wsdl:message>
    <wsdl:message name="sendReceiveDataRequest">
        <wsdl:part type="x1:myComplexStruct" name="in"/>
    </wsdl:message>
    <wsdl:message name="sendReceiveDataResponse">
        <wsdl:part type="x1:myComplexStruct" name="out"/>
    </wsdl:message>
    <wsdl:portType name="GreeterRPCLit">
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
    </wsdl:portType>
    <wsdl:binding name="Greeter_SOAPBinding_RPCLit" type="tns:GreeterRPCLit">
        <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="sayHi">
            <soap:operation soapAction="" style="rpc"/>
            <wsdl:input>
                <soap:body namespace="http://apache.org/hello_world_rpclit" use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body namespace="http://apache.org/hello_world_rpclit" use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="greetMe">
            <soap:operation soapAction="" style="rpc"/>
            <wsdl:input>
                <soap:body namespace="http://apache.org/hello_world_rpclit" use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body namespace="http://apache.org/hello_world_rpclit" use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="sendReceiveData">
            <soap:operation soapAction="" style="rpc"/>
               <wsdl:input>
                   <soap:body namespace="http://apache.org/hello_world_rpclit" use="literal"/>
               </wsdl:input>
               <wsdl:output>
                   <soap:body namespace="http://apache.org/hello_world_rpclit" use="literal"/>
               </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="SOAPServiceRPCLit">
        <wsdl:port binding="tns:Greeter_SOAPBinding_RPCLit" name="SoapPortRPCLit">
            <soap:address location="http://localhost:9000/SoapContext/SoapPort"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

| XFire-CXF-hello_world_RPCLit.zip( 14 k) | w__w_w___.___ja___v_a_2__s_.___c_o___m___
