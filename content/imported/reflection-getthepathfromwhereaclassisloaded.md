---
title: Get the path from where a class is loaded
nav: Get the path from where a ...
description: + getClass().getProtectionDomain().getCodeSource().getLocation());
section: Imported - java2s Archive
order: 2174
source: https://web.archive.org/web/20140829090943/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getthepathfromwhereaclassisloaded.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Main csl = new Main();
    csl.getCodeSourceLocation();
  }
  private void getCodeSourceLocation() {
    System.out.println("Code source location: "
        + getClass().getProtectionDomain().getCodeSource().getLocation());
  }
}
```

| 7.11.1. | Loading a Class That Is Not on the Classpath |
|---|---|
| 7.11.2. | Get the path from where a class is loaded |
| 7.11.3. | Obtain from where a Class is loaded |
| 7.11.4. | Load the class source location from Class.getResource() |
| 7.11.5. | Returns a reference to a file with the specified name that is located somewhere on the classpath. |
