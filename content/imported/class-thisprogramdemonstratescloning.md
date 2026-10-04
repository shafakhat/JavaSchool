---
title: This program demonstrates cloning
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20111014030743/http://www.java2s.com:80/Code/Java/Class/Thisprogramdemonstratescloning.htm
---
This program demonstrates cloning

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
 * This program demonstrates cloning.
 * @version 1.10 2002-07-01
 * @author Cay Horstmann
 */
public class CloneTest
{
   public static void main(String[] args)
   {
      try
      {
         Employee original = new Employee("John Q. Public", 50000);
         original.setHireDay(2000, 1, 1);
         Employee copy = original.clone();
         copy.raiseSalary(10);
         copy.setHireDay(2002, 12, 31);
         System.out.println("original=" + original);
         System.out.println("copy=" + copy);
      }
      catch (CloneNotSupportedException e)
      {
         e.printStackTrace();
      }
   }
}
class Employee implements Cloneable
{
   public Employee(String n, double s)
   {
      name = n;
      salary = s;
      hireDay = new Date();
   }
   public Employee clone() throws CloneNotSupportedException
   {
      // call Object.clone()
      Employee cloned = (Employee) super.clone();
      // clone mutable fields
      cloned.hireDay = (Date) hireDay.clone();
      return cloned;
   }
   /**
    * Set the hire day to a given date.
    * @param year the year of the hire day
    * @param month the month of the hire day
    * @param day the day of the hire day
    */
   public void setHireDay(int year, int month, int day)
   {
      Date newHireDay = new GregorianCalendar(year, month - 1, day).getTime();
      // Example of instance field mutation
      hireDay.setTime(newHireDay.getTime());
   }
   public void raiseSalary(double byPercent)
   {
      double raise = salary * byPercent / 100;
      salary += raise;
   }
   public String toString()
   {
      return "Employee[name=" + name + ",salary=" + salary + ",hireDay=" + hireDay + "]";
   }
   private String name;
   private double salary;
   private Date hireDay;
}
```

1.  A Cloning Example
---  ---
2.  Class is declared to be cloneable.
3.  Arrays are automatically cloneable
4.  Clone objects
5.  Creating a Deep Copy
6.  Shallow Copy Test
7.  Deep Copy Test
8.  Uses serialization to perform deep copy cloning.
9.  Tests cloning to see if destination of references are also cloned
10.  Creating local copies with clone
11.  You can insert Cloneability at any level of inheritance
12.  Cloning a composed object
13.  Serializable and clone
14.  Go through a few gyrations to add cloning to your own class
15.  Checking to see if a reference can be cloned
16.  The clone operation works for only a few items in the standard Java library
17.  Demonstration of cloning
18.  Simple demo of avoiding side-effects by using Object.clone
19.  Clone an object with clone method from parent
20.  Manipulate properties after clone operation
21.  Deep clone Object
22.  Serializable Clone
23.  Utility for object cloning
24.  Clone Via Serialization
25.  Clone demo
26.  Deep clone serializing/de-serializng Clone
27.  Implements a pool of internalized objects
28.  A collection of utilities to workaround limitations of Java clone framework
29.  Returns a copy of the object, or null if the object cannot be serialized.
30.  Deep-copies the values from one object to the other
31.  Object Deep copy
