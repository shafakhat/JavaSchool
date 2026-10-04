---
title: Changing a single character in a StringBuffer object
nav: Changing a single characte...
description: StringBuffer phrase = new StringBuffer("one two three four");
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20070329223202/http://www.java2s.com:80/Tutorial/Java/0120__Development/ChangingasinglecharacterinaStringBufferobject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer phrase = new StringBuffer("one two three four");
    phrase.setCharAt(3, 'Z');
    System.out.println(phrase);
  }
}
java title=Example.java
oneZtwo three four
```
