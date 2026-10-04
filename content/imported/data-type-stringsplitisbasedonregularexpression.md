---
title: String.split() is based on regular expression
nav: String.split() is based on...
description: Imported from the java2s.com archive: String.split() is based on regular expression
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Stringsplitisbasedonregularexpression.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) throws Exception {
    String s3 = "{A}{this is a test}{1234}";
    String[] words = s3.split("[{}]");
    for (String str : words) {
      System.out.println(str);
    }
  }
}
/*
A
this is a test
1234
*/
```
