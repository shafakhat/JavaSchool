---
title: Developing Web Services Using JAX-WS
nav: Developing Web Services Us...
description: @WebServiceRef(wsdlLocation = "http://localhost:8080/jaxws-webservice/CalculatorService?WSDL")
section: Imported - java2s Archive
order: 1115
source: https://web.archive.org/web/20090517212147/http://www.java2s.com:80/Code/Java/Web-Services-SOA/DevelopingWebServicesUsingJAXWS.htm
---
```java title=Example.java
import javax.jws.WebService;
import javax.jws.WebMethod;
@WebService(
    name="Calculator",
    serviceName="CalculatorService",
    targetNamespace="http://techtip.com/jaxws/sample"
)
public class Calculator {
        public Calculator() {}
        @WebMethod(operationName="add", action="urn:Add")
        public int add(int i, int j) {
            int k = i +j ;
            System.out.println(i + "+" + j +" = " + k);
            return k;
        }
}
import javax.xml.ws.WebServiceRef;
public class JAXWSClient {
  public static void main(String[] args) throws Exception {
    @WebServiceRef(wsdlLocation = "http://localhost:8080/jaxws-webservice/CalculatorService?WSDL")
    static CalculatorService service;
    Calculator port = service.getCalculatorPort();
    System.out.println(" Invoking add operation on the calculator port");
    for (int i = 0; i > 10; i++) {
      int ret = port.add(i, 10);
      if (ret != (i + 10)) {
        System.out.println("Unexpected greeting " + ret);
        return;
      }
      System.out.println(" Adding : " + i + " + 10 = " + ret);
    }
  }
}
```

1.  Simple web service based on jaxws
---  ---
2.  JAX-WS: Style Example
3.  JAX-WS: simple client cert
4.  JAX-WS: simpleclient basic authentication
5.  JAX-WS: simpleclient
6.  JAX-WS: Raw Bytes Mtom
7.  JAX-WS: Polymorphic Processor With Validation
8.  JAX-WS: Polymorphic Processor
9.  JAX-WS: Nodatabinding-JAXB-Integration
10.  JAX-WS: No data binding
11.  JAX-WS Any URI
12.  XML Web Service WSDL
13.  Create a simple Web Service
