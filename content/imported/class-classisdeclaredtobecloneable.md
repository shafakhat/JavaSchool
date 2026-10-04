---
title: Class is declared to be cloneable.
nav: Class is declared to be cl...
description: System.out.println("CloneNotSupportedException thrown " + cnse);
section: Imported - java2s Archive
order: 1138
source: https://web.archive.org/web/20090531214952/http://www.java2s.com:80/Code/Java/Class/Classisdeclaredtobecloneable.htm
---
```java title=Example.java
class Employee implements Cloneable {
  String name;
  int salary;
  public Employee(String name, int salary) {
    this.name = name;
    this.salary = salary;
  }
  public Employee() {
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public void setSalary(int salary) {
    this.salary = salary;
  }
  public int getSalary() {
    return this.salary;
  }
  public Object clone() throws CloneNotSupportedException {
    try {
      return super.clone();
    } catch (CloneNotSupportedException cnse) {
      System.out.println("CloneNotSupportedException thrown " + cnse);
      throw new CloneNotSupportedException();
    }
  }
}
public class Main {
  public static void main(String[] args) {
    try {
      Employee e = new Employee("Dolly", 1000);
      System.out.println(e);
      System.out.println("The employee's name is " + e.getName());
      System.out.println("The employees's pay is " + e.getSalary());
      Employee eClone = (Employee) e.clone();
      System.out.println(eClone);
      System.out.println("The clone's name is " + eClone.getName());
      System.out.println("The clones's pay is " + eClone.getSalary());
    } catch (CloneNotSupportedException cnse) {
      System.out.println("Clone not supported");
    }
  }
}
```

1.  A Cloning Example
---  ---
2.  Arrays are automatically cloneable
3.  Clone objects
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
