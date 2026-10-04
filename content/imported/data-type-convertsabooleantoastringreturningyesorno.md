---
title: Converts a boolean to a String returning 'yes' or 'no'
nav: Converts a boolean to a St...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1454
source: https://web.archive.org/web/20140829090628/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertsabooleantoaStringreturningyesorno.htm
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
   * Converts a boolean to a String returning <code>'yes'</code>
   * or <code>'no'</code>.
   *
   * <pre>
   *   BooleanUtils.toStringYesNo(true)   = "yes"
   *   BooleanUtils.toStringYesNo(false)  = "no"
   * </pre>
   *
   * @param bool  the Boolean to check
   * @return <code>'yes'</code>, <code>'no'</code>,
   *  or <code>null</code>
   */
  public static String toStringYesNo(boolean bool) {
      return toString(bool, "yes", "no");
  }
  /**
   * Converts a boolean to a String returning one of the input Strings.
   *
   * <pre>
   *   BooleanUtils.toString(true, "true", "false")   = "true"
   *   BooleanUtils.toString(false, "true", "false")  = "false"
   * </pre>
   *
   * @param bool  the Boolean to check
   * @param trueString  the String to return if <code>true</code>,
   *  may be <code>null</code>
   * @param falseString  the String to return if <code>false</code>,
   *  may be <code>null</code>
   * @return one of the two input Strings
   */
  public static String toString(boolean bool, String trueString, String falseString) {
      return bool ? trueString : falseString;
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
