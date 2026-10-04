---
title: Generic structure with constraints
nav: Generic structure with con...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20111010003058/http://java2s.com:80/Code/Java/Generics/Genericstructurewithconstraints.htm
---
Generic structure with constraints

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
 * @version 1.00 2004-05-10
 * @author Cay Horstmann
 */
public class PairTest3
{
   public static void main(String[] args)
   {
      Manager ceo = new Manager("Gus Greedy", 800000, 2003, 12, 15);
      Manager cfo = new Manager("Sid Sneaky", 600000, 2003, 12, 15);
      Pair<Manager> buddies = new Pair<Manager>(ceo, cfo);
      printBuddies(buddies);
      ceo.setBonus(1000000);
      cfo.setBonus(500000);
      Manager[] managers = { ceo, cfo };
      Pair<Employee> result = new Pair<Employee>();
      minmaxBonus(managers, result);
      System.out.println("first: " + result.getFirst().getName()
         + ", second: " + result.getSecond().getName());
      maxminBonus(managers, result);
      System.out.println("first: " + result.getFirst().getName()
         + ", second: " + result.getSecond().getName());
   }
   public static void printBuddies(Pair<? extends Employee> p)
   {
      Employee first = p.getFirst();
      Employee second = p.getSecond();
      System.out.println(first.getName() + " and " + second.getName() + " are buddies.");
   }
   public static void minmaxBonus(Manager[] a, Pair<? super Manager> result)
   {
      if (a == null || a.length == 0) return;
      Manager min = a[0];
      Manager max = a[0];
      for (int i = 1; i < a.length; i++)
      {
         if (min.getBonus() > a[i].getBonus()) min = a[i];
         if (max.getBonus() < a[i].getBonus()) max = a[i];
      }
      result.setFirst(min);
      result.setSecond(max);
   }
   public static void maxminBonus(Manager[] a, Pair<? super Manager> result)
   {
      minmaxBonus(a, result);
      PairAlg.swapHelper(result); // OK--swapHelper captures wildcard type
   }
}
class PairAlg
{
   public static boolean hasNulls(Pair<?> p)
   {
      return p.getFirst() == null || p.getSecond() == null;
   }
   public static void swap(Pair<?> p) { swapHelper(p); }
   public static <T> void swapHelper(Pair<T> p)
   {
      T t = p.getFirst();
      p.setFirst(p.getSecond());
      p.setSecond(t);
   }
}
class Employee
{
   public Employee(String n, double s, int year, int month, int day)
   {
      name = n;
      salary = s;
      GregorianCalendar calendar = new GregorianCalendar(year, month - 1, day);
      hireDay = calendar.getTime();
   }
   public String getName()
   {
      return name;
   }
   public double getSalary()
   {
      return salary;
   }
   public Date getHireDay()
   {
      return hireDay;
   }
   public void raiseSalary(double byPercent)
   {
      double raise = salary * byPercent / 100;
      salary += raise;
   }
   private String name;
   private double salary;
   private Date hireDay;
}
class Manager extends Employee
{
   /**
      @param n the employee's name
      @param s the salary
      @param year the hire year
      @param month the hire month
      @param day the hire day
   */
   public Manager(String n, double s, int year, int month, int day)
   {
      super(n, s, year, month, day);
      bonus = 0;
   }
   public double getSalary()
   {
      double baseSalary = super.getSalary();
      return baseSalary + bonus;
   }
   public void setBonus(double b)
   {
      bonus = b;
   }
   public double getBonus()
   {
      return bonus;
   }
   private double bonus;
}
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
 * @version 1.00 2004-05-10
 * @author Cay Horstmann
 */
 class Pair<T>
{
   public Pair() { first = null; second = null; }
   public Pair(T first, T second) { this.first = first;  this.second = second; }
   public T getFirst() { return first; }
   public T getSecond() { return second; }
   public void setFirst(T newValue) { first = newValue; }
   public void setSecond(T newValue) { second = newValue; }
   private T first;
   private T second;
}
```

1.  Java generic: Use a wildcard.
---  ---
2.  Java generic: Bounded Wildcard arguments
3.  Use a wildcard.
4.  Bounded Wildcard arguments.
5.  Generic cast
6.  Return an implementation of a Comparable
