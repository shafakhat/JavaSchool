---
title: How to write multiple assignments in a single statement
nav: How to write multiple assi...
description: Imported from the java2s.com archive: How to write multiple assignments in a single statement
section: Imported - java2s Archive
order: 1171
source: https://web.archive.org/web/20140829082219/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Howtowritemultipleassignmentsinasinglestatement.htm
---
```java title=Example.java
public class MainClass{
  public static void main(String[] argv){
    int a, b, c;
    a = b = c = 777;
    System.out.println(a);
    System.out.println(b);
    System.out.println(c);
  }
}
java title=Example.java
777
777
777
```
