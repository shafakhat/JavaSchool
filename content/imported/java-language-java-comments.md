---
title: Java Tutorial - Java Comments
nav: Java Tutorial - Java Comme...
description: Comments in source provide information about the source code. It is a good practice to write comments to document the source code
section: Imported - java2s Archive
order: 50438
source: https://www.java2s.com/Tutorials/Java/Java_Language/4070__Java_Comments.html
---
Comments in source provide information about the source code. It is a good practice to write comments to document the source code

There are three types of comment supported in Java.

- Single-line,
- Multiline and
- Documentation comment.

## Single-line comment

Java single line comment starts from // and ends till the end of that line.

```java title=Example.java
publicclass Main {
  // This is a single line comment.
publicstaticvoid main(String[] argv) {
  }
}
```

## Multiline comment

Java multiline comment is between /* and */. Everything from /* through */ is ignored by the compiler.

```java title=Example.java
publicclass Main {
  /* This
     is
     a
     Multiline
     comment.
  */publicstaticvoid main(String[] argv) {
  }
}
```

## Java documentation comment(Javadoc)

Javadoc Documentation comment is used to produce an HTML file that documents your program. In short we usually call Java documentation comment javadoc.

A Javadoc comment occupies one or more lines of source code. The documentation comment begins with a /** and ends with a */. Everything from /** through */ is ignored by the compiler.

The following example demonstrates a Javadoc comment:

```java title=Example.java
/**
* Application entry point
*
* @param args array of command-line arguments passed to this method
*/
publicstatic void main(String[] args)
{
// TODO code application logic here
}
```

This example begins with a Javadoc comment that describes the main() method. /** and */ contains a description of the method, which could include HTML tags such as <p>, <code> and /</code>, and the @param Javadoc tag (an @-prefixed instruction).

The following list identifies several commonly used tags:

- @author identifies the source code's author.
- @deprecated identifies a source code entity that should no longer be used.
- @param identifies one of a method's parameters.
- @see provides a see-also reference.
- @since identifies the software release where the entity first originated.
- @return identifies the kind of value that the method returns.

The following code has more documentation comments

```java title=Example.java
/**
 * A simple class for introducing a Java application.
 *
 * @author yourName
 */publicclass HelloWorld {
  /**
   * Application entry point
   *
   * @param args
   *          array of command-line arguments passed to this method
   */publicstaticvoid main(String[] args) {
    System.out.println("Hello, world!");
  }
}
```

We can extract these documentation comments into a set of HTML files by using the JDK's javadoc tool, as follows:

javadoc command defaults to generating HTML-based documentation for public classes and public/protected members of these classes.

- « Previous
