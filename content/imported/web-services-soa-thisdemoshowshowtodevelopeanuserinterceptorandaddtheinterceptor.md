---
title: This demo shows how to develope an user interceptor and add the interceptor into the interceptor chain through configuration
nav: This demo shows how to dev...
description: This demo shows how to develope an user interceptor and add the interceptor into the interceptor chain through configuration
section: Imported - java2s Archive
order: 1142
source: https://web.archive.org/web/20071106044930/http://www.java2s.com:80/Code/Java/Web-Services-SOA/Thisdemoshowshowtodevelopeanuserinterceptorandaddtheinterceptorintotheinterceptorchainthroughconfiguration.htm
---
This demo shows how to develope an user interceptor and add the interceptor into the interceptor chain through configuration

```java title=Example.java
Stream GZIP Interceptor Demo
============================
This demo shows how to develope an user interceptor and add
the interceptor into the interceptor chain through configuration.
Please review the README in the samples directory before
continuing.
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
From the samples/streamInterceptor directory, the ant build script
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
From the samples/streamInterceptor directory, first create the target
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
  javac -d build/classes src/demo/stream/interceptor/*.java
  javac -d build/classes src/demo/stream/client/*.java
  javac -d build/classes src/demo/stream/server/*.java
For Windows:
  set classpath=%classpath%;%CXF_HOME%\lib\cxf-manifest-incubator.jar;.\build\classes
  javac -d build\classes src\demo\stream\interceptor\*.java
  javac -d build\classes src\demo\stream\client\*.java
  javac -d build\classes src\demo\stream\server\*.java
Running the demo using java
---------------------------
From the samples/streamInterceptor directory run the commands, entered on a
single command line:
For UNIX (must use forward slashes):
    java -Dcxf.config.file=server.xml
         demo.stream.server.Server &
    java -Dcxf.config.file=client.xml
         demo.stream.client.Client ./wsdl/hello_world.wsdl
The server process starts in the background.  After running the client,
use the kill command to terminate the server process.
For Windows (may use either forward or back slashes):
  start
    java -Dcxf.config.file=server.xml
         demo.stream.server.Server
    java -Dcxf.config.file=client.xml
       demo.stream.client.Client .\wsdl\hello_world.wsdl
A new command windows opens for the server process.  After running the
client, terminate the server process by issuing Ctrl-C in its command window.
To remove the code generated from the WSDL file and the .class
files, either delete the build directory and its contents or run:
  ant clean
```

XFire-CXF-streamInterceptor.zip( 14 k)
1.  This demo shows a client creating a callback object by passing an EndpointReferenceType to the server
2.  This demo shows how JAX-WS handlers are used
3.  This demo illustrates the use of the JAX-WS APIs to run a simple client against a standalone server using SOAP 1.1 over HTTP
4.  This demo illustrates the use of the JAX-WS asynchronous invocation model
5.  MTOSI 1.1 Samples

w___ww__._j__a_va_2__s__.__co___m__
