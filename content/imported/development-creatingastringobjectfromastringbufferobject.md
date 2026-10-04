---
title: Creating a String Object From a StringBuffer Object
nav: Creating a String Object F...
description: StringBuffer palindrome = new StringBuffer("so many dynamos");
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20070329233425/http://www.java2s.com:80/Tutorial/Java/0120__Development/CreatingaStringObjectFromaStringBufferObject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer palindrome = new StringBuffer("so many dynamos");
    String aString = palindrome.toString();
    System.out.println(aString);
  }
}
```

```java title=Example.java
so many dynamos
```
