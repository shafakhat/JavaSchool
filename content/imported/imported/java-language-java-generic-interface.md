---
title: Java Tutorial - How to use Java generic interface
nav: Java Tutorial - How to use...
description: type-param-list is a comma-separated list of type parameters. When a generic interface is implemented, you must specify the type arguments, as shown here:
section: Imported - java2s Archive
order: 50459
source: https://www.java2s.com/Tutorials/Java/Java_Language/8020__Java_generic_interface.html
---
```java title=Example.java
```

In Java we create generic interface.

## Syntax

Here is the generalized syntax for a generic interface:

```java title=Example.java
interfaceinterface-name<type-param-list> { // ...
```

type-param-list is a comma-separated list of type parameters. When a generic interface is implemented, you must specify the type arguments, as shown here:

```java title=Example.java
classclass-name<type-param-list>
   implementsinterface-name<type-arg-list> {
```

## Note

In general, if a class implements a generic interface, then that class must also be generic. If a class implements a specific type of generic interface, such as shown here:

```java title=Example.java
class MyClass implements MinMax<Integer> { // OK
```

then the implementing class does not need to be generic.

Generic interfaces are specified like generic classes.

## Example

```java title=Example.java
interface MinMax<T extends Comparable<T>> {
  T max();//fromwww.java2s.com
}
class MyClass<T extends Comparable<T>> implements MinMax<T> {
  T[] vals;
  MyClass(T[] o) {
    vals = o;
  }
  public T max() {
    T v = vals[0];
    for (int i = 1; i < vals.length; i++) {
      if (vals[i].compareTo(v) > 0) {
        v = vals[i];
      }
    }
    return v;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Integer inums[] = { 3, 6, 2, 8, 6 };
    Character chs[] = { 'b', 'r', 'p', 'w' };
    MyClass<Integer> a = new MyClass<Integer>(inums);
    MyClass<Character> b = new MyClass<Character>(chs);
    System.out.println(a.max());
    System.out.println(b.max());
  }
}
```

The code above generates the following result.

- « Previous
