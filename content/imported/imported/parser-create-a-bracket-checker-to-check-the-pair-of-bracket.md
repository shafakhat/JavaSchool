---
title: Java Algorithms How to - Create a Bracket Checker to check the pair of Bracket
nav: Java Algorithms How to - C...
description: We would like to know how to create a Bracket Checker to check the pair of Bracket.
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20150410121030/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Parser/Create_a_Bracket_Checker_to_check_the_pair_of_Bracket.htm
---
```java title=Example.java
Back to Parser  ↑
```

## Question

We would like to know how to create a Bracket Checker to check the pair of Bracket.

## Answer

```java title=Example.java
import java.io.IOException;
//fromwww.java2s.compublicclass BracketChecker {
  private String input;

  public BracketChecker(String in) {
    input = in;
  }

  publicvoid check() {
    int stackSize = input.length();
    Stack theStack = new Stack(stackSize);

    for (int j = 0; j < input.length(); j++)
    {
      char ch = input.charAt(j);
      switch (ch) {
      case'{': // opening symbols
case'[':
      case'(':
        theStack.push(ch); // push them
break;

      case'}': // closing symbols
case']':
      case')':
        if (!theStack.isEmpty()) // if stack not empty,
        {
          char chx = theStack.pop(); // pop and check
if ((ch == '}' && chx != '{') || (ch == ']' && chx != '[')
              || (ch == ')' && chx != '('))
            System.out.println("Error: " + ch + " at " + j);
        } else// prematurely empty
          System.out.println("Error: " + ch + " at " + j);
        break;
      default: // no action on other characters
break;
      }
    }
    if (!theStack.isEmpty())
      System.out.println("Error: missing right delimiter");
  }

  publicstaticvoid main(String[] args) throws IOException {
    String input = "{Java [Source] (and) {[(Support)]}}";
    BracketChecker theChecker = new BracketChecker(input);
    theChecker.check();
  }

}

class Stack {
  privateint maxSize;

  privatechar[] stackArray;

  privateint top;

  public Stack(int max) {
    maxSize = max;
    stackArray = newchar[maxSize];
    top = -1;
  }

  publicvoid push(char j) {
    stackArray[++top] = j;
  }

  publicchar pop() {
    return stackArray[top--];
  }

  publicchar peek() {
    return stackArray[top];
  }

  publicboolean isEmpty() {
    return (top == -1);
  }
}
```

```java title=Example.java
Back to Parser  ↑
```
