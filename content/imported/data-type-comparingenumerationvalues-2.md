---
title: Comparing Enumeration Values
nav: Comparing Enumeration Values
description: Imported from the java2s.com archive: Comparing Enumeration Values
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparingEnumerationValues.htm
---
```java title=Example.java
publicclass MainClass {
  enum Season {
    spring, summer, fall, winter
  };
  publicstaticvoid main(String[] arg) {
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
