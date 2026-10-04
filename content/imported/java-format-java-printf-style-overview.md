---
title: Java Format - Java printf-style Formatting
nav: Java Format - Java printf-...
description: The java.util.Formatter class supports printf-style formatting.
section: Imported - java2s Archive
order: 50390
source: https://www.java2s.com/Tutorials/Java/Java_Format/0050__Java_Printf_Style_Overview.html
---
```java title=Example.java
```

The java.util.Formatter class supports printf-style formatting.

printf-style formatting is well supported by C programming language.

The following code uses C's Printf-style Formatting in Java.

```java title=Example.java
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Formatting strings
    System.out.printf("%1$s, %2$s,  and  %3$s %n", "ABC", "DEF", "XYZ");
    System.out.printf("%3$s, %2$s,  and  %1$s %n", "ABC", "DEF", "XYZ");
    // Formatting numbers
    System.out.printf("%1$4d, %2$4d, %3$4d %n", 1, 10, 100);
    System.out.printf("%1$4d, %2$4d, %3$4d %n", 10, 100, 1000);
    System.out.printf("%1$-4d, %2$-4d,  %3$-4d %n", 1, 10, 100);
    System.out.printf("%1$-4d, %2$-4d,  %3$-4d %n", 10, 100, 1000);
    // Formatting date and time
    Date dt = new Date();
    System.out.printf("Today is  %tD  %n", dt);
    System.out.printf("Today is  %tF  %n", dt);
    System.out.printf("Today is  %tc  %n", dt);
  }
}
```

The code above generates the following result.

## Formatter class

We can use the System.out.println() and System.out.print() methods to print text on the standard output.

System.out is an instance of the java.io.PrintStream class, which has println() and print() instance methods.

PrintStream class also has format() and printf() which can support the printf-style formatting.

static format() from the String class also support the printf-style formatting.

The formatting behavior of the format()/printf() method of the PrintStream class and the format() static method of the String class is the same.

The format()/printf() method in the PrintStream class writes the formatted output to an output stream, whereas the format() method of the String class returns the formatted output.

The format()/printf() method of the PrintStream class and the format() static method of the String class are depending on the Formatter class.

A Formatter is used to format text, which can write to the following destinations:

- An Appendable (e.g. StringBuffer, StringBuilder, Writer, etc.)
- A File
- An OutputStream
- A PrintStream

The following code shows how to use Formatter class to format the data and store the result in StringBuilder class.

```java title=Example.java
import java.util.Date;
import java.util.Formatter;
publicclass Main {
  publicstaticvoid main(String[] args) {
    StringBuilder sb = new StringBuilder();
    Formatter fm = new Formatter(sb);
    // Formatting strings
    fm.format("%1$s, %2$s,  and  %3$s %n", "A", "B", "C");
    fm.format("%3$s, %2$s,  and  %1$s %n", "D", "E", "F");
    // Formatting numbers
    fm.format("%1$4d, %2$4d, %3$4d %n", 1, 10, 100);
    fm.format("%1$4d, %2$4d, %3$4d %n", 10, 100, 1000);
    fm.format("%1$-4d, %2$-4d,  %3$-4d %n", 1, 10, 100);
    fm.format("%1$-4d, %2$-4d,  %3$-4d %n", 10, 100, 1000);
    // Formatting date and time
    Date dt = new Date();
    fm.format("Today  is %tD  %n", dt);
    fm.format("Today  is %tF %n", dt);
    fm.format("Today  is %tc %n", dt);
    // Display the entire formatted string
    System.out.println(sb.toString());
  }
}
```

The code above generates the following result.

## Format to a file

To write all formatted text to a file, use the following code.

We have to handle the FileNotFoundException, which may be thrown from the constructor of the Formatter class if the specified file does not exist.

And we have to call its close() method to close the output file.

```java title=Example.java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Formatter;
publicclass Main {
  publicstatic void main(String[] args) {
    File file = new File("xyz.txt");
    Formatter fm = null;
    try {
      // Create a Formatter that will write the output the file
      fm = new Formatter(file);
      // Formatting strings
      fm.format("%1$s, %2$s,  and  %3$s %n", "A", "B", "C");
      fm.format("%3$s, %2$s,  and  %1$s %n", "A", "B", "C");
      // Format more text here...
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } finally {
      if (fm != null) {
        fm.close();
      }
    }
  }
}
```

## format() method from Formatter class

The format() method of the Formatter class is overloaded. Its declarations are as follows.

```java title=Example.java
Formatter format(String format, Object... args)
Formatter format(Locale l, String format, Object...  args)
```

The first version of the format() method uses the default locale for formatting. The second version allows you to specify a locale.

The format()/printf() method of the PrintStream class and the format() method of the String class support these two versions of the format() method.

- « Previous
