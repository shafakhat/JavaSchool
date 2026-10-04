---
title: Java Tutorial - Java Nested Class
nav: Java Tutorial - Java Neste...
description: Classes that are declared outside of any class are top-level classes. Nested classes are classes declared as members of other classes or scopes.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Language/5060__Java_Nested_Class.html
---
Classes that are declared outside of any class are top-level classes. Nested classes are classes declared as members of other classes or scopes.

There are four kinds of nested classes:

- static member classes,
- nonstatic member classes,
- anonymous classes
- local classes.

## Java Anonymous Classes

An anonymous class is a class without a name and simultaneously declared. You can instantiate an anonymous class where it is legal to specify an expression.

An anonymous class instance can only access local final variables and final parameters.

How to define an anonymous class?

```java title=Example.java
abstract class People {
  abstract void speak();
}public class Main {
  public static void main(final String[] args) {
    new People() {
      String msg = "test";
      @Override
      void speak() {
        System.out.println(msg);
      }
    }.speak();
  }
}
```

The code above generates the following result.

## Example

The following code declares and instantiates an anonymous class that implements an interface.

```java title=Example.java
interface People {
  abstract void speak();
}public class Main {
  public static void main(final String[] args) {
    new People() {
      String msg = (args.length == 1) ? args[0] : "nothing to say";
      @Override
      public void speak() {
        System.out.println(msg);
      }
    }.speak();
  }
}
```

The code above generates the following result.

## Java Local Classes

A local class is a class that is declared anywhere that a local variable is declared. A local class has the same scope as a local variable.

A local class has a name and can be reused. A local class instance can access the surrounding scope's local final variables and final parameters.

Java Local Class

```java title=Example.java
class MyClass { void myMethod(final int x) {
    final int y = x;
    class LocalClass {
      int a = x;
      int b = y;
    }
    LocalClass lc = new LocalClass();
    System.out.println(lc.a);
    System.out.println(lc.b);
  }
}
public class Main {
  public static void main(String[] args) {
    MyClass ec = new MyClass();
    ec.myMethod(10);
  }
}
```

The code above generates the following result.

## Example 2

The following code declares an Iterator interface and Iter inner class.

```java title=Example.java
class Item{private String name;
  private String value;
  public Item(String n, String v){
    name = n;
    value = v;
  }
  public String toString(){
    return name + value;
  }
}
interface Iterator {
  boolean hasMoreElements();
  Object nextElement();
}
class ItemManager {
  private Item[] itemArray;
  private int index = 0;
  ItemManager(int size) {
    itemArray = new Item[size];
  }
  Iterator iterator() {
    class Iter implements Iterator {
      int index = 0;
      @Override
      public boolean hasMoreElements() {
        return index < itemArray.length;
      }
      @Override
      public Object nextElement() {
        return itemArray[index++];
      }
    }
    return new Iter();
  }
  void add(Item item) {
    itemArray[index++] = item;
  }
}
public class Main {
  public static void main(String[] args) {
    ItemManager itemManager = new ItemManager(5);
    itemManager.add(new Item("#1", "A"));
    itemManager.add(new Item("#2", "B"));
    itemManager.add(new Item("#3", "C"));
    Iterator iter = itemManager.iterator();
    while (iter.hasMoreElements()){
      System.out.println(iter.nextElement());
    }
  }
}
```

The output:

## Java Member Classes

A member class is a member of an enclosing class. Each instance of the member class associates with an instance of the enclosing class.

The member class's instance methods can call instance methods in the enclosing class and access the enclosing class instance's nonstatic fields.

The following code has one outer class named EnclosingClass and a nonstatic member class named EnclosedClass.

```java title=Example.java
class EnclosingClass {
  private int outerVariable;
 private void privateOuterMethod() {
    System.out.println(outerVariable);
  }
  class EnclosedClass {
    void accessEnclosingClass() {
      outerVariable = 1;
      privateOuterMethod();
    }
  }
}
public class Main {
  public static void main(String[] args) {
    EnclosingClass ec = new EnclosingClass();
    ec.new EnclosedClass().accessEnclosingClass(); // Output: 1
  }
}
```

The code above generates the following result.

## Example 3

The following code uses inner class ItemList to store the items.

