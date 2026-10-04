---
title: Insert an annotation to suppress warning
nav: Insert an annotation to su...
description: Imported from the java2s.com archive: Insert an annotation to suppress warning
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20090901173654/http://www.java2s.com:80/Tutorial/Java/0020__Language/Insertanannotationtosuppresswarning.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
public class Main {
  @SuppressWarnings("unchecked")
  public static void main(String[] args) {
    ArrayList data = new ArrayList();
    data.add("hello");
    data.add("world");
    Iterator it = data.iterator();
    while (it.hasNext()) {
      System.out.println(it.next());
    }
  }
}
```
