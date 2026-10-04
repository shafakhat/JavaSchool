---
title: Java Swing Tutorial - Java CardLayout() Constructor
nav: Java Swing Tutorial - Java...
description: CardLayout() constructor from CardLayout has the following syntax.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/0040__CardLayout.CardLayout_.htm
---
```java title=Example.java
Back to CardLayout  ↑
```

## Syntax

CardLayout() constructor from CardLayout has the following syntax.

```java title=Example.java
public CardLayout()
```

## Example

In the following code shows how to use CardLayout.CardLayout() constructor.

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
  CardLayout card = new CardLayout();
  public CardLayoutPanel() {
    setLayout(card);
    JButton button;
    for (int i = 1; i <= 6; i++) {
      add(button = new JButton("Press " + i), "Card" + i);
      button.addActionListener(this);
    }
  }
  publicvoid actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
```

- Back to CardLayout ↑
