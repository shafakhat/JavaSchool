---
title: Load image and sound from Jar file
nav: Load image and sound from ...
description: URL imageURL = getClass().getClassLoader().getResource("images/k.jpeg");
section: Imported
order: 20060
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/LoadimageandsoundfromJarfile.htm
---
```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.Line;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
public class Main extends JFrame {
  JButton button;
  ImageIcon buttonIcon;
  Clip buhClip;
  public Main() throws Exception {
    URL imageURL = getClass().getClassLoader().getResource("images/k.jpeg");
    buttonIcon = new ImageIcon(imageURL);
    button = new JButton("Click to Buh!", buttonIcon);
    button.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        if (buhClip != null) {
          buhClip.setFramePosition(0);
          buhClip.start();
        } else
          System.out.println("Couldn't load sound");
      }
    });
    getContentPane().add(button);
    URL soundURL = getClass().getClassLoader().getResource("sounds/b.aiff");
    Line.Info linfo = new Line.Info(Clip.class);
    Line line = AudioSystem.getLine(linfo);
    buhClip = (Clip) line;
    AudioInputStream ais = AudioSystem.getAudioInputStream(soundURL);
    buhClip.open(ais);
  }
  public static final void main(String[] args) throws Exception {
    JFrame frame = new Main();
    frame.pack();
    frame.setVisible(true);
  }
}
```
