---
title: Format Calendar with String.format()
nav: Format Calendar with Strin...
description: Object a[] = { "String 1", "String 2", Calendar.getInstance() };
section: Imported - java2s Archive
order: 1314
source: https://web.archive.org/web/20140829075240/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FormatCalendarwithStringformat.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String args[]) {
    Object a[] = { "String 1", "String 2", Calendar.getInstance() };
    System.out.println(String.format("Hi %1$s at %2$s ( %3$tY %3$tm %3$te )", a));
  }
}
//Hi String 1 at String 2 ( 2009 03 2 )
```
