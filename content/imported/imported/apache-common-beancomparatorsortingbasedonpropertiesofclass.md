---
title: Bean Comparator ( Sorting based on Properties of class )
nav: Bean Comparator ( Sorting ...
description: Bean Comparator ( Sorting based on Properties of class ) : Collection « Apache Common « Java
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20091208131033/http://www.java2s.com:80/Code/Java/Apache-Common/BeanComparatorSortingbasedonPropertiesofclass.htm
---
Bean Comparator ( Sorting based on Properties of class ) : Collection « Apache Common « Java

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
-------------
package com.googelcode.jpractices;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import org.apache.commons.beanutils.BeanComparator;
import com.googelcode.jpractices.common.Person;
/**
 * Copyright 2009 @ jPractices v 1.0
 * @SVN URL : http://jpractices.googlecode.com
 * @author Ganesh Gowtham
 * @Homepage : http://ganesh.gowtham.googlepages.com
 */
public class BeanComparatorExample {
  List<Person> personList = new ArrayList<Person>();
  /**
   * Basic method which creates the list of person object's
   *
   */
  void setUpData() {
    personList.add(new Person("jennefer", "gowtham", 35000));
    personList.add(new Person("britney", "spears", 45000));
    personList.add(new Person("tom", "gowtham", 36000));
    personList.add(new Person("joe", "dummy", 45000));
  }
  void sortPersons(String propertyName)
  {
    Comparator<Person> comp = new BeanComparator(propertyName);
    Collections.sort(personList, comp);
    for (Person person : personList) {
      System.out.println(person);
    }
  }
  public static void main(String[] args) {
    BeanComparatorExample beanComparatorExample = new BeanComparatorExample();
    beanComparatorExample.setUpData();
    beanComparatorExample.sortPersons("firstName");
  }
}
```

1.  Collection Bag
---  ---
2.  Transformer Example
3.  Collection BidiMap
4.  Collection Buffer
5.  Collection Closure
6.  Comparator Example For BuildIn Data Type
7.  Comparator Example For User Defined Class
8.  Cookie Bag 2
9.  Factory Example 1
10.  HashMap Example 1
11.  List Example 1
12.  MapHeaven 1
13.  Multi Key Example 1
14.  MultiKey Example 2
15.  Set Example 1
16.  Set Example 2
