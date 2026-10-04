---
title: Java OCA OCP Practice Question 1008
nav: Java OCA OCP Practice Ques...
description: Which statement(s) are correct about the following code? (Choose all that apply)
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1008.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which statement(s) are correct about the following code? (Choose all that apply)

```java title=Example.java
publicclassRectangle {
  protectedstaticInteger chew() throwsException {
    System.out.println("Rectangle is printing");
    return 1; /*fromwww.java2s.com*/
  }
}
publicclass Square extendsRectangle {
  publicNumber chew() throwsRuntimeException {
    System.out.println("Square is printing on wood");
    return 2;
  }
}
```

- A. It will compile without issue.
- B. It fails to compile because the type of the exception the method throws is a subclass of the type of exception the parent method throws.
- C. It fails to compile because the return types are not covariant.
- D. It fails to compile because the method is protected in the parent class and public in the subclass.
- E. It fails to compile because of a static modifier mismatch between the two methods.

```java title=Example.java
C, E.
```

## Note

The code doesn't compile, so option A is incorrect.

Option B is also not correct because the rules for overriding a method allow a subclass to define a method with an exception that is a subclass of the exception in the parent method.

Option C is correct because the return types are not covariant; in particular, Number is not a subclass of Integer.

Option D is incorrect because the subclass defines a method that is more accessible than the method in the parent class, which is allowed.

Finally, option E is correct because the method is declared as static in the parent class and not so in the child class.

For non-private methods in the parent class, both methods must use static (hide) or neither should use static (override).

PreviousNext

## Related

- Java OCA OCP Practice Question 1005
- Java OCA OCP Practice Question 1006
- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1009
- Java OCA OCP Practice Question 1010
