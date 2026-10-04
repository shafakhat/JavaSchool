---
title: Scala Tutorial - Scala Method Declaration
nav: Scala Tutorial - Scala Met...
description: Scala method declarations have the def keyword, the method name, parameters, optional return type, the = keyword, and the method body.myMethod takes no parameters and ret
section: Imported - java2s Archive
order: 50101
source: https://www.java2s.com/Tutorials/Java/Scala/3010__Scala_Method_Declaration.html
---
```java title=Example.java
« Previous
```

- Next »

Scala method declarations have the def keyword, the method name, parameters, optional return type, the = keyword, and the method body.myMethod takes no parameters and returns a String:

```java title=Example.java

def myMethod():String = "java2s.com"
```

myOtherMethod takes no parameters and returns a String, but the return type is not explicitly declared because the compiler infers the return type.

```java title=Example.java

def myOtherMethod() = "Moof"
```

We declare the parameters inside the method declaration's parentheses. The parameter name must be followed by the parameter's type:

```java title=Example.java

def foo(a: Int):String = a.toString
```

We can declare multiple parameters:

```java title=Example.java

def f2(a: Int, b:Boolean):String= if (b)a.toString else"false"
```

We can pass the type of a parameter or the return type as a parameter.

The following code takes a parameter p and a type parameter T and returns a List of T.

Thus, if you pass an Int, you'll get a List[Int], and if you pass a String, you'll get a List[String].

```java title=Example.java

deflist[T](p:T):List[T] = p :: Nil
list(1)
list("Hello")
```

And the last parameter in the list may be a variable-length argument.

If the last parameter is a variable-length argument, it is a Seq of the type of the variable-length argument, so in this case the as parameter is a Seq[Int]:

```java title=Example.java

def largest(as: Int*): Int = as.reduceLeft((a, b)=> a max b)
```

A variable-length argument method may be called as follows:

```java title=Example.java

largest(1)
largest(2,3,99)
largest(3,22,33,22)
```

We can mix type parameters with variable-length arguments:

```java title=Example.java

def mkString[T](as: T*):String = as.foldLeft("")(_ + _.toString)
```

And we can put bounds on the type parameters. In this case, the types that are passed in must be Number or a subclass of Number:

```java title=Example.java

def sum[T <:Number](as:T*): Double = as.foldLeft(0d)(_ + _.doubleValue)
```

Methods can be declared within any code scope, except at the top level, where classes, traits, and objects are declared.

Methods can reference any variables in their scope as seen in the following code.

```java title=Example.java

def readLines(br: BufferedReader) = {
    var ret: List[String] = Nil
    def readAll():Unit= br.readLinematch {
        case null =>
        case s => ret ::= s ; readAll()
    }
    readAll()
    ret.reverse
}
```

Methods that override declared methods must include the override modifier.

Methods that override abstract methods may include the override modifier.

```java title=Example.java

abstract class Base {
    def thing: String
}
class One extends Base {
    def thing= "Moof"
}
```

Methods that take no parameters and variables can be accessed the same way, and a val can override a def in a superclass as shown in the following code.

```java title=Example.java

class Two extends One{
override val thing= (new java.util.Date).toString
}
class Three extends One{
override lazy val thing= super.thing + (new java.util.Date).toString
}
```

## Call-by-Name

In Scala we can pass parameters to methods and functions: call-by-name, which passes a code block to the callee.

Each time the callee accesses the parameter, the code block is executed and the value is calculated.

## Method Invocation

Scala provides a number of syntactic variations for invoking methods.

There's the standard Java dot notation:

```java title=Example.java

instance.method()
```

But if a method does not take any parameters, the ending parentheses are optional:

```java title=Example.java

instance.method
```

This allows methods without parameters methods to appear as properties or fields on the target instance.

Methods that take a single parameter can be invoked just as in Java:

```java title=Example.java

instance.method(param)
```

But methods that take a single parameter can be invoked without dots or parentheses:

```java title=Example.java

instance.method param
```

Because Scala allows method names to contain symbols such as +, -, *, and ?, Scala's dot less method notation creates a syntactically neutral way of invoking methods that are hard-coded operators in Java.

```java title=Example.java

object Main {
  def main(args: Array[String]) {
     println(2.1.*(4.3))
     println(2.1* 4.3)
  }
}
```

Finally, we invoke multiparameter methods in Scala just as in Java:

```java title=Example.java

instance.method(p1, p2)
```

If a Scala method takes a type parameter, wecan also explicitly pass the type parameter:

```java title=Example.java

instance.method[TypeParam](p1,p2)
```

- Next »
- « Previous
