---
title: Java Action disable action to disable component
nav: Java Action disable action...
description: privateJMenuItem disableActionItem = newJMenuItem("Disable the Action");
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20210102122120/http://www.java2s.com/ref/java/java-action-disable-action-to-disable-component.html
---
- javax.swing
- javax.swing AbstractAction Action ActionMap BorderFactory BoundedRangeModel Box BoxLayout ButtonGroup DefaultComboBoxModel DefaultListCellRenderer DefaultListModel GroupLayout Icon ImageIcon InputMap InputVerifier JButton JCheckBox JCheckBoxMenuItem JColorChooser JComboBox JComponent JDesktopPane JDialog JEditorPane JFileChooser JFormattedTextField JFrame JInternalFrame JLabel JLayer JList JMenu JMenuItem JOptionPane JPanel JPasswordField JPopupMenu JProgressBar JRadioButton JRadioButtonMenuItem JRootPane JScrollBar JScrollPane JSlider JSpinner JTabbedPane JTable JTextArea JTextField JTextPane JToggleButton JToolBar JTree KeyStroke ListSelectionModel SpinnerDateModel SpinnerListModel SpinnerModel SpinnerNumberModel SpringLayout SwingUtilities SwingWorker Timer ToolTipManager UIManager

## Description

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.AbstractAction;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JToolBar;

publicclass Main extendsJFrame {
   publicstaticfinalString ENABLE = "ENABLE";
   publicstaticfinalString DISABLE = "DISABLE";

   privateJToolBar toolBar = newJToolBar();
   privateJMenuBar menuBar = newJMenuBar();
   privateJMenu testMenu = newJMenu("Test");
   private MyAction theAction = new MyAction();
   privateJMenuItem disableActionItem = newJMenuItem("Disable the Action");

   public Main() {
      this.setJMenuBar(menuBar);
      menuBar.add(testMenu);//fromwww.java2s.com

      testMenu.add(theAction);
      toolBar.add(theAction);

      disableActionItem.setActionCommand(DISABLE);
      testMenu.add(disableActionItem);
      disableActionItem.addActionListener(newActionListener() {
         publicvoid actionPerformed(ActionEvent e) {
            if (e.getActionCommand().equals(DISABLE)) {
               theAction.setEnabled(false);
               disableActionItem.setText("Enable the Action");
               disableActionItem.setActionCommand(ENABLE);
            } else {
               theAction.setEnabled(true);
               disableActionItem.setText("Disable the Action");
               disableActionItem.setActionCommand(DISABLE);
            }
         }
      });
      this.getContentPane().add(toolBar, BorderLayout.NORTH);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      this.setSize(320, 200);
      this.setVisible(true);
   }

   publicstaticvoid main(String[] args) {
      Main t = new Main();
   }
}

class MyAction extendsAbstractAction {
   public MyAction() {
      super("Change Color");
   }
   publicvoid actionPerformed(ActionEvent e) {
      System.out.println("action");
   }
}
```

PreviousNext

## Related

- Java AbstractAction transfer focus
- Java Action attribute
- Java Action create
- Java Swing ActionMap list action
- Java BorderFactory create line border
