---
title: Java OCA OCP Practice Question 1044
nav: Java OCA OCP Practice Ques...
description: } //fromwww.java2s.compublicstaticvoid main (String [] args){
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20210101014707/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1044.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the result of compiling and running this code?

```java title=Example.java
class MyException extendsThrowable{}
class MyException1 extends MyException{}
class MyException2 extends MyException{}
class MyException3 extends MyException2{}

publicclass Main{
   void myMethod () throws MyException{
      thrownew MyException3 ();
    } //fromwww.java2s.compublicstaticvoid main (String [] args){
      Main et = new Main ();
      try{
         et.myMethod ();
       }
      catch (MyException me){
         System.out.println ("MyException thrown");
       }
      catch (MyException3 me3){
         System.out.println ("MyException3 thrown");
       }
      finally{
         System.out.println (" Done");
       }
    }
}
```

Select 1 option

- A. MyException thrown
- B. MyException3 thrown
- C. MyException thrown Done D. MyException3 thrown Done
- E. It fails to compile

```java title=Example.java
Correct Option is  : E
```

## Note

You can have multiple catch blocks to catch different kinds of exceptions, including exceptions that are subclasses of other exceptions.

The catch clause for more specific exceptions should come before the catch clause for more general exceptions.

Failure to do so results in a compiler error as the more specific exception is unreachable.

catch for MyException3 cannot follow catch for MyException because if MyException3 is thrown, it will be caught by the catch clause for MyException.

There is no way the catch clause for MyException3 can ever execute.

And so it becomes an "unreachable" statement.

PreviousNext

## Related

- Java OCA OCP Practice Question 1041
- Java OCA OCP Practice Question 1042
- Java OCA OCP Practice Question 1043
- Java OCA OCP Practice Question 1045
- Java OCA OCP Practice Question 1046
