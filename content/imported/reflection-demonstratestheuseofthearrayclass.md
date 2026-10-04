---
title: Demonstrates the use of the Array class
nav: Demonstrates the use of th...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 2160
source: https://web.archive.org/web/20140829094510/http://www.java2s.com/Tutorial/Java/0125__Reflection/DemonstratestheuseoftheArrayclass.htm
---
```java title=Example.java
/*
 *     file: ArrayDemo.java
 *  package: oreilly.hcj.reflection
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.lang.reflect.Array;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision$
 */
public class ArrayDemo {
  /**
   * Copy an array and return the copy.
   *
   * @param input The array to copy.
   *
   * @return The coppied array.
   *
   * @throws IllegalArgumentException If input is not an array.
   */
  public static Object copyArray(final Object input) {
    final Class type = input.getClass();
    if (!type.isArray()) {
      throw new IllegalArgumentException();
    }
    final int length = Array.getLength(input);
    final Class componentType = type.getComponentType();
    final Object result = Array.newInstance(componentType, length);
    for (int idx = 0; idx < length; idx++) {
      Array.set(result, idx, Array.get(input, idx));
    }
    return result;
  }
  /**
   * Run the demo.
   *
   * @param args Command line arguments (ignored).
   */
  public static void main(final String[] args) {
    try {
      int[] x = new int[] { 2, 3, 8, 7, 5 };
      char[] y = new char[] { 'a', 'z', 'e' };
      String[] z = new String[] { "Jim", "John", "Joe" };
      System.out.println(" -- x and y --");
      outputArrays(x, y);
      System.out.println(" -- x and copy of x --");
      outputArrays(x, copyArray(x));
      System.out.println(" -- y and copy of y --");
      outputArrays(y, copyArray(y));
      System.out.println(" -- z and copy of z --");
      outputArrays(z, copyArray(z));
    } catch (final Exception ex) {
      ex.printStackTrace();
    }
  }
  /**
   * Print out 2 arrays in columnar format.
   *
   * @param first The array for the first column.
   * @param second The array for the second column.
   *
   * @throws IllegalArgumentException __UNDOCUMENTED__
   */
  public static void outputArrays(final Object first, final Object second) {
    if (!first.getClass()
              .isArray()) {
      throw new IllegalArgumentException("first is not an array.");
    }
    if (!second.getClass()
               .isArray()) {
      throw new IllegalArgumentException("second is not an array.");
    }
    final int lengthFirst = Array.getLength(first);
    final int lengthSecond = Array.getLength(second);
    final int length = Math.max(lengthFirst, lengthSecond);
    for (int idx = 0; idx < length; idx++) {
      System.out.print("[" + idx + "]\t");
      if (idx < lengthFirst) {
        System.out.print(Array.get(first, idx) + "\t\t");
      } else {
        System.out.print("\t\t");
      }
      if (idx < lengthSecond) {
        System.out.print(Array.get(second, idx) + "\t");
      }
      System.out.println();
    }
  }
}
/* ########## End of File ########## */
```

| 7.9.1. | Determining If an Object Is an Array |
|---|---|
| 7.9.2. | Demonstrates the use of the Array class |
| 7.9.3. | Create array with Array.newInstance |
| 7.9.4. | Is field an array |
| 7.9.5. | Create integer array with Array.newInstance |
| 7.9.6. | Use Array.setInt to fill an array |
| 7.9.7. | Use Array.setShort and Array.setLong |
| 7.9.8. | Getting the Length and Dimensions of an Array Object |
| 7.9.9. | Getting the Component Type of an Array Object |
| 7.9.10. | Array reflection and two dimensional array |
| 7.9.11. | class name for double and float array |
| 7.9.12. | Returns the length of the specified array, can deal with Object arrays and with primitive arrays. |
