---
title: Adding Another Collection
nav: Adding Another Collection
description: Imported from the java2s.com archive: Adding Another Collection
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20070630140827/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AddingAnotherCollection.htm
---
```java title=Example.java
public boolean addAll(Collection c)
public boolean addAll(int index, Collection c)
```

```java title=Example.java
import java.util.Vector;
public class MainClass {
  public static void main(String args[]) {
    Vector v = new Vector(5);
    for (int i = 0; i < 10; i++) {
      v.insertElementAt(i,0);
    }
    System.out.println(v);
    Vector v2 = new Vector();
    v2.addAll(v);
    v2.addAll(v);
    System.out.println(v2);
  }
}
```

```java title=Example.java
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
