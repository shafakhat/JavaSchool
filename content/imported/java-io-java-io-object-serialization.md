---
title: Java IO Tutorial - Java Object Serialization
nav: Java IO Tutorial - Java Ob...
description: An object of the ObjectOutputStream class is used to serialize an object.
section: Imported - java2s Archive
order: 50210
source: https://www.java2s.com/Tutorials/Java/Java_io/0400__Java_io_Object_Serialization.html
---
```java title=Example.java
```

An object of the ObjectOutputStream class is used to serialize an object.

An object of the ObjectInputStream class is used to deserialize an object.

ObjectOutputStream is inherited from OutputStream. ObjectInputStream is inherited from InputStream.

The class must implement the Serializable or Externalizable interface to be serialized or deserialized.

The Serializable interface is a marker interface.

If we want the objects of a Person class to be serialized, we need to declare the Person class as follows:

```java title=Example.java
publicclass Person   implements Serializable  {
}
```

Java takes care of the details of reading/writing a Serializable object from/to a stream. We just need to pass the object to write/read to/from a stream to one of the methods of the stream classes.

Implementing the Externalizable interface gives us more control in reading and writing objects from/to a stream.

It inherits the Serializable interface. It is declared as follows:

```java title=Example.java
publicinterface  Externalizable extends Serializable  {
    void  readExternal(ObjectInput in)  throws   IOException,  ClassNotFoundException;
    void  writeExternal(ObjectOutput out) throws   IOException;
}
```

Java calls the readExternal() method when we read an object from a stream. It calls the writeExternal() method when we write an object to a stream.

We have to write the logic to read and write an object's fields inside the readExternal() and writeExternal() methods, respectively.

The class implementing the Externalizable interface looks like the following:

```java title=Example.java
publicclass Person  implements Externalizable  {
    publicvoid  readExternal(ObjectInput in)  throws   IOException,  ClassNotFoundException {
        // Write the logic to read the Person object fields  from  the   stream
    }
    publicvoid  writeExternal(ObjectOutput out) throws   IOException  {
        // Write  the   logic to write Person   object fields  to the   stream
    }
}
```

## Serializing Objects

The following code creates an object of the ObjectOutputStream class and save an object to a person.ser file.

```java title=Example.java
ObjectOutputStream oos  = new ObjectOutputStream(new FileOutputStream("person.ser"));
```

To save an object to a ByteArrayOutputStream, we construct an object output stream as follows:

```java title=Example.java
ByteArrayOutputStream baos  = new ByteArrayOutputStream();
// Creates an  object output stream to write objects to the   byte   array  output stream
ObjectOutputStream oos  = new ObjectOutputStream(baos);
```

Use the writeObject() method of the ObjectOutputStream class to serialize the object by passing the object reference as an argument, like so:

```java title=Example.java
oos.writeObject(p1);
```

Finally, use the close() method to close the object output stream when we are done writing all objects to it:

```java title=Example.java
oos.close();
```

The following code shows how to serialize a Person Class That Implements the Serializable Interface.

```java title=Example.java
import java.io.Serializable;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
class Person implements Serializable {
  private String name = "Unknown";
  private String gender = "Unknown";
  privatedouble height = Double.NaN;
  public Person(String name, String gender, double height) {
    this.name = name;
    this.gender = gender;
    this.height = height;
  }
  @Override
  public String toString() {
    return"Name: " + this.name + ", Gender:   " + this.gender + ",  Height: "
        + this.height;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Person p1 = new Person("John", "Male", 1.7);
    Person p2 = new Person("Wally", "Male", 1.7);
    Person p3 = new Person("Katrina", "Female", 1.4);
    File fileObject = newFile("person.ser");
    try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(
        fileObject))) {
      oos.writeObject(p1);
      oos.writeObject(p2);
      oos.writeObject(p3);
      // Display the serialized objects on the standard output
      System.out.println(p1);
      System.out.println(p2);
      System.out.println(p3);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Deserializing Objects

The following code shows how to create an object of the ObjectInputStream class and read an object from a person.ser file.

```java title=Example.java
ObjectInputStream ois  = new ObjectInputStream(new FileInputStream("person.ser"));
```

To read objects from a ByteArrayInputStream, create an object output stream as follows:

```java title=Example.java
ObjectInputStream ois  = new ObjectInputStream(Byte-Array-Input-Stream-Reference);
```

Use the readObject() method of the ObjectInputStream class to deserialize the object.

```java title=Example.java
Object obj  = oos.readObject();
```

Finally, close the object input stream as follows:

```java title=Example.java
ois.close();
```

The following code shows how to reading Objects from a File.

```java title=Example.java
import java.io.File;
import java.io.FileInputStream;
import java.io.ObjectInputStream;
publicclass Main {
  publicstatic void main(String[] args) {
    File fileObject = new File("person.ser");
    try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(
        fileObject))) {
      Person p1 = (Person) ois.readObject();
      Person p2 = (Person) ois.readObject();
      Person p3 = (Person) ois.readObject();
      System.out.println(p1);
      System.out.println(p2);
      System.out.println(p3);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

## Externalizable Object Serialization

To serialize and deserialize Externalizable objects, implement the Externalizable interface.

```java title=Example.java
import java.io.Externalizable;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
class PersonExt implements Externalizable {
  private String name = "Unknown";
  private String gender = "Unknown";
  privatedouble height = Double.NaN;
  public PersonExt() {
  }
  public PersonExt(String name, String gender, double height) {
    this.name = name;
    this.gender = gender;
    this.height = height;
  }
  public String toString() {
    return"Name: " + this.name + ", Gender:   " + this.gender + ",  Height: "
        + this.height;
  }
  publicvoid readExternal(ObjectInput in) throws IOException,
      ClassNotFoundException {
    this.name = in.readUTF();
    this.gender = in.readUTF();
  }
  publicvoid writeExternal(ObjectOutput out) throws IOException {
    out.writeUTF(this.name);
    out.writeUTF(this.gender);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    PersonExt p1 = new PersonExt("John", "Male", 6.7);
    PersonExt p2 = new PersonExt("Wally", "Male", 5.7);
    PersonExt p3 = new PersonExt("Katrina", "Female", 5.4);
    File fileObject = newFile("personext.ser");
    try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(
        fileObject))) {
      oos.writeObject(p1);
      oos.writeObject(p2);
      oos.writeObject(p3);
      System.out.println(p1);
      System.out.println(p2);
      System.out.println(p3);
    } catch (IOException e1) {
      e1.printStackTrace();
    }
    fileObject = newFile("personext.ser");
    try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(
        fileObject))) {
      p1 = (PersonExt) ois.readObject();
      p2 = (PersonExt) ois.readObject();
      p3 = (PersonExt) ois.readObject();
      // Let's display the objects that are read
      System.out.println(p1);
      System.out.println(p2);
      System.out.println(p3);
      // Print the input path
      System.out.println("Objects were  read   from  "
          + fileObject.getAbsolutePath());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
