---
title: Predicate Chain ( Chaining of two or more predicate's )
nav: Predicate Chain ( Chaining...
description: public Person(String firstName, String lastName, int salary) {
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20100212033408/http://java2s.com/Code/Java/Apache-Common/PredicateChainChainingoftwoormorepredicates.htm
---
Predicate Chain ( Chaining of two or more predicate's )

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
---------------
package com.googelcode.jpractices;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import org.apache.commons.beanutils.BeanPredicate;
import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.collections.Predicate;
import org.apache.commons.collections.PredicateUtils;
import org.apache.commons.collections.functors.EqualPredicate;
import com.googelcode.jpractices.common.Person;
/**
 * Copyright 2009 @ jPractices v 1.0
 * @SVN URL : http://jpractices.googlecode.com
 * @author Ganesh Gowtham
 * @Homepage : http://ganesh.gowtham.googlepages.com
 */
public class PredicateChainExample {
  List<Person> personList = new ArrayList<Person>();
  /**
   * Basic method which creates the list of person object's
   *
   */
  void setUpData() {
    personList.add(new Person("ganesh", "gowtham", 35000));
    personList.add(new Person("britney", "spears", 45000));
    personList.add(new Person("ganesh", "gowtham", 36000));
    personList.add(new Person("ganesh", "dummy", 45000));
  }
  /**
   *
   * Here we are adding multiple predicate
   * filters the collection so that final person object will contain
   * firstName as "ganesh" & lastName as "gowtham"
   */
  void filterDataUsingMultipleCriteria() {
    EqualPredicate firstNameEqlPredicate = new EqualPredicate("ganesh");
    BeanPredicate firtsNameBeanPredicate = new BeanPredicate("firstName", firstNameEqlPredicate);
    EqualPredicate lastNameEqlPredicate2 = new EqualPredicate("gowtham");
    BeanPredicate lastNameBeanPredicate2 = new BeanPredicate("lastName", lastNameEqlPredicate2);
    Predicate[] allPredicateArray = { firtsNameBeanPredicate, lastNameBeanPredicate2 };
    Predicate allPredicate = PredicateUtils.allPredicate(allPredicateArray);
    Collection<Person> filteredCollection = CollectionUtils.select(personList, allPredicate);
    for (Person person : filteredCollection) {
      System.out.println(person);
    }
  }
  public static void main(String[] args) {
    PredicateChainExample chainExample = new PredicateChainExample();
    chainExample.setUpData();
    chainExample.filterDataUsingMultipleCriteria();
  }
}
```

predicate_example3.zip( 811 k)
1.  Custom Predicate
