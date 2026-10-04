---
title: Colocated Demo using Document/Literal Style
nav: Colocated Demo using Docum...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1110
source: https://web.archive.org/web/20071105161220/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ColocatedDemousingDocumentLiteralStyle.htm
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
=============================================
Please review the README in the samples directory before
continuing.
Prerequisite
------------
If your environment already includes cxf-incubator.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory README.  If your environment is not
properly configured, or if you are planning on using wsdl2java,
javac, and java to build and run the demos, you must set the
environment.
Building and running the demo using ant
---------------------------------------
From the samples/colocated directory, the ant build script
can be used to build and run the demo.
Using either UNIX or Windows:
  ant build
  ant client
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Building the demo using wsdl2java and javac
-------------------------------------------
From the samples/colocated directory, first create the target
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
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-incubator.jar:./build/classes
  javac -d build/classes src/demo/colocated/server/*.java
  javac -d build/classes src/demo/colocated/client/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-incubator.jar;.\build\classes
  javac -d build\classes src\demo\colocated\server\*.java
  javac -d build\classes src\demo\colocated\client\*.java
Running the demo using java
---------------------------
From the samples/colocated directory run the commands, entered on a
single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         -Dcxf.config.file=./coloc.xml
         demo.colocated.client.Client ./wsdl/hello_world.wsdl
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         -Dcxf.config.file=.\coloc.xml
         demo.colocated.client.Client .\wsdl\hello_world.wsdl
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
////////////////////////////////////////////////////////////////////
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
package demo.colocated.client;
import java.io.File;
import java.net.URL;
import javax.xml.namespace.QName;
import demo.colocated.server.Server;
import org.apache.hello_world_soap_http.Greeter;
import org.apache.hello_world_soap_http.PingMeFault;
import org.apache.hello_world_soap_http.SOAPService;
import org.apache.hello_world_soap_http.types.FaultDetail;
public final class Client {
    private static final QName SERVICE_NAME
        = new QName("http://apache.org/hello_world_soap_http", "SOAPService");
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        if (args.length == 0) {
            System.out.println("please specify wsdl");
            System.exit(1);
        }
        Server.main(new String[]{"inProcess"});
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
///////////////////////////////////////////////////////////////////////////
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
package demo.colocated.common;
import javax.xml.ws.ProtocolException;
import org.apache.cxf.interceptor.Fault;
import org.apache.cxf.message.Message;
import org.apache.cxf.phase.AbstractPhaseInterceptor;
import org.apache.cxf.phase.Phase;
public class ThrowFaultInterceptor extends AbstractPhaseInterceptor<Message> {
    public ThrowFaultInterceptor() {
        super(Phase.PREPARE_SEND);
    }
    public void handleMessage(Message message) throws Fault {
        Boolean isColoc = (Boolean)message.get("org.apache.cxf.message.Message.COLOCATED");
        if (isColoc == null || isColoc == Boolean.FALSE) {
            String str = new String("Collocated Invocation should have been detected.");
            throw new ProtocolException(str);
        }
    }
}
///////////////////////////////////////////////////////////////////////////
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
package demo.colocated.server;
import java.util.logging.Logger;
import org.apache.hello_world_soap_http.Greeter;
import org.apache.hello_world_soap_http.PingMeFault;
import org.apache.hello_world_soap_http.types.FaultDetail;
@javax.jws.WebService(portName = "SoapPort", serviceName = "SOAPService",
                      targetNamespace = "http://apache.org/hello_world_soap_http",
                      endpointInterface = "org.apache.hello_world_soap_http.Greeter")
public class GreeterImpl implements Greeter {
    private static final Logger LOG =
        Logger.getLogger(GreeterImpl.class.getPackage().getName());
    /* (non-Javadoc)
     * @see org.apache.hello_world_soap_http.Greeter#greetMe(java.lang.String)
     */
    public String greetMe(String me) {
        LOG.info("Executing operation greetMe");
        System.out.println("Executing operation greetMe");
        System.out.println("Message received: " + me + "\n");
        return "Hello " + me;
    }
    /* (non-Javadoc)
     * @see org.apache.hello_world_soap_http.Greeter#greetMeOneWay(java.lang.String)
     */
    public void greetMeOneWay(String me) {
        LOG.info("Executing operation greetMeOneWay");
        System.out.println("Executing operation greetMeOneWay\n");
        System.out.println("Hello there " + me);
    }
    /* (non-Javadoc)
     * @see org.apache.hello_world_soap_http.Greeter#sayHi()
     */
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
///////////////////////////////////////////////////////////////////////////
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
package demo.colocated.server;
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
        if (!"inProcess".equals(args[0])) {
            Thread.sleep(5 * 60 * 1000);
            System.out.println("Server exiting");
            System.exit(0);
        }
    }
}
///////////////////////////////////////////////////////////////////////////
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
    targetNamespace="http://apache.org/hello_world_soap_http"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://apache.org/hello_world_soap_http"
    xmlns:x1="http://apache.org/hello_world_soap_http/types"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:types>
        <schema targetNamespace="http://apache.org/hello_world_soap_http/types"
            xmlns="http://www.w3.org/2001/XMLSchema"
        xmlns:tns="http://apache.org/hello_world_soap_http/types"
            elementFormDefault="qualified">
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
                        <element name="requestType" type="string"/>
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
        <wsdl:operation name="pingMe">
            <wsdl:input name="pingMeRequest" message="tns:pingMeRequest"/>
            <wsdl:output name="pingMeResponse" message="tns:pingMeResponse"/>
            <wsdl:fault name="pingMeFault" message="tns:pingMeFault"/>
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
        <wsdl:operation name="pingMe">
            <soap:operation style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="pingMeFault">
                <soap:fault name="pingMeFault" use="literal"/>
            </wsdl:fault>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="SOAPService">
        <wsdl:port binding="tns:Greeter_SOAPBinding" name="SoapPort">
            <soap:address location="http://localhost:9000/SoapContext/SoapPort"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-colocated.zip( 14 k)
1.  Hello World Dispatch Demo using Document/Literal Style
2.  The use of Apache CXF's xml binding: how xml binding works with the doc-lit bare style
3.  Apache CXF's xml binding: how xml binding works with the doc-lit wrapped style
4.  XFire CXF integration

www__.___j_av_a__2_s.co_m___
