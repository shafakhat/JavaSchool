---
title: Count Up Down Latch
nav: Count Up Down Latch
description: * Redistribution and use in source and binary forms, with or without
section: Imported - java2s Archive
order: 2051
source: https://web.archive.org/web/20140630074917/http://www.java2s.com/Tutorial/Java/0120__Development/CountUpDownLatch.htm
---
```java title=Example.java
/* Copyright (c) 2001-2009, The HSQL Development Group
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this
 * list of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * Neither the name of the HSQL Development Group nor the names of its
 * contributors may be used to endorse or promote products derived from this
 * software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL HSQL DEVELOPMENT GROUP, HSQLDB.ORG,
 * OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
import java.util.concurrent.CountDownLatch;
public class CountUpDownLatch {
    CountDownLatch latch;
    int            count;
    public CountUpDownLatch() {
        latch      = new CountDownLatch(1);
        this.count = count;
    }
    public void await() throws InterruptedException {
        if (count == 0) {
            return;
        }
        latch.await();
    }
    public void countDown() {
        count--;
        if (count == 0) {
            latch.countDown();
        }
    }
    public long getCount() {
        return count;
    }
    public void countUp() {
        if (latch.getCount() == 0) {
            latch = new CountDownLatch(1);
        }
        count++;
    }
    public void setCount(int count) {
        if (count == 0) {
            if (latch.getCount() != 0) {
                latch.countDown();
            }
        } else if (latch.getCount() == 0) {
            latch = new CountDownLatch(1);
        }
        this.count = count;
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
