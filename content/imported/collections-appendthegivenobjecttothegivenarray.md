---
title: Append the given Object to the given array
nav: Append the given Object to...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20100222021259/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AppendthegivenObjecttothegivenarray.htm
---
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
   * Return whether the given array is empty: that is, <code>null</code>
   * or of zero length.
   * @param array the array to check
   * @return whether the given array is empty
   */
  public static boolean isEmpty(Object[] array) {
    return (array == null || array.length == 0);
  }
  /**
   * Append the given Object to the given array, returning a new array
   * consisting of the input array contents plus the given Object.
   * @param array the array to append to (can be <code>null</code>)
   * @param obj the Object to append
   * @return the new array (of the same component type; never <code>null</code>)
   */
  public static Object[] addObjectToArray(Object[] array, Object obj) {
    Class compType = Object.class;
    if (array != null) {
      compType = array.getClass().getComponentType();
    }
    else if (obj != null) {
      compType = obj.getClass();
    }
    int newArrLength = (array != null ? array.length + 1 : 1);
    Object[] newArr = (Object[]) Array.newInstance(compType, newArrLength);
    if (array != null) {
      System.arraycopy(array, 0, newArr, 0, array.length);
    }
    newArr[newArr.length - 1] = obj;
    return newArr;
  }
  /**
   * Convert the given array (which may be a primitive array) to an
   * object array (if necessary of primitive wrapper objects).
   * A <code>null</code> source value will be converted to an
   * empty Object array.
   * @param source the (potentially primitive) array
   * @return the corresponding object array (never <code>null</code>)
   * @throws IllegalArgumentException if the parameter is not an array
   */
  public static Object[] toObjectArray(Object source) {
    if (source instanceof Object[]) {
      return (Object[]) source;
    }
    if (source == null) {
      return new Object[0];
    }
    if (!source.getClass().isArray()) {
      throw new IllegalArgumentException("Source is not an array: " + source);
    }
    int length = Array.getLength(source);
    if (length == 0) {
      return new Object[0];
    }
    Class wrapperType = Array.get(source, 0).getClass();
    Object[] newArray = (Object[]) Array.newInstance(wrapperType, length);
    for (int i = 0; i < length; i++) {
      newArray[i] = Array.get(source, i);
    }
    return newArray;
  }
}
```
