---
title: Get full package name
nav: Get full package name
description: Imported from the java2s.com archive: Get full package name
section: Imported - java2s Archive
order: 2123
source: https://web.archive.org/web/20140829075823/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getfullpackagename.htm
---
```java title=Example.java
public class Main {
  public static String getPackageName(Class c) {
    String fullyQualifiedName = c.getName();
    int lastDot = fullyQualifiedName.lastIndexOf('.');
    if (lastDot == -1) {
      return "";
    }
    return fullyQualifiedName.substring(0, lastDot);
  }
  public static void main(String[] args) {
    System.out.println(getPackageName(java.awt.Frame.class));
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
