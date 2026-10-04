---
title: Character Stack
nav: Character Stack
description: /*******************************************************************************
section: Imported - java2s Archive
order: 2480
source: https://web.archive.org/web/20140829083717/http://www.java2s.com/Tutorial/Java/0140__Collections/CharacterStack.htm
---
```java title=Example.java
/*******************************************************************************
 * Copyright (c) 2008 xored software, Inc.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     xored software, Inc. - initial API and Implementation (Alex Panchenko)
 *******************************************************************************/
import java.util.EmptyStackException;
public class CharacterStack {
  private char[] buffer;
  private int size;
  public CharacterStack() {
    this(16);
  }
  /**
   * @param capacity
   */
  public CharacterStack(int capacity) {
    buffer = new char[capacity];
    size = 0;
  }
  /**
   * @return
   */
  public int size() {
    return size;
  }
  /**
   * @return
   */
  public char peek() {
    final int len = size;
    if (size == 0) {
      throw new EmptyStackException();
    }
    return buffer[len - 1];
  }
  /**
   * @return
   */
  public char pop() {
    int len = size;
    if (len == 0) {
      throw new EmptyStackException();
    }
    --len;
    final char result = buffer[len];
    size = len;
    return result;
  }
  /**
   * @param c
   */
  public void push(char c) {
    if (size == buffer.length) {
      char[] newBuffer = new char[buffer.length * 2 + 1];
      System.arraycopy(buffer, 0, newBuffer, 0, buffer.length);
      buffer = newBuffer;
    }
    buffer[size++] = c;
  }
}
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
