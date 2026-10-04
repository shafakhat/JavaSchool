---
title: The effect of final on fields
nav: The effect of final on fie...
description: Imported from the java2s.com archive: The effect of final on fields
section: Imported - java2s Archive
order: 1140
source: https://web.archive.org/web/20140829085854/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Theeffectoffinalonfields.htm
---
```java title=Example.java
import java.util.Random;
class A {
  int i; // Package access
  public A(int i) {
    this.i = i;
  }
}
public class MainClass {
  private static Random rand = new Random();
  private String id;
  public MainClass(String id) {
    this.id = id;
  }
  // Can be compile-time constants:
  private final int VAL_ONE = 9;
  private static final int VAL_TWO = 99;
  // Typical public constant:
  public static final int VAL_THREE = 39;
  // Cannot be compile-time constants:
  private final int i4 = rand.nextInt(20);
  static final int i5 = rand.nextInt(20);
  private A v1 = new A(11);
  private final A v2 = new A(22);
  private static final A v3 = new A(33);
  // Arrays:
  private final int[] a = { 1, 2, 3, 4, 5, 6 };
  public String toString() {
    return id + ": " + "i4 = " + i4 + ", i5 = " + i5;
  }
  public static void main(String[] args) {
    MainClass fd1 = new MainClass("fd1");
    fd1.v2.i++;
    fd1.v1 = new A(9);
    for (int i = 0; i < fd1.a.length; i++)
      fd1.a[i]++;
    System.out.println(fd1);
    System.out.println("Creating new FinalData");
    MainClass fd2 = new MainClass("fd2");
    System.out.println(fd1);
    System.out.println(fd2);
  }
}
java title=Example.java
fd1: i4 = 15, i5 = 5
Creating new FinalData
fd1: i4 = 15, i5 = 5
fd2: i4 = 15, i5 = 5
```

| 5.27.1. | final Variables |
|---|---|
| 5.27.2. | 'Blank' final fields |
| 5.27.3. | Java Final variable: Once created and initialized, its value can not be changed |
| 5.27.4. | Using 'final' with method arguments |
| 5.27.5. | The effect of final on fields |
| 5.27.6. | You can override a private or private final method |
| 5.27.7. | Making an entire class final |
| 5.27.8. | Demonstrates how final variables are replaced at compilation time |
| 5.27.9. | Demonstration of final class members |
| 5.27.10. | Base class for demonstation of final methods |
| 5.27.11. | Demonstration of final constants |
| 5.27.12. | Demonstration of final variables |
