---
title: A bean that can be used to keep track of a counter
nav: A bean that can be used to...
description: public class Counter implements java.util.Iterator, Serializable {
section: Imported - java2s Archive
order: 2046
source: https://web.archive.org/web/20140701164706/http://www.java2s.com/Tutorial/Java/0120__Development/Abeanthatcanbeusedtokeeptrackofacounter.htm
---
```java title=Example.java
/*
 * Copyright (c) 2002-2003 by OpenSymphony
 * All rights reserved.
 */
import java.io.Serializable;
/**
 * <p/>
 * Since it is an Iterator it can be used by the iterator tag
 *
 * @author Rickard Öberg (rickard@middleware-company.com)
 * @version $Revision: 1282 $
 * @see <related>
 */
public class Counter implements java.util.Iterator, Serializable {
    boolean wrap = false;
    // Attributes ----------------------------------------------------
    long first = 1;
    long current = first;
    long interval = 1;
    long last = -1;
    public void setAdd(long addition) {
        current += addition;
    }
    public void setCurrent(long current) {
        this.current = current;
    }
    public long getCurrent() {
        return current;
    }
    public void setFirst(long first) {
        this.first = first;
        current = first;
    }
    public long getFirst() {
        return first;
    }
    public void setInterval(long interval) {
        this.interval = interval;
    }
    public long getInterval() {
        return interval;
    }
    public void setLast(long last) {
        this.last = last;
    }
    public long getLast() {
        return last;
    }
    // Public --------------------------------------------------------
    public long getNext() {
        long next = current;
        current += interval;
        if (wrap && (current > last)) {
            current -= ((1 + last) - first);
        }
        return next;
    }
    public long getPrevious() {
        current -= interval;
        if (wrap && (current < first)) {
            current += (last - first + 1);
        }
        return current;
    }
    public void setWrap(boolean wrap) {
        this.wrap = wrap;
    }
    public boolean isWrap() {
        return wrap;
    }
    public boolean hasNext() {
        return ((last == -1) || wrap) ? true : (current <= last);
    }
    public Object next() {
        return new Long(getNext());
    }
    public void remove() {
        // Do nothing
    }
}
///////////////////
/*
 * Copyright (c) 2002-2003 by OpenSymphony
 * All rights reserved.
 */
package com.opensymphony.webwork.util;
import junit.framework.TestCase;
/**
 * User: plightbo
 * Date: Jan 7, 2004
 * Time: 7:55:35 PM
 */
public class CounterTest extends TestCase {
    Counter c = new Counter();
    public void testCurrentAfterNext() {
        long next = c.getNext();
        long current = c.getCurrent();
        assertEquals(next + 1, current);
    }
    public void testCurrentBeforeNext() {
        long current = c.getCurrent();
        long next = c.getNext();
        assertEquals(current, next);
    }
    public void testWrap() {
        c.setWrap(true);
        c.setLast(1);
        long a = c.getNext();
        long b = c.getNext();
        assertEquals(1, a);
        assertEquals(1, b);
    }
}
```

| 6.59.1. | Prints messages formatted for a specific line width. |
|---|---|
| 6.59.2. | A bean that can be used to keep track of a counter |
| 6.59.3. | Swing Console |
| 6.59.4. | Methods for logging events |
| 6.59.5. | Debug Utility |
| 6.59.6. | A helper class for printing indented text |
| 6.59.7. | Random data for test |
| 6.59.8. | Count Up Down Latch |
| 6.59.9. | A simple logging facility. |
| 6.59.10. | Printing indented text |
