---
title: Helper method for creating list
nav: Helper method for creating...
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 2462
source: https://web.archive.org/web/20140516124008/http://www.java2s.com/Tutorial/Java/0140__Collections/Helpermethodforcreatinglist.htm
---
```java title=Example.java
/**
 * Copyright (C) 2007 Google Inc.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
/**
 * Helper methods related to {@link List}s.
 *
 * @author maxr@google.com (Max Ross)
 */
public class Lists {
  private Lists() { }
  /**
   * Construct a new {@link ArrayList}, taking advantage of type inference to
   * avoid specifying the type on the rhs.
   */
  public static <E> ArrayList<E> newArrayList() {
    return new ArrayList<E>();
  }
  /**
   * Construct a new {@link ArrayList} with the specified capacity, taking advantage of type inference to
   * avoid specifying the type on the rhs.
   */
  public static <E> ArrayList<E> newArrayListWithCapacity(int initialCapacity) {
    return new ArrayList<E>(initialCapacity);
  }
  /**
   * Construct a new {@link ArrayList} with the provided elements, taking advantage of type inference to
   * avoid specifying the type on the rhs.
   */
  public static <E> ArrayList<E> newArrayList(E... elements) {
    ArrayList<E> set = newArrayList();
    Collections.addAll(set, elements);
    return set;
  }
  /**
   * Construct a new {@link ArrayList} with the contents of the provided {@link Iterable}, taking advantage of type inference to
   * avoid specifying the type on the rhs.
   */
  public static <E> ArrayList<E> newArrayList(Iterable<? extends E> elements) {
    ArrayList<E> list = newArrayList();
    for(E e : elements) {
      list.add(e);
    }
    return list;
  }
  /**
   * Construct a new {@link LinkedList}, taking advantage of type inference to
   * avoid specifying the type on the rhs.
   */
  public static <E> LinkedList<E> newLinkedList() {
    return new LinkedList<E>();
  }
}
```

| 9.12.1. | LinkedList Class |
|---|---|
| 9.12.2. | Get first and last elements from LinkedList |
| 9.12.3. | Get elements from LinkedList |
| 9.12.4. | Get SubList from LinkedList |
| 9.12.5. | Adding Elements: add a single element |
| 9.12.6. | Add elements at beginning and end of LinkedList |
| 9.12.7. | LinkedList: add, addFirst, addLast, remove |
| 9.12.8. | Retrieving the Ends from a LinkedList |
| 9.12.9. | Removing Elements |
| 9.12.10. | Making a stack from a LinkedList |
| 9.12.11. | Making a queue from a LinkedList |
| 9.12.12. | Convert Collection to ArrayList |
| 9.12.13. | Remove all elements or clear LinkedList |
| 9.12.14. | Remove first and last elements of LinkedList |
| 9.12.15. | Remove range of elements from LinkedList |
| 9.12.16. | Remove specified element from LinkedList |
| 9.12.17. | Convert LinkedList to Array with zero length array |
| 9.12.18. | Convert LinkedList to Array with full length array |
| 9.12.19. | Convert a LinkedList to ArrayList |
| 9.12.20. | Implementing a Stack |
| 9.12.21. | Implementing a Queue with LinkedList |
| 9.12.22. | Wrap queue to synchronize the methods |
| 9.12.23. | Search elements of LinkedList |
| 9.12.24. | Replace an Element of LinkedList |
| 9.12.25. | Add object to LinkedList |
| 9.12.26. | Check if a particular element exists in LinkedList |
| 9.12.27. | Create an object array from elements of LinkedList |
| 9.12.28. | Using a LinkedList in multi-thread |
| 9.12.29. | A basic priority linked list: maintaining an individual LinkedList for each priority level. |
| 9.12.30. | Helper method for creating list |
