---
title: A class that wraps an array with a List interface.
nav: A class that wraps an arra...
description: A class that wraps an array with a List interface. : List « Collections Data Structure « Java
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20091016224931/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AclassthatwrapsanarraywithaListinterface.htm
---
A class that wraps an array with a List interface. : List « Collections Data Structure « Java

```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import java.lang.reflect.Array;
import java.util.AbstractList;
/**
 *
 * @author Chris Schultz &lt;chris@christopherschultz.net$gt;
 * @version $Revision: 685685 $ $Date: 2006-04-14 19:40:41 $
 * @since 1.6
 */
public class ArrayListWrapper extends AbstractList
{
    private Object array;
    public ArrayListWrapper(Object array)
    {
        this.array = array;
    }
    public Object get(int index)
    {
        return Array.get(array, index);
    }
    public Object set(int index, Object element)
    {
        Object old = get(index);
        Array.set(array, index, element);
        return old;
    }
    public int size()
    {
        return Array.getLength(array);
    }
}
```

1.  Using the Double Brace Initialization.
---  ---
2.  Add to end Performance compare: LinkList and ArrayList
3.  Add to start Performance compare: LinkList and ArrayList
4.  Convert array to list and sort
5.  Shuffle a list
6.  Sort a list
7.  Bidirectional Traversal with ListIterator
8.  Int list
9.  Linked List example
10.  List to array
11.  List Reverse Test
12.  Build your own Linked List class
13.  List Search Test
14.  Convert a List to a Set
15.  Set Operating on Lists: addAll, removeAll, retainAll, subList
16.  Convert collection into array
17.  Convert LinkedList to array
18.  Convert Set into List
19.  If a List contains an item
20.  ListSet extends List and Set
21.  List containing other lists
22.  Helper method for creating list
23.  Generic to list
24.  List implementation with lazy array construction and modification tracking.
25.  Utility methods for operating on memory-efficient lists. All lists of size 0 or 1 are assumed to be immutable.
