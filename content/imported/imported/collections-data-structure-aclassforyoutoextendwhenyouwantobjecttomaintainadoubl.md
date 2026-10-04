---
title: A class for you to extend when you want object to maintain a doubly linked list
nav: A class for you to extend ...
description: A class for you to extend when you want object to maintain a doubly linked list : Link List « Collections Data Structure « Java
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20091108200406/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Aclassforyoutoextendwhenyouwantobjecttomaintainadoublylinkedlist.htm
---
A class for you to extend when you want object to maintain a doubly linked list : Link List « Collections Data Structure « Java

```java title=Example.java
/**
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
 * Provides a base class for you to extend when you want object to maintain a
 * doubly linked list to other objects without using a collection class.
 *
 * @author chirino
 */
public class LinkedNode {
    protected LinkedNode next = this;
    protected LinkedNode prev = this;
    protected boolean tail = true;
    public LinkedNode getHeadNode() {
        if (isHeadNode()) {
            return this;
        }
        if (isTailNode()) {
            return next;
        }
        LinkedNode rc = prev;
        while (!rc.isHeadNode()) {
            rc = rc.prev;
        }
        return rc;
    }
    public LinkedNode getTailNode() {
        if (isTailNode()) {
            return this;
        }
        if (isHeadNode()) {
            return prev;
        }
        LinkedNode rc = next;
        while (!rc.isTailNode()) {
            rc = rc.next;
        }
        return rc;
    }
    public LinkedNode getNext() {
        return tail ? null : next;
    }
    public LinkedNode getPrevious() {
        return prev.tail ? null : prev;
    }
    public boolean isHeadNode() {
        return prev.isTailNode();
    }
    public boolean isTailNode() {
        return tail;
    }
    /**
     * @param rightHead the node to link after this node.
     * @return this
     */
    public LinkedNode linkAfter(LinkedNode rightHead) {
        if (rightHead == this) {
            throw new IllegalArgumentException("You cannot link to yourself");
        }
        if (!rightHead.isHeadNode()) {
            throw new IllegalArgumentException("You only insert nodes that are the first in a list");
        }
        LinkedNode rightTail = rightHead.prev;
        if (tail) {
            tail = false;
        } else {
            rightTail.tail = false;
        }
        rightHead.prev = this; // link the head of the right side.
        rightTail.next = next; // link the tail of the right side
        next.prev = rightTail; // link the head of the left side
        next = rightHead; // link the tail of the left side.
        return this;
    }
    /**
     * @param leftHead the node to link after this node.
     * @return
     * @return this
     */
    public LinkedNode linkBefore(LinkedNode leftHead) {
        if (leftHead == this) {
            throw new IllegalArgumentException("You cannot link to yourself");
        }
        if (!leftHead.isHeadNode()) {
            throw new IllegalArgumentException("You only insert nodes that are the first in a list");
        }
        // The left side is no longer going to be a tail..
        LinkedNode leftTail = leftHead.prev;
        leftTail.tail = false;
        leftTail.next = this; // link the tail of the left side.
        leftHead.prev = prev; // link the head of the left side.
        prev.next = leftHead; // link the tail of the right side.
        prev = leftTail; // link the head of the right side.
        return leftHead;
    }
    /**
     * Removes this node out of the linked list it is chained in.
     */
    public void unlink() {
        // If we are allready unlinked...
        if (prev == this) {
            reset();
            return;
        }
        if (tail) {
            prev.tail = true;
        }
        // Update the peers links..
        next.prev = prev;
        prev.next = next;
        // Update our links..
        reset();
    }
    public void reset() {
        next = this;
        prev = this;
        tail = true;
    }
}
/////////////////////////////////////
/**
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
package org.apache.activemq.util;
import junit.framework.TestCase;
/**
 * @author chirino
 */
public class LinkedNodeTest extends TestCase {
    static class IntLinkedNode extends LinkedNode {
        public final int v;
        public IntLinkedNode(int v) {
            this.v = v;
        };
        @Override
        public String toString() {
            return "" + v;
        }
    }
    IntLinkedNode i1 = new IntLinkedNode(1);
    IntLinkedNode i2 = new IntLinkedNode(2);
    IntLinkedNode i3 = new IntLinkedNode(3);
    IntLinkedNode i4 = new IntLinkedNode(4);
    IntLinkedNode i5 = new IntLinkedNode(5);
    IntLinkedNode i6 = new IntLinkedNode(6);
    public void testLinkAfter() {
        i1.linkAfter(i2.linkAfter(i3));
        // Order should be 1,2,3
        assertTrue(i1.getNext() == i2);
        assertTrue(i1.getNext().getNext() == i3);
        assertNull(i1.getNext().getNext().getNext());
        assertTrue(i3.getPrevious() == i2);
        assertTrue(i3.getPrevious().getPrevious() == i1);
        assertNull(i3.getPrevious().getPrevious().getPrevious());
        assertTrue(i1.isHeadNode());
        assertFalse(i1.isTailNode());
        assertFalse(i2.isHeadNode());
        assertFalse(i2.isTailNode());
        assertTrue(i3.isTailNode());
        assertFalse(i3.isHeadNode());
        i1.linkAfter(i4.linkAfter(i5));
        // Order should be 1,4,5,2,3
        assertTrue(i1.getNext() == i4);
        assertTrue(i1.getNext().getNext() == i5);
        assertTrue(i1.getNext().getNext().getNext() == i2);
        assertTrue(i1.getNext().getNext().getNext().getNext() == i3);
        assertNull(i1.getNext().getNext().getNext().getNext().getNext());
        assertTrue(i3.getPrevious() == i2);
        assertTrue(i3.getPrevious().getPrevious() == i5);
        assertTrue(i3.getPrevious().getPrevious().getPrevious() == i4);
        assertTrue(i3.getPrevious().getPrevious().getPrevious().getPrevious() == i1);
        assertNull(i3.getPrevious().getPrevious().getPrevious().getPrevious().getPrevious());
        assertTrue(i1.isHeadNode());
        assertFalse(i1.isTailNode());
        assertFalse(i4.isHeadNode());
        assertFalse(i4.isTailNode());
        assertFalse(i5.isHeadNode());
        assertFalse(i5.isTailNode());
        assertFalse(i2.isHeadNode());
        assertFalse(i2.isTailNode());
        assertTrue(i3.isTailNode());
        assertFalse(i3.isHeadNode());
    }
    public void testLinkBefore() {
        i3.linkBefore(i2.linkBefore(i1));
        assertTrue(i1.getNext() == i2);
        assertTrue(i1.getNext().getNext() == i3);
        assertNull(i1.getNext().getNext().getNext());
        assertTrue(i3.getPrevious() == i2);
        assertTrue(i3.getPrevious().getPrevious() == i1);
        assertNull(i3.getPrevious().getPrevious().getPrevious());
        assertTrue(i1.isHeadNode());
        assertFalse(i1.isTailNode());
        assertFalse(i2.isHeadNode());
        assertFalse(i2.isTailNode());
        assertTrue(i3.isTailNode());
        assertFalse(i3.isHeadNode());
        i2.linkBefore(i5.linkBefore(i4));
        // Order should be 1,4,5,2,3
        assertTrue(i1.getNext() == i4);
        assertTrue(i1.getNext().getNext() == i5);
        assertTrue(i1.getNext().getNext().getNext() == i2);
        assertTrue(i1.getNext().getNext().getNext().getNext() == i3);
        assertNull(i1.getNext().getNext().getNext().getNext().getNext());
        assertTrue(i3.getPrevious() == i2);
        assertTrue(i3.getPrevious().getPrevious() == i5);
        assertTrue(i3.getPrevious().getPrevious().getPrevious() == i4);
        assertTrue(i3.getPrevious().getPrevious().getPrevious().getPrevious() == i1);
        assertNull(i3.getPrevious().getPrevious().getPrevious().getPrevious().getPrevious());
        assertTrue(i1.isHeadNode());
        assertFalse(i1.isTailNode());
        assertFalse(i4.isHeadNode());
        assertFalse(i4.isTailNode());
        assertFalse(i5.isHeadNode());
        assertFalse(i5.isTailNode());
        assertFalse(i2.isHeadNode());
        assertFalse(i2.isTailNode());
        assertTrue(i3.isTailNode());
        assertFalse(i3.isHeadNode());
    }
    public void testUnlink() {
        i1.linkAfter(i2.linkAfter(i3));
        i3.linkAfter(i4);
        i1.linkBefore(i5);
        i1.linkAfter(i6);
        // Order should be 5,1,6,2,3,4
        i4.unlink();
        i5.unlink();
        i6.unlink();
        // Order should be 1,2,3
        assertTrue(i1.getNext() == i2);
        assertTrue(i1.getNext().getNext() == i3);
        assertNull(i1.getNext().getNext().getNext());
        assertTrue(i3.getPrevious() == i2);
        assertTrue(i3.getPrevious().getPrevious() == i1);
        assertNull(i3.getPrevious().getPrevious().getPrevious());
        assertTrue(i1.isHeadNode());
        assertFalse(i1.isTailNode());
        assertFalse(i2.isHeadNode());
        assertFalse(i2.isTailNode());
        assertTrue(i3.isTailNode());
        assertFalse(i3.isHeadNode());
    }
}
```

