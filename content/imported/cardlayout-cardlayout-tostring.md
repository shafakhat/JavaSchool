---
title: Java Swing Tutorial - Java CardLayout.toString()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use CardLayout.toString() method.
section: Imported - java2s Archive
order: 1185
source: https://web.archive.org/web/20150325015425/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/0460__CardLayout.toString_.htm
---
## Syntax

CardLayout.toString() has the following syntax.

```java title=Example.java
public String toString()
```

## Example

In the following code shows how to use CardLayout.toString() method.

```java title=Example.java
import java.awt.CardLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main {
  public static void main(String[] args) {
    JFrame aWindow = new JFrame();
    aWindow.setSize(400, 400);
    aWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    aWindow.add(new CardLayoutPanel());
    aWindow.setVisible(true);
  }
}
class CardLayoutPanel extends JPanel implements ActionListener {
  CardLayout card = new CardLayout(50, 50);
  public CardLayoutPanel() {
    setLayout(card);
    JButton button;
    for (int i = 1; i <= 6; i++) {
      add(button = new JButton("Press " + i), "Card" + i);
      button.addActionListener(this);
    }
    System.out.println(card.toString());
  }
  public void actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
java title=Example.java
```
