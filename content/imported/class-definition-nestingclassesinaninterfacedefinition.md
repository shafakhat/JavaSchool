---
title: Nesting Classes in an Interface Definition
nav: Nesting Classes in an Inte...
description: An inner class to an interface will be static and public by default.
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20070430045546/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/NestingClassesinanInterfaceDefinition.htm
---
An inner class to an interface will be static and public by default.

```java title=Example.java
interface Port {
  // Methods & Constants declared in the interface...
  class Info {
    // Definition of the class...
  }
}
public class MainClass {
  public static void main(String[] a) {
    Port.Info info = new Port.Info();
  }
}
```
