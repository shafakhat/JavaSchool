---
title: Accessible Field Iterator
nav: Accessible Field Iterator
description: Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20111125090032/http://java2s.com/Code/Java/Reflection/AccessibleFieldIterator.htm
---
```java title=Example.java
/*
Copyright 2011 Karl-Michael Schneider
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
//package org.jwatter.util;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Set;
/**
 * An iterator over the fields that are accessible in a given class and any subclass of that class.
 * Any non private field declared in the given class is accessible in that class and its subclasses.
 * A field declared in a superclass of the given class is only accessible in that class and its
 * subclasses if it is not private and if it is not hidden by another field with the same name.
 * Synthetic fields are not returned by the iterator.
 *
 * Fields are returned beginning with the accessible fields declared in the given class, followed by
 * any accessible fields in the given class's superclass, and so on. Fields are returned in the
 * order in which they are declared within each class.
 */
public class AccessibleFieldIterator
        implements Iterator<Field> {
    protected Class<?> klass;
    protected Class<?> currentClass;
    protected LinkedList<Field> fieldQueue;
    protected AppendableIterator<Field> fieldQueueIterator;
    protected Set<String> visibleFieldNames;
    /**
     * Creates a new iterator that iterates over the fields that are accessible in the given class
     * and its subclasses.
     *
     * @param cls
     *        the class whose accessible fields the iterator will return.
     */
    public AccessibleFieldIterator (Class<?> cls) {
        this.klass = cls;
        this.currentClass = cls;
        this.fieldQueue = new LinkedList<Field>();
        this.fieldQueueIterator = new AppendableIterator<Field>(fieldQueue);
        this.visibleFieldNames = new HashSet<String>();
        this.addMoreFields();
    }
    /*
     * (non-Javadoc)
     *
     * @see java.util.Iterator#hasNext()
     */
    public boolean hasNext () {
        this.ensureMoreFields();
        return this.fieldQueueIterator.hasNext();
    }
    /*
     * (non-Javadoc)
     *
     * @see java.util.Iterator#next()
     */
    public Field next () {
        this.ensureMoreFields();
        return this.fieldQueueIterator.next();
    }
    /*
     * (non-Javadoc)
     *
     * @see java.util.Iterator#remove()
     */
    public void remove () {
        throw new UnsupportedOperationException("remove is not supported by this iterator");
    }
    protected void ensureMoreFields () {
        if (this.currentClass == null) {
            // all fields have been returned
            return;
        }
        if (this.fieldQueueIterator.hasNext()) {
            // there are still fields in the queue
            return;
        }
        // more fields exist, add them to the queue
        this.addMoreFields();
    }
    // search for accessible fields in the current class and add them to the queue
    // if the current class has no accessible fields, move up in the class hierarchy
    // until some fields are found or there is no more superclass
    protected void addMoreFields () {
        boolean needMoreFields = true;
        while (needMoreFields) {
            for (Field field : this.currentClass.getDeclaredFields()) {
                if (!(field.isSynthetic() || Modifier.isPrivate(field.getModifiers()) || this.visibleFieldNames
                                                                                                               .contains(field
                                                                                                                              .getName()))) {
                    try {
                        field.setAccessible(true);
                        this.fieldQueueIterator.add(field);
                        this.visibleFieldNames.add(field.getName());
                        needMoreFields = false;
                    }
                    catch (SecurityException e) {
                        // ignore fields that cannot be set accessible
                    }
                }
            }
            if (needMoreFields) {
                // found no accessible fields in the current class
                this.currentClass = this.currentClass.getSuperclass();
                if (this.currentClass == null) {
                    // no more fields
                    return;
                }
            }
        }
    }
}
/**
 * An iterator over a collection of elements that allows to add new elements to
 * it (and to the underlying collection). New elements are always appended to
 * the iteration sequence.
 *
 * Note that modifying the underlying collection externally (using any other
 * method than those provided by the iterator) does not affect the iterator.
 *
 * @author kschneider
 *
 */
class AppendableIterator<T> implements Iterator<T>
{
  protected Collection<T> elements;
  protected LinkedList<T> iteratorQueue;
  protected T last;
  protected boolean nextCalled;
  /**
   * Creates a new iterator, using a HashSet as the underlying set. Initially,
   * the underlying set is empty.
   */
  public AppendableIterator ()
  {
    this(new HashSet<T>());
  }
  /**
   * Creates a new iterator, using the specified collection as the underlying
   * collection. The iteration order of the elements that are present in the
   * collection at the time the iterator is created is the same as if
   * iterating over the collection.
   *
   * @param initialElements
   *            the underlying set for this iterator
   * @throws NullPointerException
   *             if the specified set is null
   */
  public AppendableIterator ( Collection<T> initialElements )
  {
    if ( initialElements == null )
    {
      throw new NullPointerException("underlying set must not be null");
    }
    elements = initialElements;
    iteratorQueue = new LinkedList<T>(initialElements);
    nextCalled = false;
  }
  /*
   * (non-Javadoc)
   *
   * @see java.util.Iterator#hasNext()
   */
  public boolean hasNext ()
  {
    return iteratorQueue.size() > 0;
  }
  /*
   * (non-Javadoc)
   *
   * @see java.util.Iterator#next()
   */
  public T next ()
  {
    if ( iteratorQueue.size() == 0 )
    {
      throw new NoSuchElementException("no more elements");
    }
    last = iteratorQueue.poll();
    nextCalled = true;
    return last;
  }
  /*
   * (non-Javadoc)
   *
   * @see java.util.Iterator#remove()
   */
  public void remove ()
  {
    if ( !nextCalled )
    {
      throw new IllegalStateException(
          "next() must be called before remove()");
    }
    nextCalled = false;
    elements.remove(last);
  }
  /**
   * Adds the specified element to this iterator and to the underlying
   * collection. The element is appended to the iteration sequence.
   *
   * @param e
   *            the element to add
   * @return true if the underlying collection has changed as a result of the
   *         call
   */
  public boolean add ( T e )
  {
    iteratorQueue.add(e);
    return elements.add(e);
  }
  /**
   * Adds the specified element to the underlying collection. If the
   * underlying collection changed as a result of the call, the element is
   * appended to the iteration sequence. Otherwise the iteration sequence is
   * not changed.
   *
   * In particular, if the underlying collection already contains the
   * specified element and does not permit duplicates, the iterator is not
   * changed.
   *
   * @param e
   *            the element to add
   * @return true if the underlying collection (and the iteration sequence)
   *         changed as a result of the call, else false
   */
  public boolean addNew ( T e )
  {
    if ( elements.add(e) )
    {
      iteratorQueue.add(e);
      return true;
    }
    else
    {
      return false;
    }
  }
  /**
   * Adds all elements in the specified collection to this iterator and to the
   * underlying collection. Elements are appended to the iteration sequence in
   * the order given when iterating over the specified collection.
   *
   * @param els
   *            the elements to add
   * @return true if the underlying collection changed as a result of the call
   */
  public boolean addAll ( Collection<T> els )
  {
    iteratorQueue.addAll(els);
    return elements.addAll(els);
  }
  /**
   * Adds each element from the specified collection to the underlying
   * collection. If the underlying collection changes as a result of adding an
   * element, the element is appended to the iteration sequence. Elements are
   * added in the order given when iterating over the specified collection.
   *
   * In particular, if the underlying collection does not permit duplicate
   * elements, only elements that are not already contained in the underlying
   * collection are added to the iterator.
   *
   * @param els
   *            the elements to add
   * @return true if any elements were added to the iterator, else false
   */
  public boolean addAllNew ( Collection<T> els )
  {
    boolean changed = false;
    for ( T e : els )
    {
      if ( addNew(e) ) changed = true;
    }
    return changed;
  }
  /**
   * Returns the underlying collection.
   *
   * @return the underlying collection
   */
  public Collection<T> getUnderlyingCollection ()
  {
    return elements;
  }
}
```

