---
title: Java Algorithms Convert infix expression to postfix expression
nav: Java Algorithms Convert in...
description: Java Algorithms Convert infix expression to postfix expression
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-algorithms-convert-infix-expression-to-postfix-expression.html
---
## Description

```java title=Example.java
import java.util.Stack;
//class InToPost
{
   private Stack<Character> theStack = new Stack<>();
   private String input;
   private String output = "";
   public InToPost(String in)   {
      input = in;
   }
   public String doTrans()
   {
      for (int j = 0; j < input.length(); j++)
      {
         char ch = input.charAt(j);
         System.out.println(theStack);
         switch (ch) {
         case '+': // it's + or - case '-':
            gotOper(ch, 1); // go pop operators break; // (precedence 1) case '*': // it's * or / case '/':
            gotOper(ch, 2); // go pop operators break; // (precedence 2) case '(': // it's a left parenthesis
            theStack.push(ch);
            break;
         case ')': // it's a right parenthesis
            gotParen(ch); // go pop operators break;
         default: // must be an operand
            output = output + ch; // write it to output break;
         }
      }
      while (!theStack.isEmpty()) // pop remaining operator
      {
         output = output + theStack.pop(); // write to output
      }
      return output;
   }
   public void gotOper(char opThis, int prec1) { // got operator from input while (!theStack.isEmpty()) {
         char opTop = theStack.pop();
         if (opTop == '(') // if it's a '('
         {
            theStack.push(opTop); // restore '(' break;
         } else // it's an operator
         {
            int prec2; // precedence of new op if (opTop == '+' || opTop == '-') // find new op prec
               prec2 = 1;
            else
               prec2 = 2;
            if (prec2 < prec1) // if prec of new op less
            { // than prec of old
               theStack.push(opTop); // save newly-popped op break;
            } else // prec of new not less
               output = output + opTop; // than prec of old
         }
      }
      theStack.push(opThis);
   }
   public void gotParen(char ch) { // got right parenthesis from input while (!theStack.isEmpty()) {
         char chx = theStack.pop();
         if (chx == '(') // if popped '(' break; // we're done else // if popped operator
            output = output + chx; // output it
      }
   }
}
public class Main {
   public static void main(String[] args) {
      String output;
      InToPost theTrans = new InToPost(" 2 3 4 + * 5 *");
      output = theTrans.doTrans(); // do the translation System.out.println("Postfix is " + output + '\n');
   }
}
```

PreviousNext

## Related
