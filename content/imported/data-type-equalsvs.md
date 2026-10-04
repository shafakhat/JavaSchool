---
title: equals() vs ==
nav: equals() vs ==
description: System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
section: Imported - java2s Archive
order: 1083
source: https://web.archive.org/web/20140829085521/http://www.java2s.com/Tutorial/Java/0040__Data-Type/equalsvs.htm
---
```java title=Example.java
class EqualsNotEqualTo {
  public static void main(String args[]) {
    String s1 = "Hello";
    String s2 = new String(s1);
    System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
    System.out.println(s1 + " == " + s2 + " -> " + (s1 == s2));
  }
}
```
