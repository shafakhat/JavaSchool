---
title: Get a list of selected files
nav: Get a list of selected files
description: chooser.addPropertyChangeListener(new PropertyChangeListener() {
section: Imported
order: 20025
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Getalistofselectedfiles.htm
---
```java title=Example.java
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.File;
import javax.swing.JFileChooser;
public class Main {
  public static void main(String[] argv) throws Exception {
    JFileChooser chooser = new JFileChooser();
    chooser.addPropertyChangeListener(new PropertyChangeListener() {
      public void propertyChange(PropertyChangeEvent evt) {
        if (JFileChooser.SELECTED_FILES_CHANGED_PROPERTY.equals(evt.getPropertyName())) {
          JFileChooser chooser = (JFileChooser) evt.getSource();
          File[] oldFiles = (File[]) evt.getOldValue();
          File[] newFiles = (File[]) evt.getNewValue();
          // Get list of selected files
          File[] files = chooser.getSelectedFiles();
        }
      }
    });
  }
}
```
