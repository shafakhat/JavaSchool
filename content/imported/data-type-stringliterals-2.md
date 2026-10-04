---
title: String Literals
nav: String Literals
description: You can compose long string literals by using the plus sign to concatenate two string literals.
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringLiterals.htm
---
You can compose long string literals by using the plus sign to concatenate two string literals.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    String s1 = "1 " + "2";
    String s2 = s1 + " = 3";
    System.out.println(s1);
    System.out.println(s2);
  }
}
java title=Example.java
1 2
1 2 = 3
```
