---
title: Java IO Tutorial - Java DataInputStream
nav: Java IO Tutorial - Java Da...
description: DataInputStream can read Java primitive data type values from an input stream.
section: Imported - java2s Archive
order: 50204
source: https://www.java2s.com/Tutorials/Java/Java_io/0130__Java_io_DataInputStream.html
---
DataInputStream can read Java primitive data type values from an input stream.

The DataInputStream class contains read methods to read a value of a data type. For example, to read an int value, it contains a readInt() method; to read a char value, it has a readChar() method, etc. It also supports reading strings using the readUTF() method.

## Example

The following code shows how to read primitive values and Strings from a File.

```java title=Example.java
import java.io.DataInputStream;
import java.io.FileInputStream;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String srcFile = "primitives.dat";
    try (DataInputStream dis = new DataInputStream(new FileInputStream(srcFile))) {
      // Read the data in the same order they were written
int intValue = dis.readInt();
      double doubleValue = dis.readDouble();
      boolean booleanValue = dis.readBoolean();
      String msg = dis.readUTF();
      System.out.println(intValue);
      System.out.println(doubleValue);
      System.out.println(booleanValue);
      System.out.println(msg);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
