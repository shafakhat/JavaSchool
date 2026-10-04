---
title: Java Algorithms Reverse a String using Stack
nav: Java Algorithms Reverse a ...
description: class Reverser {/* w ww . j a va 2s. c o m*/ private String input;
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-algorithms-reverse-a-string-using-stack.html
---
## Description

```java title=Example.java
import java.util.Stack;
class Reverser { private String input;
   private String output;
   public Reverser(String in) {
      input = in;
   }
   public String doRev(){
      Stack<Character> theStack = new Stack<>();
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
public class Main {
   public static void main(String[] args) {
      Reverser theReverser = new Reverser("www.demo2s.com");
      String output = theReverser.doRev(); // use it System.out.println("Reversed: " + output);
   }
}
```

PreviousNext

## Related
