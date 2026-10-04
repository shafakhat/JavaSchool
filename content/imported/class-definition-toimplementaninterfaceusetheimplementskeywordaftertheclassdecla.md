---
title: To implement an interface
nav: To implement an interface
description: Imported from the java2s.com archive: To implement an interface
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20070430045333/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Toimplementaninterfaceusetheimplementskeywordaftertheclassdeclaration.htm
---
```java title=Example.java
public class CanonDriver implements Printable {
         public void print (Object obj) {
             // code that does the printing
         }
}
```

- An implementation class has to override all methods in the interface.
- A class can implement multiple interfaces.
