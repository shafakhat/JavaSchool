---
title: Array Of int Arrays
nav: Array Of int Arrays
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2309
source: https://web.archive.org/web/20140829093614/http://www.java2s.com/Tutorial/Java/0140__Collections/ArrayOfintArrays.htm
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
public class ArrayOfArraysDemo2 {
  public static void main(String[] args) {
    int[][] aMatrix = new int[4][];
    // populate matrix
    for (int i = 0; i < aMatrix.length; i++) {
      aMatrix[i] = new int[5]; // create sub-array
      for (int j = 0; j < aMatrix[i].length; j++) {
        aMatrix[i][j] = i + j;
      }
    }
    // print matrix
    for (int i = 0; i < aMatrix.length; i++) {
      for (int j = 0; j < aMatrix[i].length; j++) {
        System.out.print(aMatrix[i][j] + " ");
      }
      System.out.println();
    }
  }
}
```

| 9.4.1. | Initialize a two-dimensional array in matrix |
|---|---|
| 9.4.2. | Arrays of Arrays |
| 9.4.3. | Arrays of Arrays in Varying Length |
| 9.4.4. | Defining Multidimensional Arrays |
| 9.4.5. | Array Of int Arrays |
| 9.4.6. | Get array upperbound |
| 9.4.7. | To get the number of dimensions |
| 9.4.8. | Array Of string Arrays |
