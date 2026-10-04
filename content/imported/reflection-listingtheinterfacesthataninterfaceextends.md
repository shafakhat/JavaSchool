---
title: Listing the Interfaces That an Interface Extends
nav: Listing the Interfaces Tha...
description: Imported from the java2s.com archive: Listing the Interfaces That an Interface Extends
section: Imported - java2s Archive
order: 2054
source: https://web.archive.org/web/20140829083211/http://www.java2s.com/Tutorial/Java/0125__Reflection/ListingtheInterfacesThatanInterfaceExtends.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    Class cls = java.util.List.class;
    Class[] intfs = cls.getInterfaces(); // java.util.Collection
  }
}
```

| 7.2.1. | The superclass of interfaces is always null |
|---|---|
| 7.2.2. | Listing the Interfaces That an Interface Extends |
| 7.2.3. | Checking whether String is an interface or class |
| 7.2.4. | If a class object is an interface or a class |
| 7.2.5. | Listing the Interfaces That a Class Implements |
| 7.2.6. | Although the type of o2 is an interface, getSuperclass() returns the object's superclass |
| 7.2.7. | The interfaces for a primitive type is an empty array |
| 7.2.8. | Return Returns true if type is implementing Map |
| 7.2.9. | Returns true if a class implements Serializable and false otherwise. |
| 7.2.10. | Get Super Interfaces |
| 7.2.11. | Get all interface and object classes that are generalizations of the provided class |
