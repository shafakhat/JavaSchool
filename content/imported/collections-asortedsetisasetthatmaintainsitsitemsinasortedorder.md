---
title: A sorted set is a set that maintains its items in a sorted order
nav: A sorted set is a set that...
description: String[] array = (String[]) set.toArray(new String[set.size()]);
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20100313070939/http://www.java2s.com:80/Tutorial/Java/0140__Collections/Asortedsetisasetthatmaintainsitsitemsinasortedorder.htm
---
```java title=Example.java
import java.util.Iterator;
import java.util.SortedSet;
import java.util.TreeSet;
public class Main {
  public static void main(String[] argv) throws Exception {
    SortedSet<String> set = new TreeSet<String>();
    set.add("b");
    set.add("c");
    set.add("a");
    Iterator it = set.iterator();
    while (it.hasNext()) {
      Object element = it.next();
    }
    String[] array = (String[]) set.toArray(new String[set.size()]);
  }
}
```
