---
title: Adds the object to the array.
nav: Adds the object to the arr...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20111106022745/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Addstheobjecttothearray.htm
---
```java title=Example.java
/*
 * Copyright 2004-2010 the Seasar Foundation and the Others.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 */
//package org.slim3.util;
import java.lang.reflect.Array;
/**
 * A utility for {@link Array}.
 *
 * @author higa
 * @since 1.0.0
 *
 */
public final class ArrayUtil {
    /**
     *
     * @param <T>
     *            the type
     * @param array
     *            the array
     * @param obj
     *            the object
     * @return the added array
     */
    @SuppressWarnings("unchecked")
    public static <T> T[] add(T[] array, T obj) {
        if (array == null && obj == null) {
            return null;
        }
        Class<?> clazz =
            obj != null ? obj.getClass() : array.getClass().getComponentType();
        int length = array != null ? array.length : 0;
        T[] newArray = (T[]) Array.newInstance(clazz, length + 1);
        if (array != null) {
            System.arraycopy(array, 0, newArray, 0, length);
        }
        newArray[length] = obj;
        return newArray;
    }
    private ArrayUtil() {
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
29.  A growable array of bytes
30.  Doubles the size of an array
31.  Concatenate arrays
32.  Double List
