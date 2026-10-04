---
title: Insert an annotation to suppress warning
nav: Insert an annotation to su...
description: Imported from the java2s.com archive: Insert an annotation to suppress warning
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Insertanannotationtosuppresswarning.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
publicclass Main {
  @SuppressWarnings("unchecked")
  publicstaticvoid main(String[] args) {
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
