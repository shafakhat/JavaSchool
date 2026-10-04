---
title: Interfaces and Abstract Classes
nav: Interfaces and Abstract Cl...
description: Imported from the java2s.com archive: Interfaces and Abstract Classes
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20070419123004/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/InterfacesandAbstractClasses.htm
---
- The interface should be regarded as a contract between a service provider and its clients.
- An abstract class is a class that cannot be instantiated
- An abstract class must be implemented by a subclass.
- In Java, the interface is a type.

Follow this format to write an interface:

```java title=Example.java
accessModifier interface interfaceName {
}
public interface Printable {
         void print (Object o);
}
```

- The Printable interface has a method, print.
- print is public even though there is no public keyword.
