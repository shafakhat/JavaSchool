---
title: Generic Triple structure
nav: Generic Triple structure
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20111010003055/http://java2s.com:80/Code/Java/Generics/GenericTriplestructure.htm
---
```java title=Example.java
/**
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */
//package org.cspoker.common.util;
public class Triple<L,M,R> {
  private final L left;
  private final M middle;
  private final R right;
  public Triple(L left, M middle, R right) {
    if(left==null){
      throw new IllegalArgumentException("Left value is not effective.");
    }
    if(middle==null){
      throw new IllegalArgumentException("Middle value is not effective.");
    }
    if(right==null){
      throw new IllegalArgumentException("Right value is not effective.");
    }
    this.left =left;
    this.middle = middle;
    this.right = right;
  }
  public L getLeft() {
    return this.left;
  }
  public M getMiddle() {
    return this.middle;
  }
  public R getRight() {
    return this.right;
  }
  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((left == null) ? 0 : left.hashCode());
    result = prime * result + ((middle == null) ? 0 : middle.hashCode());
    result = prime * result + ((right == null) ? 0 : right.hashCode());
    return result;
  }
  @SuppressWarnings("unchecked")
  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Triple<Object, Object, Object> other = (Triple<Object, Object, Object>) obj;
    if (left == null) {
      if (other.left != null)
        return false;
    } else if (!left.equals(other.left))
      return false;
    if (middle == null) {
      if (other.middle != null)
        return false;
    } else if (!middle.equals(other.middle))
      return false;
    if (right == null) {
      if (other.right != null)
        return false;
    } else if (!right.equals(other.right))
      return false;
    return true;
  }
  @Override
  public String toString() {
    return "<"+left+","+middle+","+right+">";
  }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Generic Data Structure
6.  Unchecked Example
7.  Generic Stack
8.  Enum and Generic
9.  Generic HashMap
10.  Foreach and generic data structure
11.  Pre generics example that uses a collection.
12.  Data structure and collections: Modern, generics version.
13.  Java generic: Generics and arrays.
14.  Collections and Data structure: the generic way
15.  The GenStack Class
16.  Create a typesafe copy of a raw set.
17.  Create a typesafe copy of a raw list.
18.  Create a typesafe copy of a raw map.
19.  Create a typesafe filter of an unchecked iterator.
20.  Create a typesafe view over an underlying raw set.
21.  Create a typesafe view over an underlying raw map.
22.  Create a typesafe filter of an unchecked enumeration.
23.  Circular Object Buffer
24.  A collection that do not hold stored elements in memory, but serialize it into a file
25.  Generic Pair
26.  A generic bag of properties used to store properties that apply to a specific target.
27.  Pool container
