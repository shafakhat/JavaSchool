---
title: Scheduling a Timer Task to Run Repeatedly
nav: Scheduling a Timer Task to...
description: Imported from the java2s.com archive: Scheduling a Timer Task to Run Repeatedly
section: Imported - java2s Archive
order: 1717
source: https://web.archive.org/web/20140829085322/http://www.java2s.com/Tutorial/Java/0120__Development/SchedulingaTimerTasktoRunRepeatedly.htm
---
```java title=Example.java
import java.util.Timer;
import java.util.TimerTask;
public class Main {
  public static void main(String[] argv) throws Exception {
    int delay = 5000; // delay for 5 sec.
    int period = 1000; // repeat every sec.
    Timer timer = new Timer();
    timer.scheduleAtFixedRate(new TimerTask() {
      public void run() {
        System.out.println("doing");
      }
    }, delay, period);
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
