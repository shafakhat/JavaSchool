---
title: This demo shows how WS-ReliableMessaging support in Apache CXF may be enabled
nav: This demo shows how WS-Rel...
description: This demo shows how WS-ReliableMessaging support in Apache CXF may be enabled
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/20071104162811/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoshowshowWSReliableMessagingsupportinApacheCXFmaybeenabled.htm
---
```java title=Example.java
WS-RM Demo
==========
The client and server both use interceptor configuration to install the
WS-RM interceptors, comprising logical interceptors (RMInInterceptor/RMOutInterceptor)
responsible for managing the reliability properties of the current message, and a
protocol interceptor (RMSoapInterceptor) responsible for encoding/decoding
these properties as SOAP Headers.
As WS-RM is dependent on WS-Addressing, the configuration uses
the same approach as the ws_addressing sample to enable this
functionality. However, you may notice that the WS-Addressing
namespace URI is different in this case (i.e.
http://schemas.xmlsoap.org/ws/2004/08/addressing as opposed to
http://www.w3.org/2005/08/addressing). This is because the WS-RM
specification is still based on an older version of WS-Addressing.
Three additional interceptors are configured:
- LoggingInInterceptor used on both the client- and server-side to log the
inbound SOAP messages and display these to the console. Notice the usage of
out-of-band RM protocol messages (CreateSequence and CreateSequenceResponse)
and the WS-RM headers in application-level messages (Sequence,
SequenceAcknowledgement, AckRequested etc.)
- LoggingOutInterceptor used on both the client- and server-side to log the
outbound SOAP messages and display these to the console.
- MessageLossSimulator used only on the client-side to simulate message
loss by discarding every second application level message. This simulated
unreliability allows the retransmission of unacknowledged messages to be
observed.
This demo also illustrates usage of the decoupled HTTP transport, whereby
a separate server->client HTTP connection is used to deliver responses
to (application or RM protocol) requests and server side originated
standalone acknowlegments.
The "partial response" referred to in the log output is the payload of
the HTTP 202 Accepted response sent on the back-channel of the original
client->server connection.
In all other respects this demo is based on the basic hello_world sample,
illustrating that WS-Addressing usage is independent of the application.
One notable addition to the familiar hello_world WSDL is the usage
of the <wsaw:UsingAddressing> extension element to indicate the
WS-Addressing support is enabled for the service endpoint.
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
From the samples/ws_rm directory, the ant build script can be used to
build and run the demo.  The server and client targets automatically build
the demo.
Using either UNIX or Windows:
  ant server
  ant client
On startup, the client makes a sequence of 4 oneway invocations.
The output of the logging interceptors will show that only the 1st and 3rd
reach their destination. Notice how after approximately 2 seconds the
messages that actually have arrived at the server will be acknowledged,
and how after approximately 4 seconds the client will resend the 2nd and 4th
application message. These will be acknowledged another 2 seconds
later so that there will be no further retransmissions from the client.
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Building the demo using wsdl2java and javac
-------------------------------------------
From the samples/ws_rm directory, first create the target directory
build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/hello_world_rm.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\hello_world_rm.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/celtix.jar:./build/classes
  javac -d build/classes src/demo/ws_rm/common/*.java
  javac -d build/classes src/demo/ws_rm/client/*.java
  javac -d build/classes src/demo/ws_rm/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\celtix.jar;.\build\classes
  javac -d build\classes src\demo\ws_rm\common\*.java
  javac -d build\classes src\demo\ws_rm\client\*.java
  javac -d build\classes src\demo\ws_rm\server\*.java
Running the demo using java
---------------------------
From the samples/ws_rm directory run the commands (entered on a single command line):
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=./logging.properties
         demo.ws_rm.server.Server &
    java -Djava.util.logging.config.file=./logging.properties
         demo.ws_rm.client.Client ./wsdl/hello_world_rm.wsdl
The server process starts in the background.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=.\logging.properties
         demo.ws_rm.server.Server
    java -Djava.util.logging.config.file=.\logging.properties
         demo.ws_rm.client.Client .\wsdl\hello_world_rm.wsdl
The server process starts in a new command window.
After running the client, terminate the server process.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
//////////////////////////////////////////////////////////////////////////////////
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
package demo.ws_rm.client;
import java.lang.reflect.UndeclaredThrowableException;
import demo.ws_rm.common.MessageLossSimulator;
import org.apache.cxf.Bus;
import org.apache.cxf.bus.spring.SpringBusFactory;
import org.apache.cxf.hello_world_soap_http.Greeter;
import org.apache.cxf.hello_world_soap_http.GreeterService;
public final class Client {
    private static final String USER_NAME = System.getProperty("user.name");
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        try {
            SpringBusFactory bf = new SpringBusFactory();
            Bus bus = bf.createBus("ws_rm.xml");
            bf.setDefaultBus(bus);
            bus.getOutInterceptors().add(new MessageLossSimulator());
            GreeterService service = new GreeterService();
            Greeter port = service.getGreeterPort();
            String[] names = new String[] {"Anne", "Bill", "Chris", "Daisy"};
            // make a sequence of 4 invocations
            for (int i = 0; i < 4; i++) {
                System.out.println("Invoking greetMeOneWay...");
                port.greetMeOneWay(names[i]);
                System.out.println("No response as method is OneWay\n");
            }
            // allow aynchronous resends to occur
            Thread.sleep(30 * 1000);
            bus.shutdown(true);
        } catch (UndeclaredThrowableException ex) {
            ex.getUndeclaredThrowable().printStackTrace();
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            System.exit(0);
        }
    }
}
//////////////////////////////////////////////////////////////////////////////////
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
package demos.ws_rm.common;
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
//////////////////////////////////////////////////////////////////////////////////
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
package demo.ws_rm.common;
import java.io.IOException;
import java.io.OutputStream;
import java.math.BigInteger;
import java.util.ListIterator;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.cxf.interceptor.Fault;
import org.apache.cxf.interceptor.InterceptorChain;
import org.apache.cxf.interceptor.MessageSenderInterceptor;
import org.apache.cxf.io.AbstractWrappedOutputStream;
import org.apache.cxf.message.Message;
import org.apache.cxf.phase.AbstractPhaseInterceptor;
import org.apache.cxf.phase.Phase;
import org.apache.cxf.phase.PhaseInterceptor;
import org.apache.cxf.ws.addressing.AddressingProperties;
import org.apache.cxf.ws.rm.RMContextUtils;
/**
 *
 */
public class MessageLossSimulator extends AbstractPhaseInterceptor<Message> {
    private static final Logger LOG = Logger.getLogger(MessageLossSimulator.class.getName());
    private int appMessageCount;
    public MessageLossSimulator() {
        super(Phase.PREPARE_SEND);
        addBefore(MessageSenderInterceptor.class.getName());
    }
    /**
      * Simulate loss of every second application message by replacing the stream normally
      * provided by the transport (in the MessageSenderInterceptor)/
     */
    public void handleMessage(Message message) throws Fault {
        AddressingProperties maps =
            RMContextUtils.retrieveMAPs(message, false, true);
        RMContextUtils.ensureExposedVersion(maps);
        String action = null;
        if (maps != null && null != maps.getAction()) {
            action = maps.getAction().getValue();
        }
        if (RMContextUtils.isRMProtocolMessage(action)) {
            return;
        }
        appMessageCount++;
        if (0 != (appMessageCount % 2)) {
            return;
        }
        InterceptorChain chain = message.getInterceptorChain();
        ListIterator it = chain.getIterator();
        while (it.hasNext()) {
            PhaseInterceptor pi = (PhaseInterceptor)it.next();
            if (MessageSenderInterceptor.class.getName().equals(pi.getId())) {
                chain.remove(pi);
                LOG.fine("Removed MessageSenderInterceptor from interceptor chain.");
                break;
            }
        }
        message.setContent(OutputStream.class, new WrappedOutputStream(message));
    }
    private class WrappedOutputStream extends AbstractWrappedOutputStream {
        private Message outMessage;
        public WrappedOutputStream(Message m) {
            this.outMessage = m;
        }
        @Override
        protected void onFirstWrite() throws IOException {
            if (LOG.isLoggable(Level.FINE)) {
                BigInteger nr = RMContextUtils.retrieveRMProperties(outMessage, true)
                    .getSequence().getMessageNumber();
                LOG.fine("Losing message " + nr);
            }
            wrappedStream = new DummyOutputStream();
        }
    }
    private class DummyOutputStream extends OutputStream {
        @Override
        public void write(int b) throws IOException {
            // TODO Auto-generated method stub
        }
    }
}
//////////////////////////////////////////////////////////////////////////////////
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
package demo.ws_rm.server;
import java.util.logging.Logger;
import org.apache.cxf.hello_world_soap_http.Greeter;
@javax.jws.WebService(serviceName = "GreeterService",
            portName = "GreeterPort",
            endpointInterface = "org.apache.cxf.hello_world_soap_http.Greeter",
            wsdlLocation = "file:./wsdl/hello_world_rm.wsdl",
            targetNamespace = "http://cxf.apache.org/hello_world_soap_http")
public class GreeterImpl implements Greeter {
    private static final Logger LOG =
        Logger.getLogger(GreeterImpl.class.getPackage().getName());
    /* (non-Javadoc)
     * @see org.apache.cxf.hello_world_soap_http.Greeter#greetMe(java.lang.String)
     */
    public String greetMe(String me) {
        LOG.info("Executing operation greetMe");
        System.out.println("Executing operation greetMe");
        System.out.println("Message received: " + me + "\n");
        return "Hello " + me;
    }
    /* (non-Javadoc)
     * @see org.apache.cxf.hello_world_soap_http.Greeter#greetMeOneWay(java.lang.String)
     */
    public void greetMeOneWay(String me) {
        LOG.info("Executing operation greetMeOneWay");
        System.out.println("Executing operation greetMeOneWay\n");
        System.out.println("Hello there " + me);
    }
    /* (non-Javadoc)
     * @see org.apache.cxf.hello_world_soap_http.Greeter#sayHi()
     */
    public String sayHi() {
        LOG.info("Executing operation sayHi");
        System.out.println("Executing operation sayHi\n");
        return "Bonjour";
    }
}
//////////////////////////////////////////////////////////////////////////////////
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
package demo.ws_rm.server;
import javax.xml.ws.Endpoint;
import org.apache.cxf.Bus;
import org.apache.cxf.bus.spring.SpringBusFactory;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new GreeterImpl();
        String address = "http://localhost:9000/SoapContext/GreeterPort";
        Endpoint e = Endpoint.publish(address, implementor);
    }
    public static void main(String args[]) throws Exception {
        SpringBusFactory bf = new SpringBusFactory();
        Bus bus = bf.createBus("ws_rm.xml");
        bf.setDefaultBus(bus);
        new Server();
        System.out.println("Server ready...");
        Thread.sleep(5 * 60 * 1000);
        bus.shutdown(true);
        System.out.println("Server exiting");
        System.exit(0);
    }
}
/////////////////////////////////////////////////////////////////////////////
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
<wsdl:definitions name="HelloWorld" targetNamespace="http://cxf.apache.org/hello_world_soap_http"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://cxf.apache.org/hello_world_soap_http"
    xmlns:x1="http://cxf.apache.org/hello_world_soap_http/types"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:types>
        <schema targetNamespace="http://cxf.apache.org/hello_world_soap_http/types"
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
    <wsdl:service name="GreeterService">
        <wsdl:port binding="tns:Greeter_SOAPBinding" name="GreeterPort">
            <soap:address location="http://localhost:9000/SoapContext/GreeterPort"/>
            <wswa:UsingAddressing xmlns:wswa="http://www.w3.org/2005/02/addressing/wsdl"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

| XFire-CXF-ws_rm.zip( 17 k) | w_ww_._j__a___v__a__2s.c___o_m___
