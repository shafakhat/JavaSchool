---
title: implements CharSequence
nav: implements CharSequence
description: /*******************************************************************************
section: Imported - java2s Archive
order: 1079
source: https://web.archive.org/web/20140829081450/http://www.java2s.com/Tutorial/Java/0040__Data-Type/implementsCharSequence.htm
---
```java title=Example.java
/*******************************************************************************
 * Copyright (c) 2008 xored software, Inc.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     xored software, Inc. - initial API and Implementation (Alex Panchenko)
 *******************************************************************************/
/**
 * {@link CharSequence} implementation backing by the char[]
 */
public class CharArraySequence implements CharSequence {
  private final char[] buff;
  private final int offset;
  private final int count;
  /**
   * @param buff
   */
  public CharArraySequence(char[] buff) {
    this(buff, 0, buff.length);
  }
  /**
   * @param buff
   * @param count
   */
  public CharArraySequence(char[] buff, int count) {
    this(buff, 0, count);
  }
  /**
   * @param buff
   * @param offset
   * @param count
   */
  public CharArraySequence(char[] buff, int offset, int count) {
    this.buff = buff;
    this.offset = offset;
    this.count = count;
  }
  /*
   * @see java.lang.CharSequence#charAt(int)
   */
  public char charAt(int index) {
    if (index < 0 || index >= count) {
      throw new StringIndexOutOfBoundsException(index);
    }
    return buff[offset + index];
  }
  /*
   * @see java.lang.CharSequence#length()
   */
  public int length() {
    return count;
  }
  /*
   * @see java.lang.CharSequence#subSequence(int, int)
   */
  public CharSequence subSequence(int beginIndex, int endIndex) {
    if (beginIndex < 0) {
      throw new StringIndexOutOfBoundsException(beginIndex);
    }
    if (endIndex > count) {
      throw new StringIndexOutOfBoundsException(endIndex);
    }
    if (beginIndex > endIndex) {
      throw new StringIndexOutOfBoundsException(endIndex - beginIndex);
    }
    return ((beginIndex == 0) && (endIndex == count)) ? this
        : new CharArraySequence(buff, offset + beginIndex, endIndex
            - beginIndex);
  }
  public String toString() {
    return new String(this.buff, this.offset, this.count);
  }
}
```

| 2.28.1. | Demonstrates the charAt and getChars |
|---|---|
| 2.28.2. | Converting Char array to String |
| 2.28.3. | Creating Character Arrays From String Objects |
| 2.28.4. | Copy characters from string into char Array |
| 2.28.5. | Creating String Objects From Character Arrays |
| 2.28.6. | new String(textArray, 9, 3): Creating String Objects From certain part of a character Array |
| 2.28.7. | Creating String Objects From Character Arrays using String.copyValueOf() |
| 2.28.8. | Creating a string from a subset of the array elements |
| 2.28.9. | Extracting a substring as an array of characters using the method getChars() |
| 2.28.10. | Using the Collection-Based for Loop with a String: Counting all vowels in a string |
| 2.28.11. | Construct one String from another. |
| 2.28.12. | demonstrates getChars( ): |
| 2.28.13. | implements CharSequence |
| 2.28.14. | Removes spaces (char <= 32) from end of this String with escape, handling null by returning null |
| 2.28.15. | Removes spaces (char <= 32) from end of this String, handling null by returning null |
| 2.28.16. | Swaps the case of a String changing upper and title case to lower case, and lower case to upper case. |
| 2.28.17. | Deletes all whitespaces from a String as defined by Character.isWhitespace(char). |
| 2.28.18. | Checks whether the String contains only digit characters. |
| 2.28.19. | Checks that the String does not contain certain characters. |
