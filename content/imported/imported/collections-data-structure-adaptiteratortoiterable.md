---
title: Adapt iterator to iterable
nav: Adapt iterator to iterable
description: public class IteratorIterable<T> implements Iterable<T>, Iterator<T> {
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20111124051228/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Adaptiteratortoiterable.htm
---
Adapt iterator to iterable

```java title=Example.java
import java.util.Iterator;
/**
 * Adapt iterator to iterable
 *
 * @author Hong Hong
 *
 * @param Iterator type
 */
public class IteratorIterable<T> implements Iterable<T>, Iterator<T> {
  protected Iterator<T> m_itr;
  public IteratorIterable(Iterator<T> itr) {
    assert(itr != null);
    m_itr = itr;
  }
  public Iterator<T> iterator() {
    return m_itr;
  }
  public boolean hasNext() {
    return m_itr.hasNext();
  }
  public T next() {
    return m_itr.next();
  }
  public void remove() {
    m_itr.remove();
  }
}
```

1.  Listing the Elements of a Collection
---  ---
2.  De-mystify the Iterator interface, showing how to write a simple Iterator for an Array of Objects
3.  Iterate over Set
4.  Demonstrate iterators.
5.  Use the for-each for loop to cycle through a collection.
6.  List Iterator
7.  Iterate a Collection and remove an item (Exception, wrong version)
8.  Use an Iterator and remove the item with Iterator.remove()
9.  An Iterator wrapper for an Enumeration.
10.  EmptyIterator is an iterator which is empty.
11.  Implements an java.util.Iterator over any array
12.  Treat an Iterator as an Iterable
13.  Iterator class for sparse values in an array.
14.  Iterator class for values contained in an array range.
15.  Array Iterator
16.  Cyclic Iteration
17.  Create singleton Iterator
18.  Empty Iterator
19.  An Iterator that wraps a number of Iterators
20.  An Iterator to iterate over the elements of an array
21.  Sorted Iterator
22.  Iterator Union of Iterators
23.  Iterator Utils
24.  Linked Iterator
25.  Prefetch Iterator
26.  Protects an given iterator by preventing calls to remove().
27.  An Iterator that returns the elements of a specified array, or other iterators etc.
28.  An Iterator wrapper for an Object[], allow us to deal with all array like structures in a consistent manner.
29.  An array iterator
30.  Static utility methods, classes, and abstract classes for iteration.
31.  Iterator Collection
32.  Convert Iterable to List
33.  A singleton null object Iterator implementation.
