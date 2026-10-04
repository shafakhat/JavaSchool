---
title: Demonstrate Timer and TimerTask.
nav: Demonstrate Timer and Time...
description: Imported from the java2s.com archive: Demonstrate Timer and TimerTask.
section: Imported - java2s Archive
order: 1711
source: https://web.archive.org/web/20140216102526/http://www.java2s.com/Tutorial/Java/0120__Development/DemonstrateTimerandTimerTask.htm
---
```java title=Example.java
import java.util.Timer;
import java.util.TimerTask;
class MyTimerTask extends TimerTask {
  public void run() {
    System.out.println("Timer task executed.");
  }
}
class TTest {
  public static void main(String args[]) {
    MyTimerTask myTask = new MyTimerTask();
    Timer myTimer = new Timer();
    myTimer.schedule(myTask, 1000, 500);
    try {
      Thread.sleep(5000);
    } catch (InterruptedException exc) {
    }
    myTimer.cancel();
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
