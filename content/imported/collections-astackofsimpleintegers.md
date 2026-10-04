---
title: A stack of simple integers
nav: A stack of simple integers
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 2469
source: https://web.archive.org/web/20140829085657/http://www.java2s.com/Tutorial/Java/0140__Collections/Astackofsimpleintegers.htm
---
```java title=Example.java
import java.util.EmptyStackException;
/*
 * $Id: IntVector.java 468655 2006-10-28 07:12:06Z minchau $
 */
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the  "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/*
 * $Id: IntStack.java 468655 2006-10-28 07:12:06Z minchau $
 */
/**
 * Implement a stack of simple integers.
 *
 * %OPT%
 * This is currently based on IntVector, which permits fast acess but pays a
 * heavy recopying penalty if/when its size is increased. If we expect deep
 * stacks, we should consider a version based on ChunkedIntVector.
 * @xsl.usage internal
 */
public class IntStack extends IntVector
{
  /**
   * Default constructor.  Note that the default
   * block size is very small, for small lists.
   */
  public IntStack()
  {
    super();
  }
  /**
   * Construct a IntVector, using the given block size.
   *
   * @param blocksize Size of block to allocate
   */
  public IntStack(int blocksize)
  {
    super(blocksize);
  }
  /**
   * Copy constructor for IntStack
   *
   * @param v IntStack to copy
   */
  public IntStack (IntStack v)
  {
    super(v);
  }
  /**
   * Pushes an item onto the top of this stack.
   *
   * @param   i   the int to be pushed onto this stack.
   * @return  the <code>item</code> argument.
   */
  public int push(int i)
  {
    if ((m_firstFree + 1) >= m_mapSize)
    {
      m_mapSize += m_blocksize;
      int newMap[] = new int[m_mapSize];
      System.arraycopy(m_map, 0, newMap, 0, m_firstFree + 1);
      m_map = newMap;
    }
    m_map[m_firstFree] = i;
    m_firstFree++;
    return i;
  }
  /**
   * Removes the object at the top of this stack and returns that
   * object as the value of this function.
   *
   * @return     The object at the top of this stack.
   */
  public final int pop()
  {
    return m_map[--m_firstFree];
  }
  /**
   * Quickly pops a number of items from the stack.
   */
  public final void quickPop(int n)
  {
    m_firstFree -= n;
  }
  /**
   * Looks at the object at the top of this stack without removing it
   * from the stack.
   *
   * @return     the object at the top of this stack.
   * @throws  EmptyStackException  if this stack is empty.
   */
  public final int peek()
  {
    try {
      return m_map[m_firstFree - 1];
    }
    catch (ArrayIndexOutOfBoundsException e)
    {
      throw new EmptyStackException();
    }
  }
  /**
   * Looks at the object at the position the stack counting down n items.
   *
   * @param n The number of items down, indexed from zero.
   * @return     the object at n items down.
   * @throws  EmptyStackException  if this stack is empty.
   */
  public int peek(int n)
  {
    try {
      return m_map[m_firstFree-(1+n)];
    }
    catch (ArrayIndexOutOfBoundsException e)
    {
      throw new EmptyStackException();
    }
  }
  /**
   * Sets an object at a the top of the statck
   *
   *
   * @param val object to set at the top
   * @throws  EmptyStackException  if this stack is empty.
   */
  public void setTop(int val)
  {
    try {
      m_map[m_firstFree - 1] = val;
    }
    catch (ArrayIndexOutOfBoundsException e)
    {
      throw new EmptyStackException();
    }
  }
  /**
   * Tests if this stack is empty.
   *
   * @return  <code>true</code> if this stack is empty;
   *          <code>false</code> otherwise.
   * @since   JDK1.0
   */
  public boolean empty()
  {
    return m_firstFree == 0;
  }
  /**
   * Returns where an object is on this stack.
   *
   * @param   o   the desired object.
   * @return  the distance from the top of the stack where the object is]
   *          located; the return value <code>-1</code> indicates that the
   *          object is not on the stack.
   * @since   JDK1.0
   */
  public int search(int o)
  {
    int i = lastIndexOf(o);
    if (i >= 0)
    {
      return size() - i;
    }
    return -1;
  }
  /**
   * Returns clone of current IntStack
   *
   * @return clone of current IntStack
   */
  public Object clone()
    throws CloneNotSupportedException
  {
    return (IntStack) super.clone();
  }
}
/**
 * A very simple table that stores a list of int.
 *
 * This version is based on a "realloc" strategy -- a simle array is
 * used, and when more storage is needed, a larger array is obtained
 * and all existing data is recopied into it. As a result, read/write
 * access to existing nodes is O(1) fast but appending may be O(N**2)
 * slow. See also SuballocatedIntVector.
 * @xsl.usage internal
 */
class IntVector implements Cloneable
{
  /** Size of blocks to allocate          */
  protected int m_blocksize;
  /** Array of ints          */
  protected int m_map[]; // IntStack is trying to see this directly
  /** Number of ints in array          */
  protected int m_firstFree = 0;
  /** Size of array          */
  protected int m_mapSize;
  /**
   * Default constructor.  Note that the default
   * block size is very small, for small lists.
   */
  public IntVector()
  {
    m_blocksize = 32;
    m_mapSize = m_blocksize;
    m_map = new int[m_blocksize];
  }
  /**
   * Construct a IntVector, using the given block size.
   *
   * @param blocksize Size of block to allocate
   */
  public IntVector(int blocksize)
  {
    m_blocksize = blocksize;
    m_mapSize = blocksize;
    m_map = new int[blocksize];
  }
  /**
   * Construct a IntVector, using the given block size.
   *
   * @param blocksize Size of block to allocate
   */
  public IntVector(int blocksize, int increaseSize)
  {
    m_blocksize = increaseSize;
    m_mapSize = blocksize;
    m_map = new int[blocksize];
  }
  /**
   * Copy constructor for IntVector
   *
   * @param v Existing IntVector to copy
   */
  public IntVector(IntVector v)
  {
    m_map = new int[v.m_mapSize];
    m_mapSize = v.m_mapSize;
    m_firstFree = v.m_firstFree;
    m_blocksize = v.m_blocksize;
    System.arraycopy(v.m_map, 0, m_map, 0, m_firstFree);
  }
  /**
   * Get the length of the list.
   *
   * @return length of the list
   */
  public final int size()
  {
    return m_firstFree;
  }
  /**
   * Get the length of the list.
   *
   * @return length of the list
   */
  public final void setSize(int sz)
  {
    m_firstFree = sz;
  }
  /**
   * Append a int onto the vector.
   *
   * @param value Int to add to the list
   */
  public final void addElement(int value)
  {
    if ((m_firstFree + 1) >= m_mapSize)
    {
      m_mapSize += m_blocksize;
      int newMap[] = new int[m_mapSize];
      System.arraycopy(m_map, 0, newMap, 0, m_firstFree + 1);
      m_map = newMap;
    }
    m_map[m_firstFree] = value;
    m_firstFree++;
  }
  /**
   * Append several int values onto the vector.
   *
   * @param value Int to add to the list
   */
  public final void addElements(int value, int numberOfElements)
  {
    if ((m_firstFree + numberOfElements) >= m_mapSize)
    {
      m_mapSize += (m_blocksize+numberOfElements);
      int newMap[] = new int[m_mapSize];
      System.arraycopy(m_map, 0, newMap, 0, m_firstFree + 1);
      m_map = newMap;
    }
    for (int i = 0; i < numberOfElements; i++)
    {
      m_map[m_firstFree] = value;
      m_firstFree++;
    }
  }
  /**
   * Append several slots onto the vector, but do not set the values.
   *
   * @param numberOfElements Int to add to the list
   */
  public final void addElements(int numberOfElements)
  {
    if ((m_firstFree + numberOfElements) >= m_mapSize)
    {
      m_mapSize += (m_blocksize+numberOfElements);
      int newMap[] = new int[m_mapSize];
      System.arraycopy(m_map, 0, newMap, 0, m_firstFree + 1);
      m_map = newMap;
    }
    m_firstFree += numberOfElements;
  }
  /**
   * Inserts the specified node in this vector at the specified index.
   * Each component in this vector with an index greater or equal to
   * the specified index is shifted upward to have an index one greater
   * than the value it had previously.
   *
   * @param value Int to insert
   * @param at Index of where to insert
   */
  public final void insertElementAt(int value, int at)
  {
    if ((m_firstFree + 1) >= m_mapSize)
    {
      m_mapSize += m_blocksize;
      int newMap[] = new int[m_mapSize];
      System.arraycopy(m_map, 0, newMap, 0, m_firstFree + 1);
      m_map = newMap;
    }
    if (at <= (m_firstFree - 1))
    {
      System.arraycopy(m_map, at, m_map, at + 1, m_firstFree - at);
    }
    m_map[at] = value;
    m_firstFree++;
  }
  /**
   * Inserts the specified node in this vector at the specified index.
   * Each component in this vector with an index greater or equal to
   * the specified index is shifted upward to have an index one greater
   * than the value it had previously.
   */
  public final void removeAllElements()
  {
    for (int i = 0; i < m_firstFree; i++)
    {
      m_map[i] = java.lang.Integer.MIN_VALUE;
    }
    m_firstFree = 0;
  }
  /**
   * Removes the first occurrence of the argument from this vector.
   * If the object is found in this vector, each component in the vector
   * with an index greater or equal to the object's index is shifted
   * downward to have an index one smaller than the value it had
   * previously.
   *
   * @param s Int to remove from array
   *
   * @return True if the int was removed, false if it was not found
   */
  public final boolean removeElement(int s)
  {
    for (int i = 0; i < m_firstFree; i++)
    {
      if (m_map[i] == s)
      {
        if ((i + 1) < m_firstFree)
          System.arraycopy(m_map, i + 1, m_map, i - 1, m_firstFree - i);
        else
          m_map[i] = java.lang.Integer.MIN_VALUE;
        m_firstFree--;
        return true;
      }
    }
    return false;
  }
  /**
   * Deletes the component at the specified index. Each component in
   * this vector with an index greater or equal to the specified
   * index is shifted downward to have an index one smaller than
   * the value it had previously.
   *
   * @param i index of where to remove and int
   */
  public final void removeElementAt(int i)
  {
    if (i > m_firstFree)
      System.arraycopy(m_map, i + 1, m_map, i, m_firstFree);
    else
      m_map[i] = java.lang.Integer.MIN_VALUE;
    m_firstFree--;
  }
  /**
   * Sets the component at the specified index of this vector to be the
   * specified object. The previous component at that position is discarded.
   *
   * The index must be a value greater than or equal to 0 and less
   * than the current size of the vector.
   *
   * @param value object to set
   * @param index Index of where to set the object
   */
  public final void setElementAt(int value, int index)
  {
    m_map[index] = value;
  }
  /**
   * Get the nth element.
   *
   * @param i index of object to get
   *
   * @return object at given index
   */
  public final int elementAt(int i)
  {
    return m_map[i];
  }
  /**
   * Tell if the table contains the given node.
   *
   * @param s object to look for
   *
   * @return true if the object is in the list
   */
  public final boolean contains(int s)
  {
    for (int i = 0; i < m_firstFree; i++)
    {
      if (m_map[i] == s)
        return true;
    }
    return false;
  }
  /**
   * Searches for the first occurence of the given argument,
   * beginning the search at index, and testing for equality
   * using the equals method.
   *
   * @param elem object to look for
   * @param index Index of where to begin search
   * @return the index of the first occurrence of the object
   * argument in this vector at position index or later in the
   * vector; returns -1 if the object is not found.
   */
  public final int indexOf(int elem, int index)
  {
    for (int i = index; i < m_firstFree; i++)
    {
      if (m_map[i] == elem)
        return i;
    }
    return java.lang.Integer.MIN_VALUE;
  }
  /**
   * Searches for the first occurence of the given argument,
   * beginning the search at index, and testing for equality
   * using the equals method.
   *
   * @param elem object to look for
   * @return the index of the first occurrence of the object
   * argument in this vector at position index or later in the
   * vector; returns -1 if the object is not found.
   */
  public final int indexOf(int elem)
  {
    for (int i = 0; i < m_firstFree; i++)
    {
      if (m_map[i] == elem)
        return i;
    }
    return java.lang.Integer.MIN_VALUE;
  }
  /**
   * Searches for the first occurence of the given argument,
   * beginning the search at index, and testing for equality
   * using the equals method.
   *
   * @param elem Object to look for
   * @return the index of the first occurrence of the object
   * argument in this vector at position index or later in the
   * vector; returns -1 if the object is not found.
   */
  public final int lastIndexOf(int elem)
  {
    for (int i = (m_firstFree - 1); i >= 0; i--)
    {
      if (m_map[i] == elem)
        return i;
    }
    return java.lang.Integer.MIN_VALUE;
  }
  /**
   * Returns clone of current IntVector
   *
   * @return clone of current IntVector
   */
  public Object clone()
    throws CloneNotSupportedException
  {
    return new IntVector(this);
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
