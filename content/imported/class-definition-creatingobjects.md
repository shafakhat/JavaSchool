---
title: Creating Objects
nav: Creating Objects
description: Using the new keyword. new is always followed by the constructor of the class.
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20140829080907/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/CreatingObjects.htm
---
Using the new keyword. new is always followed by the constructor of the class.
For example, to create an Employee object, you write:

```java title=Example.java
Employee employee = new Employee();
```

| Here, 'employee' is an object reference of type Employee. |
|---|
| Once you have an object, you can call its methods and access its fields, by using the object reference. You use a period (.) to call a method or a field. |
| For example: |

```java title=Example.java
objectReference.methodName
objectReference.fieldName
```

The following code, for instance, creates an Employee object and assigns values to its age and salary fields:

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Employee employee = new Employee();
    employee.age = 24;
    employee.salary = 50000;
  }
}
class Employee {
    public int age;
    public double salary;
    public Employee() {
    }
    public Employee(int ageValue, double salaryValue) {
        age = ageValue;
        salary = salaryValue;
    }
}
```

When an object is created, the JVM also performs initialization that assign default values to fields.
