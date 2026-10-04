---
title: Using new methods in TimeUnit
nav: Using new methods in TimeU...
description: Imported from the java2s.com archive: Using new methods in TimeUnit
section: Imported - java2s Archive
order: 1719
source: https://web.archive.org/web/20140829083404/http://www.java2s.com/Tutorial/Java/0120__Development/UsingnewmethodsinTimeUnit.htm
---
```java title=Example.java
import java.util.concurrent.TimeUnit;
public class TimeUnitDemo {
  public static void main(String[] args) {
    TimeUnit tu = TimeUnit.DAYS;
    System.out.println(tu.toDays(1));
    System.out.println(tu.toHours(1));
    System.out.println(tu.toMinutes(1));
  }
}
```
