---
title: Java Algorithms How to - Make a rock paper scissor game
nav: Java Algorithms How to - M...
description: Imported from the java2s.com archive: Java Algorithms How to - Make a rock paper scissor game
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20160730055245/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Make_a_rock_paper_scissor_game.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to make a rock paper scissor game.

## Answer

```java title=Example.java
import java.util.Random;
//fromwww.java2s.comenum Gesture {
  rock(1), paper(2), scissors(3);

  privateint type;

  Gesture(int type) {
    this.type = type;
  }

  publicint getType() {
    return type;
  }
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    String choice = "S";

    if (choice.equals("S")) {
      generateDraw(Gesture.scissors);
    } elseif (choice.equals("R")) {
      generateDraw(Gesture.rock);
    } elseif (choice.equals("P")) {
      generateDraw(Gesture.paper);
    }

  }

  publicstaticvoid generateDraw(Gesture gesture) {
    final Random random = new Random();
    finalint computerDraw = random.nextInt(3);
    System.out.println(computerDraw);

    if (computerDraw > gesture.getType()) {
      System.out.println("You lose.");
    } elseif (computerDraw < gesture.getType()) {
      System.out.println("You win.");
    } else {
      System.out.println("It is a tie.");

    }
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
