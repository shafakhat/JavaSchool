---
title: Downcasting and Run-Time Type Identification (RTTI)
nav: Downcasting and Run-Time T...
description: Imported from the java2s.com archive: Downcasting and Run-Time Type Identification (RTTI)
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20070713024702/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/DowncastingandRunTimeTypeIdentificationRTTI.htm
---
```java title=Example.java
class Useful {
  public void f() {
  }
  public void g() {
  }
}
class MoreUseful extends Useful {
  public void f() {
  }
  public void g() {
  }
  public void u() {
  }
  public void v() {
  }
  public void w() {
  }
}
public class MainClass {
  public static void main(String[] args) {
    Useful[] x = { new Useful(), new MoreUseful() };
    x[0].f();
    x[1].g();
    // x[1].u();
    ((MoreUseful) x[1]).u(); // Downcast/RTTI
    ((MoreUseful) x[0]).u(); // Exception thrown
  }
}
```
