---
title: Java Collection Tutorial - Java Collections Algorithms
nav: Java Collection Tutorial -...
description: We can also use sort(Comparator c) in the List interface to sort a List without using the Collections class.
section: Imported - java2s Archive
order: 50342
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0400__Java_Collections_Algorithms.html
---
```java title=Example.java
« Previous
```

- Next »

## Sort a List

Two static methods in the Collections class sorts List.

- sort(List list) sorts the elements in a List in the order defined by the Comparable interface that is implemented by the elements.
- sort(List list, Comparator c) sorts the elements with a Comparator object passed in.

We can also use sort(Comparator c) in the List interface to sort a List without using the Collections class.

The following code demonstrates how to sort a List:

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("J");
    list.add("R");
    list.add("C");
    list.add("X");
    System.out.println("List: " + list);
    // Uses Comparable implementation in String class
// to sort the list in natural order
    Collections.sort(list);
    System.out.println("Sorted List:  " + list);
  }
}
```

The code above generates the following result.

## Example

The following code sorts the list in ascending order of the length of their elements using the sort() method in the List interface:

```java title=Example.java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("R");
    list.add("CSS");
    list.add("XML");
    System.out.println("List: " + list);
    // Uses List.sort() method with a Comparator
    list.sort(Comparator.comparing(String::length));
    System.out.println("Sorted List:  " + list);
  }
}
```

The code above generates the following result.

The sort() method uses a modified mergesort algorithm which is a stable sort.

In a stable sort the equal elements will stay at their current positions after the sort operation.

Sorting gives n*log(n) performance, where n is the number of elements in the List.

## Search a List

Two static binarySearch() method in the Collections class search for a key in a List.

This method uses the binary search algorithm to perform the search.

```java title=Example.java

int  binarySearch(List list,  T  key)
int  binarySearch(List list, T  key, Comparator c)
```

A List must be sorted in ascending order before we can use the binarySearch() method.

If the key is found in the List, the method returns its index in the List.

If the key is not found in the list, it returns (-(insertion_index) -1), where the Math.abs((-(insertion_index) -1)) is the index where we can insert this key still keep the list in order.

The return is a negative value when the key is not found in the List.

The following snippet of code shows how to use this method:

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("R");
    list.add("CSS");
    list.add("XML");
    Collections.sort(list);
    System.out.println("List: " + list);
    int index = Collections.binarySearch(list, "CSS");
    System.out.println("CSS in List  is at " + index);
    index = Collections.binarySearch(list, "Javascript");
    System.out.println("Javascript in List is  at " + index);
  }
}
```

The code above generates the following result.

Since "Javascript" is not in the List, the binary search returned -3. It means that if you insert "Javascript" in the List, it will be inserted at index 2, which is computed using the expression (-(-2+1)).

## Shuffle a List

Shuffling gives us a random permutation of the elements in a List.

The two versions of the shuffle() methods from Collections class are as follows:

```java title=Example.java

void  shuffle(List list)
void  shuffle(List list, Random  rnd)
```

The following code shows how to use the shuffle methods.

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("R");
    list.add("CSS");
    list.add("XML");
    Collections.sort(list);
    System.out.println("List: " + list);
    Collections.shuffle(list);
    System.out.println("List: " + list);
    Collections.shuffle(list);
    System.out.println("List: " + list);
  }
}
```

The code above generates the following result.

## Reverse List

We can use the reverse() static method of the Collections class to reverse elements in a List.

```java title=Example.java

void  reverse(List list)
```

The following code shows how to use the reverse() method.

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("R");
    list.add("CSS");
    list.add("XML");
    Collections.sort(list);
    System.out.println("List: " + list);
    Collections.reverse(list);
    System.out.println("List: " + list);
  }
}
```

The code above generates the following result.

## Swap List Items

Swapping swaps two elements in a List.

The swap() static method of the Collections class does the swapping.

```java title=Example.java

void  swap(List list, int i, int j)
```

i and j are indexes of two elements and they must be between 0 and size - 1, where size is the size of the List.

The following code shows how to reorder elements of a List using these methods.

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("R");
    list.add("CSS");
    list.add("XML");
    Collections.sort(list);
    System.out.println("List: " + list);
    // Swap elements at indexes 1 and 3
    Collections.swap(list, 1, 3);
    System.out.println(list);
  }
}
```

The code above generates the following result.

## Rotate a List

```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("R");
    list.add("CSS");
    list.add("XML");
    Collections.sort(list);
    System.out.println("List: " + list);
    // Rotate elements by 2
    Collections.rotate(list, 2);
    System.out.println("After  Rotating by  2: " + list);
  }
}
```

The code above generates the following result.

## Creating Different Views of a Collection

We can create a LIFO Queue view of a Deque using the asLifoQueue() static method of the Collections class:

```java title=Example.java

