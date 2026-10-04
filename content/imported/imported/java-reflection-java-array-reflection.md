---
title: Java Reflection - Java Array Reflection
nav: Java Reflection - Java Arr...
description: We can use isArray() method from Class class to check if a class is an array.
section: Imported - java2s Archive
order: 50409
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0090__Java_Array_Reflection.html
---
```java title=Example.java
« Previous
```

- Next »

We can use isArray() method from Class class to check if a class is an array.

We can create an array, read and modify its element's values using reflection through java.lang.reflect.Array class.

The getLength() method from Array class gets the length of an array.

All methods from the Array class are static.

To create an array, use the overloaded static method newInstance() from the Array class.

```java title=Example.java

Object newInstance(Class<?> componentType,  int  arrayLength)
Object newInstance(Class<?> componentType,  int... dimensions)
```

The first method creates an array from the specified component type and array length.

The second version creates an array of the specified component type and dimensions.

The return type from the newInstance() method is Object and we need to cast it to the actual array type.

The following code creates an array of int of length 5.

```java title=Example.java

int[] ids = (int[])Array.newInstance(int.class, 5);
```

To create an array of int of dimension 5 by 3.

```java title=Example.java

int[][] matrix = (int[][])Array.newInstance(int.class, 5, 3);
```

## Example

The following code shows how to create an array dynamically and manipulate its elements.

```java title=Example.java
import java.lang.reflect.Array;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    try {
      Object my = Array.newInstance(int.class, 2);
      int n1 = Array.getInt(my, 0);
      int n2 = Array.getInt(my, 1);
      System.out.println("n1 = " + n1 + ", n2=" + n2);
      Array.set(my, 0, 11);
      Array.set(my, 1, 12);
      n1 = Array.getInt(my, 0);
      n2 = Array.getInt(my, 1);
      System.out.println("n1 = " + n1 + ", n2=" + n2);
    } catch (NegativeArraySizeException | IllegalArgumentException
        | ArrayIndexOutOfBoundsException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

## Get the dimension of an array

Java supports an array of arrays.

The method getComponentType() from Class class returns the Class object for an array's element type.

The following code illustrates how to get the dimension of an array.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int[][][] intArray = newint[1][2][3];
/*www.java2s.com*/
    System.out.println("int[][][] dimension is " + getArrayDimension(intArray));
  }
  publicstaticint getArrayDimension(Object array) {
    int dimension = 0;
    Class c = array.getClass();
    if (!c.isArray()) {
      thrownew IllegalArgumentException("Object is not  an  array");
    }
    while (c.isArray()) {
      dimension++;
      c = c.getComponentType();
    }
    return dimension;
  }
}
```

The code above generates the following result.

## Expanding an Array

Java array is a fixed-length data structure.

To enlarge array we can create an array of a bigger size and copy the old array elements to the new one

The following code shows how to expand an Array Using Reflection

```java title=Example.java
import java.lang.reflect.Array;
import java.util.Arrays;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] ids = newint[2];
    System.out.println(ids.length);
    System.out.println(Arrays.toString(ids));
    ids = (int[]) expandBy(ids, 2);
    ids[2] = 3;
    System.out.println(ids.length);
    System.out.println(Arrays.toString(ids));
  }
  publicstatic Object expandBy(Object oldArray, int increment) {
    Object newArray = null;
    int oldLength = Array.getLength(oldArray);
    int newLength = oldLength + increment;
    Class<?> c = oldArray.getClass();
    newArray = Array.newInstance(c.getComponentType(), newLength);
    System.arraycopy(oldArray, 0, newArray, 0, oldLength);
    return newArray;
  }
}
```

The code above generates the following result.

- Next »
- « Previous
