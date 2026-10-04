---
title: Handle an exception and move on.
nav: Handle an exception and mo...
description: Imported from the java2s.com archive: Handle an exception and move on.
section: Imported - java2s Archive
order: 1180
source: https://web.archive.org/web/20140829082435/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Handleanexceptionandmoveon.htm
---
```java title=Example.java
import java.util.Random;
public class MainClass {
  public static void main(String args[]) {
    int a = 0, b = 0, c = 0;
    Random r = new Random();
    for (int i = 0; i < 32000; i++) {
      try {
        b = r.nextInt();
        c = r.nextInt();
        a = 12345 / (b / c);
      } catch (ArithmeticException e) {
        System.out.println("Division by zero.");
        a = 0; // set a to zero and continue
      }
      System.out.println("a: " + a);
    }
  }
}
```
