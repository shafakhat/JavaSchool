---
title: Java Collection Tutorial - Java Set
nav: Java Collection Tutorial -...
description: A set represents a collection of unique objects. The ordering of elements in a set is irrelevant.
section: Imported - java2s Archive
order: 50331
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0100__Java_Set.html
---
A set represents a collection of unique objects. The ordering of elements in a set is irrelevant.

The Collections Framework offers three types of sets:

- Mathematical set
- Sorted set
- Navigable set

## Mathematical Set

The Set interface models a set in mathematics. A set is a collection of unique elements.

Java allows at most one null element in a Set. The ordering of the elements in a Set is not important.

Java does not guarantee the ordering of the elements in a Set.

When looping through all elements of a Set, you get each element in the Set once.

The Collections Framework provides the HashSet class as an implementation for the Set interface.

The following code shows how to create a Set and add elements to it. When adding duplicate elements to a Set and they are ignored silently.

Two elements in a Set are considered equal if comparing them using the equals() method returns true.

```java title=Example.java
import java.util.HashSet;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Set<String> s1 = new HashSet<>();
    // Add a few elements
    s1.add("HTML");
    s1.add("CSS");
    s1.add("XML");
    s1.add("XML"); // Duplicate
// Create another set by copying s1
    Set<String> s2 = new HashSet<>(s1);
    // Add a few more elements
    s2.add("Java");
    s2.add("SQL");
    s2.add(null); // one null is fine
    s2.add(null); // Duplicate
    System.out.println("s1: " + s1);
    System.out.println("s1.size(): " + s1.size());
    System.out.println("s2: " + s2);
    System.out.println("s2.size(): " + s2.size());
  }
}
```

The code above generates the following result.

HashSet Method Reference

## LinkedHashSet

The Collections Framework offers the LinkedHashSet class as another implementation class for the Set interface.

The HashSet does not guarantee the ordering of elements during iteration. LinkedHashSet keeps the element order as the elements were inserted.

```java title=Example.java
import java.util.LinkedHashSet;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Set<String> s1 = new LinkedHashSet<>();
    s1.add("A");
    s1.add("B");
    s1.add("C");
    s1.add("D");
    System.out.println("LinkedHashSet: " + s1);
  }
}
```

The code above generates the following result.

LinkedHashSet Method Reference

## Set Operation

We can perform union, intersection, and difference operations on sets.

```java title=Example.java
// Union  of  s1  and  s2  will be  stored in s1
s1.add(s2);
// Intersection of  s1  and  s2  will be  stored in s1
s1.retainAll(s2);
// Difference of  s1  and  s2  will be  stored in s1
s1.removeAll(s2);
```

During the set operations, the s1 is modified. To keep the original set unchanged, make a copy before the operation:

```java title=Example.java
Set  s1Unions2  = new HashSet(s1); // Make a  copy  of  s1
s1Unions2.addAll(s2);
```

To test if a set s1 is a subset of another set s2, use the s2.containsAll(s1) method.

```java title=Example.java
import java.util.HashSet;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Set<String> s1 = new HashSet<>();
    s1.add("HTML");
    s1.add("CSS");
    s1.add("XML");
    Set<String> s2 = new HashSet<>();
    s2.add("Java");
    s2.add("Javascript");
    s2.add("CSS");
    System.out.println("s1: " + s1);
    System.out.println("s2: " + s2);
    performUnion(s1, s2);
    performIntersection(s1, s2);
    performDifference(s1, s2);
    testForSubset(s1, s2);
  }
  publicstaticvoid performUnion(Set<String> s1, Set<String> s2) {
    Set<String> s1Unions2 = new HashSet<>(s1);
    s1Unions2.addAll(s2);
    System.out.println("s1 union  s2: " + s1Unions2);
  }
  publicstaticvoid performIntersection(Set<String> s1, Set<String> s2) {
    Set<String> s1Intersections2 = new HashSet<>(s1);
    s1Intersections2.retainAll(s2);
    System.out.println("s1 intersection  s2: " + s1Intersections2);
  }
  publicstaticvoid performDifference(Set<String> s1, Set<String> s2) {
    Set<String> s1Differences2 = new HashSet<>(s1);
    s1Differences2.removeAll(s2);
    Set<String> s2Differences1 = new HashSet<>(s2);
    s2Differences1.removeAll(s1);
    System.out.println("s1 difference s2: " + s1Differences2);
    System.out.println("s2 difference s1: " + s2Differences1);
  }
  publicstaticvoid testForSubset(Set<String> s1, Set<String> s2) {
    System.out.println("s2 is  subset s1: " + s1.containsAll(s2));
    System.out.println("s1 is  subset s2: " + s2.containsAll(s1));
  }
}
```

The code above generates the following result.

- « Previous
