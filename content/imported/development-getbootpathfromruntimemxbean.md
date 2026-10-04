---
title: Get Boot path from RuntimeMXBean
nav: Get Boot path from Runtime...
description: Imported from the java2s.com archive: Get Boot path from RuntimeMXBean
section: Imported - java2s Archive
order: 1491
source: https://web.archive.org/web/20140829090406/http://www.java2s.com/Tutorial/Java/0120__Development/GetBootpathfromRuntimeMXBean.htm
---
```java title=Example.java
import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import java.util.Date;
public class Main {
  public static void main(String args[]) throws Exception {
    RuntimeMXBean mx = ManagementFactory.getRuntimeMXBean();
    System.out.println(mx.getBootClassPath());
  }
}
```

| 6.8.1. | Get the system properties from RuntimeMXBean |
|---|---|
| 6.8.2. | Get the JVM uptime from RuntimeMXBean |
| 6.8.3. | Get ClassPath from RuntimeMXBean |
| 6.8.4. | Get Boot path from RuntimeMXBean |
| 6.8.5. | Get system start time from RuntimeMXBean |
