---
title: Java IO Tutorial - Java Console
nav: Java IO Tutorial - Java Co...
description: The purpose of the Console class is to make the interaction between a Java program and the console easier.
section: Imported - java2s Archive
order: 50214
source: https://www.java2s.com/Tutorials/Java/Java_io/0720__Java_io_Console.html
---
```java title=Example.java
```

The purpose of the Console class is to make the interaction between a Java program and the console easier.

The Console class is a utility class in the java.io package that gives access to the system console.

The console is not guaranteed to be accessible in a Java program on all machines. For example, if your Java program is run as a service, no console will be associated to the JVM.

We get the instance of the Console class by using the static console() method of the System class as follows:

```java title=Example.java

Console  console = System.console();
if (console !=  null)  {
    console.printf("Console is available.")
}
```

The Console class has a printf() method that is used to display formatted string on the console. We also have a printf() method in the PrintStream class to write the formatted data.

The following code illustrates how to use the Console class.

The program prompts the user to enter a user name and a password. If the user enters password letmein, the program prints a message.

```java title=Example.java
import java.io.Console;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Console console = System.console();
    if (console != null) {
      console.printf("Console is  available.%n");
    } else {
      System.out.println("Console is  not  available.%n");
      return; // A console is not available
    }
    String userName = console.readLine("User Name: ");
    char[] passChars = console.readPassword("Password: ");
    String passString = new String(passChars);
    if (passString.equals("letmein")) {
      console.printf("Hello %s", userName);
    } else {
      console.printf("Invalid  password");
    }
  }
}
```

The code above generates the following result.

- « Previous
