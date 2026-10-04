---
title: static section of Initializer
nav: static section of Initiali...
description: Imported from the java2s.com archive: static section of Initializer
section: Imported - java2s Archive
order: 1209
source: https://web.archive.org/web/20140829082648/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/staticsectionofInitializer.htm
---
```java title=Example.java
public class ClassInitializer5 {
  static String tz;
  static {
    java.util.Properties p = System.getProperties();
    p.list(System.out);
    tz = p.getProperty("user.timezone");
    if (tz.equals(""))
      tz = "Default";
  }
  public static void main(String[] args) {
    System.out.println("timezone = " + tz);
  }
}
```
