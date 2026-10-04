---
title: Java OCA OCP Practice Question 1112
nav: Java OCA OCP Practice Ques...
description: The display() method of SuperClass is invoked to display the s variable of Question.
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20210101014718/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1112.html
---
## Question

What is the output of the following program?

```java title=Example.java
class Question extends SuperClass {
   String s = "this";

   publicstaticvoid main(String[] args) {
      new Question();
   }/*fromwww.java2s.com*/

   Question() {
      super.display(s);
   }

   void display(String s) {
      System.out.println("this: " + s);
   }
}

class SuperClass {
   String s = "super";

   void display(String s) {
      System.out.println("super: " + s);
   }
}
```

- A. this: this
- B. super: this
- C. this: super
- D. super: super

```java title=Example.java
B.
```

## Note

The display() method of SuperClass is invoked to display the s variable of Question.

PreviousNext

## Related

- Java OCA OCP Practice Question 1109
- Java OCA OCP Practice Question 1110
- Java OCA OCP Practice Question 1111
- Java OCA OCP Practice Question 1113
- Java OCA OCP Practice Question 1114
