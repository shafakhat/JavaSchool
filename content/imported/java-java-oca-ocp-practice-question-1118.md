---
title: Java OCA OCP Practice Question 1118
nav: Java OCA OCP Practice Ques...
description: class MyClass{ //fromwww.java2s.compublicvoid play () throwsException{
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20210101014719/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1118.html
---
## Question

What will the following program print when compiled and run?

```java title=Example.java
class MyClass{ publicvoid play () throwsException{
    System.out.println ("Playing...");
   }
}
publicclass MySubClass extends MyClass{
   publicvoid play (){
      System.out.println ("Playing MySubClass...");
    }
   publicstaticvoid main (String [] args){
       MyClass g = new MySubClass ();
       g.play ();
    }
}
```

Select 1 option

- A. It will not compile.
- B. It will throw an Exception at runtime.
- C. Playing MySubClass...
- D. Playing...
- E. None of these.

```java title=Example.java
Correct Option is  : A
```

## Note

Observe that play() in MyClass declares Exception in its throws clause.

class MySubClass overrides the play() method without any throws clause.

This is valid because a list of no exception is a valid subset of a list of exceptions thrown by the superclass method.

Now, even though the actual object referred to by 'g' is of class MySubClass, the class of the variable g is of class MyClass.

At compile time, compiler assumes that g.play() might throw an exception, because MyClass's play method declares it, and thus expects this call to be either wrapped in a try-catch or the main method to have a throws clause for the main() method.

PreviousNext

## Related

- Java OCA OCP Practice Question 1115
- Java OCA OCP Practice Question 1116
- Java OCA OCP Practice Question 1117
- Java OCA OCP Practice Question 1119
- Java OCA OCP Practice Question 1120
