---
title: Get hash code for primitive data types
nav: Get hash code for primitiv...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20100314201128/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Gethashcodeforprimitivedatatypes.htm
---
```java title=Example.java
import java.lang.reflect.Array;
import java.util.Arrays;
/*
 * Copyright 2002-2007 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//Revised from springframework
/**
 * Miscellaneous object utility methods. Mainly for internal use within the
 * framework; consider Jakarta's Commons Lang for a more comprehensive suite
 * of object utilities.
 *
 * @author Juergen Hoeller
 * @author Keith Donald
 * @author Rod Johnson
 * @author Rob Harrop
 * @author Alex Ruiz
 * @since 19.03.2004
 * @see org.apache.commons.lang.ObjectUtils
 */
abstract class ObjectUtils {
  private static final int INITIAL_HASH = 7;
  private static final int MULTIPLIER = 31;
  private static final String EMPTY_STRING = "";
  private static final String NULL_STRING = "null";
  private static final String ARRAY_START = "{";
  private static final String ARRAY_END = "}";
  private static final String EMPTY_ARRAY = ARRAY_START + ARRAY_END;
  private static final String ARRAY_ELEMENT_SEPARATOR = ", ";
  /**
   * Return the same value as <code>{@link Boolean#hashCode()}</code>.
   * @see Boolean#hashCode()
   */
  public static int hashCode(boolean bool) {
    return bool ? 1231 : 1237;
  }
  /**
   * Return the same value as <code>{@link Double#hashCode()}</code>.
   * @see Double#hashCode()
   */
  public static int hashCode(double dbl) {
    long bits = Double.doubleToLongBits(dbl);
    return hashCode(bits);
  }
  /**
   * Return the same value as <code>{@link Float#hashCode()}</code>.
   * @see Float#hashCode()
   */
  public static int hashCode(float flt) {
    return Float.floatToIntBits(flt);
  }
  /**
   * Return the same value as <code>{@link Long#hashCode()}</code>.
   * @see Long#hashCode()
   */
  public static int hashCode(long lng) {
    return (int) (lng ^ (lng >>> 32));
  }
}
```
