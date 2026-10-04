---
title: Generate a random array of numbers
nav: Generate a random array of...
description: Imported from the java2s.com archive: Generate a random array of numbers
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20101101055010/http://www.java2s.com:80/Tutorial/Java/0120__Development/Generatearandomarrayofnumbers.htm
---
```java title=Example.java
import java.util.Random;
public class Main {
  public static void main(String[] args) {
    Random r = new Random();
    // generate some random boolean values
    boolean[] booleans = new boolean[10];
    for (int i = 0; i < booleans.length; i++) {
      booleans[i] = r.nextBoolean();
    }
    for (boolean b : booleans) {
      System.out.print(b + ", ");
    }
    // generate a uniformly distributed int random numbers
    int[] integers = new int[10];
    for (int i = 0; i < integers.length; i++) {
      integers[i] = r.nextInt();
    }
    for (int i : integers) {
      System.out.print(i + ", ");
    }
    // generate a uniformly distributed float random numbers
    float[] floats = new float[10];
    for (int i = 0; i < floats.length; i++) {
      floats[i] = r.nextFloat();
    }
    for (float f : floats) {
      System.out.print(f + ", ");
    }
    // generate a Gaussian normally distributed random numbers
    double[] gaussians = new double[10];
    for (int i = 0; i < gaussians.length; i++) {
      gaussians[i] = r.nextGaussian();
    }
    for (double d : gaussians) {
      System.out.print(d + ", ");
    }
  }
}
```
