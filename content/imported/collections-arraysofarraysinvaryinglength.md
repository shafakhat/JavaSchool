---
title: Arrays of Arrays in Varying Length
nav: Arrays of Arrays in Varyin...
description: Imported from the java2s.com archive: Arrays of Arrays in Varying Length
section: Imported - java2s Archive
order: 2308
source: https://web.archive.org/web/20140829091505/http://www.java2s.com/Tutorial/Java/0140__Collections/ArraysofArraysinVaryingLength.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    float[][] samples = new float[6][]; // Define 6 elements,
    // each is an array
    for (int i = 0; i < samples.length; i++) {
      samples[i] = new float[i + 1]; // Allocate each array
    }
    for (int i = 0; i < samples.length; i++) {
      System.out.println(samples[i].length);
    }
  }
}
java title=Example.java
1
2
3
4
5
6
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
