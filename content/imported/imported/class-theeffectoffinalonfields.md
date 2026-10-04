---
title: The effect of final on fields
nav: The effect of final on fie...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1079
source: https://web.archive.org/web/20090531211320/http://www.java2s.com:80/Code/Java/Class/Theeffectoffinalonfields.htm
---
```java title=Example.java
// : c06:FinalData.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.Random;
class Value {
  int i; // Package access
  public Value(int i) {
    this.i = i;
  }
}
public class FinalData {
  private static Random rand = new Random();
  private String id;
  public FinalData(String id) {
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
  private Value v1 = new Value(11);
  private final Value v2 = new Value(22);
  private static final Value v3 = new Value(33);
  // Arrays:
  private final int[] a = { 1, 2, 3, 4, 5, 6 };
  public String toString() {
    return id + ": " + "i4 = " + i4 + ", i5 = " + i5;
  }
  public static void main(String[] args) {
    FinalData fd1 = new FinalData("fd1");
    //! fd1.VAL_ONE++; // Error: can't change value
    fd1.v2.i++; // Object isn't constant!
    fd1.v1 = new Value(9); // OK -- not final
    for (int i = 0; i < fd1.a.length; i++)
      fd1.a[i]++; // Object isn't constant!
    //! fd1.v2 = new Value(0); // Error: Can't
    //! fd1.v3 = new Value(1); // change reference
    //! fd1.a = new int[3];
    System.out.println(fd1);
    System.out.println("Creating new FinalData");
    FinalData fd2 = new FinalData("fd2");
    System.out.println(fd1);
    System.out.println(fd2);
  }
} ///:~
```

1.  Java Final variable: Once created and initialized, its value can not be changed
---  ---
2.  Blank final fields
3.  Experiment with final args to functions
4.  Using final with method arguments
5.  Making an entire class final
