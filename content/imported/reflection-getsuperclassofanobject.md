---
title: Get super class of an object
nav: Get super class of an object
description: Imported from the java2s.com archive: Get super class of an object
section: Imported - java2s Archive
order: 2202
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getsuperclassofanobject.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Object o = new String("Hello");
    Class clazz = o.getClass().getSuperclass();
    System.out.println("Super Class = " + clazz);
    o = new StringIndexOutOfBoundsException("Error message");
    clazz = o.getClass().getSuperclass();
    System.out.println("Super Class = " + clazz);
  }
}
```

| 7.13.1. | Get super class of an object |
|---|---|
| 7.13.2. | Superclass of Object is null |
| 7.13.3. | Get all methods including the inherited method. Using the getMethods(), we can only access public methods. |
| 7.13.4. | The superclass of primitive types is always null |
| 7.13.5. | Getting the Superclass of an Object |
| 7.13.6. | Is Inheritable |
