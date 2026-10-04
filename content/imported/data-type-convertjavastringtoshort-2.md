---
title: Convert Java String to Short
nav: Convert Java String to Short
description: Imported from the java2s.com archive: Convert Java String to Short
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavaStringtoShort.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    Short sObj1 = new Short("100");
    System.out.println(sObj1);
    String str = "100";
    Short sObj2 = Short.valueOf(str);
    System.out.println(sObj2);
  }
}
```
