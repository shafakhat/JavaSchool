---
title: A growable array of bytes
nav: A growable array of bytes
description: /*********************************************************************
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20111106030951/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Agrowablearrayofbytes.htm
---
A growable array of bytes

```java title=Example.java
/*********************************************************************
*
*      Copyright (C) 2005 Andrew Khan
*
* This library is free software; you can redistribute it and/or
* modify it under the terms of the GNU Lesser General Public
* License as published by the Free Software Foundation; either
* version 2.1 of the License, or (at your option) any later version.
*
* This library is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
* Lesser General Public License for more details.
*
* You should have received a copy of the GNU Lesser General Public
* License along with this library; if not, write to the Free Software
* Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
***************************************************************************/
//package jxl.biff;
/**
 * A growable array of bytes
 */
public class ByteArray
{
  /**
   * The array grow size
   */
  private int growSize;
  /**
   * The current array
   */
  private byte[] bytes;
  /**
   * The current position
   */
  private int pos;
  // The default grow size
  private final static int defaultGrowSize = 1024;
  /**
   * Constructor
   */
  public ByteArray()
  {
    this(defaultGrowSize);
  }
  /**
   * Constructor
   *
   * @param gs
   */
  public ByteArray(int gs)
  {
    growSize = gs;
    bytes = new byte[defaultGrowSize];
    pos = 0;
  }
  /**
   * Adds a byte onto the array
   *
   * @param b the byte
   */
  public void add(byte b)
  {
    checkSize(1);
    bytes[pos] = b;
    pos++;
  }
  /**
   * Adds an array of bytes onto the array
   *
   * @param b the array of bytes
   */
  public void add(byte[] b)
  {
    checkSize(b.length);
    System.arraycopy(b, 0, bytes, pos, b.length);
    pos += b.length;
  }
  /**
   * Gets the complete array
   *
   * @return the array
   */
  public byte[] getBytes()
  {
    byte[] returnArray = new byte[pos];
    System.arraycopy(bytes, 0, returnArray, 0, pos);
    return returnArray;
  }
  /**
   * Checks to see if there is sufficient space left on the array.  If not,
   * then it grows the array
   *
   * @param sz the amount of bytes to add
   */
  private void checkSize(int sz)
  {
    while (pos + sz >= bytes.length)
    {
      //  Grow the array
      byte[] newArray = new byte[bytes.length + growSize];
      System.arraycopy(bytes, 0, newArray, 0, pos);
      bytes = newArray;
    }
  }
}
```

1.  Growable int[]
---  ---
2.  Your own auto-growth Array
3.  Long Vector
4.  Int Vector (from java-objects-database)
5.  ArrayList of int primitives
6.  ArrayList of long primitives
7.  ArrayList of short primitives
8.  ArrayList of double primitives
9.  ArrayList of boolean primitives
10.  ArrayList of char primitives
11.  ArrayList of byte primitives
12.  Growable String array with type specific access methods.
13.  Auto Size Array
14.  Dynamic Int Array
15.  Dynamic Long Array
16.  Int Array
17.  Int Array List
18.  ArrayList of float primitives
19.  Fast Array
20.  Extensible vector of bytes
21.  Int Vector
22.  A two dimensional Vector
23.  Lazy List creation based on ArrayList
24.  Append the given Object to the given array
25.  Adds all the elements of the given arrays into a new array.
26.  Simple object pool
27.  A variable length Double Array: expanding and contracting its internal storage array as elements are added and removed.
28.  Append item to array
29.  Doubles the size of an array
30.  Adds the object to the array.
31.  Concatenate arrays
32.  Double List
