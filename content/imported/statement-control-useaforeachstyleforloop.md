---
title: Use a for-each style for loop
nav: Use a for-each style for l...
description: Imported from the java2s.com archive: Use a for-each style for loop
section: Imported - java2s Archive
order: 1329
source: https://web.archive.org/web/20140223103131/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Useaforeachstyleforloop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int nums[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int sum = 0;
    // use for-each style for to display and sum the values
    for(int x : nums) {
      System.out.println("Value is: " + x);
      sum += x;
    }
    System.out.println("Summation: " + sum);
  }
}
java title=Example.java
Value is: 1
Value is: 2
Value is: 3
Value is: 4
Value is: 5
Value is: 6
Value is: 7
Value is: 8
Value is: 9
Value is: 10
Summation: 55
```
