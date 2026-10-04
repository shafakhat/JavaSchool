---
title: uses an enum, rather than interface variables, to represent the answers.
nav: uses an enum, rather than ...
description: Imported from the java2s.com archive: uses an enum, rather than interface variables, to represent the answers.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/usesanenumratherthaninterfacevariablestorepresenttheanswers.htm
---
```java title=Example.java
import java.util.Random;
enum Answers {
  NO, YES, MAYBE, LATER, SOON, NEVER
}
class Question {
  Random rand = new Random();
  Answers ask() {
    int prob = (int) (100 * rand.nextDouble());
    if (prob < 15)
      return Answers.MAYBE; // 15%
elseif (prob < 30)
      return Answers.NO; // 15%
elseif (prob < 60)
      return Answers.YES; // 30%
elseif (prob < 75)
      return Answers.LATER; // 15%
elseif (prob < 98)
      return Answers.SOON; // 13%
elsereturn Answers.NEVER; // 2%
  }
}
class AskMe {
  staticvoid answer(Answers result) {
    switch (result) {
    case NO:
      System.out.println("No");
      break;
    case YES:
      System.out.println("Yes");
      break;
    case MAYBE:
      System.out.println("Maybe");
      break;
    case LATER:
      System.out.println("Later");
      break;
    case SOON:
      System.out.println("Soon");
      break;
    case NEVER:
      System.out.println("Never");
      break;
    }
  }
  publicstaticvoid main(String args[]) {
    Question q = new Question();
    answer(q.ask());
    answer(q.ask());
    answer(q.ask());
    answer(q.ask());
  }
}
```
