---
title: Convert Java String to Long example
nav: Convert Java String to Lon...
description: Imported from the java2s.com archive: Convert Java String to Long example
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavaStringtoLongexample.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    Long lObj1 = new Long("100");
    System.out.println(lObj1);

    String str = "100";
    Long lObj2 = Long.valueOf(str);
    System.out.println(lObj2);
  }
}
```
