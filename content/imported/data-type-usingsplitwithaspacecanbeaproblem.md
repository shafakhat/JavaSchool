---
title: Using split() with a space can be a problem
nav: Using split() with a space...
description: Imported from the java2s.com archive: Using split() with a space can be a problem
section: Imported - java2s Archive
order: 1138
source: https://web.archive.org/web/20140217215654/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usingsplitwithaspacecanbeaproblem.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) throws Exception {
    String s3 = "A  B C";
    String[] words = s3.split(" ");
    for (String s : words) {
      System.out.println(s);
    }
  }
}
/*
A
B
C
*/
```
