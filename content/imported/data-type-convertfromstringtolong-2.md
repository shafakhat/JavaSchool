---
title: Convert from String to long
nav: Convert from String to long
description: Imported from the java2s.com archive: Convert from String to long
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertfromStringtolong.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String str = "0.5";
    long l = Long.valueOf(str).longValue();
    // or
    Long L = Long.parseLong(str);
  }
}
```
