---
title: Pass value array to String.format()
nav: Pass value array to String...
description: Imported from the java2s.com archive: Pass value array to String.format()
section: Imported - java2s Archive
order: 1165
source: https://web.archive.org/web/20100412210718/http://java2s.com:80/Tutorial/Java/0040__Data-Type/PassvaluearraytoStringformat.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    System.out.printf("Hi %s at %s", "value", "value 2");
    String a[] = { "value 1", "value 2" };
    System.out.println(String.format("hi %s at %s", a));
  }
}
```
