---
title: To find out if an element is on the stack
nav: To find out if an element ...
description: Imported from the java2s.com archive: To find out if an element is on the stack
section: Imported - java2s Archive
order: 2467
source: https://web.archive.org/web/20140829084025/http://www.java2s.com/Tutorial/Java/0140__Collections/Tofindoutifanelementisonthestackthesearchmethod.htm
---
```java title=Example.java
public int search(Object element)
```

| The element at the top of the stack is at position 1. |
|---|
| Position 2 is next, then 3, and so on. |
| If the requested object is not found on the stack, -1 is returned. |

```java title=Example.java
import java.util.Stack;
public class MainClass {
  public static void main (String args[]) {
    Stack s = new Stack();
    s.push("A");
    s.push("B");
    s.push("C");
    System.out.println("Next: " + s.peek());
    s.push("D");
    System.out.println(s.pop());
    s.push("E");
    s.push("F");
    int count = s.search("E");
    while (count != -1 && count > 1) {
      s.pop();
      count--;
    }
    System.out.println(s);
  }
}
java title=Example.java
Next: C
D
[A, B, C, E]
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
