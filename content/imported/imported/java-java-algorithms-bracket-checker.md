---
title: Java Algorithms Bracket Checker
nav: Java Algorithms Bracket Ch...
description: privateString input; // input stringpublic BracketChecker(String in) // constructor
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-bracket-checker.html
---
## Description

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
