---
title: Determining from Where a Class Was Loaded
nav: Determining from Where a C...
description: Imported from the java2s.com archive: Determining from Where a Class Was Loaded
section: Imported - java2s Archive
order: 2145
source: https://web.archive.org/web/20140829075549/http://www.java2s.com/Tutorial/Java/0125__Reflection/DeterminingfromWhereaClassWasLoaded.htm
---
```java title=Example.java
import java.net.URL;
import java.security.CodeSource;
import java.security.ProtectionDomain;
public class Main {
  public Main() {
    Class cls = this.getClass();
    ProtectionDomain pDomain = cls.getProtectionDomain();
    CodeSource cSource = pDomain.getCodeSource();
    URL loc = cSource.getLocation();
  }
  public static void main(String[] argv) throws Exception {
  }
}
```

| 7.7.1. | URL class loader |
|---|---|
| 7.7.2. | extends URLClassLoader |
| 7.7.3. | Load classes |
| 7.7.4. | how to use reflection to print the names and values of all nonstatic fields of an object |
| 7.7.5. | Runs a jar application from any url |
| 7.7.6. | BufferedReader reflection |
| 7.7.7. | Get the class By way of an object |
| 7.7.8. | Get the class By way of a string |
| 7.7.9. | Get the class By way of .class |
| 7.7.10. | Catch InvocationTargetException |
| 7.7.11. | Determining from Where a Class Was Loaded |
| 7.7.12. | Dynamically Reloading a Modified Class |
| 7.7.13. | Creating an Object Using a Constructor Object |
| 7.7.14. | Create an object from a string |
| 7.7.15. | Using the forName() method |
| 7.7.16. | Context ClassLoader |
| 7.7.17. | A tree structure that maps inheritance hierarchies of classes |
| 7.7.18. | Analyze ClassLoader hierarchy for any given object or class loader |
| 7.7.19. | Instantiate unknown class at runtime and call the object's methods |
| 7.7.20. | Load Class |
