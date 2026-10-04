---
title: Create a simple Web Service
nav: Create a simple Web Service
description: Imported from the java2s.com archive: Create a simple Web Service
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20100209023559/http://java2s.com/Code/Java/Web-Services-SOA/CreateasimpleWebService.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Calendar;
import javax.jws.WebMethod;
import javax.jws.WebService;
@WebService()
public class Main {
  @WebMethod
  public String getTime() {
    Calendar calendar = Calendar.getInstance();
    SimpleDateFormat sdf = new SimpleDateFormat("HH:mm");
    return (sdf.format(calendar.getTime()));
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
13.  Developing Web Services Using JAX-WS
