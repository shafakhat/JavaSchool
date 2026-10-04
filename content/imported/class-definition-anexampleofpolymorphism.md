---
title: An example of polymorphism
nav: An example of polymorphism
description: Imported from the java2s.com archive: An example of polymorphism
section: Imported - java2s Archive
order: 1198
source: https://web.archive.org/web/20140215092803/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Anexampleofpolymorphism.htm
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

| 5.24.1. | Polymorphism |
|---|---|
| 5.24.2. | An example of polymorphism |
| 5.24.3. | Downcasting and Run-Time Type Identification (RTTI) |
| 5.24.4. | Constructors and polymorphism don't produce what you might expect |
| 5.24.5. | Dynamic Method Dispatch |
| 5.24.6. | Using run-time polymorphism. |
