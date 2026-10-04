---
title: Joins the elements of the provided Iterator into a single String containing the provided elements.
nav: Joins the elements of the ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1146
source: https://web.archive.org/web/20100604104935/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JoinstheelementsoftheprovidedIteratorintoasingleStringcontainingtheprovidedelements.htm
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
import java.util.Iterator;
import java.util.List;
public class Main {
  /**
   * Joins the elements of the provided <code>Iterator</code> into
   * a single String containing the provided elements.
   *
   * No delimiter is added before or after the list.
   * A <code>null</code> separator is the same as an empty String ("").
   *
   * See the examples here: {@link #join(Object[],String)}.
   *
   * @param iterator  the <code>Iterator</code> of values to join together, may be null
   * @param separator  the separator character to use, null treated as ""
   * @return the joined String, <code>null</code> if null iterator input
   */
  public static String join(Iterator iterator, String separator) {
      // handle null, zero and one elements before building a buffer
      if (iterator == null) {
          return null;
      }
      if (!iterator.hasNext()) {
          return "";
      }
      Object first = iterator.next();
      if (!iterator.hasNext()) {
          return toString(first);
      }
      // two or more elements
      StringBuffer buf = new StringBuffer(256); // Java default is 16, probably too small
      if (first != null) {
          buf.append(first);
      }
      while (iterator.hasNext()) {
          if (separator != null) {
              buf.append(separator);
          }
          Object obj = iterator.next();
          if (obj != null) {
              buf.append(obj);
          }
      }
      return buf.toString();
  }
  // ToString
  //-----------------------------------------------------------------------
  /**
   * Gets the <code>toString</code> of an <code>Object</code> returning
   * an empty string ("") if <code>null</code> input.
   *
   * <pre>
   * ObjectUtils.toString(null)         = ""
   * ObjectUtils.toString("")           = ""
   * ObjectUtils.toString("bat")        = "bat"
   * ObjectUtils.toString(Boolean.TRUE) = "true"
   * </pre>
   *
   * @see StringUtils#defaultString(String)
   * @see String#valueOf(Object)
   * @param obj  the Object to <code>toString</code>, may be null
   * @return the passed in Object's toString, or nullStr if <code>null</code> input
   * @since 2.0
   */
  public static String toString(Object obj) {
      return obj == null ? "" : obj.toString();
  }
}
```
