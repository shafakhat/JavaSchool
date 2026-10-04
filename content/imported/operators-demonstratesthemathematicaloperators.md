---
title: Demonstrates the mathematical operators
nav: Demonstrates the mathemati...
description: Imported from the java2s.com archive: Demonstrates the mathematical operators
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20070716073034/http://www.java2s.com:80/Tutorial/Java/0060__Operators/Demonstratesthemathematicaloperators.htm
---
```java title=Example.java
import java.util.Random;
public class MainClass {
  static void printInt(String s, int i) {
    System.out.println(s + " = " + i);
  }
  static void printFloat(String s, float f) {
    System.out.println(s + " = " + f);
  }
  public static void main(String[] args) {
    Random rand = new Random();
    int i, j, k;
    j = rand.nextInt(100) + 1;
    k = rand.nextInt(100) + 1;
    printInt("j", j);
    printInt("k", k);
    i = j + k;
    printInt("j + k", i);
    i = j - k;
    printInt("j - k", i);
    i = k / j;
    printInt("k / j", i);
    i = k * j;
    printInt("k * j", i);
    i = k % j;
    printInt("k % j", i);
    j %= k;
    printInt("j %= k", j);
    // Floating-point number tests:
    float u, v, w; // applies to doubles, too
    v = rand.nextFloat();
    w = rand.nextFloat();
    printFloat("v", v);
    printFloat("w", w);
    u = v + w;
    printFloat("v + w", u);
    u = v - w;
    printFloat("v - w", u);
    u = v * w;
    printFloat("v * w", u);
    u = v / w;
    printFloat("v / w", u);
    // the following also works for
    // char, byte, short, int, long,
    // and double:
    u += v;
    printFloat("u += v", u);
    u -= v;
    printFloat("u -= v", u);
    u *= v;
    printFloat("u *= v", u);
    u /= v;
    printFloat("u /= v", u);
  }
}
java title=Example.java
j = 31
k = 84
j + k = 115
j - k = -53
k / j = 2
k * j = 2604
k % j = 22
j %= k = 31
v = 0.79780066
w = 0.9309381
v + w = 1.7287388
v - w = -0.13313746
v * w = 0.7427031
v / w = 0.8569857
u += v = 1.6547863
u -= v = 0.8569857
u *= v = 0.6837037
u /= v = 0.8569856
```
