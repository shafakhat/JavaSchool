---
title: AWT and Swing
nav: AWT & Swing
description: Desktop Java UI - AWT components, Swing's improved toolkit, layouts, the event dispatch thread and the swing-worker pattern.
section: Advanced Java
order: 80
---

## AWT vs Swing in one glance

| | AWT (1995) | Swing (1998, 4.x today) |
|---|---|---|
| Components | Heavyweight (native peers: Button → OS button) | Lightweight (pure Java, drawn) |
| Look & feel | OS-dependent | Pluggable (Metal, Nimbus, system) |
| Functionality | Basic widgets | Rich set + models + accessibility |
| Threading | UI on EDT | UI on EDT (strictly) |
| Verdict | layout/event concepts still vital | the toolkit to know (or JavaFX) |

```text title=package map
java.awt            Frame, Panel, Button, Graphics, layouts, events
javax.swing         JFrame, JButton, JTable, models, SwingWorker
javax.swing.event   listeners, model events
```

## A minimal Swing application

```java title=HelloSwing.java
import javax.swing.*;
import java.awt.*;

public class HelloSwing {
    public static void main(String[] args) {
        // UI creation must happen on the Event Dispatch Thread
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("JavaSchool");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JPanel panel = new JPanel(new BorderLayout(8, 8));
            JLabel label = new JLabel("Hello from Swing!", SwingConstants.CENTER);
            JButton button = new JButton("Click me");
            button.addActionListener(e -> {                 // listener pattern
                label.setText("Clicked " + System.nanoTime() % 1000 + "!");
            });

            panel.add(label, BorderLayout.CENTER);
            panel.add(button, BorderLayout.SOUTH);
            frame.setContentPane(panel);
            frame.setSize(360, 200);
            frame.setLocationRelativeTo(null);              // center screen
            frame.setVisible(true);
        });
    }
}
```

Rules worth tattooing on your arm:

1. **Create UI only on the EDT** (`SwingUtilities.invokeLater`).
2. **Never block the EDT** - long work goes to a worker thread.
3. **Update components only from the EDT** - worker results come back via `invokeLater`/`publish`.

## Layout managers

```java title=Layouts.java
import javax.swing.*;
import java.awt.*;

public class Layouts {
    public static void main(String[] args) {
        JPanel flow    = new JPanel(new FlowLayout());            // left-to-right rows
        JPanel border  = new JPanel(new BorderLayout(4, 4));      // N/S/E/W + center
        JPanel grid    = new JPanel(new GridLayout(2, 3, 6, 6));  // equal cells
        JPanel box     = new JPanel(new BoxLayout(box, BoxLayout.Y_AXIS));

        for (int i = 1; i <= 3; i++) {
            grid.add(new JButton("B" + i));
        }
        border.add(new JButton("North"), BorderLayout.NORTH);
        border.add(new JButton("Center"), BorderLayout.CENTER);

        // Swing adds GridBagLayout (flexible, weights) and CardLayout (pages)
        System.out.println("layouts ready: " + flow.getLayout()
            + ", " + border.getLayout().getClass().getSimpleName());
    }
}
```

| Layout | Use for |
|---|---|
| `FlowLayout` | toolbars, button rows |
| `BorderLayout` | frame regions (menu north, status south, content center) |
| `GridLayout` | equal-size grids (keypads, boards) |
| `GridBagLayout` | complex resizable forms (powerful but verbose) |
| `BoxLayout` / `GroupLayout` | vertical stacks; generated GUI builders |

## Events: the listener model

```java title=Events.java
import javax.swing.*;
import java.awt.event.*;

public class Events {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        JTextField field = new JTextField(12);

        // anonymous class listener (pre-lambda style you'll still see)
        field.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    System.out.println("typed: " + field.getText());
                }
            }
        });

        // lambda style - interfaces with one method are natural lambdas
        JButton ok = new JButton("OK");
        ok.addActionListener(e -> System.out.println("ok pressed"));
        ok.addMouseListener(new MouseAdapter() {
            @Override public void mouseClicked(MouseEvent e) { /* ... */ }
        });

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```

Event flow: **source** (button) → registered **listener** callback on the **EDT**. One queue for all UI events keeps Swing single-threaded and (mostly) race-free.

## Doing work off the EDT

```java title=SwingWorkerDemo.java
import javax.swing.*;

public class SwingWorkerDemo {
    public static void main(String[] args) {
        JLabel status = new JLabel("idle...");
        JFrame f = new JFrame("Worker");
        f.add(status);
        f.setSize(300, 120);
        f.setVisible(true);

        new SwingWorker<String, Void>() {
            @Override
            protected String doInBackground() throws Exception {
                Thread.sleep(1500);                 // simulate heavy/IO work
                return "result ready";
            }

            @Override
            protected void done() throws Exception {
                status.setText(get());               // back on the EDT
            }
        }.execute();
    }
}
```

Modern alternatives: `CompletableFuture.supplyAsync(...).thenAcceptAsync(ui::set, edt)`, or virtual threads for IO-heavy desktop backends.

## Applets vs frames

Swing applets (`JApplet`) shared the component tree but lived in the browser sandbox - see [Applets](applets.html) for why that path ended. Desktop Swing survives in trading terminals, IDEs (IntelliJ's UI is Swing), admin tools and anywhere a mature, no-web UI still ships.

## Where the archive examples live

The sidebar's archive section includes dozens of imported java2s **Swing component examples** (JTable models, JList rendering, layout tricks, event adapters) - browse *Imported - java2s Archive* in the sidebar.

Related: [Applets](applets.html) · [Event handling & GUI in the archive](threads-animationswingandthread.html) · [JavaFX overview in Modern Java](modern-java.html)
