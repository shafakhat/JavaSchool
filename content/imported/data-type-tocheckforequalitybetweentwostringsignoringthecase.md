---
title: To check for equality between two strings ignoring the case
nav: To check for equality betw...
description: Imported from the java2s.com archive: To check for equality between two strings ignoring the case
section: Imported - java2s Archive
order: 1219
source: https://web.archive.org/web/20070328185809/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Tocheckforequalitybetweentwostringsignoringthecase.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String a = "a";
    String b = "A";
    if(a.equalsIgnoreCase(b)){
      System.out.println("a==b");
    }else{
      System.out.println("a!=b");
    }
  }
}
```

```java title=Example.java
a==b
```
