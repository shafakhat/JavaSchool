---
title: Checks whether the String contains only digit characters.
nav: Checks whether the String ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckswhethertheStringcontainsonlydigitcharacters.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;

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
 * Provides extra functionality for Java Number classes.
 *
 * @author <a href="mailto:rand_mcneely@yahoo.com">Rand McNeely</a>
 * @author Stephen Colebourne
 * @author <a href="mailto:steve.downey@netfolio.com">Steve Downey</a>
 * @author Eric Pugh
 * @author Phil Steitz
 * @since 1.0
 * @version $Id: NumberUtils.java 488819 2006-12-19 21:50:04Z bayard $
 *
 */publicclass Main {

  //--------------------------------------------------------------------
/**
   * Checks whether the <code>String</code> contains only
   * digit characters.
   *
   * <code>Null</code> and empty String will return
   * <code>false</code>.
   *
   * @param str  the <code>String</code> to check
   * @return <code>true</code> if str contains only unicode numeric
   */publicstaticboolean isDigits(String str) {
      if ((str == null) || (str.length() == 0)) {
          return false;
      }
      for (int i = 0; i < str.length(); i++) {
          if (!Character.isDigit(str.charAt(i))) {
              return false;
          }
      }
      return true;
  }
}
```
