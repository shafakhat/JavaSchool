---
title: A SOAP message with an attachment and XML-binary Optimized Packaging
nav: A SOAP message with an att...
description: A SOAP message with an attachment and XML-binary Optimized Packaging
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20071013012028/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ASOAPmessagewithanattachmentandXMLbinaryOptimizedPackaging.htm
---
```java title=Example.java
MTOM Demo for SWA & XOP
=============================================
This demo illustrates the use of a SOAP message
with an attachment and XML-binary Optimized Packaging.
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
From the samples/mtom directory, the ant build script
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
From the samples/mtom directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/mtom_xop.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\mtom_xop.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes
  javac -d build/classes src/demo/mtom/client/*.java
  javac -d build/classes src/demo/mtom/server/*.java
  cp src/demo/mtom/client/me.bmp build/classes/demo/mtom/client/me.bmp
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes
  javac -d build\classes src\demo\mtom\client\*.java
  javac -d build\classes src\demo\mtom\server\*.java
  copy src\demo\mtom\client\me.bmp build\classes\demo\mtom\client\me.bmp
Running the demo using java
---------------------------
From the samples/mtom directory run the following commands.
They are entered on a single command line.
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.mtom.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.mtom.client.Client ./wsdl/mtom_xop.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.mtom.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.mtom.client.Client .\wsdl\mtom_xop.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
Building and running the demo in a servlet container
----------------------------------------------------
From the samples/mtom directory, the ant build script
can be used to create the war file that is deployed into the
servlet container.
Build the war file with the command:
  ant war
The war file will be included in the directory
samples/mtom/build/war.  Simply copy the war file into
the servlet container's deployment directory.  For example,
with Tomcat copy the war file into the directory
<installationDirectory>/webapps.  The servlet container will
extract the war and deploy the application.
Make sure already copy all jars from CXF_HOME/lib to
<TomcatInstallationDirectory>/shared/lib
Using ant, run the client application with the command:
  ant client-servlet -Dbase.url=http://localhost:#
Where # is the TCP/IP port used by the servlet container,
e.g., 8080.
Using java, run the client application with the command:
  For UNIX:
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.mtom.client.Client http://localhost:#/mtom/services/mtom?wsdl
  For Windows:
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
       demo.mtom.client.Client http://localhost:#/mtom/services/mtom?wsdl
Where # is the TCP/IP port used by the servlet container,
e.g., 8080.
//////////////////////////////////////////////////////////////////
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
package demo.mtom.client;
import java.awt.Image;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URL;
import javax.activation.DataHandler;
import javax.imageio.ImageIO;
import javax.mail.util.ByteArrayDataSource;
import javax.xml.namespace.QName;
import javax.xml.ws.Binding;
import javax.xml.ws.BindingProvider;
import javax.xml.ws.Holder;
import javax.xml.ws.soap.SOAPBinding;
import org.apache.cxf.mime.TestMtom;
import org.apache.cxf.mime.TestMtomService;
public final class Client {
    private static final QName SERVICE_NAME = new QName("http://cxf.apache.org/mime", "TestMtomService");
    private static final QName PORT_NAME = new QName("http://cxf.apache.org/mime", "TestMtomPort");
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        Client client = new Client();
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
        TestMtomService tms = new TestMtomService(wsdlURL, SERVICE_NAME);
        TestMtom port = (TestMtom) tms.getPort(PORT_NAME, TestMtom.class);
        Binding binding = ((BindingProvider)port).getBinding();
        ((SOAPBinding)binding).setMTOMEnabled(true);
        InputStream pre = client.getClass().getResourceAsStream("me.bmp");
        long fileSize = 0;
        for (int i = pre.read(); i != -1; i = pre.read()) {
            fileSize++;
        }
        Holder<byte[]> param = new Holder<byte[]>();
        param.value = new byte[(int) fileSize];
        System.out.println("Start test without Mtom enable!");
        System.out.println("Sending out the me.bmp Image content to server, data size is " + fileSize);
        InputStream in = client.getClass().getResourceAsStream("me.bmp");
        in.read(param.value);
        Holder<String> name = new Holder<String>("call detail");
        port.testXop(name, param);
        System.out.println("received byte[] back from server, the size is " + param.value.length);
        Image image = ImageIO.read(new ByteArrayInputStream(param.value));
        System.out.println("build image with the returned byte[] back from server successfully, hashCode="
                + image.hashCode());
        System.out.println("Successfully run demo without mtom enable");
        System.out.println("Start test with Mtom enable!");
        System.out.println("Sending out the me.bmp Image content to server, data size is " + fileSize);
        Holder<DataHandler> handler = new Holder<DataHandler>();
        byte[] data = new byte[(int) fileSize];
        client.getClass().getResourceAsStream("me.bmp").read(data);
        handler.value = new DataHandler(new ByteArrayDataSource(data, "application/octet-stream"));
        port.testMtom(name, handler);
        InputStream mtomIn = handler.value.getInputStream();
        fileSize = 0;
        for (int i = mtomIn.read(); i != -1; i = mtomIn.read()) {
            fileSize++;
        }
        System.out.println("received DataHandler back from server, the size is " + fileSize);
        System.out.println("Successfully run demo with mtom enable");
        System.exit(0);
    }
    private static InputStream getResourceStream(File file) throws Exception {
        InputStream in = new FileInputStream(file);
        return in;
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
package demo.mtom.server;
import javax.xml.ws.Binding;
import javax.xml.ws.Endpoint;
import javax.xml.ws.soap.SOAPBinding;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new TestMtomImpl();
        String address = "http://localhost:9000/mime-test";
        Endpoint ep = Endpoint.publish(address, implementor);
        Binding binding = ep.getBinding();
        ((SOAPBinding)binding).setMTOMEnabled(true);
    }
    public static void main(String args[]) throws Exception {
        new Server();
        System.out.println("Server ready...");
        Thread.sleep(5 * 60 * 1000);
        System.out.println("Server exiting");
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
package demo.mtom.server;
import java.io.InputStream;
import javax.activation.DataHandler;
import javax.jws.WebService;
import javax.xml.ws.Holder;
import org.apache.cxf.mime.TestMtom;
@WebService(serviceName = "TestMtomService",
                portName = "TestMtomPort",
                endpointInterface = "org.apache.cxf.mime.TestMtom",
                targetNamespace = "http://cxf.apache.org/mime")
public class TestMtomImpl implements TestMtom {
    public void testXop(Holder<String> name, Holder<byte[]> attachinfo) {
        System.out.println("Received image holder data from client");
        System.out.println("The image holder data length is " + attachinfo.value.length);
        name.value = "return detail + " + name.value;
    }
    public void testMtom(Holder<String> name, Holder<DataHandler> attachinfo) {
        try {
            System.out.println("Received image holder data with mtom enable from client");
            InputStream mtomIn = attachinfo.value.getInputStream();
            long fileSize = 0;
            System.out.println("The image holder data length is " + mtomIn.available());
            name.value = "return detail + " + name.value;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
/////////////////////////////////////////////////////////////////////////////
<?xml version="1.0" encoding="utf-8"?>
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
<wsdl:definitions name="SOAPBuilders-mime-cr-test" xmlns:types="http://cxf.apache.org/mime/types"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:tns="http://cxf.apache.org/mime"
    xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/"
    xmlns:xmime="http://www.w3.org/2005/05/xmlmime"
    targetNamespace="http://cxf.apache.org/mime">
    <wsdl:types>
        <schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://cxf.apache.org/mime/types"
            xmlns:xmime="http://www.w3.org/2005/05/xmlmime" elementFormDefault="qualified">
            <complexType name="XopType">
                <sequence>
                    <element name="name" type="xsd:string" />
                    <element name="attachinfo" type="xsd:base64Binary"/>
                </sequence>
            </complexType>
            <element name="testXop" type="types:XopType" />
            <element name="testXopResponse" type="types:XopType" />
            <complexType name="MtomType">
                <sequence>
                    <element name="name" type="xsd:string" />
                    <element name="attachinfo" type="xsd:base64Binary" xmime:expectedContentTypes="application/octet-stream"/>
                </sequence>
            </complexType>
            <element name="testMtom" type="types:MtomType" />
            <element name="testMtomResponse" type="types:MtomType" />
        </schema>
    </wsdl:types>
    <wsdl:message name="testXopIn">
        <wsdl:part name="data" element="types:testXop" />
    </wsdl:message>
    <wsdl:message name="testXopOut">
        <wsdl:part name="data" element="types:testXopResponse" />
    </wsdl:message>
    <wsdl:message name="testMtomIn">
        <wsdl:part name="data" element="types:testMtom" />
    </wsdl:message>
    <wsdl:message name="testMtomOut">
        <wsdl:part name="data" element="types:testMtomResponse" />
    </wsdl:message>
    <wsdl:portType name="TestMtom">
        <wsdl:operation name="testXop">
            <wsdl:input message="tns:testXopIn" />
            <wsdl:output message="tns:testXopOut" />
        </wsdl:operation>
        <wsdl:operation name="testMtom">
            <wsdl:input message="tns:testMtomIn" />
            <wsdl:output message="tns:testMtomOut" />
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="TestMtomBinding" type="tns:TestMtom">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http" />
        <wsdl:operation name="testXop">
            <soap:operation soapAction="" />
            <wsdl:input>
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="testMtom">
            <soap:operation soapAction="" />
            <wsdl:input>
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="TestMtomService">
        <wsdl:port name="TestMtomPort" binding="tns:TestMtomBinding">
            <soap:address location="http://localhost:9000/mime-test" />
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-mtom.zip( 15 k)
1.  JAX-WS: SOAP Element Any Type
2.  JAX-WS: SOAP Element
3.  Hello World SOAP12 Demo using Document/Literal Style: the use of Apache CXF's SOAP 1.2 capabilities
4.  This demo illustrates Apache CXF's support for SOAP headers
5.  Demonstrates the capabilities and power of SOAP with Attachment support and the Attachment API of AXIS2

w_w__w_.___j_a___v___a__2___s._c___o___m_
