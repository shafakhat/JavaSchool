---
title: Converts a String to a Boolean.
nav: Converts a String to a Boo...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertsaStringtoaBoolean.htm
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
   */publicstatic Boolean toBooleanObject(String str) {
      if ("true".equalsIgnoreCase(str)) {
          return Boolean.TRUE;
      } elseif ("false".equalsIgnoreCase(str)) {
          return Boolean.FALSE;
      } elseif ("on".equalsIgnoreCase(str)) {
          return Boolean.TRUE;
      } elseif ("off".equalsIgnoreCase(str)) {
          return Boolean.FALSE;
      } elseif ("yes".equalsIgnoreCase(str)) {
          return Boolean.TRUE;
      } elseif ("no".equalsIgnoreCase(str)) {
          return Boolean.FALSE;
      }
      // no match
return null;
  }
}
```
