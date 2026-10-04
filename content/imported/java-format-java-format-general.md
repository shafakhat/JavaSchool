---
title: Java Format - Java printf format
nav: Java Format - Java printf ...
description: Different format characters can format values of different data types. For example, 's' is used to format a value as a string.
section: Imported - java2s Archive
order: 50394
source: https://www.java2s.com/Tutorials/Java/Java_Format/0090__Java_Format_General.html
---
Different format characters can format values of different data types. For example, 's' is used to format a value as a string.

Java printf formatting types can format data types in four categories:

- General formatting
- Character formatting
- Numeric formatting
- Date/Time formatting

## Uppercase variants

Many of the conversion characters have uppercase variants. For example, 'S' is the uppercase variant of 's'.

The uppercase variant converts the formatted output to uppercase.

The following code demonstrates the effect of using the uppercase variant 'S'.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.printf("%s and  %<S", "abc");
  }
}
```

The code above generates the following result.

## General Formatting

The general formatting can format values of any data types.

The following table has the list of conversions that are available under the general formatting category.

- Conversion letter: b Upper case: B Outputs "true" or "false" based on the argument. "false" for a null argument and false Boolean argument. Otherwise, "true."
- Conversion letter: h Upper case: H Output the hash code in hexadecimal format of the argument in a string. If the argument is null, it produces "null".
- Conversion letter: s Upper case: S Output a string representation of the argument. If the argument is null, it produces a "null" string. If the argument implements the Formattable interface, it invokes the formatTo() method on the argument. If the argument does not implement the Formattable interface, toString() method is invoked.

The general syntax for a format specifier for general formatting is

```java title=Example.java
%<argument_index$><flags><width><.precision><conversion>
```

The width specifies the minimum number of characters in the output.

If the length of the string representation is less than the width value, the result will be padded with spaces.

By default, the space padding is performed to the left of the argument value. If '-' flag is used, space padding is performed to the right.

The width and precision together decide the final content of the result.

The precision specifies the maximum number of characters of the output. The precision is applied to the argument before the width is applied.

If the precision is less than the length of the argument, the argument is truncated to the length set in the precision value, and space padding is performed to match the length to the value of the width.

Consider the following snippet of code:

```java title=Example.java
System.out.printf("'%4.1s'",  "abc");
```

The code above generates the following result.

## Example

The following are some examples of using Boolean, string and hash code formatting conversions.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Boolean conversion
    System.out.printf("'%b', '%6b', '%.4b'%n", true, false, true);
    System.out.printf("'%b', '%6b', '%.4b'%n", "A", "B", "C");
    System.out.printf("'%B', '%6b',  '%.4b'%n", "A", "B", "C");
    System.out.printf("%b %n", 2014);
    System.out.printf("%b %n", new Object());
// String conversion
    System.out.printf("'%s',  '%5s',  '%.3s'%n", "A", "B", "C");
    System.out.printf("'%S',  '%5S', '%.3S'%n", "A", "B", "C");
    // Use '-' flag to left-justify the result.
// width requires the '-' flag
    System.out.printf("'%S', '%-5S', '%.3S'%n", "A", "B", "C");
    System.out.printf("%s %n", 2014);
    System.out.printf("%s %n", true);
    System.out.printf("%s %n", new Object());
    // Hash Code conversion
    System.out.printf("'%h', '%5h', '%.3h'%n", "A", "B", "A");
    System.out.printf("'%H', '%5H',  '%.3H'%n", "A", "B", "A");
    System.out.printf("%h %n", 2014);
    System.out.printf("%h %n", true);
    System.out.printf("%h %n", new Object());
  }
}
```

The code above generates the following result.

## Custom Formatter

We can use custom formatting through 's' and 'S' conversions.

If the value implements java.util.Formattable interface, the 's' or 'S' conversion calls the value's formatTo() method to get the formatted result.

The formatTo() method from the value can accept a Formatter object, flags, width, and precision as the parameters.

We can check for alternate flag '#'. We can support uppercase variant 'S' of 's' conversion.

```java title=Example.java
import java.util.Formattable;
import java.util.FormattableFlags;
import java.util.Formatter;
class MyFormattableObject implements Formattable {
  publicvoid formatTo(Formatter formatter, int flags, int width, int precision) {
    int alternateFlagValue = FormattableFlags.ALTERNATE & flags;
    if (alternateFlagValue == FormattableFlags.ALTERNATE) {
      System.out.println("FormattableFlags.ALTERNATE");
    }
    int upperFlagValue = FormattableFlags.UPPERCASE & flags;
    if (upperFlagValue == FormattableFlags.UPPERCASE) {
      System.out.println(FormattableFlags.UPPERCASE);
    }
    int leftJustifiedFlagValue = FormattableFlags.LEFT_JUSTIFY & flags;
    if (leftJustifiedFlagValue == FormattableFlags.LEFT_JUSTIFY) {
      System.out.println("Left-justified flag '-' is used");
    } else {
      System.out.println("Left-justified flag '-' is not used");
    }
    formatter.format("value");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MyFormattableObject fp = new MyFormattableObject();
    System.out.printf("%s %n", fp );
    System.out.printf("%#s %n", fp );
    System.out.printf("%S %n", fp );
    System.out.printf("%#S %n", fp );
  }
}
```

The code above generates the following result.

## Character Formatting

Character formatting applies to char primitive data type or Character objects, as well as the byte, Byte, short, Short, int, or Integer values which are valid Unicode code points.

To test if an integer value represents a valid Unicode code, use the static method Character.isValidCodePoint(int value).

The conversion character for character formatting is 'c' or uppercase variant 'C'.

The flag '#' and the precision are not supported for character formatting.

The flag '-' and width controls the width and alignment as in the general formatting.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.printf("%c %n",  'a');
    System.out.printf("%C %n",  'a');
    System.out.printf("%C %n",  98);
    System.out.printf("'%5C' %n",  102);
    System.out.printf("'%-5C' %n",  102);
  }
}
```

The code above generates the following result.

- « Previous