```java title=Example.java
class Item { private String name;
  private String desc;
  Item(String name, String desc) {
    this.name = name;
    this.desc = desc;
  }
  String getName() {
    return name;
  }
  String getDesc() {
    return desc;
  }
  @Override
  public String toString() {
    return "Name = " + getName() + ", Desc = " + getDesc();
  }
}
class ItemManager {
  private ItemList itemList;
  private int index = 0;
  ItemManager() {
    itemList = new ItemList(2);
  }
  boolean hasMoreElements() {
    return index < itemList.size();
  }
  Item nextElement() {
    return itemList.get(index++);
  }
  void add(Item item) {
    itemList.add(item);
  }
  private class ItemList {
    private Item[] itemArray;
    private int index = 0;
    ItemList(int initSize) {
      itemArray = new Item[initSize];
    }
    void add(Item item) {
      if (index >= itemArray.length) {
        Item[] temp = new Item[itemArray.length * 2];
        for (int i = 0; i < itemArray.length; i++)
          temp[i] = itemArray[i];
        itemArray = temp;
      }
      itemArray[index++] = item;
    }
    Item get(int i) {
      return itemArray[i];
    }
    int size() {
      return index;
    }
  }
}
public class Main {
  public static void main(String[] args) {
    ItemManager itemManager = new ItemManager();
    itemManager.add(new Item("1", "A"));
    itemManager.add(new Item("2", "B"));
    itemManager.add(new Item("3", "C"));
    while (itemManager.hasMoreElements())
      System.out.println(itemManager.nextElement());
  }
}
```

The code above generates the following result.

## Example 4

The following program illustrates how to define and use an inner class.

```java title=Example.java
 class Outer {int outer_x = 100;
  void test() {
    Inner inner = new Inner();
    inner.display();
  }
  class Inner {
    void display() {
      System.out.println("display: outer_x = " + outer_x);
    }
  }
}
public class Main {
  public static void main(String args[]) {
    Outer outer = new Outer();
    outer.test();
  }
}
```

Output from this application is shown here:

## Example 5

The inner class members are accessible only within the inner class and may not be used by the outer class. If you try to compile the following code, you will get error message.

```java title=Example.java
 public class Main {
  int outer_x = 100;
  // this is an inner class
 class Inner {
    int y = 10; // y is local to Inner
 void display() {
      System.out.println("display: outer_x = " + outer_x);
    }
  }
  void showy() {
    System.out.println(y);
  }
}
```

When compiling the code above:

## Java Static Member Classes

A static member class is a static member of an enclosing class. A static member class cannot access the enclosing class's instance fields and invoke its instance methods.

A static member can access the enclosing class's static fields and invoke its static methods including private fields and methods.

The following code has a static member class declaration.

```java title=Example.java
class Demo {public static void main(String[] args) {
    Main.EnclosedClass.accessEnclosingClass();
    Main.EnclosedClass ec = new Main.EnclosedClass();
    ec.accessEnclosingClass2();
  }
}
class Main {
  private static int outerVariable;
  private static void privateStaticOuterMethod() {
    System.out.println(outerVariable);
  }
  static void staticOuterMethod() {
    EnclosedClass.accessEnclosingClass();
  }
  static class EnclosedClass {
    static void accessEnclosingClass() {
      outerVariable = 1;
      privateStaticOuterMethod();
    }
    void accessEnclosingClass2() {
      staticOuterMethod();
    }
  }
}
```

The static member classes can declare multiple implementations of their enclosing class.

## Example 6

The following code declares a Rectangle class and it uses static member class to provide Rectangle implementation for different data types, one is for double type and another is for float type.

```java title=Example.java
abstract class Rectangle {
  abstract double getX();
abstract double getY();
  abstract double getWidth();
  abstract double getHeight();
  static class Double extends Rectangle {
    private double x, y, width, height;
    Double(double x, double y, double width, double height) {
      this.x = x;
      this.y = y;
      this.width = width;
      this.height = height;
    }
    double getX() {
      return x;
    }
    double getY() {
      return y;
    }
    double getWidth() {
      return width;
    }
    double getHeight() {
      return height;
    }
  }
  static class Float extends Rectangle {
    private float x, y, width, height;
    Float(float x, float y, float width, float height) {
      this.x = x;
      this.y = y;
      this.width = width;
      this.height = height;
    }
    double getX() {
      return x;
    }
    double getY() {
      return y;
    }
    double getWidth() {
      return width;
    }
    double getHeight() {
      return height;
    }
  }
  private Rectangle() {
  }
  boolean contains(double x, double y) {
    return (x >= getX() && x < getX() + getWidth()) && (y >= getY() && y < getY() + getHeight());
  }
}
public class Main {
  public static void main(String[] args) {
    Rectangle r = new Rectangle.Double(10.0, 10.0, 20.0, 30.0);
    r = new Rectangle.Float(10.0f, 10.0f, 20.0f, 30.0f);
  }
}
```

- « Previous
