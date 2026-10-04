---
title: Java Collection Tutorial - Java Sorted Set
nav: Java Collection Tutorial -...
description: SortedSet interface represents a sorted set in Java Collection Framework.
section: Imported - java2s Archive
order: 50332
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0110__Java_Sorted_Set.html
---
```java title=Example.java
```

A sorted set is a set with ordering on its elements.

SortedSet interface represents a sorted set in Java Collection Framework.

The elements in a SortedSet can be sorted in a natural order with Comparable interface or using a Comparator.

A SortedSet must know how to sort its elements as they are added by checking two interfaces:

- If its elements implement the Comparable interface, it will use the compareTo() method to sort items. We can call this as sorting in natural order.
- We can passin a Comparator to do custom sorting.

If a Comparator is specified, the Comparator is used for sorting and ignore the Comparable interface.

The TreeSet class is an implementation for the SortedSet interface in the Collections Framework.

TreeSet API

SortedSet API

## Example

In the following code we add String objects to the SortedSet.

The String class implements the Comparable interface.

SortedSet would use the Comparable interface and its the compareTo() method to sort the String values.

```java title=Example.java
import java.util.SortedSet;
import java.util.TreeSet;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a sorted set of some names
    SortedSet<String> sortedNames = new TreeSet<>();
    sortedNames.add("Java");
    sortedNames.add("SQL");
    sortedNames.add("HTML");
    sortedNames.add("CSS");
    // Print the sorted set of names
    System.out.println(sortedNames);
  }
}
```

The code above generates the following result.

## Example 2

The following code shows how to store a list of person objects in a SortedSet.

We cannot add an object of the Person class in a SortedSet unless we also supply a Comparator object since the Person class doesn't implement the Comparable interface.

The following code creates a SortedSet of persons using a Comparator that sorts the persons using their names:

```java title=Example.java
SortedSet<Person> personsSortedByName = new TreeSet<>(Comparator.comparing(Person::getName));
```

The code uses a method reference to create a lambda expression for creating the Comparator object.

```java title=Example.java
import java.util.Comparator;
import java.util.SortedSet;
import java.util.TreeSet;
publicclass Main {
  publicstaticvoid main(String[] args) {
    SortedSet<Person> personsById = new TreeSet<>(
        Comparator.comparing(Person::getId));
    personsById.add(new Person(1, "X"));
    personsById.add(new Person(2, "Z"));
    personsById.add(new Person(3, "A"));
    personsById.add(new Person(4, "C"));
    personsById.add(new Person(4, "S")); // A duplicate Person
    System.out.println("Persons by  Id:");
    personsById.forEach(System.out::println);
    SortedSet<Person> personsByName = new TreeSet<>(
        Comparator.comparing(Person::getName));
    personsByName.add(new Person(1, "X"));
    personsByName.add(new Person(2, "Z"));
    personsByName.add(new Person(3, "A"));
    personsByName.add(new Person(4, "C"));
    System.out.println("Persons by  Name: ");
    personsByName.forEach(System.out::println);
  }
}
class Person {
  privateint id;
  private String name;
  public Person(int id, String name) {
    this.id = id;
    this.name = name;
  }
  publicint getId() {
    return id;
  }
  publicvoid setId(int id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  @Override
  publicboolean equals(Object o) {
    if (!(o instanceof Person)) {
      return false;
    }
    // id must be the same for two Persons to be equal
    Person p = (Person) o;
    if (this.id == p.getId()) {
      return true;
    }
    return false;
  }
  @Override
  publicint hashCode() {
    return this.id;
  }
  @Override
  public String toString() {
    return"(" + id + ", " + name + ")";
  }
}
```

The code above generates the following result.

## Example 3

The SortedSet interface inherits all methods of the Set interface and it adds some more methods to return subsets.

subSet(E fromElement, E toElement) method from SortedSet returns the elements between fromElement(inclusive) and toElement(exclusive).

```java title=Example.java
import java.util.SortedSet;
import java.util.TreeSet;
publicclass Main {
  publicstaticvoid main(String[] args) {
    SortedSet<String> names = new TreeSet<>();
    names.add("HTML");
    names.add("Java");
    names.add("SQL");
    names.add("CSS");
    System.out.println("Sorted Set: " + names);
    System.out.println("First: " + names.first());
    System.out.println("Last: " + names.last());
    SortedSet<String> ssBeforeCSS = names.headSet("CSS");
    System.out.println(ssBeforeCSS);
    SortedSet<String> ssBetwenCSSAndHTML = names.subSet("CSS", "HTML");
    System.out.println(ssBetwenCSSAndHTML);
    SortedSet<String> ssBetwenCSSAndHTML2 = names.subSet("CSS", "HTML");
    System.out.println(ssBetwenCSSAndHTML2);
    SortedSet<String> ssCSSAndAfter = names.tailSet("CSS");
    System.out.println(ssCSSAndAfter);
  }
}
```

The code above generates the following result.

## Example 4

The following snippet of code creates a SortedSet using a Comparator that places the null element first:

```java title=Example.java
import java.util.Comparator;
import java.util.SortedSet;
import java.util.TreeSet;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Sort the names based on their length, placing null first
    SortedSet<String> names = new TreeSet<>(Comparator.nullsFirst(Comparator
        .comparing(String::length)));
    names.add("XML");
    names.add("CSS");
    names.add("HTML");
    names.add(null); // Adds a null
// Print the names
    names.forEach(System.out::println);
  }
}
```

The code above generates the following result.

- « Previous
