---
title: The switch Statement
nav: The switch Statement
description: Imported from the java2s.com archive: The switch Statement
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20070525051348/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/TheswitchStatementademo.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int choice = 2;
    switch (choice) {
    case 1:
      System.out.println("Choice 1 selected");
      break;
    case 2:
      System.out.println("Choice 2 selected");
      break;
    case 3:
      System.out.println("Choice 3 selected");
      break;
    default:
      System.out.println("Default");
      break;
    }
  }
}
java title=Example.java
Choice 2 selected
```
