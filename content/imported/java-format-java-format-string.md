---
title: Java Format - Java printf Format String
nav: Java Format - Java printf ...
description: Formatting data using a Formatter requires two types of inputs:
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Format/0060__Java_Format_String.html
---
Formatting data using a Formatter requires two types of inputs:

- A format string
- A list of values

The format string defines how to format the list of values.

A format string may contain static texts and embedded format specifiers. The static text is outputted in the result as it is in the format string.

A format specifier serves two purposes.

- It acts as a placeholder for the formatted data inside the format string
- It specifies how the data should be formatted

## format specifier

Suppose you want to print a text with the birth date of a person. The following is an example of such a text:

```java title=Example.java
January 16, 1970  is Mike's birth day. Let's go and celebrate.
January 11, 1971  is John's birth day. Let's go and celebrate.
January 16, 1972  is Jane's birth day. Let's go and celebrate.
January 16, 1973  is Kite's birth day. Let's go and celebrate.
```

The above text contains fixed text and formatted text. In order to reuse the format and fill in person's name and the birthday we can write a template as follows:

```java title=Example.java
<month> <day>,  <year>  is <name>'s  birth  day. Let's go and celebrate.
```

The date of birthday is enclosed in angle brackets as well as the name of the person. We can call them placeholder. Later on we can provide real value for the placeholders.

To use the template in Formatter class, we convert a placeholder to a format specifier. The template becomes a format string.

A format specifier starts with a percent sign %.

We can rewrite the template string which can be used with the Formatter class as follows.

```java title=Example.java
%1$tB %1$td,  %1$tY is %2$s's  birth  day. Let's go and celebrate.
```

In this format string, %1$tB, %1$td, %1$tY, and %2$s are format specifiers.

The rest text in the format string, such as "birth day. Let's go and celebrate.", are fixed texts.

## Example

The following code shows how to use the above format string to print formatted text.

In the code we created a LocalDate which stores the birthday for Mike.

The local date value and "Mike" becomes the input values for the format string.

```java title=Example.java
import java.time.LocalDate;
import java.time.Month;
public class Main {
  public static void main(String[] args) {
    LocalDate dob = LocalDate.of(1971, Month.MAY, 16);
    System.out.printf(
        "%1$tB %1$td,  %1$tY is %2$s's birth day. Let's go and celebrate.",
        dob, "Mike");
  }
}
```

The code above generates the following result.

## Syntax for a format specifier

The general syntax for a format specifier is as follows:

```java title=Example.java
%<argument-index$><flags><width><.precision><conversion>
```

The % and conversion parts are mandatory, all other parts are optional.

There is no space between format specifiers and the % marks the start of a format specifier inside a format string.

To escape % use %%.

argument-index$ specifies the index of the argument. It has an integer followed by a $.

The first argument is referred to as 1$, the second as 2$, and so on. We can refer to the same argument multiple times.

The flags contains a set of characters and specifies the format of the output. The valid values for flags depend on the data type of the argument.

The width specifies the minimum number of characters needed to output.

The .precision whose exact meaning varies depending on conversion specifies the maximum number of characters to output.

For a decimal number, .precision starts with a dot ..

The conversion, a mandatory part, specifies how to format the value.

There are two special format specifiers:

- "%%" format outputs "%"
- "%n" format outputs a platform-specific newline character.

The following code shows how to use these two special format specifiers:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.printf("The rate is 10%%.%nA%nB");
  }
}
```

The code above generates the following result.

```java title=Example.java
The rate is 10%.
A
B
```

The code above generates the following result.

- « Previous
