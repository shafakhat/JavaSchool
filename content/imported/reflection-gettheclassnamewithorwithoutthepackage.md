---
title: Get the class name with or without the package
nav: Get the class name with or...
description: Imported from the java2s.com archive: Get the class name with or without the package
section: Imported - java2s Archive
order: 2131
source: https://web.archive.org/web/20140829080255/http://www.java2s.com/Tutorial/Java/0125__Reflection/Gettheclassnamewithorwithoutthepackage.htm
---
```java title=Example.java
public class Main {
  public static String getClassName(Class c) {
    String className = c.getName();
    int firstChar;
    firstChar = className.lastIndexOf('.') + 1;
    if (firstChar > 0) {
      className = className.substring(firstChar);
    }
    return className;
  }
  public static void main(String[] args) {
    System.out.println(getClassName(java.awt.Frame.class));
  }
}
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
