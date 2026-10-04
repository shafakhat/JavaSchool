---
title: To get the number of dimensions
nav: To get the number of dimen...
description: Imported from the java2s.com archive: To get the number of dimensions
section: Imported - java2s Archive
order: 2313
source: https://web.archive.org/web/20140829091052/http://www.java2s.com/Tutorial/Java/0140__Collections/Togetthenumberofdimensions.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    String[][] data = new String[3][4];
    System.out.println(getDimension(data));
  }
  public static int getDimension(Object array) {
    int dim = 0;
    Class c = array.getClass();
    while (c.isArray()) {
      c = c.getComponentType();
      dim++;
    }
    return (dim);
  }
}
//2
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
