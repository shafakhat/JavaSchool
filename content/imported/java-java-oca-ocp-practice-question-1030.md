---
title: Java OCA OCP Practice Question 1030
nav: Java OCA OCP Practice Ques...
description: What should be inserted in the code given below at line marked // 10:
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1030.html
---
## Question

What should be inserted in the code given below at line marked // 10:

```java title=Example.java
class MyClass{
}
class MyComparable implementsComparable<MyClass>{
   publicint compareTo (  *INSERT CODE HERE*  x ){ //10 return 0;
    }
}
```

Select 1 option

- A. Object
- B. MyClass
- C. Object<MyClass>
- D. Comparable<MyClass>
- E. Comparable

```java title=Example.java
Correct Option is  : B
```

## Note

Since MyComparable class specifies that it implements the Comparable interface that has been typed to MyClass, it must implement compareTo() method that takes a MyClass.

Had it not declared a typed Comparable in its implements clause, compareTo(Object x) would have been correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1029
- Java OCA OCP Practice Question 1031
- Java OCA OCP Practice Question 1032
