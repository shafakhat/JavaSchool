---
title: Performs an xor on a set of booleans.
nav: Performs an xor on a set o...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1167
source: https://web.archive.org/web/20100222021254/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Performsanxoronasetofbooleans.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * Operations on boolean primitives and Boolean objects.
 *
 * This class tries to handle <code>null</code> input gracefully.
 * An exception will not be thrown for a <code>null</code> input.
 * Each method documents its behaviour in more detail.
 *
 * @author Stephen Colebourne
 * @author Matthew Hawthorne
 * @author Gary Gregory
 * @since 2.0
 * @version $Id: BooleanUtils.java 589050 2007-10-27 05:07:45Z bayard $
 */
public class Main {
  /**
   * Performs an xor on a set of booleans.
   *
   * <pre>
   *   BooleanUtils.xor(new boolean[] { true, true })   = false
   *   BooleanUtils.xor(new boolean[] { false, false }) = false
   *   BooleanUtils.xor(new boolean[] { true, false })  = true
   * </pre>
   *
   * @param array  an array of <code>boolean<code>s
   * @return <code>true</code> if the xor is successful.
   * @throws IllegalArgumentException if <code>array</code> is <code>null</code>
   * @throws IllegalArgumentException if <code>array</code> is empty.
   */
  public static boolean xor(boolean[] array) {
      // Validates input
      if (array == null) {
          throw new IllegalArgumentException("The Array must not be null");
      } else if (array.length == 0) {
          throw new IllegalArgumentException("Array is empty");
      }
      // Loops through array, comparing each item
      int trueCount = 0;
      for (int i = 0; i < array.length; i++) {
          // If item is true, and trueCount is < 1, increments count
          // Else, xor fails
          if (array[i]) {
              if (trueCount < 1) {
                  trueCount++;
              } else {
                  return false;
              }
          }
      }
      // Returns true if there was exactly 1 true item
      return trueCount == 1;
  }
  /**
   * Performs an xor on an array of Booleans.
   *
   * <pre>
   *   BooleanUtils.xor(new Boolean[] { Boolean.TRUE, Boolean.TRUE })   = Boolean.FALSE
   *   BooleanUtils.xor(new Boolean[] { Boolean.FALSE, Boolean.FALSE }) = Boolean.FALSE
   *   BooleanUtils.xor(new Boolean[] { Boolean.TRUE, Boolean.FALSE })  = Boolean.TRUE
   * </pre>
   *
   * @param array  an array of <code>Boolean<code>s
   * @return <code>true</code> if the xor is successful.
   * @throws IllegalArgumentException if <code>array</code> is <code>null</code>
   * @throws IllegalArgumentException if <code>array</code> is empty.
   * @throws IllegalArgumentException if <code>array</code> contains a <code>null</code>
   */
  public static Boolean xor(Boolean[] array) {
      if (array == null) {
          throw new IllegalArgumentException("The Array must not be null");
      } else if (array.length == 0) {
          throw new IllegalArgumentException("Array is empty");
      }
      boolean[] primitive = null;
      try {
          primitive = toPrimitive(array);
      } catch (NullPointerException ex) {
          throw new IllegalArgumentException("The array must not contain any null elements");
      }
      return xor(primitive) ? Boolean.TRUE : Boolean.FALSE;
  }
  /**
   * Converts an array of object Booleans to primitives.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  a <code>Boolean</code> array, may be <code>null</code>
   * @return a <code>boolean</code> array, <code>null</code> if null array input
   * @throws NullPointerException if array content is <code>null</code>
   */
  public static boolean[] toPrimitive(Boolean[] array) {
      if (array == null) {
          return null;
      } else if (array.length == 0) {
          return new boolean[0];
      }
      final boolean[] result = new boolean[array.length];
      for (int i = 0; i < array.length; i++) {
          result[i] = array[i].booleanValue();
      }
      return result;
  }
}
```
