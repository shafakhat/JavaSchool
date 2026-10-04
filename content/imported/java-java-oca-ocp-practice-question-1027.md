---
title: Java OCA OCP Practice Question 1027
nav: Java OCA OCP Practice Ques...
description: Option B is incorrect, since an abstract class could implement Printable without the need to override the print() method.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1027.html
---
## Question

Which statements are true about the following code?

Choose all that apply

```java title=Example.java
1: interfacePrintable {
2:   publicabstractvoid print();
3: }
4: publicinterface Writable extendsPrintable {
5:   publicvoid write();
6: }
```

- A. The Writable interface doesn't compile.
- B. A class that implements Printable must override the print() method.
- C. A class that implements Writable inherits both the print() and write() methods.
- D. A class that implements Writable only inherits the write() method.
- E. An interface cannot extend another interface.

```java title=Example.java
C.
```

## Note

The code compiles without issue, so option A is wrong.

Option B is incorrect, since an abstract class could implement Printable without the need to override the print() method.

Option C is correct; any class that implements Writable automatically inherits its methods, as well as any inherited methods defined in the parent interface. Because option C is correct, it follows that option D is incorrect.

Finally, an interface can extend multiple interfaces, so option E is incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1025
- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1029
