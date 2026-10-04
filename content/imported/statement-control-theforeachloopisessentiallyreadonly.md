---
title: The for-each loop is essentially read-only
nav: The for-each loop is essen...
description: Imported from the java2s.com archive: The for-each loop is essentially read-only
section: Imported - java2s Archive
order: 1326
source: https://web.archive.org/web/20140223082435/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Theforeachloopisessentiallyreadonly.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int nums[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    for(int x : nums) {
      System.out.print(x + " ");
      x = x * 10; // no effect on nums
    }
    System.out.println();
    for(int x : nums)
      System.out.print(x + " ");
    System.out.println();
  }
}
java title=Example.java
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
```
