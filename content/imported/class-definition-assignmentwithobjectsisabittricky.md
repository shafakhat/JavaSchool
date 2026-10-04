---
title: Assignment with objects is a bit tricky.
nav: Assignment with objects is...
description: Imported from the java2s.com archive: Assignment with objects is a bit tricky.
section: Imported - java2s Archive
order: 1250
source: https://web.archive.org/web/20140829090316/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Assignmentwithobjectsisabittricky.htm
---
```java title=Example.java
class Number {
  int i;
}
public class MainClass {
  public static void main(String[] args) {
    Number n1 = new Number();
    Number n2 = new Number();
    n1.i = 9;
    n2.i = 47;
    System.out.println("1: n1.i: " + n1.i + ", n2.i: " + n2.i);
    n1 = n2;
    System.out.println("2: n1.i: " + n1.i + ", n2.i: " + n2.i);
    n1.i = 27;
    System.out.println("3: n1.i: " + n1.i + ", n2.i: " + n2.i);
  }
}
java title=Example.java
1: n1.i: 9, n2.i: 47
2: n1.i: 47, n2.i: 47
3: n1.i: 27, n2.i: 27
```
