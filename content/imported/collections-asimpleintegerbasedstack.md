---
title: A simple integer based stack.
nav: A simple integer based sta...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2474
source: https://web.archive.org/web/20140829083741/http://www.java2s.com/Tutorial/Java/0140__Collections/Asimpleintegerbasedstack.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 *
 * moved to org.apache.xerces.util by neilg to support the
 * XPathMatcher.
 * @author  Andy Clark, IBM
 *
 * @version $Id: IntStack.java 447241 2006-09-18 05:12:57Z mrglavas $
 */
public final class IntStack {
    //
    // Data
    //
    /** Stack depth. */
    private int fDepth;
    /** Stack data. */
    private int[] fData;
    //
    // Public methods
    //
    /** Returns the size of the stack. */
    public int size() {
        return fDepth;
    }
    /** Pushes a value onto the stack. */
    public void push(int value) {
        ensureCapacity(fDepth + 1);
        fData[fDepth++] = value;
    }
    /** Peeks at the top of the stack. */
    public int peek() {
        return fData[fDepth - 1];
    }
    /** Returns the element at the specified depth in the stack. */
    public int elementAt(int depth) {
        return fData[depth];
    }
    /** Pops a value off of the stack. */
    public int pop() {
        return fData[--fDepth];
    }
    /** Clears the stack. */
    public void clear() {
        fDepth = 0;
    }
    // debugging
    /** Prints the stack. */
    public void print() {
        System.out.print('(');
        System.out.print(fDepth);
        System.out.print(") {");
        for (int i = 0; i < fDepth; i++) {
            if (i == 3) {
                System.out.print(" ...");
                break;
            }
            System.out.print(' ');
            System.out.print(fData[i]);
            if (i < fDepth - 1) {
                System.out.print(',');
            }
        }
        System.out.print(" }");
        System.out.println();
    }
    //
    // Private methods
    //
    /** Ensures capacity. */
    private void ensureCapacity(int size) {
        if (fData == null) {
            fData = new int[32];
        }
        else if (fData.length <= size) {
            int[] newdata = new int[fData.length * 2];
            System.arraycopy(fData, 0, newdata, 0, fData.length);
            fData = newdata;
        }
    }
} // class IntStack
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
