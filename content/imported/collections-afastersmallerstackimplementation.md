---
title: A faster, smaller stack implementation.
nav: A faster, smaller stack im...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2468
source: https://web.archive.org/web/20140829083850/http://www.java2s.com/Tutorial/Java/0140__Collections/Afastersmallerstackimplementation.htm
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
import java.util.ArrayList;
import java.util.Collection;
import java.util.EmptyStackException;
/**
 * A faster, smaller stack implementation. ArrayListStack is final and unsynchronized (the JDK's
 * methods are synchronized). In addition you can set the initial capacity if you want via the
 * ArrayListStack(int) constructor.
 *
 * @author Jonathan Locke
 * @param <T>
 */
public final class ArrayListStack<T> extends ArrayList<T>
{
  private static final long serialVersionUID = 1L;
  /**
   * Construct.
   *
   * @param initialCapacity
   *            Initial capacity of the stack
   */
  public ArrayListStack(final int initialCapacity)
  {
    super(initialCapacity);
  }
  /**
   * Construct.
   */
  public ArrayListStack()
  {
    this(10);
  }
  /**
   * Construct.
   *
   * @param collection
   *            The collection to add
   */
  public ArrayListStack(final Collection<T> collection)
  {
    super(collection);
  }
  /**
   * Pushes an item onto the top of this stack.
   *
   * @param item
   *            the item to be pushed onto this stack.
   */
  public final void push(final T item)
  {
    add(item);
  }
  /**
   * Removes the object at the top of this stack and returns that object.
   *
   * @return The object at the top of this stack
   * @exception EmptyStackException
   *                If this stack is empty.
   */
  public final T pop()
  {
    final T top = peek();
    remove(size() - 1);
    return top;
  }
  /**
   * Looks at the object at the top of this stack without removing it.
   *
   * @return The object at the top of this stack
   * @exception EmptyStackException
   *                If this stack is empty.
   */
  public final T peek()
  {
    int size = size();
    if (size == 0)
    {
      throw new EmptyStackException();
    }
    return get(size - 1);
  }
  /**
   * Tests if this stack is empty.
   *
   * @return <code>true</code> if and only if this stack contains no items; <code>false</code>
   *         otherwise.
   */
  public final boolean empty()
  {
    return size() == 0;
  }
  /**
   * Returns the 1-based position where an object is on this stack. If the object <tt>o</tt>
   * occurs as an item in this stack, this method returns the distance from the top of the stack
   * of the occurrence nearest the top of the stack; the topmost item on the stack is considered
   * to be at distance <tt>1</tt>. The <tt>equals</tt> method is used to compare <tt>o</tt>
   * to the items in this stack.
   *
   * @param o
   *            the desired object.
   * @return the 1-based position from the top of the stack where the object is located; the
   *         return value <code>-1</code> indicates that the object is not on the stack.
   */
  public final int search(final T o)
  {
    int i = lastIndexOf(o);
    if (i >= 0)
    {
      return size() - i;
    }
    return -1;
  }
}
```

| 9.13.1. | Stack Basics: last-in, first-out behavior |
|---|---|
| 9.13.2. | Adding Elements: To add an element to a stack, call the push() method |
| 9.13.3. | Removing Elements: To remove an element from the stack, the pop() method |
| 9.13.4. | If the size of the stack is zero, true is returned; otherwise, false is returned |
| 9.13.5. | Checking the Top: To get the element without removing: using the peek() method |
| 9.13.6. | To find out if an element is on the stack: the search() method |
| 9.13.7. | Demonstrate the generic Stack class. |
| 9.13.8. | A faster, smaller stack implementation. |
| 9.13.9. | A simple integer based stack. |
| 9.13.10. | A stack of simple integers |
| 9.13.11. | A very simple unsynchronized stack. This one is faster than the java.util-Version. |
| 9.13.12. | An implementation of the java.util.Stack based on an ArrayList instead of a Vector, so it is not synchronized to protect against multi-threaded access. |
| 9.13.13. | Character Stack |
| 9.13.14. | Growable Object stack with type specific access methods |
| 9.13.15. | Growable String stack with type specific access methods. |
| 9.13.16. | Growable int stack with type specific access methods |
| 9.13.17. | Stack for boolean values |
| 9.13.18. | extends ArrayList to create Stack |
