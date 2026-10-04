---
title: A writer for char strings
nav: A writer for char strings
description: * Redistribution and use in source and binary forms, with or without
section: Imported - java2s Archive
order: 2391
source: https://web.archive.org/web/20140829080138/http://www.java2s.com/Tutorial/Java/0140__Collections/Awriterforcharstrings.htm
---
```java title=Example.java
/* Copyright (c) 2001-2009, The HSQL Development Group
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this
 * list of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * Neither the name of the HSQL Development Group nor the names of its
 * contributors may be used to endorse or promote products derived from this
 * software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL HSQL DEVELOPMENT GROUP, HSQLDB.ORG,
 * OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
/**
 *
 * @author Fred Toussi (fredt@users dot sourceforge.net)
 * @version 1.9.0
 * @since 1.9.0
 */
public class CharArrayWriter {
  protected char[] buffer;
  protected int count;
  public CharArrayWriter(char[] buffer) {
    this.buffer = buffer;
  }
  public void write(int c) {
    if (count == buffer.length) {
      ensureSize(count + 1);
    }
    buffer[count++] = (char) c;
  }
  void ensureSize(int size) {
    if (size <= buffer.length) {
      return;
    }
    int newSize = buffer.length;
    while (newSize < size) {
      newSize *= 2;
    }
    char[] newBuffer = new char[newSize];
    System.arraycopy(buffer, 0, newBuffer, 0, count);
    buffer = newBuffer;
  }
  public void write(String str, int off, int len) {
    ensureSize(count + len);
    str.getChars(off, off + len, buffer, count);
    count += len;
  }
  public void reset() {
    count = 0;
  }
  public void reset(char[] buffer) {
    count = 0;
    this.buffer = buffer;
  }
  public char[] toCharArray() {
    char[] newBuffer = new char[count];
    System.arraycopy(buffer, 0, newBuffer, 0, count);
    return (char[]) newBuffer;
  }
  public int size() {
    return count;
  }
  /**
   * Converts input data to a string.
   *
   * @return the string.
   */
  public String toString() {
    return new String(buffer, 0, count);
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
