---
title: Using Comparable and Comparator
nav: Using Comparable and Compa...
description: Implementing java.lang.Comparable enables you to define one way to compare instances of your class. Objects sometimes might be comparable in more ways. Comparator defines
section: Imported - java2s Archive
order: 2319
source: https://web.archive.org/web/20140223091030/http://www.java2s.com/Tutorial/Java/0140__Collections/UsingComparableandComparator.htm
---
Implementing java.lang.Comparable enables you to define one way to compare instances of your class. Objects sometimes might be comparable in more ways. Comparator defines how two objects should be compared. To make objects comparable in two ways, you need two comparators.

```java title=Example.java
import java.util.Arrays;
import java.util.Comparator;
class Person implements Comparable {
  private String firstName;
  private String lastName;
  private int age;
  public String getFirstName() {
    return firstName;
  }
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }
  public String getLastName() {
    return lastName;
  }
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }
  public int getAge() {
    return age;
  }
  public void setAge(int age) {
    this.age = age;
  }
  public int compareTo(Object anotherPerson) throws ClassCastException {
    if (!(anotherPerson instanceof Person)) {
      throw new ClassCastException("A Person object expected.");
    }
    int anotherPersonAge = ((Person) anotherPerson).getAge();
    return this.age - anotherPersonAge;
  }
}
class LastNameComparator implements Comparator {
  public int compare(Object person, Object anotherPerson) {
    String lastName1 = ((Person) person).getLastName().toUpperCase();
    String firstName1 = ((Person) person).getFirstName().toUpperCase();
    String lastName2 = ((Person) anotherPerson).getLastName().toUpperCase();
    String firstName2 = ((Person) anotherPerson).getFirstName().toUpperCase();
    if (lastName1.equals(lastName2)) {
      return firstName1.compareTo(firstName2);
    } else {
      return lastName1.compareTo(lastName2);
    }
  }
}
class FirstNameComparator implements Comparator {
  public int compare(Object person, Object anotherPerson) {
    String lastName1 = ((Person) person).getLastName().toUpperCase();
    String firstName1 = ((Person) person).getFirstName().toUpperCase();
    String lastName2 = ((Person) anotherPerson).getLastName().toUpperCase();
    String firstName2 = ((Person) anotherPerson).getFirstName().toUpperCase();
    if (firstName1.equals(firstName2)) {
      return lastName1.compareTo(lastName2);
    } else {
      return firstName1.compareTo(firstName2);
    }
  }
}
public class MainClass {
  public static void main(String[] args) {
    Person[] persons = new Person[4];
    persons[0] = new Person();
    persons[0].setFirstName("A");
    persons[0].setLastName("X");
    persons[0].setAge(56);
    persons[1] = new Person();
    persons[1].setFirstName("S");
    persons[1].setLastName("C");
    persons[1].setAge(8);
    persons[2] = new Person();
    persons[2].setFirstName("E");
    persons[2].setLastName("H");
    persons[2].setAge(16);
    persons[3] = new Person();
    persons[3].setFirstName("B");
    persons[3].setLastName("Q");
    persons[3].setAge(69);
    System.out.println("Natural Order");
    for (int i = 0; i < 4; i++) {
      Person person = persons[i];
      String lastName = person.getLastName();
      String firstName = person.getFirstName();
      int age = person.getAge();
      System.out.println(lastName + ", " + firstName + ". Age:" + age);
    }
    Arrays.sort(persons, new LastNameComparator());
    System.out.println();
    System.out.println("Sorted by last name");
    for (int i = 0; i < 4; i++) {
      Person person = persons[i];
      String lastName = person.getLastName();
      String firstName = person.getFirstName();
      int age = person.getAge();
      System.out.println(lastName + ", " + firstName + ". Age:" + age);
    }
    Arrays.sort(persons, new FirstNameComparator());
    System.out.println();
    System.out.println("Sorted by first name");
    for (int i = 0; i < 4; i++) {
      Person person = persons[i];
      String lastName = person.getLastName();
      String firstName = person.getFirstName();
      int age = person.getAge();
      System.out.println(lastName + ", " + firstName + ". Age:" + age);
    }
    Arrays.sort(persons);
    System.out.println();
    System.out.println("Sorted by age");
    for (int i = 0; i < 4; i++) {
      Person person = persons[i];
      String lastName = person.getLastName();
      String firstName = person.getFirstName();
      int age = person.getAge();
      System.out.println(lastName + ", " + firstName + ". Age:" + age);
    }
  }
}
java title=Example.java
Natural Order
X, A. Age:56
C, S. Age:8
H, E. Age:16
Q, B. Age:69
Sorted by last name
C, S. Age:8
H, E. Age:16
Q, B. Age:69
X, A. Age:56
Sorted by first name
X, A. Age:56
Q, B. Age:69
H, E. Age:16
C, S. Age:8
Sorted by age
C, S. Age:8
H, E. Age:16
X, A. Age:56
Q, B. Age:69
```

| 9.1.1. | The Collections Framework consists of three parts |
|---|---|
| 9.1.2. | Framework Interfaces |
| 9.1.3. | Interface type and its implementation |
| 9.1.4. | Conversion of different Collection data types |
| 9.1.5. | Making Your Objects Comparable and Sortable |
| 9.1.6. | Using Comparable and Comparator |
| 9.1.7. | Deep clone collection: Returns a new collection containing clones of all the items in the specified collection. |
