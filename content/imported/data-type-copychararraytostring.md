---
title: Copy char array to string
nav: Copy char array to string
description: char[] data = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' };
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Copychararraytostring.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    char[] data = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' };
    String text = String.valueOf(data);
    System.out.println(text);
    text = String.copyValueOf(data, 3, 5);
    System.out.println(text);
  }
}
```
