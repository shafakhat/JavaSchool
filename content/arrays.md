---
title: Java Arrays
nav: Arrays
description: Declare, initialize, access, loop and clone arrays; multi-dimensional arrays and common array algorithms.
section: Java Basics
order: 80
---

## What is an array?

An array is a fixed-size container holding elements of the **same type**. Each element has an index starting at **0**.

```java title=FirstArray.java
import java.util.Arrays;

public class FirstArray {
    public static void main(String[] args) {
        // declare + allocate
        int[] scores = new int[3];
        scores[0] = 90;
        scores[1] = 85;
        scores[2] = 78;

        // declare + initialize in one line
        String[] names = {"Aditi", "Rahul", "Mei"};

        System.out.println(scores[0]);      // 90
        System.out.println(names[2]);       // Mei
        System.out.println(scores.length);  // 3 (length, not a method)
        System.out.println(Arrays.toString(scores));  // [90, 85, 78]
    }
}
```

> **Warning:** Accessing `scores[3]` throws `ArrayIndexOutOfBoundsException` at runtime. `scores.length` is always the maximum legal index + 1.

## Ways to initialize

```java title=Init.java
import java.util.Arrays;

public class Init {
    public static void main(String[] args) {
        int[] a = new int[5];                    // all zeros
        int[] b = {1, 2, 3};                     // literal
        int[] c = new int[]{4, 5, 6};            // explicit literal
        double[] d = new double[3];              // 0.0
        boolean[] e = new boolean[2];            // false
        String[] f = new String[2];              // null!

        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(d));
        System.out.println(f[0] == null);        // true - reference arrays start null
    }
}
```

Default values: `0`, `0.0`, `false`, `'\0'`, `null`.

## Looping over an array

```java title=LoopArray.java
public class LoopArray {
    public static void main(String[] args) {
        double[] prices = {19.99, 5.50, 120.0};

        // classic index loop - when you need the position
        for (int i = 0; i < prices.length; i++) {
            System.out.println(i + " -> " + prices[i]);
        }

        // for-each - when you only need the value
        double total = 0;
        for (double p : prices) {
            total += p;
        }
        System.out.printf("total = %.2f%n", total);
    }
}
```

## Searching, min/max, copying

```java title=Algorithms.java
import java.util.Arrays;

public class Algorithms {
    public static void main(String[] args) {
        int[] nums = {7, 2, 9, 4, 9};

        // linear search
        int target = 4;
        int foundAt = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) { foundAt = i; break; }
        }
        System.out.println("index of 4 = " + foundAt);

        // min / max
        int min = nums[0], max = nums[0];
        for (int n : nums) {
            if (n < min) min = n;
            if (n > max) max = n;
        }
        System.out.println("min=" + min + " max=" + max);

        // built-in tools
        int[] copy = Arrays.copyOf(nums, nums.length);   // full copy
        int[] sorted = nums.clone();                     // another copy
        Arrays.sort(sorted);                             // ascending
        System.out.println(Arrays.toString(sorted));
        System.out.println(Arrays.binarySearch(sorted, 9)); // works on SORTED arrays

        // fill
        int[] board = new int[4];
        Arrays.fill(board, -1);
        System.out.println(Arrays.toString(board));
    }
}
```

> **Tip:** `Arrays.equals(a, b)` compares content; `a == b` only compares references. `Arrays.deepEquals` handles nested arrays.

## Two-dimensional arrays

A 2D array is "an array of arrays" - perfect for grids, matrices and tables:

```java title=Matrix.java
import java.util.Arrays;

public class Matrix {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // nested loops
        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[row].length; col++) {
                System.out.printf("%4d", matrix[row][col]);
            }
            System.out.println();
        }

        // sum of a row
        System.out.println("row 1 sum = " + Arrays.stream(matrix[1]).sum());

        // jagged arrays: rows of different lengths
        int[][] jagged = new int[3][];
        jagged[0] = new int[2];
        jagged[1] = new int[4];
        jagged[2] = new int[1];
        System.out.println("rows=" + jagged.length + " r1=" + jagged[1].length);
    }
}
```

```text title=Output
   1   2   3
   4   5   6
   7   8   9
row 1 sum = 15
rows=3 r1=4
```

## Passing arrays to methods

Arrays are **objects**, so methods receive a *reference* - changes to elements are visible to the caller:

```java title=PassArrays.java
import java.util.Arrays;

public class PassArrays {
    static void doubleAll(int[] values) {
        for (int i = 0; i < values.length; i++) {
            values[i] *= 2;          // mutates the caller's array
        }
    }

    static int sum(int... nums) {    // varargs = array under the hood
        int s = 0;
        for (int n : nums) s += n;
        return s;
    }

    public static void main(String[] args) {
        int[] data = {1, 2, 3};
        doubleAll(data);
        System.out.println(Arrays.toString(data));   // [2, 4, 6]

        System.out.println(sum(1, 2, 3, 4));         // 10
        System.out.println(sum());                   // 0
    }
}
```

Reassigning the parameter itself (`values = new int[0]`) only affects the method's local reference - not the caller.

## When to use something else

Arrays are fast and memory-friendly, but fixed-size. When you need to grow dynamically, use a collection:

| Need | Use |
|---|---|
| Fixed size, same type, max speed | `array` |
| Grow/shrink, insert/remove | `ArrayList` |
| Unique elements | `HashSet` |
| Key-value lookup | `HashMap` |

Continue to [Methods](methods.html), or jump to [Collections](collections.html).

> **Remember:** In Java, arrays are objects too - `length` is a field, `clone()`/`stream()` are methods, and they can be passed like any other object.
