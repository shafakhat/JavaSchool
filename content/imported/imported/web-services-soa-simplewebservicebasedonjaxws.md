---
title: Simple web service based on jaxws
nav: Simple web service based o...
description: @WebServiceRef(wsdlLocation="http://localhost:8080/Hello/HelloService?WSDL")
section: Imported - java2s Archive
order: 1127
source: https://web.archive.org/web/20090203010344/http://www.java2s.com:80/Code/Java/Web-Services-SOA/Simplewebservicebasedonjaxws.htm
---
Simple web service based on jaxws

```java title=Example.java
/*
 * Client.java
 *
 * Created on March 7, 2006, 11:31 PM
 */
package client;
import javax.xml.ws.WebServiceRef;
import endpoint.HelloService;
import endpoint.Hello;
public class Client
{
    @WebServiceRef(wsdlLocation="http://localhost:8080/Hello/HelloService?WSDL")
    static HelloService service;
    public static void main(String[] args)
    {
        Client client = new Client();
        client.doHello();
    }
    public void doHello()
    {
        try
        {
            Hello port = service.getHelloPort();
            String ret = port.getHello(System.getProperty("user.name"));
            System.out.println("Hello result = " + ret);
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}
/////////////////////////
package endpoint;
import javax.jws.WebService;
@WebService
public class Hello
{
    public String getHello(String name)
    {
        return "Hello " + name + "!";
    }
}
```

hello-jaxws.zip( 1 k)
1.  JAX-WS: Style Example
2.  JAX-WS: simple client cert
3.  JAX-WS: simpleclient basic authentication
4.  JAX-WS: simpleclient
5.  JAX-WS: Raw Bytes Mtom
6.  JAX-WS: Polymorphic Processor With Validation
7.  JAX-WS: Polymorphic Processor
8.  JAX-WS: Nodatabinding-JAXB-Integration
9.  JAX-WS: No data binding
10.  JAX-WS Any URI
11.  XML Web Service WSDL
