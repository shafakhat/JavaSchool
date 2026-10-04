---
title: Java OCA OCP Practice Question 1017
nav: Java OCA OCP Practice Ques...
description: Although the definition of methods on lines 2 and 5 vary, both will be converted to public abstract by the compiler.
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20210101014702/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1017.html
---
## Question

Choose the correct statement about the following code:

```java title=Example.java
1: publicinterfacePrintable {
2:   void fly();
3: }
4: interfaceArea {
5:   publicabstractObject getArea();
6: }
7: abstractclass Falcon implementsPrintable, Area {
8: }
```

- A. It compiles without issue.
- B. The code will not compile because of line 2.
- C. The code will not compile because of line 4.
- D. The code will not compile because of line 5.
- E. The code will not compile because of lines 2 and 5.
- F. The code will not compile because the class Falcon doesn't implement the interface methods.

```java title=Example.java
A.
```

## Note

Although the definition of methods on lines 2 and 5 vary, both will be converted to public abstract by the compiler.

Line 4 is fine, because an interface can have public or default access.

Finally, the class Falcon doesn't need to implement the interface methods because it is marked as abstract.

Therefore, the code will compile without issue.

PreviousNext

## Related

- Java OCA OCP Practice Question 1014
- Java OCA OCP Practice Question 1015
- Java OCA OCP Practice Question 1016
- Java OCA OCP Practice Question 1018
- Java OCA OCP Practice Question 1019
