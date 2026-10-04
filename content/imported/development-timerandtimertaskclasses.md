---
title: Timer and TimerTask Classes
nav: Timer and TimerTask Classes
description: Imported from the java2s.com archive: Timer and TimerTask Classes
section: Imported - java2s Archive
order: 1714
source: https://web.archive.org/web/20140412160016/http://www.java2s.com/Tutorial/Java/0120__Development/TimerandTimerTaskClasses.htm
---
```java title=Example.java
import java.util.Timer;
import java.util.TimerTask;
class GCTask extends TimerTask {
  public void run() {
    System.out.println("Running the scheduled task...");
    System.gc();
  }
}
public class Main {
  public static void main(String[] args) {
    Timer timer = new Timer();
    GCTask task = new GCTask();
    timer.schedule(task, 5000, 5000);
    int counter = 1;
    while (true) {
      try {
        Thread.sleep(500);
      } catch (InterruptedException e) {
      }
    }
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
