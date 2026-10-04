---
title: ArrayList implements the empty Serializable interface
nav: ArrayList implements the e...
description: If all of the elements of an ArrayList are Serializable, you can then serialize the list to an ObjectOutputStream and later read it back from an ObjectInputStream.
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20070707111512/http://www.java2s.com:80/Tutorial/Java/0140__Collections/ArrayListimplementstheemptySerializableinterface.htm
---
If all of the elements of an ArrayList are Serializable, you can then serialize the list to an ObjectOutputStream and later read it back from an ObjectInputStream.

```java title=Example.java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Arrays;
import java.util.List;
public class MainClass {
  public static void main(String[] a) throws Exception {
    List list = Arrays.asList(new String[] { "A", "B", "C", "D" });
    FileOutputStream fos = new FileOutputStream("list.ser");
    ObjectOutputStream oos = new ObjectOutputStream(fos);
    oos.writeObject(list);
    oos.close();
    FileInputStream fis = new FileInputStream("list.ser");
    ObjectInputStream ois = new ObjectInputStream(fis);
    List anotherList = (List) ois.readObject();
    ois.close();
    System.out.println(anotherList);
  }
}
```

```java title=Example.java

[A, B, C, D]
```
