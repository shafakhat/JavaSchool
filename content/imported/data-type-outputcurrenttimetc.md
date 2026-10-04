---
title: Output current time
nav: Output current time
description: Imported from the java2s.com archive: Output current time
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20140126093306/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Outputcurrenttimetc.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] argv) throws Exception {
    Calendar cal = Calendar.getInstance();
    System.out.printf("Current time and date: %tc\n", cal);
  }
}
```
