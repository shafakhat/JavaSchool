---
title: Only replace first occurence
nav: Only replace first occurence
description: Imported from the java2s.com archive: Only replace first occurence
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Onlyreplacefirstoccurence.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    String text = "a b c e a b";
    System.out.println(text.replaceFirst("(?:a b)+", "x y"));
  }
}
//x y c e a b
```
