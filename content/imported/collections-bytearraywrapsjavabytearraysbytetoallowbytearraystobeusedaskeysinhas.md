---
title: ByteArray wraps java byte arrays (byte[]) to allow byte arrays to be used as keys in hashtables.
nav: ByteArray wraps java byte ...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2392
source: https://web.archive.org/web/20140829075708/http://www.java2s.com/Tutorial/Java/0140__Collections/ByteArraywrapsjavabytearraysbytetoallowbytearraystobeusedaskeysinhashtables.htm
---
```java title=Example.java
/*
   Derby - Class org.apache.derby.iapi.util.ByteArray
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to you under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */
import java.io.ObjectOutput;
import java.io.ObjectInput;
import java.io.IOException;
/**
  ByteArray wraps java byte arrays (byte[]) to allow
  byte arrays to be used as keys in hashtables.
  This is required because the equals function on
  byte[] directly uses reference equality.
  This class also allows the trio of array, offset and length
  to be carried around as a single object.
*/
public final class ByteArray
{
  private byte[] array;
  private int    offset;
  private int    length;
  /**
    Create an instance of this class that wraps ths given array.
    This class does not make a copy of the array, it just saves
    the reference.
  */
  public ByteArray(byte[] array, int offset, int length) {
    this.array = array;
    this.offset = offset;
    this.length = length;
  }
  public ByteArray(byte[] array) {
    this(array, 0, array.length);
  }
  public ByteArray()
  {
  }
  public void setBytes(byte[] array)
  {
    this.array = array;
    offset = 0;
    length = array.length;
  }
  public void setBytes(byte[] array, int length)
  {
    this.array = array;
    this.offset = 0;
    this.length = length;
  }
  public void setBytes(byte[] array, int offset, int length)
  {
    this.array = array;
    this.offset = offset;
    this.length = length;
  }
  /**
    Value equality for byte arrays.
  */
  public boolean equals(Object other) {
    if (other instanceof ByteArray) {
      ByteArray ob = (ByteArray) other;
      return ByteArray.equals(array, offset, length, ob.array, ob.offset, ob.length);
    }
    return false;
  }
  /**
  */
  public int hashCode() {
    byte[] larray = array;
    int hash = length;
    for (int i = 0; i < length; i++) {
      hash += larray[i + offset];
    }
    return hash;
  }
  public final byte[] getArray() {
    return array;
  }
  public final int getOffset() {
    return offset;
  }
  public final int getLength() {
    return length;
  }
  public final void setLength(int newLength) {
    length = newLength;
  }
  /**
   * Read this object from a stream of stored objects.
   *
   * @param in read this.
   *
   * @exception IOException         thrown on error
   */
  public void readExternal( ObjectInput in ) throws IOException
  {
    int len = length = in.readInt();
    offset = 0;
    array = new byte[len];
    in.readFully(array, 0, len);
  }
  /**
   * Write the byte array out w/o compression
   *
   * @param out write bytes here.
   *
   * @exception IOException   thrown on error
   */
  public void writeExternal(ObjectOutput out) throws IOException
  {
    out.writeInt(length);
    out.write(array, offset, length);
  }
  /**
    Compare two byte arrays using value equality.
    Two byte arrays are equal if their length is
    identical and their contents are identical.
  */
  private static boolean equals(byte[] a, int aOffset, int aLength, byte[] b, int bOffset, int bLength) {
    if (aLength != bLength)
      return false;
    for (int i = 0; i < aLength; i++) {
      if (a[i + aOffset] != b[i + bOffset])
        return false;
    }
    return true;
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
