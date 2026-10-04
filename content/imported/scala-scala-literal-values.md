---
title: Scala Tutorial - Scala Literal Values
nav: Scala Tutorial - Scala Lit...
description: Integer literals can be expressed in decimal, hexadecimal, or octal.
section: Imported - java2s Archive
order: 50084
source: https://www.java2s.com/Tutorials/Java/Scala/0150__Scala_Literal_Values.html
---
```java title=Example.java
```

## Integer Literals

Integer literals can be expressed in decimal, hexadecimal, or octal.

The details are summarized in the following Table.

Kind  Format  Examples
---  ---  ---
Decimal  0 or a nonzero digit followed by zero or more digits (0-9)  0, 1, 321
Hexadecimal  0x followed by one or more hexadecimal digits (0-9, A-F, a-f)  0xFF, 0x1a3b
Octal  0 followed by one or more octal digits (0-7)a  013, 077

A Octal literals are deprecated as of Scala 2.10.

You indicate a negative number by prefixing the literal with a - sign.

For Long literals, it is necessary to append the L or l character at the end of the literal, unless you are assigning the value to a variable declared to be Long.

Otherwise, Int is inferred.

The valid values for an integer literal are bounded by the type of the variable to which the value will be assigned.

The following Table defines the limits, which are inclusive.

Target type  Minimum (inclusive)  Maximum (inclusive)
---  ---  ---
Long  -2 63  2 63 - 1
Int  -2 31  2 31 - 1
Short  -2 15  2 15 - 1
Char  0  2 16 - 1
Byte  -2 7  2 7 - 1

A compile-time error occurs if an integer literal number is specified that is outside these ranges.

## Floating-Point Literals

Floating-point literals are expressions with an optional minus sign, zero or more digits, followed by a period ., followed by one or more digits.

For Float literals, append the F or f character at the end of the literal. Otherwise, a Double is assumed.

We can optionally append a D or d for a Double.

Floating-point literals can be expressed with or without exponentials.

The format of the exponential part is e or E, followed by an optional + or -, followed by one or more digits.

Here are some example floating-point literals. Double is inferred unless the declared variable is Float or an f or F suffix is used:

```java title=Example.java
     .14
     3.14
     3.14f
     3.14F
     3.14d
     3.14D
     3e5
     3E5
     3.14e+5
     3.14e-5
     3.14e-5
     3.14e-5f
     3.14e-5F
     3.14e-5d
     3.14e-5D
```

## Boolean Literals

The Boolean literals are true and false.

The type of the variable to which they are assigned will be inferred to be Boolean:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val b1 = true
     val b2 = false
     println(b1);
     println(b2);
  }
}
```

## Character Literals

A character literal is either a printable Unicode character or an escape sequence, written between single quotes.

A character with a Unicode value between 0 and 255 can be represented by an octal escape, i.e., a backslash (\) followed by a sequence of up to three octal characters.

Here are some examples:

```java title=Example.java
      'A'
      '\u0041'  // 'A' in Unicode
      '\n'
      '\012'    // '\n' in octal
      '\t'
```

The valid escape sequences are shown in the following Table.

Sequence  Meaning
---  ---
\b  Backspace (BS)
\t  Horizontal tab (HT)
\n  Line feed (LF)
\f  Form feed (FF)
\r  Carriage return (CR)
\"  Double quote ( ")
\'  Single quote ( ')
\\  Backslash (\)

## String Literals

A string literal is a sequence of characters enclosed in double quotes or triples of double quotes, i.e., """...""".

For string literals in double quotes, the allowed characters are the same as the character literals.

To include a double quote " character in string, it must be "escaped" with a \ character.

Here are some examples:

```java title=Example.java
     "This is a\ntest"
     "He said, \"SQL is for database!\""
     "First\tSecond"
```

The string literals bounded by triples of double quotes are called multiline string literals.

These strings can cover several lines. The line feeds will be part of the string. They can include any characters, including one or two double quotes together, but not three together.

They are useful for strings with \ characters that don't form valid Unicode or escape sequences.

Here are three example strings:

```java title=Example.java
     """This is a \ntest"""
     """He said, "SQL is for database!" """
     """First line\n
     Second line\t
     Fourth line"""
```

When using multiline strings in code, to indent the substrings for proper code formatting use String.stripMargin.

It removes all whitespace in the substrings up to and including the first occurrence of a vertical bar |.

To add whitespace indentation, put the whitespace after the |.

Consider this example:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     println(hello("This is a test") );
  }
  def hello(name: String) = s"""Welcome!
       Hello, $name!
       * (Star!!)
       |Hi.
       |    whitespace.""" .stripMargin
}
```

To use a different leading character than |, use the overloaded version of stripMargin that takes a Char (character) argument.

If the whole string has a prefix or suffix you want to remove, there are corresponding strip Prefix and stripSuffix methods.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     println(goodbye("JavaSchool"));
  }
  def goodbye(name: String) =
       s"""xxxGoodbye, ${name}yyy
       xxxCome again!yyy""" .stripPrefix("xxx").stripSuffix("yyy")
}
```

## Symbol Literals

Scala has symbols type, which are interned strings, meaning that two symbols with the same "name" will actually refer to the same object in memory.

A symbol literal is a single quote ', followed by one or more digits, letters, or underscores ("_"), except the first character can't be a digit.

## Function Literals

(i: Int, s: String) => s+i is a function literal of type Function2[Int,String,String] (String is returned).

You can even use the literal syntax for a type declaration.

The following declarations are equivalent:

```java title=Example.java
     val f1: (Int,String) => String       = (i, s) => s+i
     val f2: Function2[Int,String,String] = (i, s) => s+i
```

## Tuple Literals

The Scala library includes TupleN classes (e.g., Tuple2), for grouping N items, with the literal syntax of a comma-separated list of the items inside parentheses.

There are separate TupleN classes for N between 1 and 22, inclusive.

For example, val tup = ("Hi", 2014) defines a Tuple2 instance with String inferred for the first element and Int inferred for the second element.

Tuple instances are immutable, first-class values, so you can assign them to variables, pass them as values, and return them from methods.

We can also use the literal syntax for Tuple type declarations:

```java title=Example.java
     val t1: (Int,String)       = (1, "two")
     val t2: Tuple2[Int,String] = (1, "two")
```

The following example demonstrates working with tuples:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val t = ("Hello", 1, 2.3)
     println( "Print the whole tuple: " + t )
     println( "Print the first item:  " + t._1 )
     println( "Print the second item: " + t._2 )
     println( "Print the third item:  " + t._3 )
     val (t1, t2, t3) = ("World",  '!', 0x22)
     println( t1 + ", " + t2 + ", " + t3 )
     val (t4, t5, t6) = Tuple3("World",  '!', 0x22)
     println( t4 + ", " + t5 + ", " + t6 )
  }
}
```

The expression t._n retrieves the nth item from tuple t, starting at one, not zero, following historical conventions.

There are several ways to define a two-element tuple, which is sometimes called a pair for short.

We can use the "arrow operator" between two values, as well as special factory methods on the tuple-related classes:

```java title=Example.java
     (1, "one")
     1 -> "one"
     Tuple2(1, "one")
```

- « Previous
