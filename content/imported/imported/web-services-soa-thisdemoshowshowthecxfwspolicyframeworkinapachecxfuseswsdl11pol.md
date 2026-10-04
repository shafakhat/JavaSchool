---
title: This demo shows how the CXF WS-Policy framework in Apache CXF uses WSDL 1.1 Policy attachments to enable the use of WS-Addressing
nav: This demo shows how the CX...
description: This demo shows how the CXF WS-Policy framework in Apache CXF uses WSDL 1.1 Policy attachments to enable the use of WS-Addressing
section: Imported - java2s Archive
order: 1140
source: https://web.archive.org/web/20071105012742/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoshowshowtheCXFWSPolicyframeworkinApacheCXFusesWSDL11PolicyattachmentstoenabletheuseofWSAddressing.htm
---
```java title=Example.java
WS-Policy Demo
==============
This demo shows how the CXF WS-Policy framework in Apache CXF uses
WSDL 1.1 Policy attachments to enable the use of WS-Addressing.
While most of the demo is very similar to the ws_addressing demo, there
are two major differences:
1.  Policy element containing an Addressing assertion is attached to
the port element in the demo's wsdl.
2. The configuration files for the client and server specify that the
CXF policy engine should be enabled.
In addition, the configuration file for the server tells the policy
engine where to look for external policy attachments. This is necessary
since neither the implementor not the interface specify wsdlLocation
in their WebService annotation (the client could also use external policy
attachments instead of WSDL 1.1 attachments).
Note that, apart from the configuration of the decoupled http endpoint
on which the client receives responses from the server, nothing else
needs to be configured. In particular, there is no need to specify the
WS-Addressing interceptors. The internals of what is involved in
ensuring that addressing headers are added to the messages (namely:
the addition of two addressing interceptors to the inbound and outbound
fault and message processing chains) are left to the policy framework,
or rather: its built-in support for the Addressing assertion.
Please review the README in the samples directory before continuing.
Prerequisite
------------
If your environment already includes cxf-manifest-incubator.jar on the CLASSPATH,
and the JDK and ant bin directories on the PATH, it is not necessary to
run the environment script described in the samples directory README.
If your environment is not properly configured, or if you are planning
on using wsdl2java, javac, and java to build and run the demos, you must
set the environment by running the script.
Building and running the demo using ant
---------------------------------------
From the samples/ws_policy directory, the ant build script can be used to
build and run the demo.  The server and client targets automatically build
the demo.
Using either UNIX or Windows:
  ant server
  ant client
Although not explicitly instructed to use these interceptors,
both client and server will use the MAPAggregator and MAPCodec
interceptors to aggregate and encode the WS-Addressing MAPs.
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Buildng the demo using wsdl2java and javac
------------------------------------------
From the samples/ws_policy directory, first create the target directory
build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/hello_world_addr.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\hello_world_addr.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes:.
  javac -d build/classes src/demo/ws_policy/common/*.java
  javac -d build/classes src/demo/ws_policy/client/*.java
  javac -d build/classes src/demo/ws_policy/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes;.
  javac -d build\classes src\demo\ws_policy\common\*.java
  javac -d build\classes src\demo\ws_policy\client\*.java
  javac -d build\classes src\demo\ws_policy\server\*.java
Running the demo using java
---------------------------
From the samples/ws_policy directory run the commands (entered on a single command line):
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=./logging.properties
         -Dcxf.config.file=server.xml
         demo.ws_policy.server.Server &
    java -Djava.util.logging.config.file=./logging.properties
         -Dcxf.config.file=client.xml
         demo.ws_policy.client.Client
The server process starts in the background.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=.\logging.properties
         -Dcxf.config.file=server.xml
         demo.ws_policy.server.Server
    java -Djava.util.logging.config.file=.\logging.properties
         -Dcxf.config.file=client.xml
         demo.ws_policy.client.Client
The server process starts in a new command window.
After running the client, terminate the server process.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
/////////////////////////////////////////////////////////////////////
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
package demo.ws_policy.client;
import org.apache.hello_world_soap_http.Greeter;
import org.apache.hello_world_soap_http.PingMeFault;
import org.apache.hello_world_soap_http.SOAPService;
public final class Client {
    private static final String USER_NAME = System.getProperty("user.name");
    private Client() {
    }
    public static void main(String args[]) {
        try {
            SOAPService service = new SOAPService();
            Greeter port = service.getSoapPort();
            System.out.println("Invoking sayHi...");
            String resp = port.sayHi();
            System.out.println("Server responded with: " + resp + "\n");
            System.out.println("Invoking greetMe...");
            resp = port.greetMe(USER_NAME);
            System.out.println("Server responded with: " + resp + "\n");
            System.out.println("Invoking greetMeOneWay...");
            port.greetMeOneWay(USER_NAME);
            System.out.println("No response from server as method is OneWay\n");
            try {
                System.out.println("Invoking pingMe, expecting exception...");
                port.pingMe();
            } catch (PingMeFault ex) {
                System.out.println("Expected exception occurred: " + ex);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }  finally {
            System.exit(0);
        }
    }
}
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
package demo.ws_policy.common;
import java.util.logging.LogRecord;
import java.util.logging.SimpleFormatter;
public class ConciseFormatter extends SimpleFormatter {
    public synchronized String format(LogRecord record) {
        String longForm = super.format(record);
        String shortForm = longForm.indexOf("INFO: ") > 0
                           ? longForm.substring(longForm.indexOf("INFO: ") + 6)
                           : longForm;
        return shortForm;
    }
}
/////////////////////////////////////////////////////////////////////
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
package demo.ws_policy.server;
import java.util.logging.Logger;
import javax.jws.WebService;
import org.apache.hello_world_soap_http.Greeter;
import org.apache.hello_world_soap_http.PingMeFault;
import org.apache.hello_world_soap_http.types.FaultDetail;
@WebService(name = "Greeter",
            serviceName = "SOAPService",
            targetNamespace = "http://apache.org/hello_world_soap_http")
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
package demo.ws_policy.server;
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
////////////////////////////////////////////////////////////////////////
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
            <wsp:Policy xmlns:wsp="http://www.w3.org/2006/07/ws-policy">
                <wsam:Addressing xmlns:wsam="http://www.w3.org/2007/02/addressing/metadata">
                    <wsp:Policy/>
                </wsam:Addressing>
            </wsp:Policy>
            <wswa:UsingAddressing xmlns:wswa="http://www.w3.org/2005/02/addressing/wsdl"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

| XFire-CXF-ws_policy.zip( 16 k) | w__w__w___.__jav_a___2_s_.c_om
