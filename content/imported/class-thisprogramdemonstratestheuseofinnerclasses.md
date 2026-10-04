---
title: This program demonstrates the use of inner classes
nav: This program demonstrates ...
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20111102081958/http://www.java2s.com:80/Code/Java/Class/Thisprogramdemonstratestheuseofinnerclasses.htm
---
This program demonstrates the use of inner classes

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
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import javax.swing.JOptionPane;
import javax.swing.Timer;
/**
 * This program demonstrates the use of inner classes.
 * @version 1.10 2004-02-27
 * @author Cay Horstmann
 */
public class InnerClassTest
{
   public static void main(String[] args)
   {
      TalkingClock clock = new TalkingClock(1000, true);
      clock.start();
      // keep program running until user selects "Ok"
      JOptionPane.showMessageDialog(null, "Quit program?");
      System.exit(0);
   }
}
/**
 * A clock that prints the time in regular intervals.
 */
class TalkingClock
{
   /**
    * Constructs a talking clock
    * @param interval the interval between messages (in milliseconds)
    * @param beep true if the clock should beep
    */
   public TalkingClock(int interval, boolean beep)
   {
      this.interval = interval;
      this.beep = beep;
   }
   /**
    * Starts the clock.
    */
   public void start()
   {
      ActionListener listener = new TimePrinter();
      Timer t = new Timer(interval, listener);
      t.start();
   }
   private int interval;
   private boolean beep;
   public class TimePrinter implements ActionListener
   {
      public void actionPerformed(ActionEvent event)
      {
         Date now = new Date();
         System.out.println("At the tone, the time is " + now);
         if (beep) Toolkit.getDefaultToolkit().beep();
      }
   }
}
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
4.  Returning a reference to an inner class
5.  Nesting a class within a scope
6.  Putting test code in a nested class
7.  Inheriting an inner class
8.  Creating a constructor for an anonymous inner class
9.  This file is to show what happens if you try to access an inner class created in another class
10.  Demonstrate an Inner Child class
11.  Demonstrate simple inner class
12.  Just to show that there is no such thing as inner methods in Java
13.  A named inner class is used to
14.  An inner class cannot be overriden like a method
15.  Proper inheritance of an inner class
16.  Using inner classes for callbacks
17.  Holds a sequence of Objects
18.  With concrete or abstract classes, inner classes are the only way to produce the effect
19.  Nested Class Static
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
21.  Accessing its enclosing instance from an inner class
22.  This program demonstrates the use of local inner classes
23.  This program demonstrates the use of static inner classes
