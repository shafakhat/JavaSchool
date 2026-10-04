---
title: Superclass of Object is null
nav: Superclass of Object is null
description: Imported from the java2s.com archive: Superclass of Object is null
section: Imported - java2s Archive
order: 2193
source: https://web.archive.org/web/20140829074655/http://www.java2s.com/Tutorial/Java/0125__Reflection/SuperclassofObjectisnull.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    Object o = new Object();
    Class sup = o.getClass().getSuperclass(); // null
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
