---
title: Generic pair structure
nav: Generic pair structure
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20111003201306/http://java2s.com:80/Code/Java/Generics/Genericpairstructure.htm
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
 * @version 1.00 2004-05-10
 * @author Cay Horstmann
 */
public class PairTest1
{
   public static void main(String[] args)
   {
      String[] words = { "Mary", "had", "a", "little", "lamb" };
      Pair<String> mm = ArrayAlg.minmax(words);
      System.out.println("min = " + mm.getFirst());
      System.out.println("max = " + mm.getSecond());
   }
}
class ArrayAlg
{
   /**
    * Gets the minimum and maximum of an array of strings.
    * @param a an array of strings
    * @return a pair with the min and max value, or null if a is null or empty
    */
   public static Pair<String> minmax(String[] a)
   {
      if (a == null || a.length == 0) return null;
      String min = a[0];
      String max = a[0];
      for (int i = 1; i < a.length; i++)
      {
         if (min.compareTo(a[i]) > 0) min = a[i];
         if (max.compareTo(a[i]) < 0) max = a[i];
      }
      return new Pair<String>(min, max);
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

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A simple generic class hierarchy.
5.  A nongeneric class can be the superclass of a generic subclass.
6.  Use the instanceof operator with a generic class hierarchy.
7.  Java hierarchy generic class
8.  Custom Generic Object Tester
9.  Pair of template arguments
10.  Simple STL Pair Implementation
