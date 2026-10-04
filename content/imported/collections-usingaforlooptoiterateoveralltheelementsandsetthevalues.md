---
title: Using a for loop to iterate over all the elements and set the values
nav: Using a for loop to iterat...
description: double[] data = new double[50]; // An array of 50 values of type double
section: Imported - java2s Archive
order: 2297
source: https://web.archive.org/web/20140829091108/http://www.java2s.com/Tutorial/Java/0140__Collections/Usingaforlooptoiterateoveralltheelementsandsetthevalues.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    double[] data = new double[50]; // An array of 50 values of type double
    for (int i = 0; i < data.length; i++) { // i from 0 to data.length-1
      data[i] = 1.0;
    }
    for (int i = 0; i < data.length; i++) { // i from 0 to data.length-1
      System.out.println(data[i]);
    }
  }
}
java title=Example.java
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
```

| 9.3.1. | How to define an Array |
|---|---|
| 9.3.2. | Initializing array elements by index |
| 9.3.3. | Alternative Array Declaration Syntax |
| 9.3.4. | Anonymous arrays are declared similarly to regular arrays |
| 9.3.5. | An array is a Java object |
| 9.3.6. | To reference the components of an array |
| 9.3.7. | The Length of an Array |
| 9.3.8. | Initializing Arrays |
| 9.3.9. | Using a for loop to iterate over all the elements and set the values |
| 9.3.10. | Arrays of Characters |
| 9.3.11. | Using the Collection-Based for Loop with an Array |
| 9.3.12. | Changing Array Size |
| 9.3.13. | Array Reallocation |
| 9.3.14. | Use System.arraycopy to duplicate array |
| 9.3.15. | Minimum and maximum number in array |
| 9.3.16. | Shuffle elements of an array |
| 9.3.17. | Merge (or add) two arrays into one |
| 9.3.18. | Circular Buffer |
