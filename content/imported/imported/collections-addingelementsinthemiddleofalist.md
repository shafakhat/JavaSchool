---
title: Adding elements in the middle of a List
nav: Adding elements in the mid...
description: Imported from the java2s.com archive: Adding elements in the middle of a List
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20070630073652/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AddingelementsinthemiddleofaList.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.List;
public class MainClass {
  public static void main(String args[]) throws Exception {
    List list = new ArrayList();
    list.add("A");
    list.add("B");
    list.add("C");
    list.add(1, "G");
    System.out.println(list);
  }
}
```

```java title=Example.java

[A, G, B, C]
```
