---
title: Private Override
nav: Private Override
description: Imported from the java2s.com archive: Private Override
section: Imported - java2s Archive
order: 1132
source: https://web.archive.org/web/20140829080245/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/PrivateOverride.htm
---
```java title=Example.java
class PrivateOverride {
  private void f() {
    System.out.println("private f()");
  }
  public static void main(String[] args) {
    PrivateOverride po = new Derived();
    po.f();
  }
}
class Derived extends PrivateOverride {
  public void f() {
    System.out.println("public f()");
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
