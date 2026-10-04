---
title: Joins the elements of the provided array into a single String containing the provided list of elements.
nav: Joins the elements of the ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20100604105605/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JoinstheelementsoftheprovidedarrayintoasingleStringcontainingtheprovidedlistofelements.htm
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
import java.util.ArrayList;
import java.util.List;
public class Main {
  /**
   * Joins the elements of the provided array into a single String
   * containing the provided list of elements.
   *
   * No delimiter is added before or after the list.
   * Null objects or empty strings within the array are represented by
   * empty strings.
   *
   * <pre>
   * StringUtils.join(null, *)               = null
   * StringUtils.join([], *)                 = ""
   * StringUtils.join([null], *)             = ""
   * StringUtils.join(["a", "b", "c"], ';')  = "a;b;c"
   * StringUtils.join(["a", "b", "c"], null) = "abc"
   * StringUtils.join([null, "", "a"], ';')  = ";;a"
   * </pre>
   *
   * @param array  the array of values to join together, may be null
   * @param separator  the separator character to use
   * @return the joined String, <code>null</code> if null array input
   * @since 2.0
   */
  public static String join(Object[] array, char separator) {
      if (array == null) {
          return null;
      }
      return join(array, separator, 0, array.length);
  }
  /**
   * Joins the elements of the provided array into a single String
   * containing the provided list of elements.
   *
   * No delimiter is added before or after the list.
   * Null objects or empty strings within the array are represented by
   * empty strings.
   *
   * <pre>
   * StringUtils.join(null, *)               = null
   * StringUtils.join([], *)                 = ""
   * StringUtils.join([null], *)             = ""
   * StringUtils.join(["a", "b", "c"], ';')  = "a;b;c"
   * StringUtils.join(["a", "b", "c"], null) = "abc"
   * StringUtils.join([null, "", "a"], ';')  = ";;a"
   * </pre>
   *
   * @param array  the array of values to join together, may be null
   * @param separator  the separator character to use
   * @param startIndex the first index to start joining from.  It is
   * an error to pass in an end index past the end of the array
   * @param endIndex the index to stop joining from (exclusive). It is
   * an error to pass in an end index past the end of the array
   * @return the joined String, <code>null</code> if null array input
   * @since 2.0
   */
  public static String join(Object[] array, char separator, int startIndex, int endIndex) {
      if (array == null) {
          return null;
      }
      int bufSize = (endIndex - startIndex);
      if (bufSize <= 0) {
          return "";
      }
      bufSize *= ((array[startIndex] == null ? 16 : array[startIndex].toString().length()) + 1);
      StringBuffer buf = new StringBuffer(bufSize);
      for (int i = startIndex; i < endIndex; i++) {
          if (i > startIndex) {
              buf.append(separator);
          }
          if (array[i] != null) {
              buf.append(array[i]);
          }
      }
      return buf.toString();
  }
}
```
