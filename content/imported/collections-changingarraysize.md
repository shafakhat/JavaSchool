---
title: Changing Array Size
nav: Changing Array Size
description: Once an array is created, its size cannot be changed. If you want to change the size, you must create a new array and populates it using the values of the old array.
section: Imported - java2s Archive
order: 2299
source: https://web.archive.org/web/20140829091238/http://www.java2s.com/Tutorial/Java/0140__Collections/ChangingArraySize.htm
---
Once an array is created, its size cannot be changed. If you want to change the size, you must create a new array and populates it using the values of the old array.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int[] numbers = { 1, 2, 3 };
    int[] temp = new int[4];
    int length = numbers.length;
    for (int j = 0; j < length; j++) {
      temp[j] = numbers[j];
    }
    numbers = temp;
  }
}
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
