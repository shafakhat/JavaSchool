---
title: Java OCA OCP Practice Question 1022
nav: Java OCA OCP Practice Ques...
description: //Insert code here publicvoid draw (){ System.out.println ("in draw ..."); }
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20210101014703/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1022.html
---
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
