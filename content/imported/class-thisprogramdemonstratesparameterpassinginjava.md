---
title: This program demonstrates parameter passing in Java
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20111125103302/http://java2s.com/Code/Java/Class/ThisprogramdemonstratesparameterpassinginJava.htm
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
 * @version 1.00 2000-01-27
 * @author Cay Horstmann
 */
public class ParamTest {
  public static void main(String[] args) {
    /*
     * Test 1: Methods can't modify numeric parameters
     */
    System.out.println("Testing tripleValue:");
    double percent = 10;
    System.out.println("Before: percent=" + percent);
    tripleValue(percent);
    System.out.println("After: percent=" + percent);
    /*
     * Test 2: Methods can change the state of object parameters
     */
    System.out.println("\nTesting tripleSalary:");
    Employee harry = new Employee("Harry", 50000);
    System.out.println("Before: salary=" + harry.getSalary());
    tripleSalary(harry);
    System.out.println("After: salary=" + harry.getSalary());
    /*
     * Test 3: Methods can't attach new objects to object parameters
     */
    System.out.println("\nTesting swap:");
    Employee a = new Employee("Alice", 70000);
    Employee b = new Employee("Bob", 60000);
    System.out.println("Before: a=" + a.getName());
    System.out.println("Before: b=" + b.getName());
    swap(a, b);
    System.out.println("After: a=" + a.getName());
    System.out.println("After: b=" + b.getName());
  }
  public static void tripleValue(double x) // doesn't work
  {
    x = 3 * x;
    System.out.println("End of method: x=" + x);
  }
  public static void tripleSalary(Employee x) // works
  {
    x.raiseSalary(200);
    System.out.println("End of method: salary=" + x.getSalary());
  }
  public static void swap(Employee x, Employee y) {
    Employee temp = x;
    x = y;
    y = temp;
    System.out.println("End of method: x=" + x.getName());
    System.out.println("End of method: y=" + y.getName());
  }
}
class Employee // simplified Employee class
{
  public Employee(String n, double s) {
    name = n;
    salary = s;
  }
  public String getName() {
    return name;
  }
  public double getSalary() {
    return salary;
  }
  public void raiseSalary(double byPercent) {
    double raise = salary * byPercent / 100;
    salary += raise;
  }
  private String name;
  private double salary;
}
```

1.  Show a class that has a method and a field with the same name
