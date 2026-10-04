---
title: An implementation of the java.util.Stack based on an ArrayList instead of a Vector, so it is not synchronized to protect against multi-threaded access.
nav: An implementation of the j...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2471
source: https://web.archive.org/web/20140829083808/http://www.java2s.com/Tutorial/Java/0140__Collections/AnimplementationofthejavautilStackbasedonanArrayListinsteadofaVectorsoitisnotsynchronizedtoprotectagainstmultithreadedaccess.htm
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
import java.util.ArrayList;
import java.util.Collection;
import java.util.EmptyStackException;
import java.util.NoSuchElementException;
/**
 * An implementation of the {@link java.util.Stack} API that is based on an
 * <code>ArrayList</code> instead of a <code>Vector</code>, so it is not
 * synchronized to protect against multi-threaded access.  The implementation
 * is therefore operates faster in environments where you do not need to
 * worry about multiple thread contention.
 *
 * The removal order of an <code>ArrayStack</code> is based on insertion
 * order: The most recently added element is removed first.  The iteration
 * order is <i>not</i> the same as the removal order.  The iterator returns
 * elements from the bottom up, whereas the {@link #remove()} method removes
 * them from the top down.
 *
 * Unlike <code>Stack</code>, <code>ArrayStack</code> accepts null entries.
 *
 * <strong>Note:</strong> this class should be bytecode-identical to the
 * version in commons collections. This is required to allow backwards
 * compability with both previous versions of BeanUtils and also allow
 * coexistance with both collections 2.1 and 3.0.
 *
 * @see java.util.Stack
 * @since Commons Collections 1.0
 * @version $Revision: 555824 $ $Date: 2007-07-13 01:27:15 +0100 (Fri, 13 Jul 2007) $
 *
 * @author Craig R. McClanahan
 * @author Paul Jack
 * @author Stephen Colebourne
 */
