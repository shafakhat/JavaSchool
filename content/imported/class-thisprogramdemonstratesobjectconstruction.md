---
title: This program demonstrates object construction
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1086
source: https://web.archive.org/web/20111023065227/http://www.java2s.com:80/Code/Java/Class/Thisprogramdemonstratesobjectconstruction.htm
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
import java.util.Random;
/**
 *
 * @version 1.01 2004-02-19
 * @author Cay Horstmann
 */
public class ConstructorTest {
  public static void main(String[] args) {
    // fill the staff array with three Employee objects
    Employee[] staff = new Employee[3];
    staff[0] = new Employee("Harry", 40000);
    staff[1] = new Employee(60000);
    staff[2] = new Employee();
    // print out information about all Employee objects
    for (Employee e : staff)
      System.out.println("name=" + e.getName() + ",id=" + e.getId() + ",salary=" + e.getSalary());
  }
}
class Employee {
  // three overloaded constructors
  public Employee(String n, double s) {
    name = n;
    salary = s;
  }
  public Employee(double s) {
    // calls the Employee(String, double) constructor
    this("Employee #" + nextId, s);
  }
  // the default constructor
  public Employee() {
    // name initialized to ""--see below
    // salary not explicitly set--initialized to 0
    // id initialized in initialization block
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
  private static int nextId;
  private int id;
  private String name = ""; // instance field initialization
  private double salary;
  // static initialization block
  static {
    Random generator = new Random();
    // set nextId to a random number between 0 and 9999
    nextId = generator.nextInt(10000);
  }
  // object initialization block
  {
    id = nextId;
    nextId++;
  }
}
```

1.  Create Object Demo
---  ---
2.  Passing objects to methods may not be what you're used to.
3.  Demonstrates Reference objects
4.  A companion class to modify immutable objects
5.  Objects that cannot be modified are immune to aliasing
6.  Examination of the way the class loader works
7.  A changeable wrapper class
8.  This program tests the Employee class
