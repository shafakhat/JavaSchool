---
title: Using the Collection-Based for Loop with an Array
nav: Using the Collection-Based...
description: You can now use it to iterate over an array or a collection without the index. Use this syntax to iterate over an array:
section: Imported - java2s Archive
order: 2298
source: https://web.archive.org/web/20140827195548/http://www.java2s.com/Tutorial/Java/0140__Collections/UsingtheCollectionBasedforLoopwithanArray.htm
---
You can now use it to iterate over an array or a collection without the index. Use this syntax to iterate over an array:

```java title=Example.java
for (componentType variable: arrayName)
```

Where arrayName is the reference to the array, componentType is the component type of the array, and variable is a variable that references each component of the array.

```java title=Example.java
import java.util.Arrays;
public class MainClass {
  public static void main(String[] arg) {
    double[] data = new double[50]; // An array of 50 values of type double
    Arrays.fill(data, 1.0);                     // Fill all elements of data with 1.0
    for (double d: data) {
      System.out.println(d);
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
