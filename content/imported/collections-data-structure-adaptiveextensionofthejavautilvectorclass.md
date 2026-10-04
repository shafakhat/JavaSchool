---
title: Adaptive extension of the java.util.Vector class
nav: Adaptive extension of the ...
description: Adaptive extension of the java.util.Vector class : Vector « Collections Data Structure « Java
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20090930080856/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AdaptiveextensionofthejavautilVectorclass.htm
---
Adaptive extension of the java.util.Vector class : Vector « Collections Data Structure « Java
Adaptive extension of the java.util.Vector class

```java title=Example.java
//revised from marf
import java.util.Vector;
import java.util.Collection;
import java.util.List;
/**
 * <p>Adaptive extension of the java.util.Vector class.</p>
 *
 * <p>You may access elements of a Vector beyond it's initial length --- the Vector
 * will be automaticall adjusted as appropriate.</p>
 *
 * <p>Useful in the applications where desirable vector's growth by setting an element
 * beyond its upper boundary automatticaly lengthens the vector to accomondate the
 * change (similar to Perl arrays).</p>
 *
 * <p>Similarly, getting an element beyond the upper boundary is not desirable failure, but
 * an empty element returned. This makes the application to see as vector of a theoretically infinite
 * in length.</p>
 *
 * TODO: allow negative index boundaries.
 *
 * $Id: FreeVector.java,v 1.12 2005/08/11 00:44:50 mokhov Exp $
 *
 * @author Serguei Mokhov
 * @version $Revision: 1.12 $
 * @since 0.3.0.1
 */
public class FreeVector
extends Vector
{
  /**
   * For serialization versioning.
   * When adding new members or make other structural
   * changes regenerate this number with the
   * <code>serialver</code> tool that comes with JDK.
   * @since 0.3.0.4
   */
  private static final long serialVersionUID = 8706834105778495182L;
  /**
   * A free vector with default capacity as specified by java.util.Vector.
   */
  public FreeVector()
  {
    super();
  }
  /**
   * Constructs this vector given capacity other than default.
   * Inherited from java.util.Vector.
   * @param piInitialCapacity initial element capacity (number of object placeholders)
   */
  public FreeVector(int piInitialCapacity)
  {
    super(piInitialCapacity);
  }
  /**
   * Constructs this vector given capacity and its increment.
   * Inherited from java.util.Vector.
   * @param piInitialCapacity initial element capacity (number of object placeholders)
   * @param piCapacityIncrement when current capacity reached, until how much capacity should be extened
   */
  public FreeVector(int piInitialCapacity, int piCapacityIncrement)
  {
    super(piInitialCapacity, piCapacityIncrement);
  }
  /**
   * Constructs this vector out of a collection.
   * Inherited from java.util.Vector.
   * @param poCollection collection for the vector elements.
   */
  public FreeVector(Collection poCollection)
  {
    super(poCollection);
  }
  /**
   * Access an element of the vector given index.
   * Overridden from java.util.Vector.
   * @param piIndex vector element index to retrieve
   * @return object cotained at specified index, null if beyond boundary
   */
  public Object elementAt(int piIndex)
  {
    if(piIndex > size() - 1)
      return null;
    return super.elementAt(piIndex);
  }
  /**
   * Set an element of the vector given index.
   * Capacity is always ensured to be able to accomodate
   * any positive inidex (barring out of memory problems).
   * Overridden from java.util.Vector.
   *
   * @param poElement element to set at the index
   * @param piIndex the index
   */
  public void setElementAt(Object poElement, int piIndex)
  {
    ensureIndexCapacity(piIndex);
    super.setElementAt(poElement, piIndex);
  }
  /**
   * Inserts an element of the vector after given index.
   * Capacity is always ensured to be able to accomodate
   * any positive inidex (barring out of memory problems).
   * Overridden from java.util.Vector.
   *
   * @param poElement element to set after the index
   * @param piIndex the index
   */
  public void insertElementAt(Object poElement, int piIndex)
  {
    ensureIndexCapacity(piIndex);
    super.insertElementAt(poElement, piIndex);
  }
  /**
   * Make sure the capacity of the vector is enough
   * to hold an element with the specified index.
   * Has effect only if the index is greater than
   * the current vector's size.
   *
   * @param piIndex the index to accomodate
   */
  public void ensureIndexCapacity(int piIndex)
  {
    if(piIndex > size() - 1)
    {
      ensureCapacity(piIndex + 1);
      setSize(piIndex + 1);
    }
  }
  /**
   * Access an element of the vector given index.
   * Overridden from java.util.Vector. Calls the overridden elementAt().
   *
   * @param piIndex vector element index to retrieve
   * @return object cotained at specified index, null if beyond boundary
   */
  public synchronized Object get(int piIndex)
  {
    return elementAt(piIndex);
  }
  /**
   * Set an element of the vector given index.
   * Capacity is always ensured to be able to accomodate
   * any positive inidex (barring out of memory problems).
   * Overridden from java.util.Vector.
   *
   * @param poElement element to set at the index
   * @param piIndex the index
   * @return object that was previously at that index.
   */
  public synchronized Object set(int piIndex, Object poElement)
  {
    Object oOldElement = elementAt(piIndex);
    setElementAt(poElement, piIndex);
    return oOldElement;
  }
  /**
   * Adds an element of the vector at the specified index.
   * Overridden from java.util.Vector. Calls the overridden insertElementAt().
   * @param piIndex the index
   * @param poElement element to set after the index
   */
  public synchronized void add(int piIndex, Object poElement)
  {
    insertElementAt(poElement, piIndex);
  }
  /**
   * Removes an element at index.
   * If the index is beyond the upper boundary, returns null.
   * Overrides java.util.Vector.
   * @param piIndex index of the element to be removed
   * @return object reference of the element just removed; null if index exceeds the upper bound
   */
  public synchronized Object remove(int piIndex)
  {
    if(piIndex >= size())
    {
      //???
      // 1 less than the index
      //ensureIndexCapacity(piIndex - 1);
      return null;
    }
    return super.remove(piIndex);
  }
  /**
   * Adds a collection of elements to this vector starting at given index.
   * Makes sure the capacity of the current vector reaches the piIndex.
   * Overrides java.util.Vector.
   *
   * @param piIndex starting index to add elements from
   * @param poCollection collection of elements to add
   *
   * @return <code>true</code> if the vector has changed
   */
  public synchronized boolean addAll(int piIndex, Collection poCollection)
  {
    ensureIndexCapacity(piIndex);
    return super.addAll(piIndex, poCollection);
  }
  /**
   * Retrieves a sublist subset of vector elements given index boundaries.
   * Makes sure the capacity of the current vector reaches the piToIndex.
   * Overrides java.util.Vector.
   *
   * @param piFromIndex starting index to fetch elements from
   * @param piToIndex last index to fetch elements to
   *
   * @return a corresponding List reference.
   */
  public synchronized List subList(int piFromIndex, int piToIndex)
  {
    ensureIndexCapacity(piToIndex);
    return super.subList(piFromIndex, piToIndex);
  }
  /**
   * Not implemented.
   * Meant to remove a set of elements between two specified indices.
   * @param piFromIndex starting index to remove elements from
   * @param piToIndex last index to remove elements to
   * @throws NotImplementedException
   */
  public synchronized void removeRange(int piFromIndex, int piToIndex)
  {
    // TODO: implement
    throw new RuntimeException( "removeRange()");
  }
  /**
   * Retrieves class' revision.
   * @return revision string
   * @since 0.3.0.2
   */
  public static String getMARFSourceCodeRevision()
  {
    return "$Revision: 1.12 $";
  }
}
// EOF
```

