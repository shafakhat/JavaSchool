---
title: Iterating over Multidimensional Arrays
nav: Iterating over Multidimens...
description: Imported from the java2s.com archive: Iterating over Multidimensional Arrays
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20140216232803/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/IteratingoverMultidimensionalArraysUseforeachstyleforonatwodimensionalarray.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int sum = 0;
    int nums[][] = new int[3][5];
    // give nums some values
    for (int i = 0; i < 3; i++)
      for (int j = 0; j < 5; j++)
        nums[i][j] = (i + 1) * (j + 1);
    // use for-each for to display and sum the values
    for (int x[] : nums) {
      for (int y : x) {
        System.out.println("Value is: " + y);
        sum += y;
      }
    }
    System.out.println("Summation: " + sum);
  }
}
java title=Example.java
Value is: 1
Value is: 2
Value is: 3
Value is: 4
Value is: 5
Value is: 2
Value is: 4
Value is: 6
Value is: 8
Value is: 10
Value is: 3
Value is: 6
Value is: 9
Value is: 12
Value is: 15
Summation: 90
```

| 4.7.1. | The For-Each Version of the for Loop |
|---|---|
| 4.7.2. | The for-each loop is essentially read-only |
| 4.7.3. | The for each loop for an enum data type |
| 4.7.4. | Using the For-Each Loop with Collections: ArrayList |
| 4.7.5. | Use a for-each style for loop |
| 4.7.6. | Using 'for each' to loop through array |
| 4.7.7. | Iterating over Multidimensional Arrays: Use for-each style for on a two-dimensional array |
| 4.7.8. | Using break with a for-each-style for |
