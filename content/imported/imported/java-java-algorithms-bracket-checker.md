---
title: Java Algorithms Bracket Checker
nav: Java Algorithms Bracket Ch...
description: privateString input; // input stringpublic BracketChecker(String in) // constructor
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-bracket-checker.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Bracket Checker

```java title=Example.java
import java.util.Stack;

class BracketChecker {
   privateString input; // input stringpublic BracketChecker(String in) // constructor
   {/*www.java2s.com*/
      input = in;
   }

   publicvoid check() {
      Stack<Character> theStack = newStack<>(); // make stackfor (int j = 0; j < input.length(); j++) // get chars in turn
      {
         char ch = input.charAt(j); // get charswitch (ch) {
         case'{': // opening symbolscase'[':
         case'(':
            theStack.push(ch); // push thembreak;

         case'}': // closing symbolscase']':
         case')':
            if (!theStack.isEmpty()) {
               char chx = theStack.pop(); // pop and checkif ((ch == '}' && chx != '{') || (ch == ']' && chx != '[') || (ch == ')' && chx != '('))
                  System.out.println("Error: " + ch + " at " + j);
            } else// prematurely emptySystem.out.println("Error: " + ch + " at " + j);
            break;
         default: // no action on other charactersbreak;
         }
      }
      if (!theStack.isEmpty())
         System.out.println("Error: missing right delimiter");
      else {
         System.out.println("no error");
      }
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      BracketChecker theChecker = new BracketChecker("(a+b)+{(4+5)+r[1]+a()}")  ;
      theChecker.check(); // check brackets
   }
}
```

PreviousNext

## Related

- Java static Import
- Java Algorithms Binary Search Tree
- Java Algorithms Binary Search Tree Animation
- Java Algorithms Convert infix expression to postfix expression
- Java Algorithms Convert number to English words
