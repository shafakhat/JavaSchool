---
title: extends TimerTask to create your own task
nav: extends TimerTask to creat...
description: Imported from the java2s.com archive: extends TimerTask to create your own task
section: Imported - java2s Archive
order: 1716
source: https://web.archive.org/web/20140429162312/http://www.java2s.com/Tutorial/Java/0120__Development/extendsTimerTasktocreateyourowntask.htm
---
```java title=Example.java
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.TimerTask;
class MyTask extends TimerTask {
  private DataOutputStream out;
  public MyTask(OutputStream dest) {
    out = new DataOutputStream(dest);
  }
  public void run() {
    try {
      out.writeInt(1);
      out.writeUTF("asdf");
    } catch (IOException e) {
      e.printStackTrace();
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
