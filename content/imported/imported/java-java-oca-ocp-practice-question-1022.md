---
title: Java OCA OCP Practice Question 1022
nav: Java OCA OCP Practice Ques...
description: //Insert code here publicvoid draw (){ System.out.println ("in draw ..."); }
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20210101014703/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1022.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Given:

```java title=Example.java
//Insert code here   publicabstractvoid draw ();
}

//Insert code here publicvoid draw (){  System.out.println ("in draw ...");  }
}
```

Which of the following lines of code can be used to complete the above code?

Select 2 options

```java title=Example.java

A. classShape  {
   and /*fromwww.java2s.com*/class Circle  extendsShape  {

B. publicclassShape  {
   and
   class Circle  extendsShape  {

C. abstractShape  {
   and
   publicclass Circle  extendsShape  {

D. publicabstractclassShape  {
   and
   class Circle  extendsShape  {

E. publicabstractclassShape  {
   and
   class Circle  implementsShape  {

F. publicinterfaceShape  {
   and
   class Circle  implementsShape  {
```

```java title=Example.java
Correct Options are  : D F
```

## Note

A. is wrong. Since there is an abstract method in the first class, the class must be declared abstract.

C. is wrong. class keyword is missing from the first declaration.

E. is wrong. You can only implement an interface not a class. So Circle implements shape is wrong.

F. is correct. By default all the methods of an interface are public and abstract so there is no need to explicitly specify the "abstract" keyword for the draw() method if you make Shape an interface. But it is not wrong to do so.

PreviousNext

## Related

- Java OCA OCP Practice Question 1019
- Java OCA OCP Practice Question 1020
- Java OCA OCP Practice Question 1021
- Java OCA OCP Practice Question 1023
- Java OCA OCP Practice Question 1024
