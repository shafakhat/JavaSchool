---
title: A Cloning Example
nav: A Cloning Example
description: return this.getClass().getName() + "[" + this.firstName + " " + this.lastName + ", "
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/20081009024409/http://www.java2s.com:80/Code/Java/Class/ACloningExample.htm
---
A Cloning Example

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Employee emp1 = new Employee("M", "A");
    emp1.setSalary(40000.0);
    Employee emp2 = (Employee) emp1.clone();
    emp1.setLastName("Smith");
    System.out.println(emp1);
    System.out.println(emp2);
  }
}
class Employee {
  private String lastName;
  private String firstName;
  private Double salary;
  public Employee(String lastName, String firstName) {
    this.lastName = lastName;
    this.firstName = firstName;
  }
  public String getLastName() {
    return this.lastName;
  }
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }
  public String getFirstName() {
    return this.firstName;
  }
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }
  public Double getSalary() {
    return this.salary;
  }
  public void setSalary(Double salary) {
    this.salary = salary;
  }
  public Object clone() {
    Employee emp;
    emp = new Employee(this.lastName, this.firstName);
    emp.setSalary(this.salary);
    return emp;
  }
  public String toString() {
    return this.getClass().getName() + "[" + this.firstName + " " + this.lastName + ", "
        + this.salary + "]";
  }
}
```

1.  Creating a Deep Copy
---  ---
2.  Shallow Copy Test
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
