---
title: Java Algorithms Reverse a String using Stack
nav: Java Algorithms Reverse a ...
description: String output = theReverser.doRev(); // use itSystem.out.println("Reversed: " + output);
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-reverse-a-string-using-stack.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Reverse a String using Stack

```java title=Example.java
import java.util.Stack;

class Reverser {/*www.java2s.com*/privateString input;
   privateString output;

   public Reverser(String in) {
      input = in;
   }

   publicString doRev(){
      Stack<Character> theStack = newStack<>();
      for (int j = 0; j < input.length(); j++) {
         char ch = input.charAt(j); // get a char from input
         theStack.push(ch); // push it
      }
      output = "";
      while (!theStack.isEmpty()) {
         char ch = theStack.pop(); // pop a char,
         output = output + ch; // append to output
      }
      return output;
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      Reverser theReverser = new Reverser("www.demo2s.com");
      String output = theReverser.doRev(); // use itSystem.out.println("Reversed: " + output);
   }
}
```

PreviousNext

## Related

- Java Algorithms Huffman code
- Java Algorithms Move along circle
- Java Algorithms Parse postfix arithmetic expressions
- Java Algorithms Search Binary Search
- Java Algorithms Search Linear Search
