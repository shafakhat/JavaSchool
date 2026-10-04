---
title: An example of polymorphism
nav: An example of polymorphism
description: Imported from the java2s.com archive: An example of polymorphism
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Anexampleofpolymorphism.htm
---
```java title=Example.java
class Employee {
  public void work() {
    System.out.println("I am an employee.");
  }
}
class Manager extends Employee {
  public void work() {
    System.out.println("I am a manager.");
  }
  public void manage() {
    System.out.println("Managing ...");
  }
}
public class PolymorphismTest1 {
  public static void main(String[] args) {
    Employee employee;
    employee = new Manager();
    System.out.println(employee.getClass().getName());
    employee.work();
    Manager manager = (Manager) employee;
    manager.manage();
  }
}
```
