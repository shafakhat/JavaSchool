---
title: Using break with a for-each-style for
nav: Using break with a for-eac...
description: Imported from the java2s.com archive: Using break with a for-each-style for
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20140829083241/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Usingbreakwithaforeachstylefor.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int sum = 0;
    int nums[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    // Use for to display and sum the values.
    for (int x : nums) {
      System.out.println("Value is: " + x);
      sum += x;
      if (x == 5){
        break; // stop the loop when 5 is obtained
      }
    }
    System.out.println("Summation of first 5 elements: " + sum);
  }
}
java title=Example.java
Value is: 1
Value is: 2
Value is: 3
Value is: 4
Value is: 5
Summation of first 5 elements: 15
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
