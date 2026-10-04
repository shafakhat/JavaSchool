---
title: An array is a Java object
nav: An array is a Java object
description: Imported from the java2s.com archive: An array is a Java object
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20070529045249/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AnarrayisaJavaobject.htm
---
```java title=Example.java
public class MainClass {
  static String[] names;
  public static void main(String[] a) {
    if (names == null) {
      System.out.println("true");
    } else {
      System.out.println("false");
    }
  }
}
```

```java title=Example.java
true
```
