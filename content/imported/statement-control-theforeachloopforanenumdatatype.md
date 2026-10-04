---
title: The for each loop for an enum data type
nav: The for each loop for an e...
description: Imported from the java2s.com archive: The for each loop for an enum data type
section: Imported - java2s Archive
order: 1327
source: https://web.archive.org/web/20140219123627/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Theforeachloopforanenumdatatype.htm
---
```java title=Example.java
for (type identifier : iterable_expression) {
  // statements
}
java title=Example.java
public class MainClass {
  enum Season {
    spring, summer, fall, winter
  }
  public static void main(String[] args) {
    for (Season season : Season.values()) {
      System.out.println(" The season is now " + season);
    }
  }
}
java title=Example.java
The season is now spring
 The season is now summer
 The season is now fall
 The season is now winter
```
