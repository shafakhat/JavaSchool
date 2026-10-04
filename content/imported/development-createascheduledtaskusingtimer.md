---
title: Create a scheduled task using timer
nav: Create a scheduled task us...
description: private DateFormat formatter = new SimpleDateFormat("hh:mm:ss a");
section: Imported - java2s Archive
order: 1713
source: https://web.archive.org/web/20140829085402/http://www.java2s.com/Tutorial/Java/0120__Development/Createascheduledtaskusingtimer.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
public class Main extends TimerTask {
  private DateFormat formatter = new SimpleDateFormat("hh:mm:ss a");
  public static void main(String[] args) {
    TimerTask task = new Main();
    Timer timer = new Timer();
    timer.scheduleAtFixedRate(task, new Date(), 1000);
  }
  public void run() {
    System.out.println(formatter.format(new Date()));
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