1.  Use for each loop to go through elements in a linkedlist
---  ---
2.  Use addFirst method to add value to the first position in a linked list
3.  To insert an object into a specific position into the list, specify the index in the add method
4.  Updating LinkedList Items
5.  Convert LinkedList to Array with zero length array
6.  Convert LinkedList to Array with full length array
7.  Checking what item is first in line without removing it: element
8.  Removing the first item from the queue: poll
9.  Convert a LinkedList to ArrayList
10.  Add elements at beginning and end of LinkedList Java example
11.  Check if a particular element exists in LinkedList Java example
12.  Create an object array from elements of LinkedList Java example
13.  Get elements from LinkedList Java example
14.  Get first and last elements from LinkedList Java example
15.  Get SubList from LinkedList Java example
16.  Iterate through elements of Java LinkedList using Iterator example
17.  Remove all elements or clear LinkedList Java example
18.  Iterate through elements of Java LinkedList using ListIterator example
19.  Remove first and last elements of LinkedList Java example
20.  Remove range of elements from LinkedList Java example
21.  Remove specified element from LinkedList Java example
22.  Replace an Element of LinkedList Java example
23.  Search elements of LinkedList Java example
24.  Add or insert an element to ArrayList using Java ListIterator Example
25.  Finding an Element in a Sorted List
26.  Create a list with an ordered list of strings
27.  Search for a non-existent element
28.  Use an Iterator to cycle through a collection in the forward direction.
29.  Implementing a Queue with LinkedList
30.  Implementing a Stack
31.  Using a LinkedList in multi-thread
32.  Convert Collection to ArrayList
33.  Wrap queue to synchronize the methods
34.  Making a stack from a LinkedList
35.  Single linked list
36.  Double LinkedList
37.  Doubly Linked list
38.  A simple Doubly Linked list class, designed to avoid O(n) behaviour on insert and delete.
39.  A List helper class that attempts to avoid unneccessary List creation.
