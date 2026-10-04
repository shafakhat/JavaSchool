---
title: sums a list of numbers entered by the user
nav: sums a list of numbers ent...
description: BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
section: Imported - java2s Archive
order: 1207
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/sumsalistofnumbersenteredbytheuser.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class ParseDemo {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str;
    int i;
    int sum = 0;
    System.out.println("Enter numbers, 0 to quit.");
    do {
      str = br.readLine();
      try {
        i = Integer.parseInt(str);
      } catch (NumberFormatException e) {
        System.out.println("Invalid format");
        i = 0;
      }
      sum += i;
      System.out.println("Current sum is: " + sum);
    } while (i != 0);
  }
}
```
