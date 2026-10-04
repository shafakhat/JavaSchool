---
title: JPA Tutorial - JPA Introduction
nav: JPA Tutorial - JPA Introdu...
description: The domain model has a class. The database has a table. JPA is a simple way to convert one to the other automatically.
section: Imported - java2s Archive
order: 50036
source: https://www.java2s.com/Tutorials/Java/JPA/index.html
---
- Next »

## Object-Relational Mapping

The domain model has a class. The database has a table. JPA is a simple way to convert one to the other automatically.

The technique of bridging the gap between the object model and the relational model is known as object-relational mapping, or O-R mapping or simply ORM.

## Creating an Entity

Regular Java classes can be transformed into entities by annotating them.

Let's start by creating a regular Java class for an employee.

```java title=Example.java
publicclass Employee {
  privateint id;
  private String name;
//fromwww.java2s.compublic Employee() {
  }
  public Employee(int id) {
    this.id = id;
  }
  publicint getId() {
    return id;
  }
  publicvoid setId(int id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
}
```

This class resembles a JavaBean-style class with two properties: id and name.

Each of these properties is represented by a pair of accessor methods to get and set the property, and is backed by a member field.

To turn Employee into an entity, we first annotate the class with @Entity. It is a marker annotation to indicate to the persistence engine that the class is an entity.

Then we use @Id annotation to mark a field as the primary key.

The following code shows the entity class.

```java title=Example.java

@Entity
publicclass Employee {
  @Id
  private int id;
  private String name;
  public Employee() {
  }
  public Employee(int id) {
    this.id = id;
  }
  public int getId() {
    return id;
  }
  public void setId(int id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
}
```

- Next »
