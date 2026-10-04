---
title: Return an implementation of a Comparable
nav: Return an implementation o...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20111010005733/http://java2s.com:80/Code/Java/Generics/ReturnanimplementationofaComparable.htm
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
import java.util.Calendar;
import java.util.GregorianCalendar;
/**
 * @version 1.00 2004-05-10
 * @author Cay Horstmann
 */
public class PairTest2
{
   public static void main(String[] args)
   {
      GregorianCalendar[] birthdays =
         {
            new GregorianCalendar(1906, Calendar.DECEMBER, 9), // G. Hopper
            new GregorianCalendar(1815, Calendar.DECEMBER, 10), // A. Lovelace
            new GregorianCalendar(1903, Calendar.DECEMBER, 3), // J. von Neumann
            new GregorianCalendar(1910, Calendar.JUNE, 22), // K. Zuse
         };
      Pair<GregorianCalendar> mm = ArrayAlg.minmax(birthdays);
      System.out.println("min = " + mm.getFirst().getTime());
      System.out.println("max = " + mm.getSecond().getTime());
   }
}
class ArrayAlg
{
   /**
      Gets the minimum and maximum of an array of objects of type T.
      @param a an array of objects of type T
      @return a pair with the min and max value, or null if a is
      null or empty
   */
   public static <T extends Comparable> Pair<T> minmax(T[] a)
   {
      if (a == null || a.length == 0) return null;
      T min = a[0];
      T max = a[0];
      for (int i = 1; i < a.length; i++)
      {
         if (min.compareTo(a[i]) > 0) min = a[i];
         if (max.compareTo(a[i]) < 0) max = a[i];
      }
      return new Pair<T>(min, max);
   }
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
6.  Generic structure with constraints
