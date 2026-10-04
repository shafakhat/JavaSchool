---
title: Java Tutorial - Java Keywords
nav: Java Tutorial - Java Keywo...
description: A keyword is a word whose meaning is defined by the programming language. Java keywords and reserved Words:
section: Imported - java2s Archive
order: 50418
source: https://www.java2s.com/Tutorials/Java/Java_Language/1010__Java_Keywords.html
---
```java title=Example.java
« Previous
```

- Next »

## Full list of keywords in Java

A keyword is a word whose meaning is defined by the programming language. Java keywords and reserved Words:

```java title=Example.java

abstract class    extends implements null      strictfp     true
assert   const    false   import     package   super        try
boolean  continue final   instanceof private   switch       void
break    default  finally int        protected synchronized volatile
byte     do       float   interface  public    this         while
case     double   for     long       return    throw
catch    else     goto    native     short     throws
char     enum     if      new        static    transient
```

An identifier is a word used by a programmer to name a variable, method, class, or label. Keywords and reserved words may not be used as identifiers. An identifier must begin with a letter, a dollar sign ($), or an underscore (_); subsequent characters may be letters, dollar signs, underscores, or digits.

Some examples are:

```java title=Example.java

foobar          // legal
Myclass         // legal
$a              // legal
3_a             // illegal: starts with a digit
!theValue       // illegal: bad 1st  char
```

Java Identifiers are case sensitive. For example, myValue and MyValue are distinct identifiers.

## Using identifiers

Identifiers are used for class names, method names, and variable names. An identifier may be any sequence of uppercase and lowercase letters, numbers, or the underscore and dollar-sign characters. Identifiers must not begin with a number. Java Identifiers are case-sensitive. The following code illustrates some examples of valid identifiers:

```java title=Example.java
publicclass Main {
  publicstatic void main(String[] argv) {
    int ATEST, count, i1, $Atest, this_is_a_test;
  }
}
```

The following code shows invalid variable names include:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv){
     int 2count, h-l, a/b,
  }
}
```

If you try to compile this code, you will get the following error message:

- Next »
- « Previous
