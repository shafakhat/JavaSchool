---
title: This program demonstrates abstract classes
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1082
source: https://web.archive.org/web/20111010001304/http://java2s.com:80/Code/Java/Class/Thisprogramdemonstratesabstractclasses.htm
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
import java.util.Date;
import java.util.GregorianCalendar;
/**
 * @version 1.01 2004-02-21
 * @author Cay Horstmann
 */
public class PersonTest
{
   public static void main(String[] args)
   {
      Person[] people = new Person[2];
      // fill the people array with Student and Employee objects
      people[0] = new Employee("Harry Hacker", 50000, 1989, 10, 1);
      people[1] = new Student("Maria Morris", "computer science");
      // print out names and descriptions of all Person objects
      for (Person p : people)
         System.out.println(p.getName() + ", " + p.getDescription());
   }
}
abstract class Person
{
   public Person(String n)
   {
      name = n;
   }
   public abstract String getDescription();
   public String getName()
   {
      return name;
   }
   private String name;
}
class Employee extends Person
{
   public Employee(String n, double s, int year, int month, int day)
   {
      super(n);
      salary = s;
      GregorianCalendar calendar = new GregorianCalendar(year, month - 1, day);
      hireDay = calendar.getTime();
   }
   public double getSalary()
   {
      return salary;
   }
   public Date getHireDay()
   {
      return hireDay;
   }
   public String getDescription()
   {
      return String.format("an employee with a salary of $%.2f", salary);
   }
   public void raiseSalary(double byPercent)
   {
      double raise = salary * byPercent / 100;
      salary += raise;
   }
   private double salary;
   private Date hireDay;
}
class Student extends Person
{
   /**
    * @param n the student's name
    * @param m the student's major
    */
   public Student(String n, String m)
   {
      // pass n to superclass constructor
      super(n);
      major = m;
   }
   public String getDescription()
   {
      return "a student majoring in " + major;
   }
   private String major;
}
```

1.  Can you call a static method of an abstract class
