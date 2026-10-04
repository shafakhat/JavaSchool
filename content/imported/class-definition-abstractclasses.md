---
title: Abstract Classes
nav: Abstract Classes
description: Provide a contract between a service provider and its clients. An abstract class can provide implementation. To make an abstract method, use the abstract modifier in fron
section: Imported - java2s Archive
order: 1474
source: https://web.archive.org/web/20140829074657/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/AbstractClasses.htm
---
Provide a contract between a service provider and its clients. An abstract class can provide implementation. To make an abstract method, use the abstract modifier in front of the method declaration.

```java title=Example.java
public abstract class DefaultPrinter {
  public String toString() {
    return "Use this to print documents.";
  }
  public abstract void print(Object document);
}
```

The toString method has an implementation, so you do not need to override this method. The print method is declared abstract and does not have a body.

```java title=Example.java
public class MyPrinter extends DefaultPrinter {
  public void print(Object document) {
    System.out.println("Printing document");
    // some code here
  }
}
```

| 5.28.1. | Abstract Classes |
|---|---|
| 5.28.2. | A demonstration of abstract. |
| 5.28.3. | Using abstract methods and classes. |
