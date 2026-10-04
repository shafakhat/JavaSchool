---
title: Schedule a task by using Timer and TimerTask.
nav: Schedule a task by using T...
description: Imported from the java2s.com archive: Schedule a task by using Timer and TimerTask.
section: Imported - java2s Archive
order: 1715
source: https://web.archive.org/web/20140413233448/http://www.java2s.com/Tutorial/Java/0120__Development/ScheduleataskbyusingTimerandTimerTask.htm
---
```java title=Example.java
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
class AutoTask extends TimerTask {
  AutoTask() {
  }
  public void run() {
    System.out.println(new Date());
  }
}
public class Main {
  public static void main(String args[]) {
    AutoTask myTask = new AutoTask();
    Timer bkTimer = new Timer();
    bkTimer.schedule(myTask, 2000, 2000);
    for (int i = 0; i < 5; i++) {
      try {
        Thread.sleep(2100);
      } catch (InterruptedException exc) {
      }
    }
    bkTimer.cancel();
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