<T> Queue<T> asLifoQueue(Deque<T>  deque)
```

To use a Map's implementation as a Set implementation, use the newSetFromMap() static method of the Collections class:

```java title=Example.java

<E> Set<E> newSetFromMap(Map<E, Boolean>  map)
```

## Read-Only Views of Collections

We can get a read-only view of a collection when passing around collection to other methods and we do not want the called method to modify your collection.

The Collections class offers the following methods to get read-only views of different types of collections:

```java title=Example.java

<T> Collection<T> unmodifiableCollection(Collection<?  extends T> c)
<T> List<T>  unmodifiableList(List<?  extends T> list)
<K,V> Map<K,V>  unmodifiableMap(Map<?  extends K,?  extends V>  m)
<K,V> NavigableMap<K,V> unmodifiableNavigableMap(NavigableMap<K,? extends  V>  m)
<T> Set<T> unmodifiableSet(Set<? extends T> s)
<T> NavigableSet<T> unmodifiableNavigableSet(NavigableSet<T>  s)
static <T> SortedSet<T> unmodifiableSortedSet(SortedSet<T>  s)
<K,V> SortedMap<K,V> unmodifiableSortedMap(SortedMap<K,? extends  V>  m)
```

We pass a collection of a specific type and get a read-only collection of the same type.

## Synchronized View of a Collection

We can get a synchronized view of a collection using one of the following static methods of the Collections class.

```java title=Example.java

<T> Collection<T> synchronizedCollection(Collection<T>  c)
<T> List<T>  synchronizedList(List<T> list)
<K,V> Map<K,V>  synchronizedMap(Map<K,V> m)
<K,V> NavigableMap<K,V> synchronizedNavigableMap(NavigableMap<K,V> m)
<T> NavigableSet<T> synchronizedNavigableSet(NavigableSet<T>  s)
<T> Set<T> synchronizedSet(Set<T> s)
<T> SortedSet<T> synchronizedSortedSet(SortedSet<T>  s)
<K,V> SortedMap<K,V> synchronizedSortedMap (SortedMap<K,V> m)
```

## Checked Collections

Generics provide compile-time type-safety for collections.

The following code has a compile-time error since we are trying to add Integer type value to a Set which can only have String value.

```java title=Example.java

Set<String> s = new HashSet<>();
s.add("Hello");
a.add(new Integer(1)); // A compile-time error
```

We can bypass the compiler check by using the following code:

```java title=Example.java

Set<String> s = new HashSet<  >();
s.add("Hello");
Set s2 = s;
s2.add(new Integer(123)); // No  runtime exception
```

We can avoid the above error by using the checked collections. The following static methods of the Collections class returns a checked collection of a specific type:

```java title=Example.java

<E> Collection<E> checkedCollection(Collection<E>  c, Class<E>  type)
<E> List<E>  checkedList(List<E> list, Class<E>  type)
<K,V> Map<K,V> checkedMap(Map<K,V>   m, Class<K> keyType,  Class<V> valueType)
<K,V> NavigableMap<K,V> checkedNavigableMap(NavigableMap<K,V>  m, Class<K> keyType,  Class<V> valueType)
<E> NavigableSet<E> checkedNavigableSet(NavigableSet<E>  s, Class<E>  type)
<E> Queue<E> checkedQueue(Queue<E> queue, Class<E>  type)
<E> Set<E> checkedSet(Set<E> s, Class<E>  type)
<K,V> SortedMap<K,V> checkedSortedMap(SortedMap<K,V>  m, Class<K> keyType, Class<V> valueType)
<E> SortedSet<E> checkedSortedSet(SortedSet<E>  s, Class<E>  type)
```

The following code rewrite the code above.

```java title=Example.java

Set<String>  checkedSet = Collections.checkedSet(new HashSet<String>(),  String.class);
Set s2 = checkedSet;
s2.add(new Integer(1)); // Throws ClassCastException
```

## Creating Empty Collections

The Collections class can return an immutable empty collection object of each type.

It can also return an empty Iterator. The following code lists such static methods in the Collections class:

```java title=Example.java

<T> List<T>  emptyList()
<K,V> Map<K,V>  emptyMap()
<T> Set<T> emptySet()
<T> Iterator<T> emptyIterator()
<T> ListIterator<T> emptyListIterator()
```

## Singleton Collections

We can create a collection that has one and only one element using Collections class.

We have to create this kind of collection object when a method accepts a collection as its argument and we have only one object to pass to that method.

Those methods are as follows:

```java title=Example.java

<T> Set<T> singleton(T o)
<T> List<T>  singletonList(T o)
<K,V> Map<K,V>  singletonMap(K key,  V  value)
```

The following code shows how to use Collections.singleton() method.

```java title=Example.java

Set<String> singletonSet  = Collections.singleton("Lonely");
// Throws a  runtime exception since a singleton set is immutable singletonSet.add("Hello");
```

- Next »
- « Previous
