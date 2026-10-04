---
title: Display the amount of free memory in the Java Virtual Machine.
nav: Display the amount of free...
description: Imported from the java2s.com archive: Display the amount of free memory in the Java Virtual Machine.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20101102172252/http://www.java2s.com:80/Tutorial/Java/0120__Development/DisplaytheamountoffreememoryintheJavaVirtualMachine.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] args) {
    DecimalFormat df = new DecimalFormat("0.00");
    long freeMem = Runtime.getRuntime().freeMemory();
    System.out.println(df.format(freeMem / 1000000F) + " MB");
  }
}
```
