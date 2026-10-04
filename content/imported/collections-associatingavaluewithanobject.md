---
title: Associating a Value with an Object
nav: Associating a Value with a...
description: Imported from the java2s.com archive: Associating a Value with an Object
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20100509115044/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AssociatingaValuewithanObject.htm
---
```java title=Example.java
import java.util.IdentityHashMap;
import java.util.Map;
public class Main {
  public static void main(String[] argv) throws Exception {
    Map objMap = new IdentityHashMap();
    Object o1 = new Integer(123);
    Object o2 = new Integer(123);
    objMap.put(o1, "first");
    objMap.put(o2, "second");
    Object v1 = objMap.get(o1); // first
    Object v2 = objMap.get(o2); // second
  }
}
```