1.  Use Vector in java.util
---  ---
2.  Finding elements in a vector
3.  Serializing a vector
4.  Save Vector to file
5.  Create Vector test
6.  Find Vector
7.  Remove Element in Vector
8.  Sequence
9.  Vector Util
10.  Iterator out of Vector
11.  Copy Elements of One Java Vector to Another Java Vector
12.  Copy Elements of Vector to Java ArrayList
13.  Create Java ArrayList From Enumeration
14.  Find maximum element of Java Vector
15.  Find Minimum element of Java Vector
16.  Get Enumeration over Java Vector
17.  Perform Binary Search on Java Vector
18.  Replace All Elements Of Java Vector
19.  Replace all occurrences of specified element of Java Vector
20.  Reverse order of all elements of Java Vector
21.  Shuffle elements of Java Vector
22.  Swap elements of Java Vector
23.  Sort Java Vector in descending order using comparator
24.  Enumerate through a Vector using Java Enumeration
25.  Append all elements of other Collection to Java Vector
26.  Copy all elements of Java Vector to an Object Array
27.  Get Size of Java Vector and loop through the elements
28.  Get Sub List of Java Vector Example
29.  Insert all elements of other Collection to Specified Index of Java Vector
30.  Iterate through elements Java Vector using Iterator
31.  Iterate through elements Java Vector using ListIterator
32.  Remove all elements from Java Vector
33.  Remove an element from specified index of Java Vector
34.  Remove specified element from Java Vector
35.  Replace an element at specified index of Java Vector
36.  Search an element of Java Vector
37.  Search an element of Java Vector from specific index
38.  Set size of Java Vector Example
39.  Sort elements of Java Vector
40.  Generic Vector with String
41.  Count distinct elements in a Vector
42.  Unmodifiable Vector Adapter
