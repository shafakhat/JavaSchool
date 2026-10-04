---
title: Changing the StringBufer Length for a StringBuffer Object
nav: Changing the StringBufer L...
description: StringBuffer newString = new StringBuffer("abcde1234567890");
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20070329231202/http://www.java2s.com:80/Tutorial/Java/0120__Development/ChangingtheStringBuferLengthforaStringBufferObject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer newString = new StringBuffer("abcde1234567890");
    System.out.println(newString.capacity());
    System.out.println(newString.length());
    System.out.println(newString);
    newString.setLength(8);
    System.out.println(newString.capacity());
    System.out.println(newString.length());
    System.out.println(newString);
  }
}
java title=Example.java
31
15
abcde1234567890
31
8
abcde123
```
