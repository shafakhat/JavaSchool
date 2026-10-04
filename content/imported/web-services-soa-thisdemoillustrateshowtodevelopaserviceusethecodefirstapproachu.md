---
title: This demo illustrates how to develop a service use the 'code first' approach using the JAX-WS APIs
nav: This demo illustrates how ...
description: This demo illustrates how to develop a service use the 'code first' approach using the JAX-WS APIs
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/20071104194305/http://www.java2s.com:80/Code/Java/Web-Services-SOA/ThisdemoillustrateshowtodevelopaserviceusethecodefirstapproachusingtheJAXWSAPIs.htm
---
```java title=Example.java
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
Hello World Demo using Document/Literal Style
=============================================
This demo illustrates how to develop a service use the "code first"
approach using the JAX-WS APIs.
Prerequisite
------------
If your environment already includes cxf-manifest-incubator.jar on the
CLASSPATH, and the JDK and ant bin directories on the PATH
it is not necessary to set the environment as described in
the samples directory README.  If your environment is not
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
From the samples/hello_world directory run the commands, entered on a
single command line:
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
<project name="hello world code first demo" default="build" basedir=".">
    <import file="common_build.xml"/>
    <target name="client" description="run demo client" depends="build">
        <property name="param" value=""/>
        <cxfrun classname="demo.hw.client.Client"
            param1=""
            param2="${op}"
            param3="${param}"/>
    </target>
    <target name="server" description="run demo server" depends="build">
        <cxfrun classname="demo.hw.server.Server"/>
    </target>
    <property name="cxf.war.file.name" value="helloworld"/>
    <target name="war" depends="build">
  <cxfwar wsdl="hello_world.wsdl" filename="${cxf.war.file.name}.war"/>
    </target>
    <target name="client-servlet" description="run demo client hitting servlet" depends="build">
        <property name="param" value=""/>
        <cxfrun classname="demo.hw.client.Client" param1="${base.url}/helloworld/services/hello_world?wsdl" param2="${op}" param3="${param}"/>
    </target>
</project>
////////////////////////////////////////////////////////////////////////
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
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import javax.xml.ws.soap.SOAPBinding;
import demo.hw.server.HelloWorld;
public final class Client {
    private static final QName SERVICE_NAME
        = new QName("http://server.hw.demo/", "HelloWorld");
    private static final QName PORT_NAME
        = new QName("http://server.hw.demo/", "HelloWorldPort");
    private Client() {
    }
    public static void main(String args[]) throws Exception {
        Service service = Service.create(SERVICE_NAME);
        // Endpoint Address
        String endpointAddress = "http://localhost:9000/helloWorld";
        // Add a port to the Service
        service.addPort(PORT_NAME, SOAPBinding.SOAP11HTTP_BINDING, endpointAddress);
        HelloWorld hw = service.getPort(HelloWorld.class);
        System.out.println(hw.sayHi("World"));
    }
}
////////////////////////////////////////////////////////////////////////
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
// START SNIPPET: service
package demo.hw.server;
import javax.jws.WebService;
@WebService
public interface HelloWorld {
    String sayHi(String text);
}
// END SNIPPET: service
////////////////////////////////////////////////////////////////////////
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
// START SNIPPET: service
package demo.hw.server;
import javax.jws.WebService;
@WebService(endpointInterface = "demo.hw.server.HelloWorld",
            serviceName = "HelloWorld")
public class HelloWorldImpl implements HelloWorld {
    public String sayHi(String text) {
        return "Hello " + text;
    }
}
// END SNIPPET: service
////////////////////////////////////////////////////////////////////////
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
        // START SNIPPET: publish
        System.out.println("Starting Server");
        HelloWorldImpl implementor = new HelloWorldImpl();
        String address = "http://localhost:9000/helloWorld";
        Endpoint.publish(address, implementor);
        // END SNIPPET: publish
    }
    public static void main(String args[]) throws Exception {
        new Server();
        System.out.println("Server ready...");
        Thread.sleep(5 * 60 * 1000);
        System.out.println("Server exiting");
        System.exit(0);
    }
}
```

| XFire-CXF-hello_world_code_first.zip( 10 k) | w___w_w___._j___a___v_a2_s_.__c___o_m__
