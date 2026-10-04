---
title: Defining Multidimensional Arrays
nav: Defining Multidimensional ...
description: Imported from the java2s.com archive: Defining Multidimensional Arrays
section: Imported - java2s Archive
order: 2311
source: https://web.archive.org/web/20140829091254/http://www.java2s.com/Tutorial/Java/0140__Collections/DefiningMultidimensionalArrays.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    long[][][] beans = new long[5][10][30];
    for (int i = 0; i < beans.length; i++) {
      for (int j = 0; j < beans[i].length; j++) {
        beans[i][j] = new long[(int) (1.0 + 6.0 * Math.random())];
      }
    }
  }
}
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
