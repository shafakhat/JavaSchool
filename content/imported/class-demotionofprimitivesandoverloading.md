---
title: Demotion of primitives and overloading
nav: Demotion of primitives and...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20090531215003/http://www.java2s.com:80/Code/Java/Class/Demotionofprimitivesandoverloading.htm
---
```java title=Example.java
// : c04:Demotion.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Demotion {
  void f1(char x) {
    System.out.println("f1(char)");
  }
  void f1(byte x) {
    System.out.println("f1(byte)");
  }
  void f1(short x) {
    System.out.println("f1(short)");
  }
  void f1(int x) {
    System.out.println("f1(int)");
  }
  void f1(long x) {
    System.out.println("f1(long)");
  }
  void f1(float x) {
    System.out.println("f1(float)");
  }
  void f1(double x) {
    System.out.println("f1(double)");
  }
  void f2(char x) {
    System.out.println("f2(char)");
  }
  void f2(byte x) {
    System.out.println("f2(byte)");
  }
  void f2(short x) {
    System.out.println("f2(short)");
  }
  void f2(int x) {
    System.out.println("f2(int)");
  }
  void f2(long x) {
    System.out.println("f2(long)");
  }
  void f2(float x) {
    System.out.println("f2(float)");
  }
  void f3(char x) {
    System.out.println("f3(char)");
  }
  void f3(byte x) {
    System.out.println("f3(byte)");
  }
  void f3(short x) {
    System.out.println("f3(short)");
  }
  void f3(int x) {
    System.out.println("f3(int)");
  }
  void f3(long x) {
    System.out.println("f3(long)");
  }
  void f4(char x) {
    System.out.println("f4(char)");
  }
  void f4(byte x) {
    System.out.println("f4(byte)");
  }
  void f4(short x) {
    System.out.println("f4(short)");
  }
  void f4(int x) {
    System.out.println("f4(int)");
  }
  void f5(char x) {
    System.out.println("f5(char)");
  }
  void f5(byte x) {
    System.out.println("f5(byte)");
  }
  void f5(short x) {
    System.out.println("f5(short)");
  }
  void f6(char x) {
    System.out.println("f6(char)");
  }
  void f6(byte x) {
    System.out.println("f6(byte)");
  }
  void f7(char x) {
    System.out.println("f7(char)");
  }
  void testDouble() {
    double x = 0;
    System.out.println("double argument:");
    f1(x);
    f2((float) x);
    f3((long) x);
    f4((int) x);
    f5((short) x);
    f6((byte) x);
    f7((char) x);
  }
  public static void main(String[] args) {
    Demotion p = new Demotion();
    p.testDouble();
  }
} ///:~
```

1.  Demonstration of both constructor and ordinary method overloading
---  ---
2.  Overloaded constructor
3.  Overloaded method
4.  Demonstration of overriding fields
5.  Overloading based on the order of the arguments
6.  Promotion of primitives and overloading
7.  Overloading a base-class method name in a derived class does not hide the base-class versions
