---
title: Java Swing Tutorial - Java CardLayout .layoutContainer (Container parent)
nav: Java Swing Tutorial - Java...
description: CardLayout.layoutContainer(Container parent) has the following syntax.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/0260__CardLayout.layoutContainer_Container_parent_.htm
---
## Syntax

CardLayout.layoutContainer(Container parent) has the following syntax.

```java title=Example.java
publicvoid layoutContainer(Container parent)
```

## Example

In the following code shows how to use CardLayout.layoutContainer(Container parent) method.

```java title=Example.java
import java.awt.CardLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main {
  publicstaticvoid main(String[] args) {
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
    card.layoutContainer(this);
  }
  publicvoid actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
```
