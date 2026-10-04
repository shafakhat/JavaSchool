---
title: Java Design Patterns Tutorial - Java Design Pattern - Data Access Object Pattern
nav: Java Design Patterns Tutor...
description: Data Access Object Pattern or DAO pattern separates data accessing API from high level business services.
section: Imported - java2s Archive
order: 50136
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0400__Java_Data_Access_Object_Pattern.html
---
```java title=Example.java
« Previous
```

Data Access Object Pattern or DAO pattern separates data accessing API from high level business services.

A DAO pattern usually has the following interface and classes.

- Data Access Object Interface defines the standard operations on a model object(s).
- Data Access Object class implements above interface. There could be more than one implementations, for example, one for database, one for file.
- Model Object Simple POJO containing get/set methods to store data.

## Example

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
//www.java2s.comclass Employee {
  private String name;
  privateint id;
  Employee(String name, int id) {
    this.name = name;
    this.id = id;
  }
  public String getName() {
    return name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  publicint getId() {
    return id;
  }
  publicvoid setId(int id) {
    this.id = id;
  }
}
interface EmployeeDao {
  public List<Employee> getAll();
  public Employee get(int id);
  publicvoid updateStudent(Employee student);
  publicvoid delete(Employee student);
}
class EmployeeDaoImpl implements EmployeeDao {
  List<Employee> employeeList;
  public EmployeeDaoImpl() {
    employeeList = new ArrayList<Employee>();
    Employee emp1 = new Employee("Jack", 0);
    Employee emp2 = new Employee("Tom", 1);
    employeeList.add(emp1);
    employeeList.add(emp2);
  }
  @Override
  publicvoid delete(Employee student) {
    employeeList.remove(student.getId());
    System.out.println("Employee: No " + student.getId()
        + ", deleted from database");
  }
  @Override
  public List<Employee> getAll() {
    return employeeList;
  }
  @Override
  public Employee get(int rollNo) {
    return employeeList.get(rollNo);
  }
  @Override
  publicvoid updateStudent(Employee emp) {
    employeeList.get(emp.getId()).setName(emp.getName());
    System.out.println("Emp:No " + emp.getId()
        + ", updated in the database");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    EmployeeDao empDao = new EmployeeDaoImpl();
    for (Employee emp : empDao.getAll()) {
      System.out.println("Emp: [No : " + emp.getId() + ", Name : "
          + emp.getName() + " ]");
    }
    Employee emp = empDao.getAll().get(0);
    emp.setName("Jane");
    empDao.updateStudent(emp);
    empDao.get(0);
    System.out.println("Emp: [No : " + emp.getId() + ", Name : "
        + emp.getName() + " ]");
  }
}
```

The code above generates the following result.

- « Previous
