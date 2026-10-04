---
title: Get the name of an array
nav: Get the name of an array
description: Imported from the java2s.com archive: Get the name of an array
section: Imported - java2s Archive
order: 2209
source: https://web.archive.org/web/20140829075331/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getthenameofanarray.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    String name = boolean[].class.getName();
    System.out.println(name);
    name = byte[].class.getName();
    System.out.println(name);
    name = char[].class.getName();
    System.out.println(name);
    name = short[].class.getName();
    System.out.println(name);
    name = int[].class.getName();
    System.out.println(name);
    name = long[].class.getName();
    System.out.println(name);
    name = float[].class.getName();
    System.out.println(name);
    name = double[].class.getName();
    System.out.println(name);
    name = String[].class.getName();
    System.out.println(name);
    name = int[][].class.getName();
    System.out.println(name);
  }
}
```

| 7.14.1. | Getting the Name of a Member Object |
|---|---|
| 7.14.2. | Unqualified names |
| 7.14.3. | Get full class name |
| 7.14.4. | Get the name of a class |
| 7.14.5. | Get the name of an array |
| 7.14.6. | Get the name of void |
| 7.14.7. | Get the unqualified name of a class |
| 7.14.8. | Get the fully-qualified name of a class |
| 7.14.9. | Get the fully-qualified name of a inner class |
| 7.14.10. | Use Class.forName to load a class |
| 7.14.11. | Get the class name in a static method |
