---
title: Using Timers
nav: Using Timers
description: The java.util.Timer class provides an alternative way to perform scheduled or recurrent tasks.
section: Imported - java2s Archive
order: 1708
source: https://web.archive.org/web/20140216131303/http://www.java2s.com/Tutorial/Java/0120__Development/UsingTimers.htm
---
The java.util.Timer class provides an alternative way to perform scheduled or recurrent tasks.

```java title=Example.java
import java.util.Timer;
import java.util.TimerTask;
public class MainClass {
  public static void main(String[] args) {
    Timer timer = new Timer();
    timer.schedule(new DisplayQuestionTask(), 0, 10 * 1000);
    try {
      Thread.sleep(10000);
    } catch (InterruptedException e) {
    }
    timer.cancel();
  }
}
class DisplayQuestionTask extends TimerTask {
  int counter = 0;
  public void run() {
    System.out.println(counter++);
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
