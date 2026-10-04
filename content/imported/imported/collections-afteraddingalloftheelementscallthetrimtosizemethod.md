---
title: After adding all of the elements, call the trimToSize() method
nav: After adding all of the el...
description: The trimToSize() method makes sure that there is no unused space in the internal data structure.
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20070707112221/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AfteraddingalloftheelementscallthetrimToSizemethod.htm
---
```java title=Example.java
public void trimToSize()
```

The trimToSize() method makes sure that there is no unused space in the internal data structure.

```java title=Example.java
import java.util.ArrayList;
public class MainClass {
  public static void main(String[] a) {
    ArrayList list = new ArrayList();
    list.add("A");
    list.ensureCapacity(10);
    list.trimToSize();
  }
}
```
