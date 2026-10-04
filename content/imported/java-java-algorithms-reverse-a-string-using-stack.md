---
title: Java Algorithms Reverse a String using Stack
nav: Java Algorithms Reverse a ...
description: String output = theReverser.doRev(); // use itSystem.out.println("Reversed: " + output);
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-reverse-a-string-using-stack.html
---
## Description

```java title=Example.java
import java.util.Stack;
class Reverser {privateString input;
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
