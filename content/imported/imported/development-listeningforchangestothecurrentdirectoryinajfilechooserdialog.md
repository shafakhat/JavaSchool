---
title: Listening for Changes to the Current Directory in a JFileChooser Dialog
nav: Listening for Changes to t...
description: chooser.addPropertyChangeListener(new PropertyChangeListener() {
section: Imported
order: 20056
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/ListeningforChangestotheCurrentDirectoryinaJFileChooserDialog.htm
---
```java title=Example.java
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.File;
import javax.swing.JFileChooser;
public class Main {
  public static void main(String[] argv) throws Exception {
    final JFileChooser chooser = new JFileChooser();
    chooser.addPropertyChangeListener(new PropertyChangeListener() {
      public void propertyChange(PropertyChangeEvent evt) {
        if (JFileChooser.DIRECTORY_CHANGED_PROPERTY.equals(evt.getPropertyName())) {
          JFileChooser chooser = (JFileChooser) evt.getSource();
          File oldDir = (File) evt.getOldValue();
          File newDir = (File) evt.getNewValue();
          File curDir = chooser.getCurrentDirectory();
        }
      }
    });
  }
}
```
