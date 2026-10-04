---
title: Convert from String to long
nav: Convert from String to long
description: Imported from the java2s.com archive: Convert from String to long
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20090912060550/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConvertfromStringtolong.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) throws Exception {
    String str = "0.5";
    long l = Long.valueOf(str).longValue();
    // or
    Long L = Long.parseLong(str);
  }
}
```
