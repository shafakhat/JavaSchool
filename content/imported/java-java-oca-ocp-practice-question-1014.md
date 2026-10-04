---
title: Java OCA OCP Practice Question 1014
nav: Java OCA OCP Practice Ques...
description: The interface variable amount is correctly declared, with public and static being assumed and automatically inserted by the compiler, so option B is incorrect.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20210101014702/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1014.html
---
## Question

Choose the correct statement about the following code:

```java title=Example.java
1: publicinterface Pet {
2:   int amount = 10;
3:   publicstaticvoid eatGrass();
4:   publicint chew() {
5:     return 13;
6:   }
7: }
```

- A. It compiles and runs without issue.
- B. The code will not compile because of line 2.
- C. The code will not compile because of line 3.
- D. The code will not compile because of line 4.
- E. The code will not compile because of lines 2 and 3.
- F. The code will not compile because of lines 3 and 4.

```java title=Example.java
F.
```

## Note

The interface variable amount is correctly declared, with public and static being assumed and automatically inserted by the compiler, so option B is incorrect.

The method declaration for eatGrass() on line 3 is incorrect because the method has been marked as static but no method body has been provided.

The method declaration for chew() on line 4 is also incorrect, since an interface method that provides a body must be marked as default or static explicitly.

Therefore, option F is the correct answer since this code contains two compile-time errors.

PreviousNext

## Related

- Java OCA OCP Practice Question 1011
- Java OCA OCP Practice Question 1012
- Java OCA OCP Practice Question 1013
- Java OCA OCP Practice Question 1015
- Java OCA OCP Practice Question 1016