public class ArrayStack extends ArrayList implements Buffer {
    /** Ensure serialization compatibility */
    private static final long serialVersionUID = 2130079159931574599L;
    /**
     * Constructs a new empty <code>ArrayStack</code>. The initial size
     * is controlled by <code>ArrayList</code> and is currently 10.
     */
    public ArrayStack() {
        super();
    }
    /**
     * Constructs a new empty <code>ArrayStack</code> with an initial size.
     *
     * @param initialSize  the initial size to use
     * @throws IllegalArgumentException  if the specified initial size
     *  is negative
     */
    public ArrayStack(int initialSize) {
        super(initialSize);
    }
    /**
     * Return <code>true</code> if this stack is currently empty.
     *
     * This method exists for compatibility with <code>java.util.Stack</code>.
     * New users of this class should use <code>isEmpty</code> instead.
     *
     * @return true if the stack is currently empty
     */
    public boolean empty() {
        return isEmpty();
    }
    /**
     * Returns the top item off of this stack without removing it.
     *
     * @return the top item on the stack
     * @throws EmptyStackException  if the stack is empty
     */
    public Object peek() throws EmptyStackException {
        int n = size();
        if (n <= 0) {
            throw new EmptyStackException();
        } else {
            return get(n - 1);
        }
    }
    /**
     * Returns the n'th item down (zero-relative) from the top of this
     * stack without removing it.
     *
     * @param n  the number of items down to go
     * @return the n'th item on the stack, zero relative
     * @throws EmptyStackException  if there are not enough items on the
     *  stack to satisfy this request
     */
    public Object peek(int n) throws EmptyStackException {
        int m = (size() - n) - 1;
        if (m < 0) {
            throw new EmptyStackException();
        } else {
            return get(m);
        }
    }
    /**
     * Pops the top item off of this stack and return it.
     *
     * @return the top item on the stack
     * @throws EmptyStackException  if the stack is empty
     */
    public Object pop() throws EmptyStackException {
        int n = size();
        if (n <= 0) {
            throw new EmptyStackException();
        } else {
            return remove(n - 1);
        }
    }
    /**
     * Pushes a new item onto the top of this stack. The pushed item is also
     * returned. This is equivalent to calling <code>add</code>.
     *
     * @param item  the item to be added
     * @return the item just pushed
     */
    public Object push(Object item) {
        add(item);
        return item;
    }
    /**
     * Returns the one-based position of the distance from the top that the
     * specified object exists on this stack, where the top-most element is
     * considered to be at distance <code>1</code>.  If the object is not
     * present on the stack, return <code>-1</code> instead.  The
     * <code>equals()</code> method is used to compare to the items
     * in this stack.
     *
     * @param object  the object to be searched for
     * @return the 1-based depth into the stack of the object, or -1 if not found
     */
    public int search(Object object) {
        int i = size() - 1;        // Current index
        int n = 1;                 // Current distance
        while (i >= 0) {
            Object current = get(i);
            if ((object == null && current == null) ||
                (object != null && object.equals(current))) {
                return n;
            }
            i--;
            n++;
        }
        return -1;
    }
    /**
     * Returns the element on the top of the stack.
     *
     * @return the element on the top of the stack
     * @throws BufferUnderflowException  if the stack is empty
     */
    public Object get() {
        int size = size();
        if (size == 0) {
            throw new BufferUnderflowException();
        }
        return get(size - 1);
    }
    /**
     * Removes the element on the top of the stack.
     *
     * @return the removed element
     * @throws BufferUnderflowException  if the stack is empty
     */
    public Object remove() {
        int size = size();
        if (size == 0) {
            throw new BufferUnderflowException();
        }
        return remove(size - 1);
    }
}
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
 * Defines a collection that allows objects to be removed in some well-defined order.
 *
 * The removal order can be based on insertion order (eg, a FIFO queue or a
 * LIFO stack), on access order (eg, an LRU cache), on some arbitrary comparator
 * (eg, a priority queue) or on any other well-defined ordering.
 *
 * Note that the removal order is not necessarily the same as the iteration
 * order.  A <code>Buffer</code> implementation may have equivalent removal
 * and iteration orders, but this is not required.
 *
 * This interface does not specify any behavior for
 * {@link Object#equals(Object)} and {@link Object#hashCode} methods.  It
 * is therefore possible for a <code>Buffer</code> implementation to also
 * also implement {@link java.util.List}, {@link java.util.Set} or
 * {@link Bag}.
 *
 * <strong>Note:</strong> this class should be bytecode-identical to the
 * version in commons collections. This is required to allow backwards
 * compability with both previous versions of BeanUtils and also allow
 * coexistance with both collections 2.1 and 3.0.
 *
 * @since Commons Collections 2.1
 * @version $Revision: 555824 $ $Date: 2007-07-13 01:27:15 +0100 (Fri, 13 Jul 2007) $
 *
 * @author Avalon
 * @author Berin Loritsch
 * @author Paul Jack
 * @author Stephen Colebourne
 */
interface Buffer extends Collection {
    /**
     * Gets and removes the next object from the buffer.
     *
     * @return the next object in the buffer, which is also removed
     * @throws BufferUnderflowException if the buffer is already empty
     */
    Object remove();
    /**
     * Gets the next object from the buffer without removing it.
     *
     * @return the next object in the buffer, which is not removed
     * @throws BufferUnderflowException if the buffer is empty
     */
    Object get();
}
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
 * The BufferUnderflowException is used when the buffer is already empty.
 *
 * NOTE: From version 3.0, this exception extends NoSuchElementException.
 *
 * @since Commons Collections 2.1
 * @version $Revision: 555824 $ $Date: 2007-07-13 01:27:15 +0100 (Fri, 13 Jul 2007) $
 *
 * @author Avalon
 * @author Berin Loritsch
 * @author Jeff Turner
 * @author Paul Jack
 * @author Stephen Colebourne
 */
 class BufferUnderflowException extends NoSuchElementException {
    /** The root cause throwable */
    private final Throwable throwable;
    /**
     * Constructs a new <code>BufferUnderflowException</code>.
     */
    public BufferUnderflowException() {
        super();
        throwable = null;
    }
    /**
     * Construct a new <code>BufferUnderflowException</code>.
     *
     * @param message  the detail message for this exception
     */
    public BufferUnderflowException(String message) {
        this(message, null);
    }
    /**
     * Construct a new <code>BufferUnderflowException</code>.
     *
     * @param message  the detail message for this exception
     * @param exception  the root cause of the exception
     */
    public BufferUnderflowException(String message, Throwable exception) {
        super(message);
        throwable = exception;
    }
    /**
     * Gets the root cause of the exception.
     *
     * @return the root cause
     */
    public final Throwable getCause() {
        return throwable;
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
