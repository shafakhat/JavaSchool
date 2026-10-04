---
title: Use an array to pass a variable number of arguments to a method. This is the old-style approach to variable-length arguments.
nav: Use an array to pass a var...
description: System.out.print("Number of args: " + v.length + " Contents: ");
section: Imported - java2s Archive
order: 1217
source: https://web.archive.org/web/20140829080732/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/UseanarraytopassavariablenumberofargumentstoamethodThisistheoldstyleapproachtovariablelengtharguments.htm
---
```java title=Example.java
class PassArray {
  static void vaTest(int v[]) {
    System.out.print("Number of args: " + v.length + " Contents: ");
    for (int x : v)
      System.out.print(x + " ");
    System.out.println();
  }
  public static void main(String args[]) {
    int n1[] = { 10 };
    int n2[] = { 1, 2, 3 };
    int n3[] = {};
    vaTest(n1); // 1 arg
    vaTest(n2); // 3 args
    vaTest(n3); // no args
  }
}
```
