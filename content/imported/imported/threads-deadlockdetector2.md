---
title: DeadLock Detector 2
nav: DeadLock Detector 2
description: * aion-emu is free software: you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20111124182721/http://java2s.com/Code/Java/Threads/DeadLockDetector2.htm
---
DeadLock Detector 2

```java title=Example.java
/**
 * This file is part of aion-emu <aion-emu.com>.
 *
 *  aion-emu is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  aion-emu is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with aion-emu.  If not, see <http://www.gnu.org/licenses/>.
 */
//package com.aionemu.commons.utils;
import java.lang.management.LockInfo;
import java.lang.management.ManagementFactory;
import java.lang.management.MonitorInfo;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;
//import com.aionemu.commons.utils.ExitCode;
/**
 * @author -Nemesiss-
 */
public class DeadLockDetector extends Thread
{
  /** What should we do on DeadLock */
  public static final byte  NOTHING  = 0;
  /** What should we do on DeadLock */
  public static final byte  RESTART  = 1;
  /** how often check for deadlocks */
  private final int      sleepTime;
  /**
   * ThreadMXBean
   */
  private final ThreadMXBean  tmx;
  /** What should we do on DeadLock */
  private final byte      doWhenDL;
  /**
   * Create new DeadLockDetector with given values.
   *
   * @param sleepTime
   * @param doWhenDL
   */
  public DeadLockDetector(int sleepTime, byte doWhenDL)
  {
    super("DeadLockDetector");
    this.sleepTime = sleepTime * 1000;
    this.tmx = ManagementFactory.getThreadMXBean();
    this.doWhenDL = doWhenDL;
  }
  /**
   * Check if there is a DeadLock.
   */
  @Override
  public final void run()
  {
    boolean deadlock = false;
    while (!deadlock)
    {
      try
      {
        long[] ids = tmx.findDeadlockedThreads();
        if (ids != null)
        {
          /** deadlock found :/ */
          deadlock = true;
          ThreadInfo[] tis = tmx.getThreadInfo(ids, true, true);
          String info = "DeadLock Found!\n";
          for (ThreadInfo ti : tis)
          {
            info += ti.toString();
          }
          for (ThreadInfo ti : tis)
          {
            LockInfo[] locks = ti.getLockedSynchronizers();
            MonitorInfo[] monitors = ti.getLockedMonitors();
            if (locks.length == 0 && monitors.length == 0)
            {
              /** this thread is deadlocked but its not guilty */
              continue;
            }
            ThreadInfo dl = ti;
            info += "Java-level deadlock:\n";
            info += "\t" + dl.getThreadName() + " is waiting to lock " + dl.getLockInfo().toString() + " which is held by " + dl.getLockOwnerName()
                + "\n";
            while ((dl = tmx.getThreadInfo(new long[]
            { dl.getLockOwnerId() }, true, true)[0]).getThreadId() != ti.getThreadId())
            {
              info += "\t" + dl.getThreadName() + " is waiting to lock " + dl.getLockInfo().toString() + " which is held by "
                  + dl.getLockOwnerName() + "\n";
            }
          }
          System.out.println(info);
          if (doWhenDL == RESTART)
          {
            System.exit(0);
          }
        }
        Thread.sleep(sleepTime);
      }
      catch (Exception e)
      {
        System.out.println(e);
      }
    }
  }
}
```

1.  Demonstrates how deadlock can be hidden in a program
---  ---
2.  Another deadlock demo
3.  ReentrantLock: test for deadlocks
4.  Deadlock Detecting
5.  Using interrupt() to break out of a blocked thread.
6.  Deadlock Detector
