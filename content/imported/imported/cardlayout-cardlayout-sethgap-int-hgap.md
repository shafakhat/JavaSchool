---
title: Java Swing Tutorial - Java CardLayout.setHgap(int hgap)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use CardLayout.setHgap(int hgap) method.
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/0400__CardLayout.setHgap_int_hgap_.htm
---
```java title=Example.java
Back to CardLayout  ↑
```

## Syntax

CardLayout.setHgap(int hgap) has the following syntax.

```java title=Example.java
publicvoid setHgap(int hgap)
```

## Example

In the following code shows how to use CardLayout.setHgap(int hgap) method.

```java title=Example.java
import java.awt.CardLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
//fromwww.java2s.comimport javax.swing.JButton;
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
    card.setVgap(50);
    card.setHgap(30);
  }
  publicvoid actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
```

- Back to CardLayout ↑
