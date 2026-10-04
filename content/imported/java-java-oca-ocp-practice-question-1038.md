---
title: Java OCA OCP Practice Question 1038
nav: Java OCA OCP Practice Ques...
description: Which of the following statements can be inserted in the blank so that the code will compile successfully?
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20210101014706/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1038.html
---
## Question

Which of the following statements can be inserted in the blank so that the code will compile successfully?

Choose all that apply

```java title=Example.java
publicclass Animal {}
publicclass Pet extends Animal {}
publicclass Fish {}
publicclass Main {
  private Animal snake;
  publicvoid setAnimal(Animal snake) { this.snake = snake; }
  publicstaticvoid main(String[] args) {
    new Main().setAnimal(  ___   );
  }
}
```

- A. new Pet()
- B. new Fish()
- C. new Animal()
- D. new Object()
- E. new String("Animal")
- F. null

```java title=Example.java
A, C, F.
```

## Note

First off, Pet is a subclass of Animal, so option A can be used.

Fish is not defined as a subclass of Animal, so it cannot be used and option B is incorrect.

The class Animal is not marked as abstract, so it can be instantiated and passed, so option C is correct.

Next, Object is a superclass of Animal, not a subclass, so it also cannot be used and option D is incorrect.

The class String is unrelated in this example, so option E is incorrect.

Finally, a null value can always be passed as an object value, regardless of type, so option F is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1035
- Java OCA OCP Practice Question 1036
- Java OCA OCP Practice Question 1037
- Java OCA OCP Practice Question 1039
- Java OCA OCP Practice Question 1040
