---
title: Java Action attribute
nav: Java Action attribute
description: SHORT_DESCRIPTION Short description of the Action; could be used as tooltip text, but not by default
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20210102122120/http://www.java2s.com/ref/java/java-action-attribute.html
---
- javax.swing
- javax.swing AbstractAction Action ActionMap BorderFactory BoundedRangeModel Box BoxLayout ButtonGroup DefaultComboBoxModel DefaultListCellRenderer DefaultListModel GroupLayout Icon ImageIcon InputMap InputVerifier JButton JCheckBox JCheckBoxMenuItem JColorChooser JComboBox JComponent JDesktopPane JDialog JEditorPane JFileChooser JFormattedTextField JFrame JInternalFrame JLabel JLayer JList JMenu JMenuItem JOptionPane JPanel JPasswordField JPopupMenu JProgressBar JRadioButton JRadioButtonMenuItem JRootPane JScrollBar JScrollPane JSlider JSpinner JTabbedPane JTable JTextArea JTextField JTextPane JToggleButton JToolBar JTree KeyStroke ListSelectionModel SpinnerDateModel SpinnerListModel SpinnerModel SpinnerNumberModel SpringLayout SwingUtilities SwingWorker Timer ToolTipManager UIManager

## Introduction

Constant  Description
---  ---
NAME  Action name, used as button label
SMALL_ICON  Icon for the Action, used as button label
SHORT_DESCRIPTION  Short description of the Action; could be used as tooltip text, but not by default
LONG_DESCRIPTION  Long description of the Action; could be used for accessibility
ACCELERATOR  KeyStroke string; can be used as the accelerator for the Action
ACTION_COMMAND_KEY  InputMap key; maps to the Action in the ActionMap of the associated JComponent
MNEMONIC_KEY  Key code; can be used as mnemonic for action
DEFAULT  Unused constant that could be used for your own property

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.KeyStroke;

publicclass Main {
   publicstaticvoid main(String[] argv) throwsException {

      Action action = new My();
      JButton button = newJButton(action);

      JFrame f = newJFrame();

      f.add(button, BorderLayout.NORTH);
      f.setSize(300, 300);//fromwww.java2s.com
      f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      f.setVisible(true);

   }
}

class My extendsAbstractAction {
   public My() {
      super("Action Name");
      putValue(Action.SHORT_DESCRIPTION, "Tool Tip Text");
      putValue(Action.LONG_DESCRIPTION, "Help Text");

      Icon icon = newImageIcon("icon.png");
      putValue(Action.SMALL_ICON, icon);

      putValue(Action.MNEMONIC_KEY, newInteger(java.awt.event.KeyEvent.VK_A));
      putValue(Action.ACCELERATOR_KEY, KeyStroke.getKeyStroke("control F2"));
   }

   publicvoid actionPerformed(ActionEvent evt) {
      System.out.println("action");
   }
};
```

PreviousNext

## Related

- Java AbstractAction set mnemonic key
- Java AbstractAction set tool tip text
- Java AbstractAction transfer focus
- Java Action create
- Java Action disable action to disable component
