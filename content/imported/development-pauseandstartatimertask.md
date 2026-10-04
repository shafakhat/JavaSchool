---
title: Pause and start a timer task
nav: Pause and start a timer task
description: Imported from the java2s.com archive: Pause and start a timer task
section: Imported - java2s Archive
order: 1735
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0120__Development/Pauseandstartatimertask.htm
---
```java title=Example.java
import java.util.Timer;
import java.util.TimerTask;
class MyTask extends TimerTask {
  int counter;
  public MyTask() {
    counter = 0;
  }
  public void run() {
    counter++;
    System.out.println("Ring " + counter);
  }
  public int getCount() {
    return counter;
  }
}
public class Main {
  private boolean running;
  private MyTask task;
  private Timer timer;
  public Main() {
    timer = new Timer(true);
  }
  public boolean isRinging() {
    return running;
  }
  public void startRinging() {
    running = true;
    task = new MyTask();
    timer.scheduleAtFixedRate(task, 0, 3000);
  }
  public void doIt() {
    running = false;
    System.out.println(task.getCount() + " times");
    task.cancel();
  }
  public static void main(String[] args) {
    Main phone = new Main();
    phone.startRinging();
    try {
      System.out.println("started running...");
      Thread.sleep(20000);
    } catch (InterruptedException e) {
    }
    phone.doIt();
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
