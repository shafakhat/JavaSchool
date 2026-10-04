---
title: The protected keyword
nav: The protected keyword
description: Imported from the java2s.com archive: The protected keyword
section: Imported - java2s Archive
order: 1127
source: https://web.archive.org/web/20140829080612/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Theprotectedkeyword.htm
---
```java title=Example.java
class A {
  private String name;
  protected void set(String nm) {
    name = nm;
  }
  public A(String name) {
    this.name = name;
  }
  public String toString() {
    return "I'm " + name;
  }
}
class B extends A {
  private int i;
  public B(String name, int i) {
    super(name);
    this.i = i;
  }
  public void change(String name, int i) {
    set(name); // Available because it's protected
    this.i = i;
  }
  public String toString() {
    return " " + i + ": " + super.toString();
  }
}
public class MainClass {
  public static void main(String[] args) {
    B orc = new B("A", 12);
    System.out.println(orc);
    orc.change("B", 19);
    System.out.println(orc);
  }
}
java title=Example.java
12: I'm A
 19: I'm B
```

| 5.25.1. | Access Control: four access control modifiers |
|---|---|
| 5.25.2. | Class Access Control Modifiers |
| 5.25.3. | Using Access Attributes |
| 5.25.4. | Class Member Access Matrix |
| 5.25.5. | Specifying Access Attributes |
| 5.25.6. | The public Book class |
| 5.25.7. | Default access level |
| 5.25.8. | Class Member Access Control Modifiers |
| 5.25.9. | Composition with public objects |
| 5.25.10. | The protected keyword |
| 5.25.11. | Private Override |
| 5.25.12. | Understand the effects of public and private access |
| 5.25.13. | In a class hierarchy, private members remain private to their class. |
| 5.25.14. | A Superclass Variable Can Reference a Subclass Object |
| 5.25.15. | Create a Singleton Object |
