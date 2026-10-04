---
title: Get ClassPath from RuntimeMXBean
nav: Get ClassPath from Runtime...
description: Imported from the java2s.com archive: Get ClassPath from RuntimeMXBean
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20111106133853/http://java2s.com/Tutorial/Java/0120__Development/GetClassPathfromRuntimeMXBean.htm
---
```java title=Example.java
import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import java.util.Date;
public class Main {
  public static void main(String args[]) throws Exception {
    RuntimeMXBean mx = ManagementFactory.getRuntimeMXBean();
    System.out.println(mx.getClassPath());
  }
}
```