1.  Field Reflection
---  ---
2.  How to set public field objects
3.  Class Reflection: field information
4.  Object Reflection: get field value
5.  Object Reflection: set value
6.  Get field of a class object and set or get its value
7.  All Fields Snippet
8.  Field modifiers: isSynthetic, isEnumConstant
9.  Field with annotations
10.  Set private field value
11.  Get fields of a class object
12.  Get all object accessible public fields
13.  Getting the Field Objects of a Class Object: By obtaining a list of all declared fields.
14.  Getting the Field Objects of a Class Object: By obtaining a list of all public fields, both declared and inherited.
15.  Getting the Field Objects of a Class Object: By obtaining a particular Field object.
16.  Get all declared fields from a class
17.  Retrieving a Predefined Color by Name
18.  Get a variable value from the variable name
19.  Fetches all fields of all access types from the supplied class and super classes
20.  Checks whether the specified class contains a field matching the specified name.
21.  whether given field is a "public static final" constant
22.  Process bean properties getter by applying the JavaBean naming conventions.
23.  Fetches the property descriptor for the named property of the supplied class
24.  Find Field
25.  Return a list of all fields (whatever access status, and on whatever superclass they were defined) that can be found on this class.
26.  Get all fields of a class.
27.  Find field 2
28.  Get class field/property
29.  Adds all Fields (from Class.getFields) to the list
30.  Retrieve a value from a property
31.  Set the value of the field of the object to the given value.
32.  Fast Property accessor for a single class.
