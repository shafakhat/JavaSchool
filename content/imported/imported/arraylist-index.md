---
title: Java Collection Tutorial - ArrayList Example
nav: Java Collection Tutorial -...
description: The following code shows how to get Size of ArrayList and loop through elements.
section: Imported - java2s Archive
order: 50344
source: https://www.java2s.com/Tutorials/Java/java.util/ArrayList/index.html
---
```java title=Example.java
« Previous
```

- Next »

## Example

The following code shows how to get Size of ArrayList and loop through elements.

```java title=Example.java
/*www.java2s.com*/import java.util.ArrayList;
publicclass Main {
  publicstaticvoid main(String[] args) {
    ArrayList<String> arrayList = new ArrayList<String>();
    arrayList.add("1");
    arrayList.add("2");
    arrayList.add("3");
    arrayList.add("java2s.com");
    int totalElements = arrayList.size();
    for (int index = 0; index < totalElements; index++)
      System.out.println(arrayList.get(index));
  }
}
```

The code above generates the following result.

## Example 2

The following code shows how to traverse through ArrayList in forward direction using ListIterator.

```java title=Example.java
//fromwww.java2s.comimport java.util.ArrayList;
import java.util.ListIterator;
publicclass Main {
  publicstaticvoid main(String[] args) {
    ArrayList<String> aList = new ArrayList<String>();
    aList.add("1");
    aList.add("2");
    aList.add("3");
    aList.add("4");
    aList.add("java2s.com");
    ListIterator listIterator = aList.listIterator();
    while (listIterator.hasNext()){
      System.out.println(listIterator.next());
    }
  }
}
```

The code above generates the following result.

## Example 3

The following code shows how to get the size of an arraylist after and before add and remove methods.

```java title=Example.java
//fromwww.java2s.comimport java.util.ArrayList;
publicclass Main {
  publicstaticvoid main(String args[]) {
    ArrayList<String> al = new ArrayList<String>();
    System.out.println("Initial size of al: " + al.size());
    al.add("C");
    al.add("A");
    al.add("E");
    al.add("B");
    al.add("D");
    al.add("F");
    al.add(1, "java2s.com");
    System.out.println("Size of al after additions: " + al.size());
    System.out.println("Contents of al: " + al);
    al.remove("F");
    al.remove(2);
    System.out.println("Size of al after deletions: " + al.size());
    System.out.println("Contents of al: " + al);
  }
}
```

The code above generates the following result.

## Example 4

The following code shows how to use set method to change the value in an array list.

```java title=Example.java
//fromwww.java2s.comimport java.util.ArrayList;
publicclass Main {
  publicstaticvoid main(String[] a) {
    ArrayList<String> nums = new ArrayList<String>();
    nums.clear();
    nums.add("One");
    nums.add("Two");
    nums.add("Three");
    System.out.println(nums);
    nums.set(0, "Uno");
    nums.set(1, "Dos");
    nums.set(2, "java2s.com");
    System.out.println(nums);
  }
}
```

The code above generates the following result.

## Constructor

- Java ArrayList() Constructor
- Java ArrayList(Collection c) Constructor
- Java ArrayList(int initialCapacity) Constructor

## Method

- Java ArrayList.add(E e)
- Java ArrayList.add(int index, E element)
- Java ArrayList.addAll(Collection c)
- Java ArrayList.addAll(int index, Collection c)
- Java ArrayList.clear()
- Java ArrayList.clone()
- Java ArrayList.contains(Object o)
- Java ArrayList.ensureCapacity(int minCapacity)
- Java ArrayList.get(int index)
- Java ArrayList.indexOf(Object o)
- Java ArrayList.isEmpty()
- Java ArrayList.iterator()
- Java ArrayList.lastIndexOf(Object o)
- Java ArrayList.listIterator()
- Java ArrayList.listIterator(int index)
- Java ArrayList.remove(int index)
- Java ArrayList.remove(Object o)
- Java ArrayList .removeAll ( Collection c)
- Java ArrayList.removeRange(int fromIndex, int toIndex)
- Java ArrayList .retainAll ( Collection c)
- Java ArrayList.set(int index, E element)
- Java ArrayList.size()
- Java ArrayList.subList(int fromIndex, int toIndex)
- Java ArrayList.toArray()
- Java ArrayList.toArray(T[] a)
- Java ArrayList.trimToSize()

- Next »
- « Previous
