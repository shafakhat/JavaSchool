---
title: Java OCA OCP Practice Question 1026
nav: Java OCA OCP Practice Ques...
description: if (flag) //1 if (flag) //2 System.out.println ("True False");
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1026.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Consider the following method...

```java title=Example.java
publicvoid ifTest (boolean flag){
   if  (flag)   //1 if  (flag)   //2 System.out.println ("True False");
   else// 3 System.out.println ("True True");
   else// 4 System.out.println ("False False");
}
```

Which of the following statements are correct ?

Select 3 options

- A. If run with an argument of 'false', it will print 'False False'
- B. If run with an argument of 'false', it will print 'True True'
- C. If run with an argument of 'true', it will print 'True False'
- D. It will never print 'True True'
- E. It will not compile.

```java title=Example.java
Correct Options are  : A C D
```

## Note

Note that if and else do not cascade. They are like opening and closing braces.

```java title=Example.java
if  (flag)   //1 if  (flag)   //2 System.out.println ("True False");
       else// 3 This closes //2 System.out.println ("True True");
   else// 4 This closes //1 System.out.println ("False False");
```

So, else at //3 is associated with if at //2 and else at //4 is associated with if at // 1

PreviousNext

## Related

- Java OCA OCP Practice Question 1023
- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1025
- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1028
