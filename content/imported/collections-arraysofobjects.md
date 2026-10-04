---
title: Arrays of Objects
nav: Arrays of Objects
description: Arrays of Objects only stores references to the actual objects, and initially each reference is null unless explicitly initialized.
section: Imported - java2s Archive
order: 2321
source: https://web.archive.org/web/20140829075827/http://www.java2s.com/Tutorial/Java/0140__Collections/ArraysofObjects.htm
---
Arrays of Objects only stores references to the actual objects, and initially each reference is null unless explicitly initialized.

```java title=Example.java
public class MainClass {
  public static void main (String args[]) {
    int array1[] = {1, 2, 3, 4, 5};
    for(int i: array1){
      System.out.println(i);
    }
  }
}
```

```java title=Example.java
1
2
3
4
5
```

| 9.6.1. | Arrays of Objects |
|---|---|
| 9.6.2. | Arrays of Strings: using 'new' operator |
| 9.6.3. | Arrays of Strings: initial values determine the size of the array |
| 9.6.4. | Demonstrate String arrays. |
| 9.6.5. | Checks whether two arrays are the same length, treating null arrays as length 0. |
| 9.6.6. | Checks whether two arrays are the same type taking into account multi-dimensional arrays. |
| 9.6.7. | Turn an array of ints into a printable string. |
| 9.6.8. | Check if the given object is an array (primitve or native). |
| 9.6.9. | Reverses the order of the given long type value array. |
| 9.6.10. | Removes the first occurrence of the specified element from the specified array. |
| 9.6.11. | Removes the element at the specified position from the specified array. |
