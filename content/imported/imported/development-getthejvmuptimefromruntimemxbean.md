---
title: Get the JVM uptime from RuntimeMXBean
nav: Get the JVM uptime from Ru...
description: Imported from java2s.com: Get the JVM uptime from RuntimeMXBean
section: Imported
order: 20032
source: http://java2s.com/Tutorial/Java/0120__Development/GettheJVMuptimefromRuntimeMXBean.htm
---
```java title=Example.java
import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import java.util.Date;
public class Main {
  public static void main(String args[]) throws Exception {
    RuntimeMXBean mx = ManagementFactory.getRuntimeMXBean();
    System.out.println(mx.getUptime() + " ms");
  }
}
```
