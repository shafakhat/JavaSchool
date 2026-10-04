---
title: public Object clone() throws CloneNotSupportedException
nav: public Object clone() thro...
description: public static void main(String[] args) throws CloneNotSupportedException {
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20101107132256/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/publicObjectclonethrowsCloneNotSupportedException.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) throws CloneNotSupportedException {
    CloneDemo2 cd2 = new CloneDemo2();
    System.out.println(cd2.salary);
    AnotherClass ac = new AnotherClass();
    System.out.println(ac.gradeLetter);
    AnotherClass y = (AnotherClass) ac.clone();
    System.out.println(y.gradeLetter);
  }
}
class CloneDemo2 implements Cloneable {
  double salary = 50000.0;
}
class AnotherClass implements Cloneable {
  char gradeLetter = 'C';
    return super.clone();
  }
}
```
