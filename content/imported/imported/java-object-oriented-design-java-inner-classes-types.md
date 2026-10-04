---
title: Java Object Oriented Design - Java Inner Classes Types
nav: Java Object Oriented Desig...
description: You can define an inner class anywhere inside a class where you can write a Java statement.
section: Imported - java2s Archive
order: 50161
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0250__Java_Inner_Classes_Types.html
---
```java title=Example.java
```

You can define an inner class anywhere inside a class where you can write a Java statement.

There are three types of inner classes. The type of inner class depends on the location and the way it is declared.

- Member inner class
- Local inner class
- Anonymous inner class

## Member Inner Class

A member inner class is declared inside a class the same way a member field or a member method is declared.

It can be declared as public, private, protected, or package-level.

The instance of a member inner class may exist only within the instance of its enclosing class.

The following code creates a member inner class.

```java title=Example.java
class Car {//www.java2s.comprivateint year;
  // A member inner class named Tire public
class Tire {
    privatedouble radius;
    public Tire(double radius) {
      this.radius = radius;
    }
    publicdouble getRadius() {
      return radius;
    }
  } // Member inner class declaration ends here
// A constructor for the Car class
public Car(int year) {
    this.year = year;
  }
  publicint getYear() {
    return year;
  }
}
```

## Local Inner Class

A local inner class is declared inside a block. Its scope is limited to the block in which it is declared.

Since its scope is limited to its enclosing block, its declaration cannot use any access modifiers such as public, private, or protected.

Typically, a local inner class is defined inside a method. However, it can also be defined inside static initializers, non-static initializers, and constructors.

The following code shows an example of a local inner class.

```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    StringList tl = new StringList();
    tl.addTitle("A");
    tl.addTitle("B");
    Iterator iterator = tl.titleIterator();
    while (iterator.hasNext()) {
      System.out.println(iterator.next());
    }
  }
}
class StringList {
  private ArrayList<String> titleList = new ArrayList<>();
  publicvoid addTitle(String title) {
    titleList.add(title);
  }
  publicvoid removeTitle(String title) {
    titleList.remove(title);
  }
  public Iterator<String> titleIterator() {
    // A local inner class - TitleIterator
class TitleIterator implements Iterator<String> {
      int count = 0;
      @Override
      publicboolean hasNext() {
        return (count < titleList.size());
      }
      @Override
      public String next() {
        return titleList.get(count++);
      }
    }
    TitleIterator titleIterator = new TitleIterator();
    return titleIterator;
  }
}
```

The code above generates the following result.

## Example

The following code has a local inner class which inherits from another public class.

```java title=Example.java
import java.util.Random;
//fromwww.java2s.comabstractclass IntGenerator {
  publicabstractint getValue() ;
}
class LocalGen {
  public IntGenerator getRandomInteger() {
    class RandomIntegerLocal extends IntGenerator {
      @Override
      publicint getValue() {
        Random rand = new Random();
        long n1 = rand.nextInt();
        long n2 = rand.nextInt();
        int value = (int) ((n1 + n2) / 2);
        return value;
      }
    }
    returnnew RandomIntegerLocal();
  } // End of getRandomInteger() method
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    LocalGen local = new LocalGen();
    IntGenerator rLocal = local.getRandomInteger();
    System.out.println(rLocal.getValue());
    System.out.println(rLocal.getValue());
  }
}
```

The code above generates the following result.

## Anonymous Inner Class

An anonymous inner class does not have a name. Since it does not have a name, it cannot have a constructor.

An anonymous class is a one-time class. You define an anonymous class and create its object at the same time.

The general syntax for creating an anonymous class and its object is as follows:

```java title=Example.java
new Interface()  {
// Anonymous  class body  goes  here
}
```

and

```java title=Example.java
new Superclass(<argument-list-for-a-superclass-constructor>)  {
// Anonymous  class body  goes  here
}
```

The new operator is used to create an instance of the anonymous class.

It is followed by either an existing interface name or an existing class name.

The interface name or class name is not the name for the newly created anonymous class.

If an interface name is used, the anonymous class implements the interface.

If a class name is used, the anonymous class inherits from the class.

The <argument-list> is used only if the new operator is followed by a class name. It is left empty if the new operator is followed by an interface name.

If <argument-list> is present, it contains the actual parameter list for a constructor of the existing class to be invoked.

The anonymous class body is written as usual inside braces.

The anonymous class body should be short for better readability.

The following code contains a simple anonymous class, which prints a message on the standard output.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    new Object() {
      // An instance initializer
      {//www.java2s.com
        System.out.println("Hello from  an  anonymous class.");
      }
    }; // A semi-colon is necessary to end the statement
  }
}
```

The code above generates the following result.

## Example 2

The following code use an anonymous class to create an Iterator.

```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
/*fromwww.java2s.com*/publicclass Main {
  private ArrayList<String> titleList = new ArrayList<>();
  publicvoid addTitle(String title) {
    titleList.add(title);
  }
  publicvoid removeTitle(String title) {
    titleList.remove(title);
  }
  public Iterator<String> titleIterator() {
    // An anonymous class
    Iterator<String> iterator = new Iterator<String>() {
      int count = 0;
      @Override
      publicboolean hasNext() {
        return (count < titleList.size());
      }
      @Override
      public String next() {
        return titleList.get(count++);
      }
    }; // Anonymous inner class ends here
return iterator;
  }
}
```

- « Previous
