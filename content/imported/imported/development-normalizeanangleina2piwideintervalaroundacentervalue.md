---
title: Normalize an angle in a 2&pi wide interval around a center value.
nav: Normalize an angle in a 2&...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported
order: 20070
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Normalizeanangleina2piwideintervalaroundacentervalue.htm
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
 */
public class Main {
  /** 2 &pi;. */
  private static final double TWO_PI = 2 * Math.PI;
  /**
   * Normalize an angle in a 2&pi wide interval around a center value.
   * This method has three main uses:
   * <ul>
   *   <li>normalize an angle between 0 and 2&pi;:<br/>
   *       <code>a = MathUtils.normalizeAngle(a, Math.PI);</code></li>
   *   <li>normalize an angle between -&pi; and +&pi;<br/>
   *       <code>a = MathUtils.normalizeAngle(a, 0.0);</code></li>
   *   <li>compute the angle between two defining angular positions:<br>
   *       <code>angle = MathUtils.normalizeAngle(end, start) - start;</code></li>
   * </ul>
   * Note that due to numerical accuracy and since &pi; cannot be represented
   * exactly, the result interval is <em>closed</em>, it cannot be half-closed
   * as would be more satisfactory in a purely mathematical view.
   * @param a angle to normalize
   * @param center center of the desired 2&pi; interval for the result
   * @return a-2k&pi; with integer k and center-&pi; &lt;= a-2k&pi; &lt;= center+&pi;
   * @since 1.2
   */
   public static double normalizeAngle(double a, double center) {
       return a - TWO_PI * Math.floor((a + Math.PI - center) / TWO_PI);
   }
}
```
