---
title: Java Design Patterns Tutorial - Java Design Pattern - Composite Pattern
nav: Java Design Patterns Tutor...
description: Composite pattern is structural pattern since it creates a tree structure of group of objects.
section: Imported - java2s Archive
order: 50120
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0090__Java_Composite_Pattern.html
---
Composite pattern is structural pattern since it creates a tree structure of group of objects.

Composite pattern treats a group of objects as a single object.

Composite pattern uses one class to represent a tree structure.

In Composite pattern we create a class contains group of its own objects.

## Example

The following code uses the Employee class to demonstrate the Composite pattern.

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
class Employee {
   private String name;
   private String title;
   private List<Employee> subordinates;
   public Employee(String name,String title) {
      this.name = name;
      this.title = title;
      subordinates = new ArrayList<Employee>();
   }
   publicvoid add(Employee e) {
      subordinates.add(e);
   }
   publicvoid remove(Employee e) {
      subordinates.remove(e);
   }
   public List<Employee> getSubordinates(){
     return subordinates;
   }
   public String toString(){
      return"Employee :[ Name : "+ name
      +", dept : "+ title +subordinates +" ]";
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      Employee CEO = new Employee("John","CEO");
      Employee headSales = new Employee("Rob","Sales");
      Employee headMarketing = new Employee("Mike","Marketing");
      Employee programmer1 = new Employee("Lili","Programmer");
      Employee programmer2 = new Employee("Bob","Programmer");
      Employee tester1 = new Employee("Jack","Tester");
      Employee tester2 = new Employee("Tom","Tester");
      CEO.add(headSales);
      CEO.add(headMarketing);
      headSales.add(tester1);
      headSales.add(tester2);
      headMarketing.add(programmer1);
      headMarketing.add(programmer2);
      //print all employees of the organization
      System.out.println(CEO);
      for (Employee headEmployee : CEO.getSubordinates()) {
         System.out.println(headEmployee);
         for (Employee employee : headEmployee.getSubordinates()) {
            System.out.println(employee);
         }
      }
   }
}
```

The code above generates the following result.

- « Previous
