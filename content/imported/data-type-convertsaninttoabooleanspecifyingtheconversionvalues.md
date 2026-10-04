---
title: Converts an int to a boolean specifying the conversion values.
nav: Converts an int to a boole...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/20100222015848/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Convertsaninttoabooleanspecifyingtheconversionvalues.htm
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
   *
   * <pre>
   *   BooleanUtils.toBoolean(0, 1, 0) = false
   *   BooleanUtils.toBoolean(1, 1, 0) = true
   *   BooleanUtils.toBoolean(2, 1, 2) = false
   *   BooleanUtils.toBoolean(2, 2, 0) = true
   * </pre>
   *
   * @param value  the Integer to convert
   * @param trueValue  the value to match for <code>true</code>
   * @param falseValue  the value to match for <code>false</code>
   * @return <code>true</code> or <code>false</code>
   * @throws IllegalArgumentException if no match
   */
  public static boolean toBoolean(int value, int trueValue, int falseValue) {
      if (value == trueValue) {
          return true;
      } else if (value == falseValue) {
          return false;
      }
      // no match
      throw new IllegalArgumentException("The Integer did not match either specified value");
  }
}
```
