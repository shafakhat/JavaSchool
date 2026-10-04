---
title: Null Safe To String
nav: Null Safe To String
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20091030211159/http://www.java2s.com:80/Code/Java/Class/NullSafeToString.htm
---
Null Safe To String

```java title=Example.java
import java.lang.reflect.Array;
import java.util.Arrays;
/*
 * Copyright 2002-2007 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//Revised from springframework
/**
 * Miscellaneous object utility methods. Mainly for internal use within the
 * framework; consider Jakarta's Commons Lang for a more comprehensive suite
 * of object utilities.
 *
 * @author Juergen Hoeller
 * @author Keith Donald
 * @author Rod Johnson
 * @author Rob Harrop
 * @author Alex Ruiz
 * @since 19.03.2004
 * @see org.apache.commons.lang.ObjectUtils
 */
abstract class ObjectUtils {
  private static final int INITIAL_HASH = 7;
  private static final int MULTIPLIER = 31;
  private static final String EMPTY_STRING = "";
  private static final String NULL_STRING = "null";
  private static final String ARRAY_START = "{";
  private static final String ARRAY_END = "}";
  private static final String EMPTY_ARRAY = ARRAY_START + ARRAY_END;
  private static final String ARRAY_ELEMENT_SEPARATOR = ", ";
  /**
   * Return a content-based String representation if <code>obj</code> is
   * not <code>null</code>; otherwise returns an empty String.
   * <p>Differs from {@link #nullSafeToString(Object)} in that it returns
   * an empty String rather than "null" for a <code>null</code> value.
   * @param obj the object to build a display String for
   * @return a display String representation of <code>obj</code>
   * @see #nullSafeToString(Object)
   */
  public static String getDisplayString(Object obj) {
    if (obj == null) {
      return EMPTY_STRING;
    }
    return nullSafeToString(obj);
  }
  /**
   * Determine the class name for the given object.
   * <p>Returns <code>"null"</code> if <code>obj</code> is <code>null</code>.
   * @param obj the object to introspect (may be <code>null</code>)
   * @return the corresponding class name
   */
  public static String nullSafeClassName(Object obj) {
    return (obj != null ? obj.getClass().getName() : NULL_STRING);
  }
  /**
   * Return a String representation of the specified Object.
   * <p>Builds a String representation of the contents in case of an array.
   * Returns <code>"null"</code> if <code>obj</code> is <code>null</code>.
   * @param obj the object to build a String representation for
   * @return a String representation of <code>obj</code>
   */
  public static String nullSafeToString(Object obj) {
    if (obj == null) {
      return NULL_STRING;
    }
    if (obj instanceof String) {
      return (String) obj;
    }
    if (obj instanceof Object[]) {
      return nullSafeToString((Object[]) obj);
    }
    if (obj instanceof boolean[]) {
      return nullSafeToString((boolean[]) obj);
    }
    if (obj instanceof byte[]) {
      return nullSafeToString((byte[]) obj);
    }
    if (obj instanceof char[]) {
      return nullSafeToString((char[]) obj);
    }
    if (obj instanceof double[]) {
      return nullSafeToString((double[]) obj);
    }
    if (obj instanceof float[]) {
      return nullSafeToString((float[]) obj);
    }
    if (obj instanceof int[]) {
      return nullSafeToString((int[]) obj);
    }
    if (obj instanceof long[]) {
      return nullSafeToString((long[]) obj);
    }
    if (obj instanceof short[]) {
      return nullSafeToString((short[]) obj);
    }
    String str = obj.toString();
    return (str != null ? str : EMPTY_STRING);
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(Object[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(String.valueOf(array[i]));
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(boolean[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(byte[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(char[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append("'").append(array[i]).append("'");
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(double[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(float[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(int[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(long[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
  /**
   * Return a String representation of the contents of the specified array.
   * <p>The String representation consists of a list of the array's elements,
   * enclosed in curly braces (<code>"{}"</code>). Adjacent elements are separated
   * by the characters <code>", "</code> (a comma followed by a space). Returns
   * <code>"null"</code> if <code>array</code> is <code>null</code>.
   * @param array the array to build a String representation for
   * @return a String representation of <code>array</code>
   */
  public static String nullSafeToString(short[] array) {
    if (array == null) {
      return NULL_STRING;
    }
    int length = array.length;
    if (length == 0) {
      return EMPTY_ARRAY;
    }
    StringBuffer buffer = new StringBuffer();
    for (int i = 0; i < length; i++) {
      if (i == 0) {
        buffer.append(ARRAY_START);
      }
      else {
        buffer.append(ARRAY_ELEMENT_SEPARATOR);
      }
      buffer.append(array[i]);
    }
    buffer.append(ARRAY_END);
    return buffer.toString();
  }
}
```

1.  ShowToString -- demo program to show default toString methods
---  ---
2.  ToString -- demo program to show a toString method
3.  Demonstrate toString() without an override
4.  To String Demo
5.  Reflection based toString() utilities
6.  Use a generic toString()
7.  Constructs pretty string representation of object value
8.  toString(Object[] array)
9.  Array To String
10.  Gets the toString of an Object returning an empty string ("") if null input.
11.  Gets the toString that would be produced by Object if a class did not override toString itself.
