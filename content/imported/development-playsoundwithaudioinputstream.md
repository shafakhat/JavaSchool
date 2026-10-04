---
title: Play sound with AudioInputStream
nav: Play sound with AudioInput...
description: public class CoreJavaSound extends Object implements LineListener {
section: Imported - java2s Archive
order: 1968
source: https://web.archive.org/web/20140829091443/http://www.java2s.com/Tutorial/Java/0120__Development/PlaysoundwithAudioInputStream.htm
---
```java title=Example.java
import java.io.File;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.Line;
import javax.sound.sampled.LineEvent;
import javax.sound.sampled.LineListener;
import javax.swing.JDialog;
import javax.swing.JFileChooser;
public class CoreJavaSound extends Object implements LineListener {
  File soundFile;
  JDialog playingDialog;
  Clip clip;
  public static void main(String[] args) throws Exception {
    CoreJavaSound s = new CoreJavaSound();
  }
  public CoreJavaSound() throws Exception {
    JFileChooser chooser = new JFileChooser();
    chooser.showOpenDialog(null);
    soundFile = chooser.getSelectedFile();
    System.out.println("Playing " + soundFile.getName());
    Line.Info linfo = new Line.Info(Clip.class);
    Line line = AudioSystem.getLine(linfo);
    clip = (Clip) line;
    clip.addLineListener(this);
    AudioInputStream ais = AudioSystem.getAudioInputStream(soundFile);
    clip.open(ais);
    clip.start();
  }
  public void update(LineEvent le) {
    LineEvent.Type type = le.getType();
    if (type == LineEvent.Type.OPEN) {
      System.out.println("OPEN");
    } else if (type == LineEvent.Type.CLOSE) {
      System.out.println("CLOSE");
      System.exit(0);
    } else if (type == LineEvent.Type.START) {
      System.out.println("START");
      playingDialog.setVisible(true);
    } else if (type == LineEvent.Type.STOP) {
      System.out.println("STOP");
      playingDialog.setVisible(false);
      clip.close();
    }
  }
}
```
