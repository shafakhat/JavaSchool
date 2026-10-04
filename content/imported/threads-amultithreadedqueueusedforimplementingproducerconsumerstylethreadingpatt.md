---
title: A multithreaded queue used for implementing producer-consumer style threading patterns
nav: A multithreaded queue used...
description: A multithreaded queue used for implementing producer-consumer style threading patterns : Collections Threads « Threads « Java
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20090904113058/http://www.java2s.com:80/Code/Java/Threads/Amultithreadedqueueusedforimplementingproducerconsumerstylethreadingpatterns.htm
---
A multithreaded queue used for implementing producer-consumer style threading patterns : Collections Threads « Threads « Java
A multithreaded queue used for implementing producer-consumer style threading patterns

```java title=Example.java
/*
 * Funambol is a mobile platform developed by Funambol, Inc.
 * Copyright (C) 2003 - 2007 Funambol, Inc.
 *
 * This program is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Affero General Public License version 3 as published by
 * the Free Software Foundation with the addition of the following permission
 * added to Section 15 as permitted in Section 7(a): FOR ANY PART OF THE COVERED
 * WORK IN WHICH THE COPYRIGHT IS OWNED BY FUNAMBOL, FUNAMBOL DISCLAIMS THE
 * WARRANTY OF NON INFRINGEMENT  OF THIRD PARTY RIGHTS.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program; if not, see http://www.gnu.org/licenses or write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301 USA.
 *
 * You can contact Funambol, Inc. headquarters at 643 Bair Island Road, Suite
 * 305, Redwood City, CA 94063, USA, or at email address info@funambol.com.
 *
 * The interactive user interfaces in modified source and object code versions
 * of this program must display Appropriate Legal Notices, as required under
 * Section 5 of the GNU Affero General Public License version 3.
 *
 * In accordance with Section 7(b) of the GNU Affero General Public License
 * version 3, these Appropriate Legal Notices must retain the display of the
 * "Powered by Funambol" logo. If the display of the logo is not reasonably
 * feasible for technical reasons, the Appropriate Legal Notices must display
 * the words "Powered by Funambol".
 */
import java.util.Stack;
/**
 * A multithreaded queue used for
 * implementing producer-consumer style threading patterns.
 * Multiple threads can wait for runnable objects being added
 * to the queue while other threads add to the queue.
 */
public class Queue {
    private Stack tasks = new Stack();
    private long defaultTimeout = 100;
    public Queue() {
    }
    /**
     * Returns the current number of runnable objects in the queue
     */
    public synchronized int size() {
        return tasks.size();
    }
    /**
     * adds a runnable object to the end of the queue.
     * At least one thread will be notified.
     */
    public synchronized void add(Object runnable) {
        tasks.push(runnable);
        notifyAll();
    }
    /**
     * Removes the first runnable object from the queue, blocking until one is available.
     */
    public synchronized Object remove() {
        while (true) {
            Object runnable = removeNoWait();
            if ( runnable != null ) {
                return runnable;
            }
            try {
                wait( defaultTimeout );
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    /**
     * Removes the first runnable object from the queue without blocking.
     * This method will return immediately with an item from the queue or null.
     * @return the first runnable object removed from the queue or null if the
     * queue is empty
     */
    public synchronized Object removeNoWait() {
        if ( ! tasks.empty() ) {
            return tasks.pop();
        } else {
            return null;
        }
    }
}
```

1.  Java 1.5 (5.0) new features: PriorityQueue
---  ---
2.  Safe list copy
3.  Safe vector copy
4.  Safe collection operation
5.  Java 1.5 (5.0) new feature: collection and thread
6.  Java Thread Performance: Collection Test
7.  Java Thread Performance: AtomicTest
8.  Rhyming Words
9.  Communicate between threads using a Queue
10.  Using a Thread-Local Variable
11.  A work queue is used to coordinate work between a producer and a set of worker threads.
12.  Return a value from a thread.
13.  Customized java.util.ArrayList: operate in a multithreaded environment where the large majority of method calls are read-only, instead of structural changes.
14.  Customized java.util.HashMap: operate in a multithreaded environment where the large majority of method calls are read-only, instead of structural changes.
15.  Customized java.util.TreeMap: operate in a multithreaded environment where the large majority of method calls are read-only, instead of structural changes.
16.  Current set
