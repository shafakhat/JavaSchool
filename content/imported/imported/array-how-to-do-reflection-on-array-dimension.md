---
title: How to do reflection on array dimension
nav: How to do reflection on ar...
description: Next »« PreviousHome » Java Tutorial » ArrayJava ArrayCreate an ArrayArray Index and lengthMultidimensional ArraysArray examplesArray copyArray compareArray Binary search
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20130905073922/http://java2s.com/Tutorials/Java/Array/How_to_do_reflection_on_array_dimension.htm
---
In this chapter you will learn:

- Get array upperbound
- Get the number of dimensions

### Get array upperbound

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    String[][] data = new String[3][4];
    System.out.println("Dimension 1: " + data.length);
    System.out.println("Dimension 2: " + data[0].length);
  }/*fromjava2s.com*/
}
```

Output:

### Get the number of dimensions

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    String[][] data = new String[3][4];
    System.out.println(getDimension(data));
  }/*java2s.com*/publicstaticint getDimension(Object array) {
    int dim = 0;
    Class c = array.getClass();
    while (c.isArray()) {
      c = c.getComponentType();
      dim++;
    }
    return (dim);
  }
}
```

Output:

#### Next chapter...

What you will learn in the next chapter:

- How to clone an Array
- Clones two dimensional float array
