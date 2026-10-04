---
title: Gets the maximum of three long values.
nav: Gets the maximum of three ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1173
source: https://web.archive.org/web/20140829083037/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getsthemaximumofthreelongvalues.htm
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
 */
/**
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
 */
public class Main {
  /**
   * Gets the maximum of three <code>long</code> values.
   *
   * @param a  value 1
   * @param b  value 2
   * @param c  value 3
   * @return  the largest of the values
   */
  public static long maximum(long a, long b, long c) {
      if (b > a) {
          a = b;
      }
      if (c > a) {
          a = c;
      }
      return a;
  }
}
```

| 2.8.1. | Long Integer Literal |
|---|---|
| 2.8.2. | Create a Long object |
| 2.8.3. | Add two long integers, checking for overflow. |
| 2.8.4. | Multiply two long integers, checking for overflow. |
| 2.8.5. | Subtract two long integers, checking for overflow. |
| 2.8.6. | Convert Long to numeric primitive data types example |
| 2.8.7. | Convert long primitive to Long object Example |
| 2.8.8. | Compute distance light travels using long variables |
| 2.8.9. | Java long Example: long is 64 bit signed type |
| 2.8.10. | Min and Max values of datatype long |
| 2.8.11. | Gets the maximum of three long values. |
| 2.8.12. | Gets the minimum of three long values. |
| 2.8.13. | Convert Java String to Long example |
| 2.8.14. | Use toString method of Long class to convert Long into String. |
| 2.8.15. | Convert from long to String |
| 2.8.16. | Convert from String to long |
| 2.8.17. | A utility class for converting a long into a human readable string. |
| 2.8.18. | Java Sort long Array Example |
| 2.8.19. | Compare Two Java long Arrays Example |
| 2.8.20. | Format long with System.out.format |
