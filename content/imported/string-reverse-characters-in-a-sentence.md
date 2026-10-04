---
title: Java Algorithms How to - Reverse characters in a sentence
nav: Java Algorithms How to - R...
description: We would like to know how to reverse characters in a sentence.
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20170606141303/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/String/Reverse_characters_in_a_sentence.htm
---
## Question

We would like to know how to reverse characters in a sentence.

## Answer

```java title=Example.java
import java.util.Stack;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String input = "This is a sentence";
    char[] charinput = input.toCharArray();
    Stack<String> stack = new Stack<String>();
    for (int i = input.length() - 1; i >= 0; i--) {
      stack.push(String.valueOf(charinput[i]));
    }
    StringBuilder StackPush = new StringBuilder();
    for (int i = 0; i < stack.size(); i++) {
      StackPush.append(stack.get(i));
    }
    System.out.println(StackPush.toString());
  }
}
```

The code above generates the following result.
