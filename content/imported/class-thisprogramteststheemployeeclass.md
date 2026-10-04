---
title: This program tests the Employee class
nav: This program tests the Emp...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20111023000025/http://www.java2s.com:80/Code/Java/Class/ThisprogramteststheEmployeeclass.htm
---
This program tests the Employee class

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
import java.util.Date;
import java.util.GregorianCalendar;
/**
 * This program tests the Employee class.
 *
 * @version 1.11 2004-02-19
 * @author Cay Horstmann
 */
public class EmployeeTest {
  public static void main(String[] args) {
    // fill the staff array with three Employee objects
    Employee[] staff = new Employee[3];
    staff[0] = new Employee("Carl Cracker", 75000, 1987, 12, 15);
    staff[1] = new Employee("Harry Hacker", 50000, 1989, 10, 1);
    staff[2] = new Employee("Tony Tester", 40000, 1990, 3, 15);
    // raise everyone's salary by 5%
    for (Employee e : staff)
      e.raiseSalary(5);
    // print out information about all Employee objects
    for (Employee e : staff)
      System.out.println("name=" + e.getName() + ",salary=" + e.getSalary() + ",hireDay="
          + e.getHireDay());
  }
}
class Employee {
  public Employee(String n, double s, int year, int month, int day) {
    name = n;
    salary = s;
    GregorianCalendar calendar = new GregorianCalendar(year, month - 1, day);
    // GregorianCalendar uses 0 for January
    hireDay = calendar.getTime();
  }
  public String getName() {
    return name;
  }
  public double getSalary() {
    return salary;
  }
  public Date getHireDay() {
    return hireDay;
  }
  public void raiseSalary(double byPercent) {
    double raise = salary * byPercent / 100;
    salary += raise;
  }
  private String name;
  private double salary;
  private Date hireDay;
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
8.  This program demonstrates object construction
