---
title: Concatenates two arrays of strings
nav: Concatenates two arrays of...
description: * wingS is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 2402
source: https://web.archive.org/web/20140829075748/http://www.java2s.com/Tutorial/Java/0140__Collections/Concatenatestwoarraysofstrings.htm
---
```java title=Example.java
/*
 * Copyright 2000,2005 wingS development team.
 *
 * This file is part of wingS (http://wingsframework.org).
 *
 * wingS is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License
 * as published by the Free Software Foundation; either version 2.1
 * of the License, or (at your option) any later version.
 *
 * Please see COPYING for the complete licence.
 */
import java.util.StringTokenizer;
/**
 * Some string manipulation utilities.
 *
 * @author <a href="mailto:haaf@mercatis.de">Armin Haaf</a>
 */
public class StringUtil {
  /**
   *
   * @param s1 the first array of strings.
   * @param s2 the second array of strings.
   * @return the resulting array with all strings in s1 and s2
   */
  public static final String[] concat(String[] s1, String[] s2) {
      String[] erg = new String[s1.length + s2.length];
      System.arraycopy(s1, 0, erg, 0, s1.length);
      System.arraycopy(s2, 0, erg, s1.length, s2.length);
      return erg;
  }
}
```

| 9.10.1. | A variable length Double Array: expanding and contracting its internal storage array as elements are added and removed. |
|---|---|
| 9.10.2. | Simple object pool. Based on ThreadPool and few other classes |
| 9.10.3. | Your own auto-growth Array |
| 9.10.4. | The character array based string |
| 9.10.5. | ByteArray wraps java byte arrays (byte[]) to allow byte arrays to be used as keys in hashtables. |
| 9.10.6. | Adds all the elements of the given arrays into a new double-type array. |
| 9.10.7. | A writer for char strings |
| 9.10.8. | Array-List for integer objects. |
| 9.10.9. | Simple object pool |
| 9.10.10. | Concatenates two arrays of strings |
| 9.10.11. | Puts the entire source array in the target array at offset offset. |
| 9.10.12. | Lazy List creation |
| 9.10.13. | Stores a list of int |
