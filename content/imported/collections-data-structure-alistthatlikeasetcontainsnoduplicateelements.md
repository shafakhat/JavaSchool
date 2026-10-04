---
title: A List that, like a Set, contains no duplicate Elements.
nav: A List that, like a Set, c...
description: /*********************************************************************
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20110927192058/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AListthatlikeaSetcontainsnoduplicateElements.htm
---
```java title=Example.java
//     package com.croftsoft.core.util;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Set;
/*********************************************************************
 *
 *
 * @author <a href="http://www.CroftSoft.com/">David Wallace Croft</a>
 * @version 1998-11-23
 *********************************************************************/
public class SetList implements Set, List
// ////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////
{
  protected List list;
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public SetList(List list)
  // ////////////////////////////////////////////////////////////////////
  {
    this.list = list;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  /*********************************************************************
   * Returns false if the List already contains the object.
   *********************************************************************/
  public synchronized boolean add(Object o)
  // ////////////////////////////////////////////////////////////////////
  {
    if (list.contains(o))
      return false;
    else
      return list.add(o);
  }
  /*********************************************************************
   * Skips objects in the Collection that already exist in the List. Returns
   * true if any of the objects were added.
   *********************************************************************/
  public synchronized boolean addAll(Collection c)
  // ////////////////////////////////////////////////////////////////////
  {
    boolean result = false;
    Iterator iterator = c.iterator();
    while (iterator.hasNext()) {
      if (this.add(iterator.next()))
        result = true;
    }
    return result;
  }
  /*********************************************************************
   * Skips object in the Collection that already exist in the List. Returns
   * true if any of the objects were added.
   *********************************************************************/
  public synchronized boolean addAll(int index, Collection c)
  // ////////////////////////////////////////////////////////////////////
  {
    boolean result = false;
    int i = 0;
    Iterator iterator = c.iterator();
    while (iterator.hasNext()) {
      Object o = iterator.next();
      if (!list.contains(o)) {
        list.add(index + i, o);
        i++;
        result = true;
      }
    }
    return result;
  }
  /*********************************************************************
   * @throws IllegalArgumentException
   *             If a duplicate object already exists in the List.
   *********************************************************************/
  public synchronized Object set(int index, Object element)
  // ////////////////////////////////////////////////////////////////////
  {
    if (list.contains(element)) {
      throw new IllegalArgumentException("duplicate");
    } else
      return list.set(index, element);
  }
  /*********************************************************************
   * @throws IllegalArgumentException
   *             If a duplicate object already exists in the List.
   *********************************************************************/
  public synchronized void add(int index, Object element)
  // ////////////////////////////////////////////////////////////////////
  {
    if (list.contains(element)) {
      throw new IllegalArgumentException("duplicate");
    } else
      list.add(index, element);
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public int size() {
    return list.size();
  }
  public boolean isEmpty() {
    return list.isEmpty();
  }
  public boolean contains(Object o) {
    return list.contains(o);
  }
  public Iterator iterator() {
    return list.iterator();
  }
  public Object[] toArray() {
    return list.toArray();
  }
  public Object[] toArray(Object a[]) {
    return list.toArray(a);
  }
  public boolean remove(Object o) {
    return list.remove(o);
  }
  public boolean containsAll(Collection c) {
    return list.containsAll(c);
  }
  public boolean removeAll(Collection c) {
    return list.removeAll(c);
  }
  public boolean retainAll(Collection c) {
    return list.retainAll(c);
  }
  public void clear() {
    list.clear();
  }
  public boolean equals(Object o) {
    return list.equals(o);
  }
  public int hashCode() {
    return list.hashCode();
  }
  public Object get(int index) {
    return list.get(index);
  }
  public Object remove(int index) {
    return list.remove(index);
  }
  public int indexOf(Object o) {
    return list.indexOf(o);
  }
  public int lastIndexOf(Object o) {
    return list.lastIndexOf(o);
  }
  public ListIterator listIterator() {
    return list.listIterator();
  }
  public ListIterator listIterator(int index) {
    return list.listIterator(index);
  }
  public List subList(int fromIndex, int toIndex) {
    return list.subList(fromIndex, toIndex);
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
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
26.  A class that wraps an array with a List interface.
27.  Splits the list.
28.  Slice a list
29.  Determines if the given lists contain the same elements. We suppose that all the elements of the given lists are different.
30.  List that allows items to be added with a priority that will affect the order in which they are later iterated over.
