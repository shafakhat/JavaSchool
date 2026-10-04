---
title: Creating a Deep Copy
nav: Creating a Deep Copy
description: emp1.address = new Address("First Street", "San F", "CA", "93702");
section: Imported - java2s Archive
order: 1157
source: https://web.archive.org/web/20081009150825/http://www.java2s.com:80/Code/Java/Class/CreatingaDeepCopy.htm
---
Creating a Deep Copy

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Employee emp1 = new Employee("M", "A");
    emp1.setSalary(40000.0);
    emp1.address = new Address("First Street", "San F", "CA", "93702");
    Employee emp2 = (Employee) emp1.clone();
    printEmployee(emp1);
    printEmployee(emp2);
    emp2.setLastName("Smith");
    emp2.address = new Address("Street", "B", "CA", "93722");
    printEmployee(emp1);
    printEmployee(emp2);
  }
  private static void printEmployee(Employee e) {
    System.out.println(e.getFirstName() + " " + e.getLastName());
    System.out.println(e.address.getAddress());
    System.out.println("Salary: " + e.getSalary());
  }
}
class Employee implements Cloneable {
  private String lastName;
  private String firstName;
  private Double salary;
  public Address address;
  public Employee(String lastName, String firstName) {
    this.lastName = lastName;
    this.firstName = firstName;
    this.address = new Address();
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
    try {
      emp = (Employee) super.clone();
      emp.address = (Address) address.clone();
    } catch (CloneNotSupportedException e) {
      return null; // will never happen
    }
    return emp;
  }
  public String toString() {
    return this.getClass().getName() + "[" + this.firstName + " " + this.lastName + ", "
        + this.salary + "]";
  }
}
class Address implements Cloneable {
  private String street;
  private String city;
  private String state;
  private String zipCode;
  public Address() {
    this.street = "";
    this.city = "";
    this.state = "";
    this.zipCode = "";
  }
  public Address(String street, String city, String state, String zipCode) {
    this.street = street;
    this.city = city;
    this.state = state;
    this.zipCode = zipCode;
  }
  public Object clone(){
    try {
      return super.clone();
    } catch (CloneNotSupportedException e) {
      return null; // will never happen
    }
  }
  public String getAddress() {
    return this.street + "\n" + this.city + ", " + this.state + " " + this.zipCode;
  }
}
```

1.  A Cloning Example
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
