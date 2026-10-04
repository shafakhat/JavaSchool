---
title: Converts a String to a Boolean.
nav: Converts a String to a Boo...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1459
source: https://web.archive.org/web/20140829090441/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertsaStringtoaBoolean.htm
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
   * <code>'true'</code>, <code>'on'</code> or <code>'yes'</code>
   * (case insensitive) will return <code>true</code>.
   * <code>'false'</code>, <code>'off'</code> or <code>'no'</code>
   * (case insensitive) will return <code>false</code>.
   * Otherwise, <code>null</code> is returned.</p>
   *
   * <pre>
   *   BooleanUtils.toBooleanObject(null)    = null
   *   BooleanUtils.toBooleanObject("true")  = Boolean.TRUE
   *   BooleanUtils.toBooleanObject("false") = Boolean.FALSE
   *   BooleanUtils.toBooleanObject("on")    = Boolean.TRUE
   *   BooleanUtils.toBooleanObject("ON")    = Boolean.TRUE
   *   BooleanUtils.toBooleanObject("off")   = Boolean.FALSE
   *   BooleanUtils.toBooleanObject("oFf")   = Boolean.FALSE
   *   BooleanUtils.toBooleanObject("blue")  = null
   * </pre>
   *
   * @param str  the String to check
   * @return the Boolean value of the string,
   *  <code>null</code> if no match or <code>null</code> input
   */
  public static Boolean toBooleanObject(String str) {
      if ("true".equalsIgnoreCase(str)) {
          return Boolean.TRUE;
      } else if ("false".equalsIgnoreCase(str)) {
          return Boolean.FALSE;
      } else if ("on".equalsIgnoreCase(str)) {
          return Boolean.TRUE;
      } else if ("off".equalsIgnoreCase(str)) {
          return Boolean.FALSE;
      } else if ("yes".equalsIgnoreCase(str)) {
          return Boolean.TRUE;
      } else if ("no".equalsIgnoreCase(str)) {
          return Boolean.FALSE;
      }
      // no match
      return null;
  }
}
```

| 2.2.1. | java.lang.Boolean |
|---|---|
| 2.2.2. | Java boolean value |
| 2.2.3. | Boolean Data Type |
| 2.2.4. | Boolean Literals |
| 2.2.5. | Boolean Variables |
| 2.2.6. | Using the boolean type |
| 2.2.7. | valueOf(): parse a String to a Boolean object |
| 2.2.8. | toString(): return the string representation of a boolean |
| 2.2.9. | Convert String to Boolean |
| 2.2.10. | Convert Boolean to String |
| 2.2.11. | Convert Java boolean Primitive to Boolean object |
| 2.2.12. | Convert Java String Object to Boolean Object |
| 2.2.13. | Create an Boolean object from boolean value |
| 2.2.14. | Compare Two Java boolean Arrays Example |
| 2.2.15. | Convert integer to boolean |
| 2.2.16. | Convert boolean to integer |
| 2.2.17. | Convert boolean value to Boolean |
| 2.2.18. | Create a boolean variable from string |
| 2.2.19. | Autoboxing/unboxing a Boolean and Character. |
| 2.2.20. | Converts a String to a Boolean. |
| 2.2.21. | Converts a boolean to a String returning 'yes' or 'no' |
| 2.2.22. | Converts an Integer to a boolean specifying the conversion values. |
| 2.2.23. | Converts an int to a boolean specifying the conversion values. |
| 2.2.24. | Performs an xor on a set of booleans. |
