---
title: Java IO Tutorial - Java Standard Input/Output/Error Streams
nav: Java IO Tutorial - Java St...
description: We can use the System.out and System.err object references wherever we can use an OutputStream object.
section: Imported - java2s Archive
order: 50213
source: https://www.java2s.com/Tutorials/Java/Java_io/0700__Java_io_Standard_Input_Output_Error_Streams.html
---
```java title=Example.java
```

We can use the System.out and System.err object references wherever we can use an OutputStream object.

We can use the System.in object wherever we can use an InputStream object.

The System class provides three static setter methods, setOut(), setIn(), and setErr(), to replace these three standard devices with your own devices.

To redirect all standard output to a file, we need to call the setOut() method by passing a PrintStream object that represents our file.

```java title=Example.java
import java.io.PrintStream;
import java.io.FileOutputStream;
import java.io.File;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    File outFile = newFile("stdout.txt");
    PrintStream ps = new PrintStream(new FileOutputStream(outFile));
    System.out.println(outFile.getAbsolutePath());
    System.setOut(ps);
    System.out.println("Hello world!");
    System.out.println("Java I/O  is cool!");
  }
}
```

The code above generates the following result.

## Standard Input Stream

We can use the System.in object to read data from a standard input device, usually a keyboard.

When a user enters data and presses the Enter key, the entered data becomes available, and the read() method returns one byte of data at a time.

The following code illustrates how to read data entered using the keyboard. \n is the new line character on Windows.

```java title=Example.java
import java.io.IOException;
publicclass EchoStdin {
  publicstaticvoid main(String[] args) throws IOException {
    System.out.print("Please type   a  message  and  press enter: ");
    int c = '\n';
    while ((c = System.in.read()) != '\n') {
      System.out.print((char) c);
    }
  }
}
```

Since System.in is an instance of InputStream, we can use any concrete decorator to read data from the keyboard; for example, we can create a BufferedReader object and read data from the keyboard one line at a time as string.

The code above generates the following result.

## Example

The following code illustrates how to use System.in object with a BufferedReader. The program keeps prompting the user to enter some text until the user enters Q or q to quit the program.

```java title=Example.java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
publicclass Main {
  publicstaticvoid main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String text = "q";
    while (true) {
      System.out.print("Please type a message (Q/q to quit) and press enter:");
      text = br.readLine();
      if (text.equalsIgnoreCase("q")) {
        System.out.println("We have  decided to exit  the   program");
        break;
      } else {
        System.out.println("We typed: " + text);
      }
    }
  }
}
```

If we want the standard input to come from a file, we will have to create an input stream object to represent that file and set that object using the System.setIn() method as in the following.

```java title=Example.java
FileInputStream fis  = new FileInputStream("stdin.txt");
System.setIn(fis);
// Now  System.in.read() will read   from  stdin.txt file
```

The code above generates the following result.

## Standard error device

The standard error device is used to display any error message. Java provides a PrintStream object called System.err. We use it as follows:

```java title=Example.java
System.err.println("This is  an  error message.");
```

- « Previous
