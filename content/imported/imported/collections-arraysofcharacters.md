---
title: Arrays of Characters
nav: Arrays of Characters
description: Imported from the java2s.com archive: Arrays of Characters
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20070531205638/http://www.java2s.com:80/Tutorial/Java/0140__Collections/ArraysofCharacters.htm
---
```java title=Example.java
public class MainClass{
  public static void main(String[] arg){
     char[] message = new char[50];
     java.util.Arrays.fill(message, 'A');
     for(char ch: message){
       System.out.println(ch);
     }
  }
}
```

```java title=Example.java

A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
```
