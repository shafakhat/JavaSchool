---
title: Define your own equals method
nav: Define your own equals met...
description: Imported from the java2s.com archive: Define your own equals method
section: Imported - java2s Archive
order: 1105
source: https://web.archive.org/web/20140829084132/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Defineyourownequalsmethod.htm
---
```java title=Example.java
class MyClass {
  private String name;
  MyClass(String name) {
    this.name = name;
  }
  public boolean equals(Object o) {
    if (!(o instanceof MyClass))
      return false;
    MyClass c = (MyClass) o;
    return name.equals(c.name);
  }
}
class EqualityDemo {
  public static void main(String[] args) {
    MyClass c1 = new MyClass("S");
    MyClass c2 = new MyClass("S");
    MyClass c3 = new MyClass("M");
    System.out.println("c1.equals (c2): " + c1.equals(c2));
    System.out.println("c1.equals (c3): " + c1.equals(c3));
  }
}
```

| 5.19.1. | Comparing Objects |
|---|---|
| 5.19.2. | Implement equals method using commons-lang |
| 5.19.3. | Use CompareToBuilder class to create compareTo method for your own class |
| 5.19.4. | Define your own equals method |
