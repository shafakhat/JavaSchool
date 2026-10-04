---
title: Java IO Tutorial - Java FileOutputStream
nav: Java IO Tutorial - Java Fi...
description: To write to a file, we need to create an object of the FileOutputStream class, which will represent the output stream.
section: Imported - java2s Archive
order: 50206
source: https://www.java2s.com/Tutorials/Java/Java_io/0210__Java_io_FileOutputStream.html
---
```java title=Example.java
```

## Creating the Output Stream

To write to a file, we need to create an object of the FileOutputStream class, which will represent the output stream.

```java title=Example.java
// Create a  file  output stream
String destFile = "test.txt";
FileOutputStream fos   = new FileOutputStream(destFile);
```

When writing to a file, Java tries to create the file if the file does not exist. We must be ready to handle this exception by placing your code in a try-catch block, as shown:

```java title=Example.java
try  {
    FileOutputStream fos   = new FileOutputStream(srcFile);
}catch  (FileNotFoundException e){
    // Error handling code  goes  here
}
```

If the file contains data, the data will be erased. To keep the existing data and append the new data to the file, we need to use another constructor of the FileOutputStream class, which accepts a boolean flag for appending the new data to the file.

To append data to the file, pass true in the second argument, use the following code.

```java title=Example.java
FileOutputStream fos   = new FileOutputStream(destFile, true);
```

## Writing the Data

The FileOutputStream class has an overloaded write() method to write data to a file. We can write one byte or multiple bytes at a time using the different versions of this method.

Typically, we write binary data using a FileOutputStream.

To write a string such as "Hello" to the output stream, convert the string to bytes.

The String class has a getBytes() method that returns an array of bytes that represents the string. We write a string to the FileOutputStream as follows:

```java title=Example.java
String text = "Hello";
byte[] textBytes = text.getBytes();
fos.write(textBytes);
```

To insert a new line, use the line.separator system variable as follows.

```java title=Example.java
String lineSeparator = System.getProperty("line.separator");
fos.write(lineSeparator.getBytes());
```

We need to flush the output stream using the flush() method.

```java title=Example.java
fos.flush();
```

Flushing an output stream indicates that if any written bytes were buffered, they may be written to the data sink.

Closing an output stream is similar to closing an input stream. We need to close the output stream using its close() method.

```java title=Example.java
// Close  the   output  stream
fos.close();
```

The close() method may throw an IOException. Use a try-with-resources to create an output stream if we want tit to be closed automatically.

The following code shows how to write Bytes to a File Output Stream.

```java title=Example.java
import java.io.File;
import java.io.FileOutputStream;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String destFile = "luci2.txt";
    // Get the line separator for the current platform
    String lineSeparator = System.getProperty("line.separator");
    String line1 = "test";
    String line2 = "test1";
    String line3 = "test2";
    String line4 = "test3";
    try (FileOutputStream fos = new FileOutputStream(destFile)) {
      fos.write(line1.getBytes());
      fos.write(lineSeparator.getBytes());
      fos.write(line2.getBytes());
      fos.write(lineSeparator.getBytes());
      fos.write(line3.getBytes());
      fos.write(lineSeparator.getBytes());
      fos.write(line4.getBytes());
      // Flush the written bytes to the file
      fos.flush();
      System.out.println("Text has  been  written to "
          + (newFile(destFile)).getAbsolutePath());
    } catch (Exception e2) {
      e2.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
