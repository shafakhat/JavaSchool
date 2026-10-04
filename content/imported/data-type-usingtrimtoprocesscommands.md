---
title: Using trim() to process commands.
nav: Using trim() to process co...
description: BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
section: Imported - java2s Archive
order: 1121
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usingtrimtoprocesscommands.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class UseTrim {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str;
    System.out.println("Enter 'stop' to quit.");
    System.out.println("Enter letter: ");
    do {
      str = br.readLine();
      str = str.trim();
      if (str.equals("I"))
        System.out.println("I");
      else if (str.equals("M"))
        System.out.println("M");
      else if (str.equals("C"))
        System.out.println("C.");
      else if (str.equals("W"))
        System.out.println("W");
    } while (!str.equals("stop"));
  }
}
```
