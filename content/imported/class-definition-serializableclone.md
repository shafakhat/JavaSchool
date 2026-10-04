---
title: Serializable Clone
nav: Serializable Clone
description: public static Object clone(final Object obj) throws Exception {
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20100529044404/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/SerializableClone.htm
---
```java title=Example.java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
public abstract class SerializableClone {
  public static Object clone(final Object obj) throws Exception {
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    ObjectOutputStream oout = new ObjectOutputStream(out);
    oout.writeObject(obj);
    ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(out.toByteArray()));
    return in.readObject();
  }
}
```
