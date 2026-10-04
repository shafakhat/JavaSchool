---
title: Create a Timer object
nav: Create a Timer object
description: Imported from the java2s.com archive: Create a Timer object
section: Imported - java2s Archive
order: 1728
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0120__Development/CreateaTimerobject.htm
---
```java title=Example.java
import java.util.Timer;
import java.util.TimerTask;
public class Main {
  Timer timer;
  public Main(int seconds) {
    timer = new Timer();
    timer.schedule(new ToDoTask(), seconds * 1000);
  }
  class ToDoTask extends TimerTask {
    public void run() {
      System.out.println("working");
      timer.cancel();
    }
  }
  public static void main(String args[]) {
    new Main(5);
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
