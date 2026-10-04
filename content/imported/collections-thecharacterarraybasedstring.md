---
title: The character array based string
nav: The character array based ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2390
source: https://web.archive.org/web/20140829080008/http://www.java2s.com/Tutorial/Java/0140__Collections/Thecharacterarraybasedstring.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 *
 * @author Eric Ye, IBM
 * @author Andy Clark, IBM
 *
 * @version $Id: XMLString.java 447247 2006-09-18 05:23:52Z mrglavas $
 */
public class XMLString {
  /** The character array. */
  public char[] ch;
  /** The offset into the character array. */
  public int offset;
  /** The length of characters from the offset. */
  public int length;
  //
  // Constructors
  //
  /** Default constructor. */
  public XMLString() {
  } // <init>()
  /**
   * Constructs an XMLString structure preset with the specified values.
   *
   * @param ch
   *          The character array.
   * @param offset
   *          The offset into the character array.
   * @param length
   *          The length of characters from the offset.
   */
  public XMLString(char[] ch, int offset, int length) {
    setValues(ch, offset, length);
  } // <init>(char[],int,int)
  /**
   * Constructs an XMLString structure with copies of the values in the given
   * structure.
   *
   * <strong>Note:</strong> This does not copy the character array; only the
   * reference to the array is copied.
   *
   * @param string
   *          The XMLString to copy.
   */
  public XMLString(XMLString string) {
    setValues(string);
  } // <init>(XMLString)
  //
  // Public methods
  //
  /**
   * Initializes the contents of the XMLString structure with the specified
   * values.
   *
   * @param ch
   *          The character array.
   * @param offset
   *          The offset into the character array.
   * @param length
   *          The length of characters from the offset.
   */
  public void setValues(char[] ch, int offset, int length) {
    this.ch = ch;
    this.offset = offset;
    this.length = length;
  } // setValues(char[],int,int)
  /**
   * Initializes the contents of the XMLString structure with copies of the
   * given string structure.
   *
   * <strong>Note:</strong> This does not copy the character array; only the
   * reference to the array is copied.
   *
   * @param s
   */
  public void setValues(XMLString s) {
    setValues(s.ch, s.offset, s.length);
  } // setValues(XMLString)
  /** Resets all of the values to their defaults. */
  public void clear() {
    this.ch = null;
    this.offset = 0;
    this.length = -1;
  } // clear()
  /**
   * Returns true if the contents of this XMLString structure and the specified
   * array are equal.
   *
   * @param ch
   *          The character array.
   * @param offset
   *          The offset into the character array.
   * @param length
   *          The length of characters from the offset.
   */
  public boolean equals(char[] ch, int offset, int length) {
    if (ch == null) {
      return false;
    }
    if (this.length != length) {
      return false;
    }
    for (int i = 0; i < length; i++) {
      if (this.ch[this.offset + i] != ch[offset + i]) {
        return false;
      }
    }
    return true;
  } // equals(char[],int,int):boolean
  /**
   * Returns true if the contents of this XMLString structure and the specified
   * string are equal.
   *
   * @param s
   *          The string to compare.
   */
  public boolean equals(String s) {
    if (s == null) {
      return false;
    }
    if (length != s.length()) {
      return false;
    }
    // is this faster than call s.toCharArray first and compare the
    // two arrays directly, which will possibly involve creating a
    // new char array object.
    for (int i = 0; i < length; i++) {
      if (ch[offset + i] != s.charAt(i)) {
        return false;
      }
    }
    return true;
  } // equals(String):boolean
  //
  // Object methods
  //
  /** Returns a string representation of this object. */
  public String toString() {
    return length > 0 ? new String(ch, offset, length) : "";
  } // toString():String
} // class XMLString
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
