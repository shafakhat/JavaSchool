---
title: Clone objects
nav: Clone objects
description: System.out.println("Person 1: " + person1.getFirstName() + " " + person1.getLastName());
section: Imported - java2s Archive
order: 1142
source: https://web.archive.org/web/20090531211836/http://www.java2s.com:80/Code/Java/Class/Cloneobjects.htm
---
Clone objects

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Person person1 = new Person();
    person1.setFirstName("F");
    person1.setLastName("L");
    Person person2 = (Person) person1.clone();
    Person person3 = (Person) person2.clone();
    System.out.println("Person 1: " + person1.getFirstName() + " " + person1.getLastName());
    System.out.println("Person 2: " + person2.getFirstName() + " " + person2.getLastName());
    System.out.println("Person 3: " + person3.getFirstName() + " " + person3.getLastName());
  }
}
class Person implements Cloneable {
  private String firstName;
  private String lastName;
  public Object clone() {
    Person obj = new Person();
    obj.setFirstName(this.firstName);
    obj.setLastName(this.lastName);
    return obj;
  }
  public String getFirstName() {
    return firstName;
  }
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }
  public String getLastName() {
    return lastName;
  }
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }
}
/*
Person 1: F L
Person 2: F L
Person 3: F L
*/
```

1.  A Cloning Example
---  ---
2.  Class is declared to be cloneable.
3.  Arrays are automatically cloneable
4.  Creating a Deep Copy
5.  Shallow Copy Test
6.  Deep Copy Test
7.  Uses serialization to perform deep copy cloning.
8.  Tests cloning to see if destination of references are also cloned
9.  Creating local copies with clone
10.  You can insert Cloneability at any level of inheritance
11.  Cloning a composed object
12.  Serializable and clone
13.  Go through a few gyrations to add cloning to your own class
14.  Checking to see if a reference can be cloned
15.  The clone operation works for only a few items in the standard Java library
16.  Demonstration of cloning
17.  Simple demo of avoiding side-effects by using Object.clone
18.  Clone an object with clone method from parent
19.  Manipulate properties after clone operation
20.  Clone demo
