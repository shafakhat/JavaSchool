---
title: Java IO Tutorial - Java DataOutputStream
nav: Java IO Tutorial - Java Da...
description: DataOutputStream can write Java primitive data type values to an output stream.
section: Imported - java2s Archive
order: 50208
source: https://www.java2s.com/Tutorials/Java/Java_io/0250__Java_io_DataOutputStream.html
---
```java title=Example.java
```

DataOutputStream can write Java primitive data type values to an output stream.

The DataOutputStream class contains a write method to write a data type. It supports writing a string to an output stream using the writeUTF(String text) method.

To write Java primitive data type values to a file named primitives.dat, we construct an object of DataOutputStream as follows:

```java title=Example.java
DataOutputStream dos  = new DataOutputStream(new FileOutputStream("primitives.dat"));
```

## Example

The following code writes an int value, a double value, a boolean value, and a string to a file named primitives.dat.

```java title=Example.java
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String destFile = "primitives.dat";
    try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(
        destFile))) {
      dos.writeInt(765);
      dos.writeDouble(6789.50);
      dos.writeBoolean(true);
      dos.writeUTF("Java Input/Output  is cool!");
      dos.flush();
      System.out.println("Data has  been  written to "
          + (newFile(destFile)).getAbsolutePath());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
