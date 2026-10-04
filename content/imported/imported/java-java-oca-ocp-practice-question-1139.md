---
title: Java OCA OCP Practice Question 1139
nav: Java OCA OCP Practice Ques...
description: What keyword is used to prevent an object from being serialized?
section: Imported - java2s Archive
order: 1110
source: https://web.archive.org/web/20210101014722/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1139.html
---
## Question

What keyword is used to prevent an object from being serialized?

- A. private
- B. volatile
- C. protected
- D. transient
- E. None of the above

```java title=Example.java
D.
```

## Note

By placing the keyword transient before an object's declaration, that value will not be included with the serialized data of the parent object.

For example,

```java title=Example.java
class T{
   privatetransientint i;

}
```

PreviousNext

## Related

- Java OCA OCP Practice Question 1136
- Java OCA OCP Practice Question 1137
- Java OCA OCP Practice Question 1138
- Java OCA OCP Practice Question 1140
- Java OCA OCP Practice Question 1141
