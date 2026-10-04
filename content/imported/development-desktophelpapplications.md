---
title: Desktop Help Applications
nav: Desktop Help Applications
description: JMenuItem browseToItem = new JMenuItem("Go to www.java2s.com");
section: Imported - java2s Archive
order: 1884
source: https://web.archive.org/web/20140829085845/http://www.java2s.com/Tutorial/Java/0120__Development/DesktopHelpApplications.htm
---
```java title=Example.java
import java.awt.Desktop;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URI;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
public class DesktopDemo {
  static Desktop desktop;
  public static void main(String[] args) {
    if (Desktop.isDesktopSupported()) {
      desktop = Desktop.getDesktop();
    } else {
      System.out.println("Desktop class is not supported");
      System.exit(1);
    }
    JMenuItem openItem = new JMenuItem("Open");
    JMenuItem editItem = new JMenuItem("Edit");
    JMenuItem printItem = new JMenuItem("Print");
    JMenuItem browseToItem = new JMenuItem("Go to JavaSchool");
    JMenuItem mailToItem = new JMenuItem("Email to a@java.com");
    JMenu fileMenu = new JMenu("File");
    JMenu mailMenu = new JMenu("Email");
    JMenu browseMenu = new JMenu("Browser");
    openItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        JFileChooser chooser = new JFileChooser();
        if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
          try {
            desktop.open(chooser.getSelectedFile().getAbsoluteFile());
          } catch (Exception ex) {
            ex.printStackTrace();
          }
        }
      }
    });
    fileMenu.add(openItem);
    editItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        JFileChooser chooser = new JFileChooser();
        if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
          try {
            desktop.edit(chooser.getSelectedFile().getAbsoluteFile());
          } catch (Exception ex) {
            ex.printStackTrace();
          }
        }
      }
    });
    fileMenu.add(editItem);
    printItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        JFileChooser chooser = new JFileChooser();
        if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
          try {
            desktop.print(chooser.getSelectedFile().getAbsoluteFile());
          } catch (Exception ex) {
            ex.printStackTrace();
          }
        }
      }
    });
    fileMenu.add(printItem);
    browseToItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          URI browseURI = new URI("JavaSchool");
          desktop.browse(browseURI);
        } catch (Exception ex) {
          System.out.println(ex.getMessage());
        }
      }
    });
    browseMenu.add(browseToItem);
    mailToItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        try {
          URI mailURI = new URI("mailto:support@java.com");
          desktop.mail(mailURI);
        } catch (Exception ex) {
          System.out.println(ex.getMessage());
        }
      }
    });
    mailMenu.add(mailToItem);
    JMenuBar jMenuBar = new JMenuBar();
    jMenuBar.add(fileMenu);
    jMenuBar.add(browseMenu);
    jMenuBar.add(mailMenu);
    JFrame frame = new JFrame();
    frame.setTitle("Desktop Helper Applications");
    frame.setSize(300, 100);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setJMenuBar(jMenuBar);
    frame.setVisible(true);
  }
}
```

| 6.39.1. | Using the Desktop class to launch a URL with default browser |
|---|---|
| 6.39.2. | Invoke the default editor to edit a file |
| 6.39.3. | Using the system default setting to open a file |
| 6.39.4. | Open a office word file with Java |
| 6.39.5. | Using system default printer to print a file out |
| 6.39.6. | Send out email |
| 6.39.7. | Open Mail client |
| 6.39.8. | Desktop Help Applications |
