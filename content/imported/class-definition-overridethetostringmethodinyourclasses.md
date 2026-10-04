---
title: override the toString method in your classes
nav: override the toString meth...
description: return "Employee[" + this.firstName + " " + this.lastName + "]";
section: Imported - java2s Archive
order: 1151
source: https://web.archive.org/web/20140829081321/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/overridethetoStringmethodinyourclasses.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Employee emp = new Employee("Martinez", "Anthony");
    System.out.println(emp.toString());
  }
}
class Employee {
  private String lastName;
  private String firstName;
  public Employee(String lastName, String firstName) {
    this.lastName = lastName;
    this.firstName = firstName;
  }
  public String toString() {
    return "Employee[" + this.firstName + " " + this.lastName + "]";
  }
}
```

| 5.32.1. | Override toString() for Box class. |
|---|---|
| 5.32.2. | override the toString method in your classes |
| 5.32.3. | Use Reflection To build toString method |
| 5.32.4. | Reflection based toString() utilities |
| 5.32.5. | Use a generic toString() |
| 5.32.6. | Jakarta Commons toString Builder |
