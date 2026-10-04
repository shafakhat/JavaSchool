---
title: Add two integers, checking for overflow.
nav: Add two integers, checking...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Addtwointegerscheckingforoverflow.htm
---
```java title=Example.java
import java.io.File;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *
 */publicclass Main {
  /**
   *
   * @param x an addend
   * @param y an addend
   * @return the sum <code>x+y</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         int
   * @since 1.1
   */publicstaticint addAndCheck(int x, int y) {
      long s = (long)x + (long)y;
      if (s < Integer.MIN_VALUE || s > Integer.MAX_VALUE) {
          thrownew ArithmeticException("overflow: add");
      }
      return (int)s;
  }
}
```
