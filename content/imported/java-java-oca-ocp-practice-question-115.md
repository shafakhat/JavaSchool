---
title: Java OCA OCP Practice Question 115
nav: Java OCA OCP Practice Ques...
description: which Java implementation most closely matches this structure?
section: Imported - java2s Archive
order: 1118
source: https://web.archive.org/web/20210101014439/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-115.html
---
## Question

Given the following class diagram,

which Java implementation most closely matches this structure?

```java title=Example.java
Diagram:
    Book
+ price
+ getRating()
java title=Example.java
A.    publicclassBook {
           publicint numOfPages;
B.    publicclassBook {
           publicString getRating() {return null;}
      }
C.    publicclassBook {
           publicint price;
           publicString getRating() {return null;}
      }
D.    publicclassBook {
           void price;
      }
java title=Example.java
C.
```

## Note

Option A does not compile because it is missing the closing bracket for the class.

Option D does not compile as void is not a valid type for a variable.

Options A and D are incorrect as they are missing the getRating() method.

Option A uses an abbreviation for price.

Option B is incorrect since it is missing the price attribute.

Option C is the correct answer as it properly defines the attribute price and method getRating().

PreviousNext

## Related

- Java OCA OCP Practice Question 112
- Java OCA OCP Practice Question 113
- Java OCA OCP Practice Question 114
- Java OCA OCP Practice Question 116
- Java OCA OCP Practice Question 117
