---
title: Puts the entire source array in the target array at offset offset.
nav: Puts the entire source arr...
description: * Copyright Aduna (http://www.aduna-software.com/) (c) 1997-2006.
section: Imported - java2s Archive
order: 2395
source: https://web.archive.org/web/20140829080216/http://www.java2s.com/Tutorial/Java/0140__Collections/Putstheentiresourcearrayinthetargetarrayatoffsetoffset.htm
---
```java title=Example.java
/*
 * Copyright Aduna (http://www.aduna-software.com/) (c) 1997-2006.
 *
 * Licensed under the Aduna BSD-style license.
 */
public class Utils {
  /**
   * Puts the entire <tt>source</tt> array in the <tt>target</tt>
   * array at offset <tt>offset</tt>.
   */
  public static void put(byte[] source, byte[] target, int offset) {
    System.arraycopy(source, 0, target, offset, source.length);
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
