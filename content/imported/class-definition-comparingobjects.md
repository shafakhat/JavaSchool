---
title: Comparing Objects
nav: Comparing Objects
description: return this.lastName.equals(emp.getLastName()) && this.firstName.equals(emp.getFirstName());
section: Imported - java2s Archive
order: 1245
source: https://web.archive.org/web/20140829085528/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ComparingObjects.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Employee emp1 = new Employee("M", "A");
    Employee emp2 = new Employee("M", "A");
    if (emp1.equals(emp2))
      System.out.println("These employees are the same.");
    else
      System.out.println("These are different employees.");
  }
}
class Employee {
  private String lastName;
  private String firstName;
  public Employee(String lastName, String firstName) {
    this.lastName = lastName;
    this.firstName = firstName;
  }
  public String getLastName() {
    return this.lastName;
  }
  public String getFirstName() {
    return this.firstName;
  }
  public boolean equals(Object obj)
  {
    if (this == obj)
      return true;
    if (this == null)
      return false;
    if (this.getClass() != obj.getClass())
      return false;
    Employee emp = (Employee) obj;
    return this.lastName.equals(emp.getLastName()) && this.firstName.equals(emp.getFirstName());
  }
}
```
