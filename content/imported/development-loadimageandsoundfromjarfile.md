---
title: Load image and sound from Jar file
nav: Load image and sound from ...
description: URL imageURL = getClass().getClassLoader().getResource("images/k.jpeg");
section: Imported - java2s Archive
order: 2035
source: https://web.archive.org/web/20140829075921/http://www.java2s.com/Tutorial/Java/0120__Development/LoadimageandsoundfromJarfile.htm
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

| 6.50.1. | Determining When a Sampled Audio Player Has Finished Playing |
|---|---|
| 6.50.2. | Setting the Volume of a Sampled Audio Player |
| 6.50.3. | Determining the Position of a Sampled Audio Player |
| 6.50.4. | Determining the Duration of a Sampled Audio File |
| 6.50.5. | Playing Streaming Sampled Audio |
| 6.50.6. | Loading and Playing Sampled Audio |
| 6.50.7. | Play an audio file from a JAR file |
| 6.50.8. | Determining the Encoding of a Sampled Audio File |
| 6.50.9. | Determining the File Format of a Sampled Audio File |
| 6.50.10. | Load image and sound from Jar file |
| 6.50.11. | A simple player for sampled sound files. |
| 6.50.12. | This is a simple program to record sounds and play them back |
| 6.50.13. | Capturing Audio with Java Sound API |
| 6.50.14. | Float Control Component |
| 6.50.15. | Make your own Java Media Player to play media files |
