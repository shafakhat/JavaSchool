---
title: Java OCA OCP Practice Question 1133
nav: Java OCA OCP Practice Ques...
description: What will be the result of attempting to compile and run the following program?
section: Imported - java2s Archive
order: 1107
source: https://web.archive.org/web/20210101014721/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1133.html
---
## Question

What will be the result of attempting to compile and run the following program?

```java title=Example.java
publicclass Main{
   publicstaticvoid main (String args []){
      boolean b = false;
      int i = 1;
      do{ /*fromwww.java2s.com*/
         i++ ;
       } while  (b =  !b);
      System.out.println ( i );
    }
}
```

Select 1 option

- A. The code will fail to compile, 'while' has an invalid condition expression.
- B. It will compile but will throw an exception at runtime.
- C. It will print 3.
- D. It will go in an infinite loop.
- E. It will print 1.

```java title=Example.java
Correct Option is  : C
```

## Note

A. is wrong.

It is perfectly valid because b = !b; returns a boolean, which is what is needed for while condition.

The 'do {} while()' loop executes at least once because the condition is checked after the iteration.

PreviousNext

## Related

- Java OCA OCP Practice Question 1130
- Java OCA OCP Practice Question 1131
- Java OCA OCP Practice Question 1132
- Java OCA OCP Practice Question 1134
- Java OCA OCP Practice Question 1135
