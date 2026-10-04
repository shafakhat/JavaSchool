---
title: Keeping the middle element only in for loop
nav: Keeping the middle element...
description: Imported from the java2s.com archive: Keeping the middle element only in for loop
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20070716023059/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Keepingthemiddleelementonlyinforloop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int limit = 10;
    int sum = 0;
    int i = 1;
    for (; i <= limit;) {
      sum += i++;
    }
    System.out.println(sum);
  }
}
java title=Example.java
55
```
