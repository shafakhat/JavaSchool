---
title: For a float value x, this method returns +1.0F if x >= 0 and -1.0F if x < 0. Returns NaN if x is NaN.
nav: For a float value x, this ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Forafloatvaluexthismethodreturns10Fifx0and10Fifx0ReturnsNaNifxisNaN.htm
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
   * For a float value x, this method returns +1.0F if x >= 0 and -1.0F if x <
   * 0. Returns <code>NaN</code> if <code>x</code> is <code>NaN</code>.
   *
   * @param x the value, a float
   * @return +1.0F or -1.0F, depending on the sign of x
   */publicstaticfloat indicator(finalfloat x) {
      if (Float.isNaN(x)) {
          return Float.NaN;
      }
      return (x >= 0.0F) ? 1.0F : -1.0F;
  }
}
```
