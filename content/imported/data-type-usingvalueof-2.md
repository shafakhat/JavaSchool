---
title: Using valueOf()
nav: Using valueOf()
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20070430174114/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/UsingvalueOf.htm
---
```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
public class MainClass {
  public static void main(String args[]) {
    Week day;
    //
    day = Week.valueOf("Monday");
    System.out.println("day contains " + day);
  }
}
```

```java title=Example.java
day contains Monday
```
