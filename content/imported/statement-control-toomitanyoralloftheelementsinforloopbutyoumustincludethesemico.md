---
title: To omit any or all of the elements in 'for' loop
nav: To omit any or all of the ...
description: Imported from the java2s.com archive: To omit any or all of the elements in 'for' loop
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20070716023404/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Toomitanyoralloftheelementsinforloopbutyoumustincludethesemicolons.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int limit = 10;
    int sum = 0;
    for (int i = 1; i <= limit;) {
      sum += i++;
    }
    System.out.println(sum);
  }
}
java title=Example.java
55
```
