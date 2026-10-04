---
title: Manipulate properties after clone operation
nav: Manipulate properties afte...
description: System.out.println("The employees's pay is " + e.getSalary());
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20101107122933/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Manipulatepropertiesaftercloneoperation.htm
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
