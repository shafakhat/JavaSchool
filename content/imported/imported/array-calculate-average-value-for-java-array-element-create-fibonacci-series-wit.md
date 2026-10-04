---
title: Calculate average value for Java array element, Create Fibonacci Series with array, Matrix calculation
nav: Calculate average value fo...
description: The following code declares an int array and stores integer value into it. Then it uses a for loop to go through each element in that array and sum the int value. Finally
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20130905061854/http://java2s.com/Tutorials/Java/Array/Calculate_average_value_for_Java_array_element_Create_Fibonacci_Series_with_array_Matrix_calculation.htm
---
In this chapter you will learn:

- Calculate Average value of Array elements
- How to Create Fibonacci Series with array
- How to use two-dimensional double type array to do Matrix calculation

### Calculate with Array

The following code declares an int array and stores integer value into it. Then it uses a for loop to go through each element in that array and sum the int value. Finally it divides the sum by the array length and output the average.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
/*java2s.com*/int[] intArray = newint[] { 1, 2, 3, 4, 5 };
    // calculate sum
int sum = 0;
    for (int i = 0; i < intArray.length; i++){
      sum = sum + intArray[i];
    }
    // calculate average
double average = sum / intArray.length;

    System.out.println("average: " + average);
  }
}
```

The output:

### Create Fibonacci Series with array

The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.

```java title=Example.java
import java.util.Arrays;
/*fromjava2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    int length = 20;
    long[] series = newlong[length];
    series[0] = 0;
    series[1] = 1;
    for (int i = 2; i < length; i++) {
      series[i] = series[i - 1] + series[i - 2];
    }
    System.out.print(Arrays.toString(series));
  }
}
```

The output:

### Two-dimensional double type array and Matrix calculation

The following code use two-dimensional double type array to do Matrix calculation

```java title=Example.java
class Matrix {//fromjava2s.comprivatedouble[][] doubleArray;

  Matrix(int nrows, int ncols) {
    doubleArray = newdouble[nrows][ncols];
  }

  int getCols() {
    return doubleArray[0].length;
  }

  int getRows() {
    return doubleArray.length;
  }

  double getValue(int row, int col) {
    return doubleArray[row][col];
  }

  void setValue(int row, int col, double value) {
    doubleArray[row][col] = value;
  }
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    Matrix a = new Matrix(1, 3);
    a.setValue(0, 0, 1); // | 1 2 3 |
    a.setValue(0, 1, 2);
    a.setValue(0, 2, 3);
    dump(a);
    Matrix b = new Matrix(3, 2);
    b.setValue(0, 0, 4); // | 4 7 |
    b.setValue(1, 0, 5); // | 5 8 |
    b.setValue(2, 0, 6); // | 6 9 |
    b.setValue(0, 1, 7);
    b.setValue(1, 1, 8);
    b.setValue(2, 1, 9);
    dump(b);
    dump(multiply(a, b));
  }

  staticvoid dump(Matrix m) {
    for (int i = 0; i < m.getRows(); i++) {
      for (int j = 0; j < m.getCols(); j++){
        System.out.print(m.getValue(i, j) + " ");
      }
      System.out.println();
    }
    System.out.println();
  }

  static Matrix multiply(Matrix a, Matrix b) {
    if (a.getCols() != b.getRows()) {
      thrownew IllegalArgumentException("rows/columns mismatch");
    }
    Matrix result = new Matrix(a.getRows(), b.getCols());
    for (int i = 0; i < a.getRows(); i++) {
      for (int j = 0; j < b.getCols(); j++) {
        for (int k = 0; k < a.getCols(); k++) {
          result.setValue(i, j, result.getValue(i, j) + a.getValue(i, k) * b.getValue(k, j));
        }
      }
    }

    return result;
  }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- Copy array
- Copy array
