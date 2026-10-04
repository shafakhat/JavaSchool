---
title: Java OCA OCP Practice Question 1100
nav: Java OCA OCP Practice Ques...
description: Which lines contain a valid constructor in the following code?
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20210101014716/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1100.html
---
## Question

Which lines contain a valid constructor in the following code?

```java title=Example.java
publicclass Main{
   public Main (int a, int b)  {  } // 1 publicvoid Main (int a)  {  }   // 2 public Main (String s); // 3 private Main (String s, int a)  {  }     //4 public Main (String s1, String s2)  {  }; //5
}
```

Select 3 options

- A. Line // 1
- B. Line // 2
- C. Line // 3
- D. Line // 4
- E. Line // 5

```java title=Example.java
Correct Options are  : A D E
```

## Note

Constructors cannot return anything. Not even void.

Constructors cannot have empty bodies (i.e. they cannot be abstract)

You can apply public, private, protected to a constructor.

But not static, final, synchronized, native and abstract.

The compiler ignores the extra semi-colon.

It is interesting to note that public void Main (int a) {} // 2 will actually compile.

It is not a constructor, but compiler considers it as a valid method!

PreviousNext

## Related

- Java OCA OCP Practice Question 1097
- Java OCA OCP Practice Question 1098
- Java OCA OCP Practice Question 1099
- Java OCA OCP Practice Question 1101
- Java OCA OCP Practice Question 1102
