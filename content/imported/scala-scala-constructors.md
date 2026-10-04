---
title: Scala Tutorial - Scala Constructors
nav: Scala Tutorial - Scala Con...
description: A class consists of class members such as fields and methods.
section: Imported - java2s Archive
order: 50106
source: https://www.java2s.com/Tutorials/Java/Scala/3060__Scala_Constructors.html
---
A class consists of class members such as fields and methods.

Fields hold the state of an object and are defined with either val or var.

Methods complete the computational tasks of the object and are defined with keyword def.

In Scala, the entire body of the class is the constructor.

If the constructor takes zero parameters, you can omit the parameter list.

Scala differentiates between a constructor declared with val fields, var fields, private val, or private var and fields without varor val.

## Parameter Declared as a val

If the constructor parameter is declared as a val, Scala generates only a getter method for it.

Let's declare a field as val as shown here:

```java title=Example.java
class Book( val title:String)
```

Because the constructor field is defined as a val, the value of the field is immutable by definition. Therefore, Scala generates only the getter method and no setter method.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    class Book( val title:String)
    val book = new Book("Scala")
    println(book);
    println(book.title )
    //book.title = "new title"  //Error
  }
}
```

In Scala, if the constructor or method takes zero parameters, you can omit the parameter list.

## Parameter Declared as a var

If the constructor parameter is declared as a var, Scala generates both accessor and mutator methods.

```java title=Example.java
class Book( var title:String)
```

So when you set the field, like so

```java title=Example.java
book.title("new title")
```

We can mutate the field of Book object because it was declared with keyword var.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    class Book( var title:String)
    val book = new Book("Beginning Scala")
    book.title = "new title"
    println(book.title )
  }
}
```

## Parameter Declared as a private val or var

You can add the private keyword to a val or var field to prevent getter and setter methods from being generated.

In this case the fields could only be accessed from within members of the class:

```java title=Example.java
class Book(privatevar title: String) {
    def printTitle {
       println(title)
    }
}
val book = new Book("Beginning Scala")
println(book.printTitle )
```

## Parameter Declared without val or var

Scala does not generate getter or setter when neither val nor var are specified on constructor parameters.

As you can see here, you cannot access the field title of the Book.

```java title=Example.java
class Book(title: String)
val book = new Book("Beginning Scala")
//book.title //Error
```

## Example

Here's Book class with one constructor parameter named title that has default value of "Scala".

Because the parameter is defined with a default value, you can call the constructor without specifying a title value:

```java title=Example.java
class Book (val title: String = "Scala")
val book = new Book
book.title
```

You can also specify the title value of your choice when creating a new Book:

```java title=Example.java
val book = new Book("new title")
book.title
```

You can also choose to provide named parameters as shown in the following code:

```java title=Example.java
val book = new Book(title="Beginning Scala")
book.title
```

## Auxiliary Constructor

We can define one or more auxiliary constructors for a class to provide different ways to create objects.

Auxiliary constructors are defined by creating methods named this.

We can define multiple auxiliary constructors, but they must have different signatures.

Each auxiliary constructor must begin with a call to a previously defined constructor.

The following code illustrates a primary constructor and two auxiliary constructors.

```java title=Example.java
class Book (var title :String, var ISBN: Int) {
    def this(title: String) {
        this(title, 2222)
    }
    def this() {
        this("CSS")
        this.ISBN = 1111
    }
    override def toString = s"$title ISBN- $ISBN"
}
```

Given these constructors, the same Book can be created in the following ways:

```java title=Example.java
val book1 = new Book
val book2 = new Book("Clojure")
val book3 = new Book("Scala", 3333)
```

An auxiliary constructor just needs to call one of the previously defined constructors.

- « Previous
