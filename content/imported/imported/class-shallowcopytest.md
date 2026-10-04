---
title: Shallow Copy Test
nav: Shallow Copy Test
description: System.out.println("Original (orginal values): " + p.getName() + " - "
section: Imported - java2s Archive
order: 1068
source: https://web.archive.org/web/20081009143506/http://www.java2s.com:80/Code/Java/Class/ShallowCopyTest.htm
---
Shallow Copy Test

```java title=Example.java
/*
Software Architecture Design Patterns in Java
by Partha Kuchana
Auerbach Publications
*/
class Person implements Cloneable {
  //Lower-level object
  private Car car;
  private String name;
  public Car getCar() {
    return car;
  }
  public String getName() {
    return name;
  }
  public void setName(String s) {
    name = s;
  }
  public Person(String s, String t) {
    name = s;
    car = new Car(t);
  }
  public Object clone() {
    //shallow copy
    try {
      return super.clone();
    } catch (CloneNotSupportedException e) {
      return null;
    }
  }
}
class Car {
  private String name;
  public String getName() {
    return name;
  }
  public void setName(String s) {
    name = s;
  }
  public Car(String s) {
    name = s;
  }
}
public class ShallowCopyTest {
  public static void main(String[] args) {
    //Original Object
    Person p = new Person("Person-A", "Civic");
    System.out.println("Original (orginal values): " + p.getName() + " - "
        + p.getCar().getName());
    //Clone as a shallow copy
    Person q = (Person) p.clone();
    System.out.println("Clone (before change): " + q.getName() + " - "
        + q.getCar().getName());
    //change the primitive member
    q.setName("Person-B");
    //change the lower-level object
    q.getCar().setName("Accord");
    System.out.println("Clone (after change): " + q.getName() + " - "
        + q.getCar().getName());
    System.out.println("Original (after clone is modified): " + p.getName()
        + " - " + p.getCar().getName());
  }
}
```

1.  A Cloning Example
---  ---
2.  Creating a Deep Copy
3.  Deep Copy Test
4.  Tests cloning to see if destination of references are also cloned
5.  Creating local copies with clone
6.  You can insert Cloneability at any level of inheritance
7.  Cloning a composed object
8.  Serializable and clone
9.  Go through a few gyrations to add cloning to your own class
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
