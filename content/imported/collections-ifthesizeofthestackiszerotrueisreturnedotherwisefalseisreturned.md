---
title: If the size of the stack is zero, true is returned; otherwise, false is returned
nav: If the size of the stack i...
description: Imported from the java2s.com archive: If the size of the stack is zero, true is returned; otherwise, false is returned
section: Imported - java2s Archive
order: 2465
source: https://web.archive.org/web/20140829084242/http://www.java2s.com/Tutorial/Java/0140__Collections/Ifthesizeofthestackiszerotrueisreturnedotherwisefalseisreturned.htm
---
```java title=Example.java
import java.util.Stack;
public class MainClass {
  public static void main (String args[]) {
    Stack s = new Stack();
    s.push("A");
    s.push("B");
    s.push("C");
    System.out.println(s.pop());
    System.out.println(s.empty());
  }
}
java title=Example.java
C
false
```

| 9.13.1. | Stack Basics: last-in, first-out behavior |
|---|---|
| 9.13.2. | Adding Elements: To add an element to a stack, call the push() method |
| 9.13.3. | Removing Elements: To remove an element from the stack, the pop() method |
| 9.13.4. | If the size of the stack is zero, true is returned; otherwise, false is returned |
| 9.13.5. | Checking the Top: To get the element without removing: using the peek() method |
| 9.13.6. | To find out if an element is on the stack: the search() method |
| 9.13.7. | Demonstrate the generic Stack class. |
| 9.13.8. | A faster, smaller stack implementation. |
| 9.13.9. | A simple integer based stack. |
| 9.13.10. | A stack of simple integers |
| 9.13.11. | A very simple unsynchronized stack. This one is faster than the java.util-Version. |
| 9.13.12. | An implementation of the java.util.Stack based on an ArrayList instead of a Vector, so it is not synchronized to protect against multi-threaded access. |
| 9.13.13. | Character Stack |
| 9.13.14. | Growable Object stack with type specific access methods |
| 9.13.15. | Growable String stack with type specific access methods. |
| 9.13.16. | Growable int stack with type specific access methods |
| 9.13.17. | Stack for boolean values |
| 9.13.18. | extends ArrayList to create Stack |
