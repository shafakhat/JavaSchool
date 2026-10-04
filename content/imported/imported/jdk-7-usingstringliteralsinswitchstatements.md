---
title: Using string literals in switch statements
nav: Using string literals in s...
description: Imported from the java2s.com archive: Using string literals in switch statements
section: Imported - java2s Archive
order: 1147
source: https://web.archive.org/web/20130301041103/http://www.java2s.com:80/Code/Java/JDK-7/Usingstringliteralsinswitchstatements.htm
---
```java title=Example.java
public class Test {
  public static void main(String[] args) {
    for (String argument : args) {
      switch (argument) {
      case "-verbose":
      case "-v":
        System.out.println("verbose");
        break;
      case "-log":
        System.out.println("logging");
        break;
      case "-help":
        System.out.println("displayHelp");
        break;
      default:
        System.out.println("Illegal command line argument");
      }
    }
  }
}
```
