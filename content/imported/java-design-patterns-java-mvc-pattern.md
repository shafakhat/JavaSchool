---
title: Java Design Patterns Tutorial - Java Design Pattern - MVC Pattern
nav: Java Design Patterns Tutor...
description: From the name we can see that the MVC pattern involves three parts:
section: Imported - java2s Archive
order: 50135
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0300__Java_MVC_Pattern.html
---
```java title=Example.java
```

MVC Pattern stands for Model-View-Controller Pattern.

From the name we can see that the MVC pattern involves three parts:

- Model - Model represents an object carrying data. It can also have logic to update controller if its data changes.
- View - View represents the visualization of the data that model contains. Usually it has the UI logic.
- Controller - Controller references both Model and view. It controls the data flow into model object and updates the view whenever data changes. It keeps View and Model separate.

## Example

```java title=Example.java
class Employee {private String id;
  private String name;
  public String getId() {
    return id;
  }
  publicvoid setId(String id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
}
class EmployeeView {
  publicvoid printEmployeeDetails(String name, String no) {
    System.out.println("Employee: ");
    System.out.println("Name: " + name);
    System.out.println("ID: " + no);
  }
}
class EmployeeController {
  private Employee model;
  private EmployeeView view;
  public EmployeeController(Employee model, EmployeeView view) {
    this.model = model;
    this.view = view;
  }
  publicvoid setEmployeeName(String name) {
    model.setName(name);
  }
  public String getEmployeeName() {
    return model.getName();
  }
  publicvoid setEmployeeId(String rollNo) {
    model.setId(rollNo);
  }
  public String getEmployeeId() {
    return model.getId();
  }
  publicvoid updateView() {
    view.printEmployeeDetails(model.getName(), model.getId());
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Employee model = new Employee();
    model.setName("Tom");
    model.setId("1");
    EmployeeView view = new EmployeeView();
    EmployeeController controller = new EmployeeController(model, view);
    controller.updateView();
    controller.setEmployeeName("New Name");
    controller.updateView();
  }
}
```

The code above generates the following result.

- « Previous
