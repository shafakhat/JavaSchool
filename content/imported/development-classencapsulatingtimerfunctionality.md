---
title: Class encapsulating timer functionality
nav: Class encapsulating timer ...
description: * Copyright (c) 2003 - 2007 OpenSubsystems s.r.o. Slovak Republic. All rights reserved.
section: Imported - java2s Archive
order: 1720
source: https://web.archive.org/web/20140413110110/http://www.java2s.com/Tutorial/Java/0120__Development/Classencapsulatingtimerfunctionality.htm
---
```java title=Example.java
/*
 * Copyright (c) 2003 - 2007 OpenSubsystems s.r.o. Slovak Republic. All rights reserved.
 *
 * Project: OpenSubsystems
 *
 * $Id: MyTimer.java,v 1.5 2007/01/07 06:14:00 bastafidli Exp $
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */
/**
 *
 * @version $Id: MyTimer.java,v 1.5 2007/01/07 06:14:00 bastafidli Exp $
 * @author Miro Halas
 * @code.reviewer Miro Halas
 * @code.reviewed Initial revision
 */
public class MyTimer
{
   // Attributes ///////////////////////////////////////////////////////////////
   /**
    * Remeber start time here.
    */
   private long m_lStartTime;
   /**
    * Remeber stop time here.
    */
   private long m_lStopTime;
   // Constructors /////////////////////////////////////////////////////////////
   /**
    * Default constructor.
    * Starts counting fro the moment it is cosntructed.
    */
   public MyTimer(
   )
   {
      reset();
   }
   // Logic ////////////////////////////////////////////////////////////////////
   /**
    * @return long - start time;
    */
   public long getStartTime()
   {
      return m_lStartTime;
   }
   /**
    * @return - stop time;
    */
   public long getStopTime()
   {
      return m_lStopTime;
   }
   /**
    * Reset the counter and start counting from scratch.
    */
   public void reset(
   )
   {
      m_lStartTime = System.currentTimeMillis();
      m_lStopTime = 0;
   }
   /**
    * Stop the timer.
    */
   public void stop(
   )
   {
      m_lStopTime = System.currentTimeMillis();
   }
   /**
    * Get timer duration (the timer doesn't stop) in milliseconds.
    *
    * @return long - difference between stop and start time.
    */
   public long getDuration(
   )
   {
      long lStopTime;
      if (m_lStopTime == 0)
      {
         lStopTime = System.currentTimeMillis();
      }
      else
      {
         lStopTime = m_lStopTime;
      }
      return lStopTime - m_lStartTime;
   }
   /**
    * Print the state of the timer without stopping it.
    * @return String - timing information
    */
   public String toString(
   )
   {
      long lTotalMS   = getDuration();
      long lMS        = lTotalMS % 1000;
      long lTotalSecs = lTotalMS / 1000;
      long lSecs      = lTotalSecs % 60;
      long lTotalMins = lTotalSecs / 60;
      long lMinutes   = lTotalMins % 60;
      long lHours     = lTotalMins / 60;
      StringBuffer sbBuffer = new StringBuffer();
      if (lHours > 0)
      {
         sbBuffer.append(lHours);
         sbBuffer.append(":");
         sbBuffer.append(lMinutes);
         sbBuffer.append(":");
         sbBuffer.append(lSecs);
         sbBuffer.append(".");
         sbBuffer.append(lMS);
      }
      else if (lMinutes > 0)
      {
         sbBuffer.append(lMinutes);
         sbBuffer.append(":");
         sbBuffer.append(lSecs);
         sbBuffer.append(".");
         sbBuffer.append(lMS);
      }
      else if (lSecs > 0)
      {
         sbBuffer.append(lSecs);
         sbBuffer.append(".");
         sbBuffer.append(lMS);
         sbBuffer.append(" seconds");
      }
      else
      {
         sbBuffer.append(lMS);
         sbBuffer.append(" ms");
      }
      return sbBuffer.toString();
   }
}
```

| 6.18.1. | Using Timers |
|---|---|
| 6.18.2. | Demonstrate Timer and TimerTask. |
| 6.18.3. | Timer and TimerTask Classes |
| 6.18.4. | Pause and start a timer task |
| 6.18.5. | Create a Timer object |
| 6.18.6. | Swing also provide a Timer class. A Timer object will send an ActionEvent to the registered ActionListener. |
| 6.18.7. | Create a scheduled task using timer |
| 6.18.8. | Schedule a task by using Timer and TimerTask. |
| 6.18.9. | Scheduling a Timer Task to Run Repeatedly |
| 6.18.10. | extends TimerTask to create your own task |
| 6.18.11. | Your own timer |
| 6.18.12. | Class encapsulating timer functionality |
