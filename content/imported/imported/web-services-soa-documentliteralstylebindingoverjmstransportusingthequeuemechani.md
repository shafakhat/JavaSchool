---
title: Document-Literal style binding over JMS Transport using the queue mechanism
nav: Document-Literal style bin...
description: Document-Literal style binding over JMS Transport using the queue mechanism
section: Imported - java2s Archive
order: 1116
source: https://web.archive.org/web/20071105053952/http://www.java2s.com:80/Code/Java/Web-Services-SOA/DocumentLiteralstylebindingoverJMSTransportusingthequeuemechanism.htm
---
Document-Literal style binding over JMS Transport using the queue mechanism

```java title=Example.java
JMS Transport Demo using Document-Literal Style
==========================================================
This sample demonstrates use of the Document-Literal style
binding over JMS Transport using the queue mechanism.
Please review the README in the samples directory before
continuing.
This demo uses ActiveMQ as the JMS implementation for
illustration purposes only. Other JMS implementations
such as Apache Qpid could also be used in the same way.
For details on how to use this demo on non-ActiveMQ
implementations please check "Using other JMS implementaions"
below.
Prerequisite
------------
If your environment already includes cxf-manifest-incubator.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory README.  If your environment is not
properly configured, or if you are planning on using wsdl2java,
javac, and java to build and run the demos, you must set the
environment.
This demo requires ActiveMQ 4.1.X. Before you run this
demo, please make sure you had installed the ActiveMQ 4.1.X and
set ACTIVEMQ_HOME and ACTIVEMQ_VERSION environment variables.
ActiveMQ 4.1.0 the version variable should be
For Unix:
export ACTIVEMQ_VERSION=4.1.0-incubator
For Windows:
set ACTIVEMQ_VERSION=4.1.0-incubator
ActiveMQ 4.1.1 the version variable should be
For Unix:
export ACTIVEMQ_VERSION=4.1.1
For Windows:
set ACTIVEMQ_VERSION=4.1.1
Before you run this demo, please start up the JMS message broker first.
From your ActiveMQ 4.1.X installation launch ActiveMQ JMS broker in a
separate window or in the background using the commandline:
For Unix:
cd <activemq.home.dir>/bin
activemq
For Windows:
cd <activemq.home.dir>\bin
activemq.bat
The location of <activemq.home.dir> depends on whether you have installed the
binary or source release.
Building and running the demo using ant
---------------------------------------
From the samples/jms_queue directory, the ant build script
can be used to build and run the demo.
Using either UNIX or Windows:
  ant build
  ant jmsbroker.start
  ant server
  ant client
To remove the code generated from the WSDL file and the .class
files, run:
  ant clean
Building the demo using wsdl2java and javac
-------------------------------------------
From the samples/jms_queue directory, first create the target
directory build/classes and then generate code from the WSDL file.
For UNIX:
  mkdir -p build/classes
  wsdl2java -d build/classes -compile ./wsdl/jms_greeter.wsdl
For Windows:
  mkdir build\classes
    Must use back slashes.
  wsdl2java -d build\classes -compile .\wsdl\jms_greeter.wsdl
    May use either forward or back slashes.
Now compile the provided client and server applications with the commands:
For UNIX:
  export CLASSPATH=$CLASSPATH:$CXF_HOME/lib/cxf-manifest-incubator.jar:./build/classes:
$ACTIVEMQ_HOME/apache-activemq-$ACTIVEMQ_VERSION.jar
  javac -d build/classes src/demo/jms_greeter/client/*.java
  javac -d build/classes src/demo/jms_greeter/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes;
%ACTIVEMQ_HOME%\apache-activemq-%ACTIVEMQ_VERSION%.jar
  javac -d build\classes src\demo\jms_greeter\client\*.java
  javac -d build\classes src\demo\jms_greeter\server\*.java
Running the demo using java
---------------------------
From the samples/jms_queue directory run the commands, entered on a
single command line:
For UNIX (must use forward slashes):
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.jms_greeter.server.Server &
    java -Djava.util.logging.config.file=$CXF_HOME/etc/logging.properties
         demo.jms_greeter.client.Client ./wsdl/jms_greeter.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.jms_greeter.server.Server
    java -Djava.util.logging.config.file=%CXF_HOME%\etc\logging.properties
         demo.jms_greeter.client.Client .\wsdl\jms_greeter.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
Now you can stop ActiveMQ JMS Broker by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
Using other JMS implementations:
-------------------------------
Using it with Apache Qpid:
-------------------------
Before running the run, you will have to set QPID_HOME in your environment,
and also have to start the Qpid broker.
The following changes are needed to the demo to make it work for Apache Qpid.
1. Changes to wsdl/jms_greeter.wsdl
- Replace the jms:address element under wsdl:port with:
      <jms:address
          destinationStyle="queue"
          jndiConnectionFactoryName="local"
          jndiDestinationName="dq">
          <jms:JMSNamingProperty name="java.naming.factory.initial"
               value="org.apache.qpid.jndi.PropertiesFileInitialContextFactory"/>
          <jms:JMSNamingProperty name="java.naming.provider.url"
               value="tcp://localhost:5672"/>
          <jms:JMSNamingProperty name="connectionfactory.local"
               value="amqp://guest:guest@clientid/test?brokerlist='tcp://localhost:5672'"/>
          <jms:JMSNamingProperty name="queue.dq" value="queue://queuetest"/>
      </jms:address>
2. Changes to build.xml.
- Replace
    <condition property="activemq.home" value="${env.ACTIVEMQ_HOME}">
        <isset property="env.ACTIVEMQ_HOME"/>
    </condition>
    <fail message="this sample need to use activemq, please setup  ACTIVEMQ_HOME in your environment"
        unless="activemq.home"/>
    <condition property="activemq.version" value="${env.ACTIVEMQ_VERSION}">
  <isset property="env.ACTIVEMQ_VERSION"/>
    </condition>
    <fail message="this sample need to use activemq, please setup ACTIVEMQ_VERSION in your envrionment"
        unless="activemq.version"/>
    <property name="thirdparty.classpath" location="${activemq.home}/incubator-activemq-${activemq.version}.jar"/>
  with
   <condition property="qpid.home" value="${env.QPID_HOME}">
        <isset property="env.QPID_HOME"/>
    </condition>
    <fail message="this sample need to use qpid, please setup QPID_HOME in your environment"
        unless="qpid.home"/>
    <property name="thirdparty.classpath" location="${qpid.home}/lib/qpid-incubating.jar"/>
- Remove the target jmsbroker.start from build.xml. This is only a helper function to start the
  Active MQ broker, and is not required if the broker can be started through the scripts.
3. Remove the file, EmbeddedBroker.java from under the directory src/demo/jms_greeter/broker. This is
   only a helper function and therefore need not be used, as long as the broker is started
   through the scripts.
//////////////////////////////////////////////////////////////////////////
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
package demo.jms_greeter.server;
import java.util.logging.Logger;
import org.apache.cxf.jms_greeter.JMSGreeterPortType;
@javax.jws.WebService(portName = "GreeterPort",
                      serviceName = "JMSGreeterService",
                      targetNamespace = "http://cxf.apache.org/jms_greeter",
                      endpointInterface = "org.apache.cxf.jms_greeter.JMSGreeterPortType",
                      wsdlLocation = "file:./wsdl/jms_greeter.wsdl")
public class GreeterJMSImpl implements JMSGreeterPortType {
    private static final Logger LOG = Logger.getLogger(GreeterJMSImpl.class.getPackage().getName());
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
    public void greetMeOneWay(String me) {
        LOG.info("Executing operation greetMeOneWay");
        System.out.println("Executing operation greetMeOneWay\n");
        System.out.println("Hello there " + me);
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
package demo.jms_greeter.broker;
import org.apache.activemq.broker.BrokerService;
import org.apache.activemq.store.memory.MemoryPersistenceAdapter;
public final class EmbeddedBroker {
    private EmbeddedBroker() {
    }
    public static void main(String[] args) throws Exception {
        BrokerService broker = new BrokerService();
        broker.setPersistenceAdapter(new MemoryPersistenceAdapter());
        broker.addConnector("tcp://localhost:61616");
        broker.start();
        System.out.println("JMS broker ready ...");
        Thread.sleep(125 * 60 * 1000);
        System.out.println("JMS broker exiting");
        broker.stop();
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
package demo.jms_greeter.client;
import java.io.File;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.util.Map;
import javax.xml.namespace.QName;
import javax.xml.ws.BindingProvider;
import org.apache.cxf.jms_greeter.JMSGreeterPortType;
import org.apache.cxf.jms_greeter.JMSGreeterService;
import org.apache.cxf.transport.jms.JMSMessageHeadersType;
import org.apache.cxf.transport.jms.JMSPropertyType;
public final class Client {
    private static final QName SERVICE_NAME =
        new QName("http://cxf.apache.org/jms_greeter", "JMSGreeterService");
    private static final QName PORT_NAME =
        new QName("http://cxf.apache.org/jms_greeter", "GreeterPort");
    private Client() {
    }
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("please specify wsdl");
            System.exit(1);
        }
        File wsdl = new File(args[0]);
        JMSGreeterService service = new JMSGreeterService(wsdl.toURL(), SERVICE_NAME);
        JMSGreeterPortType greeter = (JMSGreeterPortType)service.getPort(PORT_NAME, JMSGreeterPortType.class);
        System.out.println("Invoking sayHi...");
        System.out.println("server responded with: " + greeter.sayHi());
        System.out.println();
        System.out.println("Invoking greetMe...");
        System.out.println("server responded with: " + greeter.greetMe(System.getProperty("user.name")));
        System.out.println();
        System.out.println("Invoking greetMeOneWay...");
        greeter.greetMeOneWay(System.getProperty("user.name"));
        System.out.println("No response from server as method is OneWay");
        System.out.println();
        // Demonstration of JMS Context usage
        InvocationHandler handler = Proxy.getInvocationHandler(greeter);
        BindingProvider  bp = null;
        if (handler instanceof BindingProvider) {
            bp = (BindingProvider)handler;
            Map<String, Object> requestContext = bp.getRequestContext();
            JMSMessageHeadersType requestHeader = new JMSMessageHeadersType();
            requestHeader.setJMSCorrelationID("JMS_QUEUE_SAMPLE_CORRELATION_ID");
            requestHeader.setJMSExpiration(3600000L);
            JMSPropertyType propType = new JMSPropertyType();
            propType.setName("Test.Prop");
            propType.setValue("mustReturn");
            requestHeader.getProperty().add(propType);
            requestContext.put("org.apache.cxf.jms.client.request.headers", requestHeader);
            //To override the default receive timeout.
            requestContext.put("org.apache.cxf.jms.client.timeout", new Long(1000));
        }
        System.out.println("Invoking sayHi with JMS Context information ...");
        System.out.println("server responded with: " + greeter.sayHi());
        if (bp != null) {
            Map<String, Object> responseContext = bp.getResponseContext();
            JMSMessageHeadersType responseHdr = (JMSMessageHeadersType)responseContext.get(
                                       "org.apache.cxf.jms.client.response.headers");
            if (responseHdr == null) {
                System.out.println("response Header should not be null");
                System.out.println();
                System.exit(1);
            }
            if ("JMS_QUEUE_SAMPLE_CORRELATION_ID".equals(responseHdr.getJMSCorrelationID())
                && responseHdr.getProperty() != null) {
                System.out.println("Received expected contents in response context");
            } else {
                System.out.println("Received wrong contents in response context");
                System.out.println();
                System.exit(2);
            }
        } else {
            System.out.println("Failed to get the binding provider cannot access context info.");
            System.exit(3);
        }
        System.out.println();
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
package demo.jms_greeter.server;
import javax.xml.ws.Endpoint;
public class Server {
    protected Server() throws Exception {
        System.out.println("Starting Server");
        Object implementor = new GreeterJMSImpl();
        String address = "http://cxf.apache.org/transports/jms";
        Endpoint.publish(address, implementor);
    }
    public static void main(String args[]) throws Exception {
        new Server();
        System.out.println("Server ready...");
        Thread.sleep(125 * 60 * 1000);
        System.out.println("Server exiting");
        System.exit(0);
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
<wsdl:definitions name="JMSGreeterService"
    targetNamespace="http://cxf.apache.org/jms_greeter"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:jms="http://cxf.apache.org/transports/jms"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://cxf.apache.org/jms_greeter"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:x1="http://cxf.apache.org/jms_greeter/types">
    <wsdl:types>
        <schema targetNamespace="http://cxf.apache.org/jms_greeter/types"
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
    <wsdl:portType name="JMSGreeterPortType">
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
    <wsdl:binding name="JMSGreeterPortBinding" type="tns:JMSGreeterPortType">
        <soap:binding style="document" transport="http://cxf.apache.org/transport/jms"/>
        <wsdl:operation name="greetMe">
            <soap:operation soapAction="" style="document"/>
            <wsdl:input name="greetMeRequest">
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output name="greetMeResponse">
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="sayHi">
            <soap:operation soapAction="" style="document"/>
            <wsdl:input name="sayHiRequest">
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output name="sayHiResponse">
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="greetMeOneWay">
            <soap:operation soapaction="" style="document"/>
            <wsdl:input name="greetMeOneWayRequest">
                <soap:body use="literal"/>
            </wsdl:input>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="JMSGreeterService">
           <wsdl:port binding="tns:JMSGreeterPortBinding" name="GreeterPort">
               <jms:address
                   destinationStyle="queue"
                   jndiConnectionFactoryName="ConnectionFactory"
                   jndiDestinationName="dynamicQueues/test.cxf.jmstransport.queue">
                   <jms:JMSNamingProperty name="java.naming.factory.initial" value="org.apache.activemq.jndi.ActiveMQInitialContextFactory"/>
                   <jms:JMSNamingProperty name="java.naming.provider.url" value="tcp://localhost:61616"/>
              </jms:address>
           </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

XFire-CXF-jms_queue.zip( 14 k)
1.  The Document-Literal style binding over JMS transport using the pub/sub mechanism

w___w___w.___j_ava_2___s_._com__
