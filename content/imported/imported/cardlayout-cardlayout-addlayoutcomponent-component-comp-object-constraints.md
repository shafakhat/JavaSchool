---
title: Java Swing Tutorial - Java CardLayout .addLayoutComponent (Component comp, Object constraints)
nav: Java Swing Tutorial - Java...
description: CardLayout.addLayoutComponent(Component comp, Object constraints) has the following syntax.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/0080__CardLayout.addLayoutComponent_Component_comp_Object_constraints_.htm
---
```java title=Example.java
Back to CardLayout  ↑
```

## Syntax

CardLayout.addLayoutComponent(Component comp, Object constraints) has the following syntax.

```java title=Example.java
publicvoid addLayoutComponent(Component comp,   Object constraints)
```

## Example

In the following code shows how to use CardLayout.addLayoutComponent(Component comp, Object constraints) method.

```java title=Example.java
//www.java2s.comimport java.awt.CardLayout;
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
    JButton button = new JButton("Press 1");
    button.addActionListener(this);
    card.addLayoutComponent(button, "1");
    add(button);

    button = new JButton("Press 2");
    button.addActionListener(this);
    card.addLayoutComponent(button, "2");
    add(button);

    button = new JButton("Press 3");
    button.addActionListener(this);
    card.addLayoutComponent(button, "3");
    add(button);

    card.show(this, "2");
  }
  publicvoid actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
```

- Back to CardLayout ↑
