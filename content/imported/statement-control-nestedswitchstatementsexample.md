---
title: Nested Switch Statements Example
nav: Nested Switch Statements E...
description: Imported from the java2s.com archive: Nested Switch Statements Example
section: Imported - java2s Archive
order: 1175
source: https://web.archive.org/web/20140829080756/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/NestedSwitchStatementsExample.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int i = 0;
    switch (i) {
    case 0:
      int j = 1;
      switch (j) {
      case 0:
        System.out.println("i is 0, j is 0");
        break;
      case 1:
        System.out.println("i is 0, j is 1");
        break;
      default:
        System.out.println("nested default case!!");
      }
      break;
    default:
      System.out.println("No matching case found!!");
    }
  }
}
//i is 0, j is 1
```
