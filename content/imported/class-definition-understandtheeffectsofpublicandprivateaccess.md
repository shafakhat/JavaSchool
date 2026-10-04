---
title: Understand the effects of public and private access
nav: Understand the effects of ...
description: System.out.println("a, b, and c: " + ob.a + " " + ob.b + " " + ob.getc());
section: Imported - java2s Archive
order: 1128
source: https://web.archive.org/web/20140829075835/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Understandtheeffectsofpublicandprivateaccess.htm
---
```java title=Example.java
class Test {
  int a; // default access
  public int b; // public access
  private int c; // private access
  void setc(int i) {
    c = i;
  }
  int getc() {
    return c;
  }
}
class AccessTest {
  public static void main(String args[]) {
    Test ob = new Test();
    ob.a = 10;
    ob.b = 20;
    ob.setc(100);
    System.out.println("a, b, and c: " + ob.a + " " + ob.b + " " + ob.getc());
  }
}
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
