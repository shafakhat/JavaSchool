---
title: Returns the hexadecimal value of the supplied byte array
nav: Returns the hexadecimal va...
description: * Copyright Aduna (http://www.aduna-software.com/) (c) 1997-2006.
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20100706223519/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Returnsthehexadecimalvalueofthesuppliedbytearray.htm
---
```java title=Example.java
/*
 * Copyright Aduna (http://www.aduna-software.com/) (c) 1997-2006.
 *
 * Licensed under the Aduna BSD-style license.
 */
public class Utils {
  /**
   * Returns the hexadecimal value of the supplied byte array. The resulting
   * string always uses two hexadecimals per byte. As a result, the length
   * of the resulting string is guaranteed to be twice the length of the
   * supplied byte array.
   */
  public static String toHexString(byte[] array) {
    StringBuilder sb = new StringBuilder(2*array.length);
    for (int i = 0; i < array.length; i++) {
      String hex = Integer.toHexString(array[i] & 0xff);
      if (hex.length() == 1) {
        sb.append('0');
      }
      sb.append(hex);
    }
    return sb.toString();
  }
}
```
