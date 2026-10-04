---
title: Convert from String to integer
nav: Convert from String to int...
description: Imported from the java2s.com archive: Convert from String to integer
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertfromStringtointeger.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String str = "25";
    int i = Integer.valueOf(str).intValue();
    // or
    i = Integer.parseInt(str);
  }
}
```
