---
title: Demonstrates the transient keyword
nav: Demonstrates the transient...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20090530054753/http://www.java2s.com:80/Code/Java/Class/Demonstratesthetransientkeyword.htm
---
Demonstrates the transient keyword

```java title=Example.java
// : c12:Logon.java
// Demonstrates the "transient" keyword.
// {Clean: Logon.out}
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Date;
public class Logon implements Serializable {
  private Date date = new Date();
  private String username;
  private transient String password;
  public Logon(String name, String pwd) {
    username = name;
    password = pwd;
  }
  public String toString() {
    String pwd = (password == null) ? "(n/a)" : password;
    return "logon info: \n   username: " + username + "\n   date: " + date
        + "\n   password: " + pwd;
  }
  public static void main(String[] args) throws Exception {
    Logon a = new Logon("Hulk", "myLittlePony");
    System.out.println("logon a = " + a);
    ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream(
        "Logon.out"));
    o.writeObject(a);
    o.close();
    Thread.sleep(1000); // Delay for 1 second
    // Now get them back:
    ObjectInputStream in = new ObjectInputStream(new FileInputStream(
        "Logon.out"));
    System.out.println("Recovering object at " + new Date());
    a = (Logon) in.readObject();
    System.out.println("logon a = " + a);
  }
} ///:~
```
