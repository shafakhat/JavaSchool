---
title: Check whether given exception is compatible with the exceptions declared in a throws clause
nav: Check whether given except...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20100820110652/http://www.java2s.com:80/Tutorial/Java/0120__Development/Checkwhethergivenexceptioniscompatiblewiththeexceptionsdeclaredinathrowsclause.htm
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
   * Check whether the given exception is compatible with the exceptions
   * declared in a throws clause.
   * @param ex the exception to checked
   * @param declaredExceptions the exceptions declared in the throws clause
   * @return whether the given exception is compatible
   */
  public static boolean isCompatibleWithThrowsClause(Throwable ex, Class[] declaredExceptions) {
    if (!isCheckedException(ex)) {
      return true;
    }
    if (declaredExceptions != null) {
      for (int i = 0; i < declaredExceptions.length; i++) {
        if (declaredExceptions[i].isAssignableFrom(ex.getClass())) {
          return true;
        }
      }
    }
    return false;
  }
  /**
   * Return whether the given throwable is a checked exception:
   * that is, neither a RuntimeException nor an Error.
   * @param ex the throwable to check
   * @return whether the throwable is a checked exception
   * @see java.lang.Exception
   * @see java.lang.RuntimeException
   * @see java.lang.Error
   */
  public static boolean isCheckedException(Throwable ex) {
    return !(ex instanceof RuntimeException || ex instanceof Error);
  }
}
```
