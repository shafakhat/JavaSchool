---
title: Java IO Tutorial - Java FileInputStream
nav: Java IO Tutorial - Java Fi...
description: In Java I/O, a stream means a flow of data. The data in the stream could be bytes, characters, objects, etc.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_io/0100__Java_io_FileInputStream.html
---
In Java I/O, a stream means a flow of data. The data in the stream could be bytes, characters, objects, etc.

To read from a file, we need to create an object of the FileInputStream class, which will represent the input stream.

```java title=Example.java
String srcFile = "test.txt";
FileInputStream fin  = new FileInputStream(srcFile);
```

The constructor of the FileInputStream class throws a FileNotFoundException if the file does not exist. To handle this exception, we need to place your code in a try-catch block, like so:

```java title=Example.java
try  {
    FileInputStream fin  = new FileInputStream(srcFile);
}catch  (FileNotFoundException e){
    // The error  handling code  goes  here
}
```

## Reading the Data

The FileInputStream class has an overloaded read() method to read data from the file. We can read one byte or multiple bytes at a time.

read() method's return type is int, though it returns a byte value. It returns -1 if the end of the file is reached.

We need to convert the returned int value to a byte to get the byte read from the file. Typically, we read a byte at a time in a loop.

Finally, we need to close the input stream using its close() method.

```java title=Example.java
// Close  the   input  stream
fin.close();
```

The close() method may throw an IOException, and because of that, we need to enclose this call inside a try-catch block.

```java title=Example.java
try  {
    fin.close();
}catch (IOException e)  {
    e.printStackTrace();
}
```

Typically, we construct an input stream inside a try block and close it in a finally block to make sure it is always closed after we are done with it.

All input/output streams are auto closeable. We can use a try-with-resources to create their instances, so they will be closed automatically regardless of an exception being thrown or not, avoiding the need to call their close() method explicitly.

The following code shows using a try-with-resources to create a file input stream:

```java title=Example.java
String srcFile = "test.txt";
try  (FileInputStream fin  = new FileInputStream(srcFile))  {
    // Use fin to read   data from  the   file here
}
catch  (FileNotFoundException e)  {
    // Handle  the   exception here
}
```

The following code shows how to read a Byte at a Time from a File Input Stream.

```java title=Example.java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
public class Main {
  public static void main(String[] args) {
    String dataSourceFile = "asdf.txt";
    try (FileInputStream fin = new FileInputStream(dataSourceFile)) {
      byte byteData;
      while ((byteData = (byte) fin.read()) != -1) {
        System.out.print((char) byteData);
      }
    } catch (FileNotFoundException e) {
      ;
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

- « Previous
