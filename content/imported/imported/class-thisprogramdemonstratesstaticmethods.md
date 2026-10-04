---
title: This program demonstrates static methods
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1088
source: https://web.archive.org/web/20111125063925/http://java2s.com/Code/Java/Class/Thisprogramdemonstratesstaticmethods.htm
---
```java title=Example.java
/*
 This program is a part of the companion code for Core Java 8th ed.
 (http://horstmann.com/corejava)
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
/**
 *
 * @version 1.01 2004-02-19
 * @author Cay Horstmann
 */
public class StaticTest {
  public static void main(String[] args) {
    // fill the staff array with three Employee objects
    Employee[] staff = new Employee[3];
    staff[0] = new Employee("Tom", 40000);
    staff[1] = new Employee("Dick", 60000);
    staff[2] = new Employee("Harry", 65000);
    // print out information about all Employee objects
    for (Employee e : staff) {
      e.setId();
      System.out.println("name=" + e.getName() + ",id=" + e.getId() + ",salary=" + e.getSalary());
    }
    int n = Employee.getNextId(); // calls static method
    System.out.println("Next available id=" + n);
  }
}
class Employee {
  public Employee(String n, double s) {
    name = n;
    salary = s;
    id = 0;
  }
  public String getName() {
    return name;
  }
  public double getSalary() {
    return salary;
  }
  public int getId() {
    return id;
  }
  public void setId() {
    id = nextId; // set id to next available id
    nextId++;
  }
  public static int getNextId() {
    return nextId; // returns static field
  }
  public static void main(String[] args) // unit test
  {
    Employee e = new Employee("Harry", 50000);
    System.out.println(e.getName() + " " + e.getSalary());
  }
  private String name;
  private double salary;
  private int id;
  private static int nextId = 1;
}
```

1.  Java static member variable example
---  ---
2.  Java static method
3.  Using Static Variables
4.  Static Init Demo
5.  Show that you do inherit static fields
6.  Show that you can't have static variables in a method
7.  Explicit static initialization with the static clause
8.  Static field, constructor and exception
