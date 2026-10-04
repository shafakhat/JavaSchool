---
title: Java Swing Tutorial - Java CardLayout .getLayoutAlignmentY (Container parent)
nav: Java Swing Tutorial - Java...
description: CardLayout.getLayoutAlignmentY(Container parent) has the following syntax.
section: Imported - java2s Archive
order: 1179
source: https://web.archive.org/web/20150325023038/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/0180__CardLayout.getLayoutAlignmentY_Container_parent_.htm
---
## Syntax

CardLayout.getLayoutAlignmentY(Container parent) has the following syntax.

```java title=Example.java
public float getLayoutAlignmentY(Container parent)
```

## Example

In the following code shows how to use CardLayout.getLayoutAlignmentY(Container parent) method.

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
    System.out.println(card.getLayoutAlignmentY(this));
  }
  public void actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
java title=Example.java
```
