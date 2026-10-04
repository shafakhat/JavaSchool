---
title: Bean Predicate with Equal Predicate
nav: Bean Predicate with Equal ...
description: public Person(String firstName, String lastName, int salary) {
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20100212033357/http://java2s.com/Code/Java/Apache-Common/BeanPredicatewithEqualPredicate.htm
---
Bean Predicate with Equal Predicate

```java title=Example.java
package com.googelcode.jpractices.common;
import org.apache.commons.lang.builder.ToStringBuilder;
/**
 * Copyright 2009 @ jPractices v 1.0
 * @SVN URL : http://jpractices.googlecode.com
 * @author Ganesh Gowtham
 * @Homepage : http://ganesh.gowtham.googlepages.com
 */
public class Person {
  private String firstName;
  private String lastName;
  private int salary;
  public Person(String firstName, String lastName, int salary) {
    super();
    this.firstName = firstName;
    this.lastName = lastName;
    this.salary = salary;
  }
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
  public int getSalary() {
    return salary;
  }
  public void setSalary(int salary) {
    this.salary = salary;
  }
  @Override
  public String toString() {
    return ToStringBuilder.reflectionToString(this);
  }
}
--------------------------------
package com.googelcode.jpractices;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import org.apache.commons.beanutils.BeanPredicate;
import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.collections.functors.EqualPredicate;
import com.googelcode.jpractices.common.Person;
/**
 * Copyright 2009 @ jPractices v 1.0
 * @SVN URL : http://jpractices.googlecode.com
 * @author Ganesh Gowtham
 * @Homepage : http://ganesh.gowtham.googlepages.com
 *
 */
public class PredicateExample {
  List<Person> personList = new ArrayList<Person>();
  /**
   * Basic method which creates the list of person object's
   *
   */
  void setUpData() {
    personList.add(new Person("ganesh", "gowtham", 25000));
    personList.add(new Person("britney", "spears", 45000));
    personList.add(new Person("ganesh", "tom", 35000));
    personList.add(new Person("sunny", "dummy", 45000));
  }
  /**
   * select's the Person object's from collection of person objects based on arg
   * @param propertyName - Person's attribute (firstName (or) lastName (or) salary )
   * @param value - Value to be compared to propertyName
   */
  void selectObjectsByName(String propertyName, String value) {
    EqualPredicate nameEqlPredicate = new EqualPredicate(value);
    BeanPredicate beanPredicate = new BeanPredicate(propertyName, nameEqlPredicate);
    Collection<Person> filteredCollection = CollectionUtils.select(personList, beanPredicate);
    System.out.println("Below are person object(s) whose " + propertyName + " is " + value);
    System.out.println("Matches for entered criteria "
        + CollectionUtils.countMatches(personList, beanPredicate));
    for (Person person : filteredCollection) {
      System.out.println(person);
    }
  }
  /**
   * select's the person object from collcetion based on propetyName and value
   * @param propertyName - Person's attribute (firstName (or) lastName (or) salary )
   * @param value - Value to be compared to propertyName
   */
  void selectObjectFromCollection(String propertyName, String value) {
    EqualPredicate nameEqlPredicate = new EqualPredicate(value);
    BeanPredicate beanPredicate = new BeanPredicate(propertyName, nameEqlPredicate);
    System.out.println("Below are person object whose " + propertyName + " is " + value);
    System.out.println(CollectionUtils.find(personList, beanPredicate));
  }
  public static void main(String[] args) {
    PredicateExample example = new PredicateExample();
    example.setUpData();
    example.selectObjectsByName("firstName", "ganesh");
    example.selectObjectFromCollection("firstName", "britney");
  }
}
```

predicate_example2.zip( 811 k)
1.  Custom Predicate
