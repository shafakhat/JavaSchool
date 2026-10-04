---
title: Java JUnit Tutorial - JUnit Introduction
nav: Java JUnit Tutorial - JUni...
description: Testing is the process of checking the functionality of an application.
section: Imported - java2s Archive
order: 50043
source: https://www.java2s.com/Tutorials/Java/JUnit/index.html
---
Testing is the process of checking the functionality of an application.

Unit testing is the testing of single entity, a class or a method.

Unit testing can be done in two ways

- Manual
- Automated

A Unit Test Case is a part of code which ensures that the another part of code works as expected.

For example, we have the following method which calculate the sum of two integers.

```java title=Example.java
publicstatic int sum(int i, int j){
   return i+j;
}
```

We can have the following test cases to check the implementation is correct.

```java title=Example.java
int i = 2;
int j = 3;
int expectedResult = 5;
TestUtil.ensure(expectedResult, sum(i,j));
```

## What is JUnit

JUnit is a unit testing framework for the Java programming language.

JUnit is an open source framework which is used for writing & running tests. JUnit promotes the idea of "testing first" rather than implementing first.

JUnit provides Annotation to identify the test methods and utility methods to assert expected results.

JUnit has Test runners for running tests.

JUnit tests can be organized into test suites which contains test cases and other test suites.

JUnit Framework can be easily integrated with either of the followings:

- Eclipse
- Ant
- Maven
