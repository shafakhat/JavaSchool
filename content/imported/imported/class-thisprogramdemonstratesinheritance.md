---
title: This program demonstrates inheritance
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1085
source: https://web.archive.org/web/20111124232313/http://java2s.com/Code/Java/Class/Thisprogramdemonstratesinheritance.htm
---
This program demonstrates inheritance

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
 * This program demonstrates inheritance.
 *
 * @version 1.21 2004-02-21
 * @author Cay Horstmann
 */
public class ManagerTest {
  public static void main(String[] args) {
    // construct a Manager object
    Manager boss = new Manager("Carl Cracker", 80000, 1987, 12, 15);
    boss.setBonus(5000);
    Employee[] staff = new Employee[3];
    // fill the staff array with Manager and Employee objects
    staff[0] = boss;
    staff[1] = new Employee("Harry Hacker", 50000, 1989, 10, 1);
    staff[2] = new Employee("Tommy Tester", 40000, 1990, 3, 15);
    // print out information about all Employee objects
    for (Employee e : staff)
      System.out.println("name=" + e.getName() + ",salary=" + e.getSalary());
  }
}
class Employee {
  public Employee(String n, double s, int year, int month, int day) {
    name = n;
    salary = s;
    GregorianCalendar calendar = new GregorianCalendar(year, month - 1, day);
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
class Manager extends Employee {
  /**
   * @param n
   *          the employee's name
   * @param s
   *          the salary
   * @param year
   *          the hire year
   * @param month
   *          the hire month
   * @param day
   *          the hire day
   */
  public Manager(String n, double s, int year, int month, int day) {
    super(n, s, year, month, day);
    bonus = 0;
  }
  public double getSalary() {
    double baseSalary = super.getSalary();
    return baseSalary + bonus;
  }
  public void setBonus(double b) {
    bonus = b;
  }
  private double bonus;
}
```

1.  Subclass definition
