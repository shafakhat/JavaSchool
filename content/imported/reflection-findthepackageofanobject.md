---
title: Find the Package of an Object
nav: Find the Package of an Obj...
description: System.out.println(new Vector().getClass().getPackage().getName());
section: Imported - java2s Archive
order: 2127
source: https://web.archive.org/web/20140829080558/http://www.java2s.com/Tutorial/Java/0125__Reflection/FindthePackageofanObject.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Vector;
public class Main {
  public static void main(String[] args) {
    System.out.println(new Vector().getClass().getPackage().getName());
    System.out.println(new ArrayList().getClass().getPackage().getName());
    System.out.println("Test String".getClass().getPackage().getName());
    System.out.println(new Integer(1).getClass().getPackage().getName());
  }
}
/*
java.util
java.util
java.lang
java.lang
*/
```

| 7.6.1. | Demonstrate Package |
|---|---|
| 7.6.2. | Get full package name |
| 7.6.3. | Get package name of a class |
| 7.6.4. | getPackage() returns null for a class in the unnamed package |
| 7.6.5. | getPackage() returns null for a primitive type or array |
| 7.6.6. | Find the Package of an Object |
| 7.6.7. | Get the class name with or without the package |
| 7.6.8. | Detect if a package is available |
| 7.6.9. | Get the package name of the specified class. |
| 7.6.10. | Get the short name of the specified class by striping off the package name. |
| 7.6.11. | Get Package Names From Dir |
| 7.6.12. | Get non Package Qualified Name |
| 7.6.13. | Returns the package portion of the specified class |
