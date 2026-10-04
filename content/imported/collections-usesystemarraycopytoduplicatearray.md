---
title: Use System.arraycopy to duplicate array
nav: Use System.arraycopy to du...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2300
source: https://web.archive.org/web/20140829091132/http://www.java2s.com/Tutorial/Java/0140__Collections/UseSystemarraycopytoduplicatearray.htm
---
```java title=Example.java
/*
 * Copyright (c) 1995 - 2008 Sun Microsystems, Inc.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   - Neither the name of Sun Microsystems nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
public class ArrayCopyDemo {
  public static void main(String[] args) {
    char[] copyFrom = { 'd', 'e', 'c', 'a', 'f', 'f', 'e', 'i', 'n', 'a', 't',
        'e', 'd' };
    char[] copyTo = new char[7];
    System.arraycopy(copyFrom, 2, copyTo, 0, 7);
    System.out.println(new String(copyTo));
  }
}
```

| 9.3.1. | How to define an Array |
|---|---|
| 9.3.2. | Initializing array elements by index |
| 9.3.3. | Alternative Array Declaration Syntax |
| 9.3.4. | Anonymous arrays are declared similarly to regular arrays |
| 9.3.5. | An array is a Java object |
| 9.3.6. | To reference the components of an array |
| 9.3.7. | The Length of an Array |
| 9.3.8. | Initializing Arrays |
| 9.3.9. | Using a for loop to iterate over all the elements and set the values |
| 9.3.10. | Arrays of Characters |
| 9.3.11. | Using the Collection-Based for Loop with an Array |
| 9.3.12. | Changing Array Size |
| 9.3.13. | Array Reallocation |
| 9.3.14. | Use System.arraycopy to duplicate array |
| 9.3.15. | Minimum and maximum number in array |
| 9.3.16. | Shuffle elements of an array |
| 9.3.17. | Merge (or add) two arrays into one |
| 9.3.18. | Circular Buffer |
