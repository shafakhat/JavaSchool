---
title: An example of polymorphism
nav: An example of polymorphism
description: Imported from the java2s.com archive: An example of polymorphism
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Anexampleofpolymorphism.htm
---
```java title=Example.java
class Employee {
  publicvoid work() {
    System.out.println("I am an employee.");
  }
}
class Manager extends Employee {
  publicvoid work() {
    System.out.println("I am a manager.");
  }
  publicvoid manage() {
    System.out.println("Managing ...");
  }
}
publicclass PolymorphismTest1 {
  publicstaticvoid main(String[] args) {
    Employee employee;
    employee = new Manager();
    System.out.println(employee.getClass().getName());
    employee.work();
    Manager manager = (Manager) employee;
    manager.manage();
  }
}
```
