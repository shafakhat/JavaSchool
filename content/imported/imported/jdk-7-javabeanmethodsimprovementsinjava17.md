---
title: JavaBean methods improvements in Java 1.7
nav: JavaBean methods improveme...
description: Expression expression = new Expression(null, person, "setName", arguments);
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20130715210210/http://www.java2s.com:80/Code/Java/JDK-7/JavaBeanmethodsimprovementsinJava17.htm
---
JavaBean methods improvements in Java 1.7

```java title=Example.java
import java.beans.Expression;
public class Test {
  public static void main(String args[]) throws Exception {
    Person person = new Person();
    String arguments[] = { "AAA" };
    Expression expression = new Expression(null, person, "setName", arguments);
    System.out.println("Name: " + person.getName());
    expression.execute();
    System.out.println("Name: " + person.getName());
    System.out.println();
    expression = new Expression(null, person, "getName", null);
    System.out.println("Name: " + person.getName());
    expression.execute();
    System.out.println("getValue: " + expression.getValue());
  }
}
class Person {
  private String name;
  public Person() {
    this("Jane", 23);
  }
  public Person(String name, int age) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
}
```
