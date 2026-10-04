---
title: Load the class source location from Class.getResource()
nav: Load the class source loca...
description: System.out.println("This class (FromWhere) is located at : " + u);
section: Imported - java2s Archive
order: 2179
source: https://web.archive.org/web/20140829092954/http://www.java2s.com/Tutorial/Java/0125__Reflection/LoadtheclasssourcelocationfromClassgetResource.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    Class theClass = Main.class;
    java.net.URL u = theClass.getResource("");
    System.out.println("This class (FromWhere) is located at : " + u);
  }
}
```

| 7.11.1. | Loading a Class That Is Not on the Classpath |
|---|---|
| 7.11.2. | Get the path from where a class is loaded |
| 7.11.3. | Obtain from where a Class is loaded |
| 7.11.4. | Load the class source location from Class.getResource() |
| 7.11.5. | Returns a reference to a file with the specified name that is located somewhere on the classpath. |
