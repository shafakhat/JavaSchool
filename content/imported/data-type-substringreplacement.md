---
title: Substring replacement.
nav: Substring replacement.
description: Imported from the java2s.com archive: Substring replacement.
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Substringreplacement.htm
---
```java title=Example.java
class StringReplace {
  publicstaticvoid main(String args[]) {
    String org = "This is a test. This is, too.";
    String search = "is";
    String sub = "was";
    String result = "";
    int i;
    do { // replace all matching substrings
      System.out.println(org);
      i = org.indexOf(search);
      if (i != -1) {
        result = org.substring(0, i);
        result = result + sub;
        result = result + org.substring(i + search.length());
        org = result;
      }
    } while (i != -1);
  }
}
```
