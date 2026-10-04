---
title: Java Algorithms Parse postfix arithmetic expressions
nav: Java Algorithms Parse post...
description: ch = input.charAt(j); // read from inputSystem.out.println(theStack);
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-parse-postfix-arithmetic-expressions.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Parse postfix arithmetic expressions

```java title=Example.java
import java.util.Stack;

class ParsePost {
   privateStack<Integer> theStack = newStack<>();
   privateString input;

   public ParsePost(String s) {
      input = s;//www.java2s.com
   }
   publicint doParse() {
      char ch;
      int j;
      int num1, num2, interAns;

      for (j = 0; j < input.length(); j++) // for each char,
      {
         ch = input.charAt(j); // read from inputSystem.out.println(theStack);
         if (ch >= '0' && ch <= '9') // if it's a number
            theStack.push((int) (ch - '0')); // push itelse// it's an operator
         {
            num2 = theStack.pop(); // pop operands
            num1 = theStack.pop();
            switch (ch) // do arithmetic
            {
            case'+':
               interAns = num1 + num2;
               break;
            case'-':
               interAns = num1 - num2;
               break;
            case'*':
               interAns = num1 * num2;
               break;
            case'/':
               interAns = num1 / num2;
               break;
            default:
               interAns = 0;
            } // end switch
            theStack.push(interAns); // push result
         }
      }
      interAns = theStack.pop(); // get answerreturn interAns;
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      int output;
      ParsePost aParser = new ParsePost("345+*612+/-");
      output = aParser.doParse();
      System.out.println("Evaluates to " + output);
   }
}
```

PreviousNext

## Related

- Java Algorithms Convert number to French words
- Java Algorithms Huffman code
- Java Algorithms Move along circle
- Java Algorithms Reverse a String using Stack
- Java Algorithms Search Binary Search
