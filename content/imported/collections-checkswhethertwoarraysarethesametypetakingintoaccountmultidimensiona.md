---
title: Checks whether two arrays are the same type taking into account multi-dimensional arrays.
nav: Checks whether two arrays ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2329
source: https://web.archive.org/web/20140829075923/http://www.java2s.com/Tutorial/Java/0140__Collections/Checkswhethertwoarraysarethesametypetakingintoaccountmultidimensionalarrays.htm
---
```java title=Example.java
import java.lang.reflect.Array;
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
/**
 * @author Stephen Colebourne
 * @author Moritz Petersen
 * @author <a href="mailto:fredrik@westermarck.com">Fredrik Westermarck</a>
 * @author Nikolay Metchev
 * @author Matthew Hawthorne
 * @author Tim O'Brien
 * @author Pete Gieser
 * @author Gary Gregory
 * @author <a href="mailto:equinus100@hotmail.com">Ashwin S</a>
 * @author Maarten Coene
 * @since 2.0
 * @version $Id: ArrayUtils.java 632503 2008-03-01 00:21:52Z ggregory $
 */
public class Main {
  /**
   * Checks whether two arrays are the same type taking into account
   * multi-dimensional arrays.
   *
   * @param array1 the first array, must not be <code>null</code>
   * @param array2 the second array, must not be <code>null</code>
   * @return <code>true</code> if type of arrays matches
   * @throws IllegalArgumentException if either array is <code>null</code>
   */
  public static boolean isSameType(Object array1, Object array2) {
      if (array1 == null || array2 == null) {
          throw new IllegalArgumentException("The Array must not be null");
      }
      return array1.getClass().getName().equals(array2.getClass().getName());
  }
}
```

| 9.6.1. | Arrays of Objects |
|---|---|
| 9.6.2. | Arrays of Strings: using 'new' operator |
| 9.6.3. | Arrays of Strings: initial values determine the size of the array |
| 9.6.4. | Demonstrate String arrays. |
| 9.6.5. | Checks whether two arrays are the same length, treating null arrays as length 0. |
| 9.6.6. | Checks whether two arrays are the same type taking into account multi-dimensional arrays. |
| 9.6.7. | Turn an array of ints into a printable string. |
| 9.6.8. | Check if the given object is an array (primitve or native). |
| 9.6.9. | Reverses the order of the given long type value array. |
| 9.6.10. | Removes the first occurrence of the specified element from the specified array. |
| 9.6.11. | Removes the element at the specified position from the specified array. |
