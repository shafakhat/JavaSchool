---
title: Converts a boolean to a String returning 'yes' or 'no'
nav: Converts a boolean to a St...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertsabooleantoaStringreturningyesorno.htm
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
 *//**
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
 */publicclass Main {
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
   */publicstatic String toStringYesNo(boolean bool) {
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
   */publicstatic String toString(boolean bool, String trueString, String falseString) {
      return bool ? trueString : falseString;
  }
}
```
