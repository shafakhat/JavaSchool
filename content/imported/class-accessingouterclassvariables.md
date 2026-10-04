---
title: Accessing Outer Class Variables
nav: Accessing Outer Class Vari...
description: Imported from the java2s.com archive: Accessing Outer Class Variables
section: Imported - java2s Archive
order: 1122
source: https://web.archive.org/web/20090530113559/http://www.java2s.com:80/Code/Java/Class/AccessingOuterClassVariables.htm
---
```java title=Example.java
public class MemberClass {
  int counter = 0;
  public class Counter {
    int counter = 10;
    public void increaseCount() {
      counter++;
      MemberClass.this.counter++;
    }
    public void displayCounts() {
      System.out.println("Inner: " + counter);
      System.out.println("Outer: " + MemberClass.this.counter);
    }
  }
  public void go() {
    Counter ct = new Counter();
    ct.increaseCount();
    ct.increaseCount();
    ct.increaseCount();
    ct.displayCounts();
  }
  public static void main(String args[]) {
    MemberClass mc = new MemberClass();
    mc.go();
  }
}
```

1.  Declaring Variables
---  ---
2.  Specifying initial values in a class definition
3.  The full process of initialization
