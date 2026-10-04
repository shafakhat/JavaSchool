---
title: Joins array elements into a single String
nav: Joins array elements into ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20100604101450/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JoinsarrayelementsintoasingleStringspecifythestartindexandendindex.htm
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
   * A <code>null</code> separator is the same as an empty String ("").
   * Null objects or empty strings within the array are represented by
   * empty strings.
   *
   * <pre>
   * StringUtils.join(null, *)                = null
   * StringUtils.join([], *)                  = ""
   * StringUtils.join([null], *)              = ""
   * StringUtils.join(["a", "b", "c"], "--")  = "a--b--c"
   * StringUtils.join(["a", "b", "c"], null)  = "abc"
   * StringUtils.join(["a", "b", "c"], "")    = "abc"
   * StringUtils.join([null, "", "a"], ',')   = ",,a"
   * </pre>
   *
   * @param array  the array of values to join together, may be null
   * @param separator  the separator character to use, null treated as ""
   * @param startIndex the first index to start joining from.  It is
   * an error to pass in an end index past the end of the array
   * @param endIndex the index to stop joining from (exclusive). It is
   * an error to pass in an end index past the end of the array
   * @return the joined String, <code>null</code> if null array input
   */
  public static String join(Object[] array, String separator, int startIndex, int endIndex) {
      if (array == null) {
          return null;
      }
      if (separator == null) {
          separator = "";
      }
      // endIndex - startIndex > 0:   Len = NofStrings *(len(firstString) + len(separator))
      //           (Assuming that all Strings are roughly equally long)
      int bufSize = (endIndex - startIndex);
      if (bufSize <= 0) {
          return "";
      }
      bufSize *= ((array[startIndex] == null ? 16 : array[startIndex].toString().length())
                      + separator.length());
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
