---
title: Listening for Changes to the Selected File in a JFileChooser Dialog
nav: Listening for Changes to t...
description: chooser.addPropertyChangeListener(new PropertyChangeListener() {
section: Imported
order: 20057
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/ListeningforChangestotheSelectedFileinaJFileChooserDialog.htm
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
        if (JFileChooser.SELECTED_FILE_CHANGED_PROPERTY.equals(evt.getPropertyName())) {
          JFileChooser chooser = (JFileChooser) evt.getSource();
          File oldFile = (File) evt.getOldValue();
          File newFile = (File) evt.getNewValue();
          File curFile = chooser.getSelectedFile();
        }
      }
    });
  }
}
```
