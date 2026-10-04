---
title: Checks whether the character is ASCII 7 bit numeric.
nav: Checks whether the charact...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckswhetherthecharacterisASCII7bitnumeric.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *//**
 * Operations on char primitives and Character objects.
 *
 * This class tries to handle <code>null</code> input gracefully.
 * An exception will not be thrown for a <code>null</code> input.
 * Each method documents its behaviour in more detail.
 *
 * @author Stephen Colebourne
 * @since 2.1
 * @version $Id: CharUtils.java 437554 2006-08-28 06:21:41Z bayard $
 */publicclass Main {
  /**
   *
   * <pre>
   *   CharUtils.isAsciiNumeric('a')  = false
   *   CharUtils.isAsciiNumeric('A')  = false
   *   CharUtils.isAsciiNumeric('3')  = true
   *   CharUtils.isAsciiNumeric('-')  = false
   *   CharUtils.isAsciiNumeric('\n') = false
   *   CharUtils.isAsciiNumeric('&copy;') = false
   * </pre>
   *
   * @param ch  the character to check
   * @return true if between 48 and 57 inclusive
   */publicstaticboolean isAsciiNumeric(char ch) {
      return ch >= '0' && ch <= '9';
  }
}
```
