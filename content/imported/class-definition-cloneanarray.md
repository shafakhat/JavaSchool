---
title: Clone an array
nav: Clone an array
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100529051913/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Cloneanarray.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *
 */
/**
 * @author Stephen Colebourne
 * @author Moritz Petersen
 * @author <a href="mailto:fredrik@westermarck.com">Fredrik Westermarck</a>
 * @author Nikolay Metchev
 * @author Matthew Hawthorne
 * @author Tim O'Brien
 * @author Pete Gieser
 * @author Gary Gregory
 * @author <a href="mailto:equinus100@hotmail.com">Ashwin S</a>
 * @author Maarten Coene
 * @since 2.0
 * @version $Id: ArrayUtils.java 632503 2008-03-01 00:21:52Z ggregory $
 */
public class Main {
  // Clone
  //-----------------------------------------------------------------------
  /**
   * Shallow clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * The objects in the array are not cloned, thus there is no special
   * handling for multi-dimensional arrays.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to shallow clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static Object[] clone(Object[] array) {
      if (array == null) {
          return null;
      }
      return (Object[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static long[] clone(long[] array) {
      if (array == null) {
          return null;
      }
      return (long[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static int[] clone(int[] array) {
      if (array == null) {
          return null;
      }
      return (int[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static short[] clone(short[] array) {
      if (array == null) {
          return null;
      }
      return (short[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static char[] clone(char[] array) {
      if (array == null) {
          return null;
      }
      return (char[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static byte[] clone(byte[] array) {
      if (array == null) {
          return null;
      }
      return (byte[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static double[] clone(double[] array) {
      if (array == null) {
          return null;
      }
      return (double[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static float[] clone(float[] array) {
      if (array == null) {
          return null;
      }
      return (float[]) array.clone();
  }
  /**
   * Clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static boolean[] clone(boolean[] array) {
      if (array == null) {
          return null;
      }
      return (boolean[]) array.clone();
  }
}
```
