---
title: Manipulate properties after clone operation
nav: Manipulate properties afte...
description: System.out.println("The employees's pay is " + e.getSalary());
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20100212194957/http://java2s.com/Code/Java/Class/Manipulatepropertiesaftercloneoperation.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    try {
      Employee e = new Employee("B", 1000);
      System.out.println(e);
      System.out.println("The employee's name is " + e.getName());
      System.out.println("The employees's pay is " + e.getSalary());
      Employee eClone = (Employee) e.clone();
      System.out.println(eClone);
      System.out.println("The clone's name is " + eClone.getName());
      System.out.println("The clones's pay is " + eClone.getSalary());
      eClone.setName("A");
      eClone.setSalary(2000);
      System.out.println("The employee's name is " + e.getName());
      System.out.println("The employees's pay is " + e.getSalary());
      System.out.println("The clone's name is " + eClone.getName());
      System.out.println("The clones's pay is " + eClone.getSalary());
    } catch (Exception e) {
      System.out.println("Exception " + e);
    }
  }
}
class Employee implements Cloneable {
  private StringBuffer name;
  private int salary;
  public Employee(String name, int salary) {
    this.name = new StringBuffer(name);
    this.salary = salary;
  }
  public Employee() {
  }
  public Object clone() throws CloneNotSupportedException {
    try {
      Employee o = (Employee) super.clone();
      o.name = new StringBuffer(name.toString());
      return o;
    } catch (CloneNotSupportedException cnse) {
      System.out.println("CloneNotSupportedException thrown " + cnse);
      throw new CloneNotSupportedException();
    }
  }
  public String getName() {
    return name.toString();
  }
  public void setName(String name) {
    this.name.delete(0, this.name.length());
    this.name.append(name);
  }
  public void setSalary(int salary) {
    this.salary = salary;
  }
  public int getSalary() {
    return this.salary;
  }
}
```

1.  A Cloning Example
---  ---
2.  Class is declared to be cloneable.
3.  Arrays are automatically cloneable
4.  Clone objects
5.  Creating a Deep Copy
6.  Shallow Copy Test
7.  Deep Copy Test
8.  Uses serialization to perform deep copy cloning.
9.  Tests cloning to see if destination of references are also cloned
10.  Creating local copies with clone
11.  You can insert Cloneability at any level of inheritance
12.  Cloning a composed object
13.  Serializable and clone
14.  Go through a few gyrations to add cloning to your own class
15.  Checking to see if a reference can be cloned
16.  The clone operation works for only a few items in the standard Java library
17.  Demonstration of cloning
18.  Simple demo of avoiding side-effects by using Object.clone
19.  Clone an object with clone method from parent
20.  Deep clone Object
21.  Serializable Clone
22.  Utility for object cloning
23.  Clone Via Serialization
24.  Clone demo
25.  Deep clone serializing/de-serializng Clone
26.  Implements a pool of internalized objects
27.  A collection of utilities to workaround limitations of Java clone framework
