---
title: Print out a Diamond
nav: Print out a Diamond
description: Imported from the java2s.com archive: Print out a Diamond
section: Imported - java2s Archive
order: 1330
source: https://web.archive.org/web/20140219022307/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/PrintoutaDiamond.htm
---
```java title=Example.java
class Diamond {
  public static void main(String[] args) {
    for (int i = 1; i < 10; i += 2) {
      for (int j = 0; j < 9 - i / 2; j++)
        System.out.print(" ");
      for (int j = 0; j < i; j++)
        System.out.print("*");
      System.out.print("\n");
    }
    for (int i = 7; i > 0; i -= 2) {
      for (int j = 0; j < 9 - i / 2; j++)
        System.out.print(" ");
      for (int j = 0; j < i; j++)
        System.out.print("*");
      System.out.print("\n");
    }
  }
}
/*
         *
        ***
       *****
      *******
     *********
      *******
       *****
        ***
         *
*/
```
