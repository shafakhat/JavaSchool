---
title: How to define an Array
nav: How to define an Array
description: An array is a named set of same-type variables. Each variable in the array is called an array element. The first element will have an index of 0.
section: Imported - java2s Archive
order: 2291
source: https://web.archive.org/web/20140829093403/http://www.java2s.com/Tutorial/Java/0140__Collections/HowtodefineanArray.htm
---
An array is a named set of same-type variables. Each variable in the array is called an array element. The first element will have an index of 0.

```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int[] intArray = new int[10];
    for (int i = 0; i < 10; i++) {
      intArray[i] = 100;
    }
    for (int i = 0; i < 10; i++) {
      System.out.println(intArray[i]);
    }
  }
}
java title=Example.java
100
100
100
100
100
100
100
100
100
100
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
