---
title: Limiting the object Types in a Variable Argument List
nav: Limiting the object Types ...
description: System.out.println(average(new Double(7), new Double(8), new Double(9), new Double(10)));
section: Imported - java2s Archive
order: 1233
source: https://web.archive.org/web/20140829083836/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/LimitingtheobjectTypesinaVariableArgumentList.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    System.out.println(average(1.0, 2.0, 3.0, 4.0, 5.0));
    System.out.println(average(3.14, 1.414, 1.732));
    System.out.println(average(new Double(7), new Double(8), new Double(9), new Double(10)));
  }
  // Average of a variable number of values
  public static double average(Double... args) {
    if (args.length == 0) {
      return 0.0;
    }
    double ave = 0.0;
    for (double value : args) {
      ave += value;
    }
    return ave / args.length;
  }
}
```
