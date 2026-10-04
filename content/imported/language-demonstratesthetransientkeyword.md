---
title: Demonstrates the 'transient' keyword
nav: Demonstrates the 'transien...
description: ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream("User.out"));
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Demonstratesthetransientkeyword.htm
---
```java title=Example.java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Date;
publicclass MainClass {
  publicstaticvoid main(String[] args) throws Exception {
    User a = new User("A", "B");
    System.out.println("logon a = " + a);
    ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream("User.out"));
    o.writeObject(a);
    o.close();
    Thread.sleep(1000); // Delay for 1 second
    ObjectInputStream in = new ObjectInputStream(new FileInputStream("User.out"));
    System.out.println("Recovering object at " + new Date());
    a = (User) in.readObject();
    System.out.println("logon a = " + a);
  }
}
class User implements Serializable {
  private Date date = new Date();
  private String username;
  privatetransient String password;
  public User(String name, String pwd) {
    username = name;
    password = pwd;
  }
  public String toString() {
    String pwd = (password == null) ? "(n/a)" : password;
    return"logon info: \n   username: " + username + "\n   date: " + date + "\n   password: "
        + pwd;
  }
}
```
