---
title: Get the system properties from RuntimeMXBean
nav: Get the system properties ...
description: Imported from java2s.com: Get the system properties from RuntimeMXBean
section: Imported
order: 20034
source: http://java2s.com/Tutorial/Java/0120__Development/GetthesystempropertiesfromRuntimeMXBean.htm
---
```java title=Example.java
import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import java.util.Date;
public class Main {
  public static void main(String args[]) throws Exception {
    RuntimeMXBean mx = ManagementFactory.getRuntimeMXBean();
    System.out.println(mx.getSystemProperties());
  }
}
```
