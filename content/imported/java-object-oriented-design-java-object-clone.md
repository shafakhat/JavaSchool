---
title: Java Object Oriented Design - Java Object Clone
nav: Java Object Oriented Desig...
description: Java does not provide an automatic mechanism to clone (copy) an object.
section: Imported - java2s Archive
order: 50156
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0200__Java_Object_Clone.html
---
Java does not provide an automatic mechanism to clone (copy) an object.

Cloning an object means copying the content of the object bit by bit.

To support clone operation, implement the clone() method in the class.

The declaration of the clone() method in the Object class is as follows:

```java title=Example.java
protected  Object clone()  throws   CloneNotSupportedException
```

clone() method is declared protected. Therefore, we cannot call it from the client code. The following code is not valid:

```java title=Example.java
Object obj  = new Object();
Object clone = obj.clone(); // Error. Cannot  access protectedclone() method
```

We need to declare the clone() method public in a class to clone objects of the class.

Its return type is Object. It means you will need to cast the returned value of the clone() method.

Suppose MyClass is cloneable. The cloning code will look as

```java title=Example.java
MyClass mc  = new MyClass();
MyClass clone = (MyClass)mc.clone(); // Need to use  a  cast
```

The clone() method in the Object class throws a CloneNotSupportedException.

To call the clone() method, we need to place the call in a try-catch block, or rethrow the exception.

## Example

The following code shows how to implement a clone method.

```java title=Example.java
class MyClass implements Cloneable {
  privatedouble value;
public MyClass(double value) {
    this.value = value;
  }
  publicvoid setValue(double value) {
    this.value = value;
  }
  publicdouble getValue() {
    return this.value;
  }
  public Object clone() {
    MyClass copy = null;
    try {
      copy = (MyClass) super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return copy;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MyClass dh = new MyClass(100.00);
    MyClass dhClone = (MyClass) dh.clone();
    System.out.println("Original:" + dh.getValue());
    System.out.println("Clone :" + dhClone.getValue());
    dh.setValue(200.00);
    dhClone.setValue(400.00);
    System.out.println("Original:" + dh.getValue());
    System.out.println("Clone :" + dhClone.getValue());
  }
}
```

The code above generates the following result.

## Example 2

The following code is not returning Object type from clone method, which is compiled only in Java 5 or later.

```java title=Example.java
class MyClass  implements Cloneable  {
    public MyClass clone()  {
       Object copy  = null;
       return  (MyClass)copy;
    }
}
```

The following code shows how to do shallow clone.

```java title=Example.java
class MyClass implements Cloneable {
  privatedouble value;
public MyClass(double value) {
    this.value = value;
  }
  publicvoid setValue(double value) {
    this.value = value;
  }
  publicdouble getValue() {
    return this.value;
  }
  public Object clone() {
    MyClass copy = null;
    try {
      copy = (MyClass) super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return copy;
  }
}
class ShallowClone implements Cloneable {
  private MyClass holder = new MyClass(0.0);
  public ShallowClone(double value) {
    this.holder.setValue(value);
  }
  publicvoid setValue(double value) {
    this.holder.setValue(value);
  }
  publicdouble getValue() {
    return this.holder.getValue();
  }
  public Object clone() {
    ShallowClone copy = null;
    try {
      copy = (ShallowClone) super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return copy;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    ShallowClone sc = new ShallowClone(100.00);
    ShallowClone scClone = (ShallowClone) sc.clone();
    System.out.println("Original:" + sc.getValue());
    System.out.println("Clone :" + scClone.getValue());
    sc.setValue(200.00);
    System.out.println("Original:" + sc.getValue());
    System.out.println("Clone :" + scClone.getValue());
  }
}
```

The code above generates the following result.

## Example 3

The code in the clone() method of the ShallowClone class is the same as for the clone() method of the MyClass class.

When the ShallowClone class calls the clone() method of the Object class using super.clone(), it receives a shallow copy of itself. That is, it shares the DoubleHolder object used in its instance variable with its clone.

In a deep cloning, you need to clone all objects referenced by all reference instance variables of an object.

```java title=Example.java
class MyClass implements Cloneable {
  privatedouble value;
public MyClass(double value) {
    this.value = value;
  }
  publicvoid setValue(double value) {
    this.value = value;
  }
  publicdouble getValue() {
    return this.value;
  }
  public Object clone() {
    MyClass copy = null;
    try {
      copy = (MyClass) super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return copy;
  }
}
class DeepClone implements Cloneable {
  private MyClass holder = new MyClass(0.0);
  public DeepClone(double value) {
    this.holder.setValue(value);
  }
  publicvoid setValue(double value) {
    this.holder.setValue(value);
  }
  publicdouble getValue() {
    return this.holder.getValue();
  }
  public Object clone() {
    DeepClone copy = null;
    try {
      copy = (DeepClone) super.clone();
      copy.holder = (MyClass) this.holder.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return copy;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    DeepClone sc = new DeepClone(100.00);
    DeepClone scClone = (DeepClone) sc.clone();
    System.out.println("Original:" + sc.getValue());
    System.out.println("Clone :" + scClone.getValue());
    sc.setValue(200.00);
    System.out.println("Original:" + sc.getValue());
    System.out.println("Clone :" + scClone.getValue());
  }
}
```

The code above generates the following result.

- « Previous
