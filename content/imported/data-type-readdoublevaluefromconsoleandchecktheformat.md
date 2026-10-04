---
title: Read double value from console and check the format
nav: Read double value from con...
description: Imported from the java2s.com archive: Read double value from console and check the format
section: Imported - java2s Archive
order: 1077
source: https://web.archive.org/web/20140324193923/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Readdoublevaluefromconsoleandchecktheformat.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.InputStreamReader;
class Main {
  public static void main(String args[]) throws Exception {
    InputStreamReader isr = new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(isr);
    while (true) {
      System.out.print("Radius? ");
      String str = br.readLine();
      double radius;
      try {
        radius = Double.valueOf(str).doubleValue();
      } catch (NumberFormatException nfe) {
        System.out.println("Incorrect format!");
        continue;
      }
      if (radius <= 0) {
        System.out.println("Radius must be positive!");
        continue;
      }
      System.out.println("radius " + radius);
      return;
    }
  }
}
```
