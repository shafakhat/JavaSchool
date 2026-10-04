---
title: Java Format - Java printf Value Index
nav: Java Format - Java printf ...
description: The following code use the s conversion to format its argument as string.
section: Imported - java2s Archive
order: 50392
source: https://www.java2s.com/Tutorials/Java/Java_Format/0070__Java_Format_Value_Index.html
---
```java title=Example.java
« Previous
```

- Next »

The following code use the s conversion to format its argument as string.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.printf("%s, %s,  and  %s",  "A",  "B", "C");
  }
}
```

The code above generates the following result.

A format specifier in a format string can refer to an argument in three ways:

- Ordinary indexing
- Explicit indexing
- Relative indexing

## Ordinary Indexing

When a format specifier does not specify an argument-index value as the code above, it is called ordinary indexing.

In ordinary indexing, the argument-index is determined by the position of the format specifier in the format string.

The first format specifier without argument-index has the index of 1, which refers to the first argument.

For the following format string,

```java title=Example.java

System.out.printf("%s, %s,  and  %s",  "A",  "B", "C");
```

The first %s has the index of 1, and the second %s has the index of 2.

The first "%s" format who has the index of 1 refers to the first argument, "A". The second "%s" format refers to the second argument, "B".

If there are more arguments than the format specifiers in the format string, the extra arguments are ignored.

A java.util.MissingFormatArgumentException is thrown if there are more format specifier than arguments.

The following code will throw the exception because the number of arguments is one less than the number of format specifiers.

```java title=Example.java
publicclass Main {
  publicstatic void main(String[] args) {
    System.out.printf("%s, %s,  and  %s",  "A",  "B");
  }
}
```

The code above generates the following result.

The last argument to the format() method of the Formatter class is a varargs argument. We can also pass an array to a varargs argument.

## Explicit Indexing

The explicit indexing specifies an argument index explicitly in a format specifier.

An argument index, an integer ending with $, is specified just after the % sign in a format specifier.

The following code uses three format specifiers with explicit indexing: "%1$s", "%2$s", and "%3$s".

```java title=Example.java
publicclass Main {
  publicstatic void main(String[] args) {
    System.out.printf("%1$s, %2$s, and %3$s",  "A",  "B", "C");
  }
}
```

The code above generates the following result.

Explicit indexing can refer to an argument at any order in the argument list.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.printf("%3$s, %2$s, and %1$s",  "A",  "B", "C");
  }
}
```

The code above generates the following result.

We can reference the same argument multiple times using explicit indexing and not to reference some arguments inside the format string.

```java title=Example.java
publicclass Main {
  publicstatic void main(String[] args) {
    System.out.printf("%3$s, %2$s, and %2$s", "A", "B", "C");
  }
}
```

The code above generates the following result.

## Relative Indexing

In relative indexing, a format specifier uses the same argument that was used by the previous format specifier.

Relative indexing does not use an argument-index value. It uses '<' character as a flag in the format specifier.

We cannot use relative indexing as the first format specifier since there must be a previous format specifier.

The following code uses relative indexing:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.printf("%1$s, %<s, %<s, %2$s, and %<s",  "A",  "B");
  }
}
```

The code above generates the following result.

It is possible to have less number of arguments than the number of format specifiers for relative indexing.

- Next »
- « Previous
