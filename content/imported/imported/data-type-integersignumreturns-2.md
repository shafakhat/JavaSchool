---
title: Integer signum() returns
nav: Integer signum() returns
description: Imported from the java2s.com archive: Integer signum() returns
section: Imported - java2s Archive
order: 1136
source: https://web.archive.org/web/20070326012425/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Integersignumreturns.htm
---
- ?if num is negative
- 0 if it is zero, and
- 1 if it is positive

```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
      System.out.println(Integer.signum(10));
      System.out.println(Integer.signum(-10));
      System.out.println(Integer.signum(0));
  }
}
```

```java title=Example.java

1
-1
0
```
