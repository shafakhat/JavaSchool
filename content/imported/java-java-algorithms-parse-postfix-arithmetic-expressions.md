---
title: Java Algorithms Parse postfix arithmetic expressions
nav: Java Algorithms Parse post...
description: ch = input.charAt(j); // read from inputSystem.out.println(theStack);
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-parse-postfix-arithmetic-expressions.html
---
## Description

```java title=Example.java
import java.util.Stack;
class ParsePost {
   privateStack<Integer> theStack = newStack<>();
   privateString input;
   public ParsePost(String s) {
      input = s;
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
