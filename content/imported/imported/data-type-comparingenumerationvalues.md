---
title: Comparing Enumeration Values
nav: Comparing Enumeration Values
description: Imported from the java2s.com archive: Comparing Enumeration Values
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20070701182732/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ComparingEnumerationValues.htm
---
```java title=Example.java
public class MainClass {
  enum Season {
    spring, summer, fall, winter
  };
  public static void main(String[] arg) {
    Season season = Season.summer;
    if (season.equals(Season.spring)) {
      System.out.println("It is Spring.");
    } else {
      System.out.println("It isn\'t Spring!");
    }
  }
}
```

```java title=Example.java
It isn't Spring!
```
