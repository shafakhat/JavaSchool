---
title: Java OCA OCP Practice Question 1065
nav: Java OCA OCP Practice Ques...
description: The non-static s variable may only be accessed with a reference to a Main object.
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20210101014710/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1065.html
---
## Question

What is wrong with the following program?

```java title=Example.java
class Main {
   String s = "abc";

   publicstaticvoid main(String[] args) {
      System.out.println(s);
   }

}
```

- A. Nothing is wrong with the program.
- B. main() cannot be declared public because Main is not public.
- C. Because main() is static, it may not access non-static s without a reference to an instance of Main.
- D. The main() argument list is incorrect.

```java title=Example.java
C.
```

## Note

The non-static s variable may only be accessed with a reference to a Main object.

PreviousNext

## Related

- Java OCA OCP Practice Question 1062
- Java OCA OCP Practice Question 1063
- Java OCA OCP Practice Question 1064
- Java OCA OCP Practice Question 1066
- Java OCA OCP Practice Question 1067
