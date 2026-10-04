---
title: Swing also provide a Timer class. A Timer object will send an ActionEvent to the registered ActionListener.
nav: Swing also provide a Timer...
description: 6.18.6.Swing also provide a Timer class. A Timer object will send an ActionEvent to the registered ActionListener. Previous / Next
section: Imported - java2s Archive
order: 1712
source: https://web.archive.org/web/20140413110122/http://www.java2s.com/Tutorial/Java/0120__Development/SwingalsoprovideaTimerclassATimerobjectwillsendanActionEventtotheregisteredActionListener.htm
---
6.18.6.Swing also provide a Timer class. A Timer object will send an ActionEvent to the registered ActionListener. Previous / Next

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Timer;
public class Main implements ActionListener {
  Timer t = new Timer(1000, this);
  Main() {
    t.start();
  }
  public void actionPerformed(ActionEvent e) {
    System.out.println("working");
  }
  public static void main(String args[]) {
    Main main = new Main();
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
