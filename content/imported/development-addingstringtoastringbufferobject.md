---
title: Adding String to a StringBuffer Object
nav: Adding String to a StringB...
description: StringBuffer newString = new StringBuffer("abcde1234567890");
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20070329235116/http://www.java2s.com:80/Tutorial/Java/0120__Development/AddingStringtoaStringBufferObject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer newString = new StringBuffer("abcde1234567890");
    newString.append("saves nine");
    System.out.println(newString);
   }
}
```

```java title=Example.java
abcde1234567890saves nine
```
