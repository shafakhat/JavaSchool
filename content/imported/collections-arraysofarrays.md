---
title: Arrays of Arrays
nav: Arrays of Arrays
description: Imported from the java2s.com archive: Arrays of Arrays
section: Imported - java2s Archive
order: 2307
source: https://web.archive.org/web/20140829091605/http://www.java2s.com/Tutorial/Java/0140__Collections/ArraysofArrays.htm
---
```java title=Example.java
public class MainClass public class MainClass {
  public static void main(String[] args) {
    float[][] t = new float[10][365]; // Temperature array
    for (int i = 0; i < t.length; i++) {
      for (int j = 0; j < t[i].length; j++) {
        t[i][j] = (float) (45.0 * Math.random() - 10.0);
      }
    }
    float average = 0.0f;
    for (int i = 0; i < t.length; i++) {
      for (int j = 0; j < t[i].length; j++) {
        average += t[i][j];
      }
    }
    System.out.println(average);
  }
}
java title=Example.java
44505.707
```

| 9.4.1. | Initialize a two-dimensional array in matrix |
|---|---|
| 9.4.2. | Arrays of Arrays |
| 9.4.3. | Arrays of Arrays in Varying Length |
| 9.4.4. | Defining Multidimensional Arrays |
| 9.4.5. | Array Of int Arrays |
| 9.4.6. | Get array upperbound |
| 9.4.7. | To get the number of dimensions |
| 9.4.8. | Array Of string Arrays |
