---
title: Creating a StringBuffer object with a specific value for the capacity
nav: Creating a StringBuffer ob...
description: Imported from the java2s.com archive: Creating a StringBuffer object with a specific value for the capacity
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20070329225142/http://www.java2s.com:80/Tutorial/Java/0120__Development/CreatingaStringBufferobjectwithaspecificvalueforthecapacity.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer newString = new StringBuffer(50);
    System.out.println(newString.capacity());
  }
}
```

```java title=Example.java
50
```
