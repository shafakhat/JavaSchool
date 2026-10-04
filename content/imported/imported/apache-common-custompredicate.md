---
title: Custom Predicate
nav: Custom Predicate
description: * @description This Predicate is responsible in selecting the salary greater than iValue
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20100212033353/http://java2s.com/Code/Java/Apache-Common/CustomPredicate.htm
---
Custom Predicate

```java title=Example.java
package com.googelcode.jpractices;
import java.io.Serializable;
import org.apache.commons.collections.Predicate;
/**
 * Copyright 2009 @ jPractices v 1.0
 * @SVN URL : http://jpractices.googlecode.com
 * @author Ganesh Gowtham
 * @Homepage : http://ganesh.gowtham.googlepages.com
 * @description This Predicate is responsible in selecting the salary greater than iValue
 */
public class SalaryHighPredicate implements Predicate, Serializable {
  /** Serial version UID */
  private static final long serialVersionUID = 5633766978029907089L;
  /** The value to compare to */
  private final int iValue;
  public SalaryHighPredicate(int salary) {
    super();
    iValue = salary;
  }
  /**
   * returns true when the salary is >= iValue
   */
  public boolean evaluate(Object object) {
    if (object instanceof Integer) {
      //System.err.println("oops");
      int value = Integer.parseInt(object.toString());
      return iValue <= value ? true : false;
    } else {
      // worst case wont happend :-)
      System.err.println("pls check whether passed attribute type");
      return false;
    }
  }
}
--------------------------------------------------------------------------------------------------------------------------------------------------------------
package com.googelcode.jpractices;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import org.apache.commons.beanutils.BeanPredicate;
import org.apache.commons.collections.CollectionUtils;
import com.googelcode.jpractices.common.Person;
/**
 * Copyright 2009 @ jPractices v 1.0
 * @SVN URL : http://jpractices.googlecode.com
 * @author Ganesh Gowtham
 * @Homepage : http://ganesh.gowtham.googlepages.com
 * @Description : Writing the own predicate to filter the person objects whose salary is
 *         greater than 26000
 */
public class CustomPredicateExample {
  List<Person> personList = new ArrayList<Person>();
  /**
   * Basic method which creates the list of person object's
   */
  void setUpData() {
    personList.add(new Person("ganesh", "gowtham", 25000));
    personList.add(new Person("britney", "spears", 45000));
    personList.add(new Person("ganesh", "tom", 35000));
    personList.add(new Person("sunny", "dummy", 45000));
  }
  void filterCollection(int salary)
  {
    SalaryHighPredicate nameEqlPredicate = new SalaryHighPredicate(salary);
    BeanPredicate beanPredicate = new BeanPredicate("salary", nameEqlPredicate);
    Collection<Person> filteredCollection = CollectionUtils
          .select(personList, beanPredicate);
    System.out.println("Shows the person object whose salary is >= 26,000 ");
    for (Person person : filteredCollection) {
      System.out.println(person);
    }
  }
  public static void main(String[] args) {
    CustomPredicateExample example = new CustomPredicateExample();
    example.setUpData();
    example.filterCollection(26000);
  }
}
---------------------------------------------------------------------------------------------------------------------------------------------------------
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
```

predicate_example1.zip( 811 k)
