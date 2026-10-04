---
title: Java Swing Tutorial - Java FocusTraversalPolicy .getComponentBefore (Container aContainer, Component aComponent)
nav: Java Swing Tutorial - Java...
description: FocusTraversalPolicy.getComponentBefore(Container aContainer, Component aComponent) has the following syntax.
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FocusTraversalPolicy/0080__FocusTraversalPolicy.getComponentBefore_Container_aContainer_Component_aComponent_.htm
---
## Syntax

FocusTraversalPolicy.getComponentBefore(Container aContainer, Component aComponent) has the following syntax.

```java title=Example.java
publicabstract Component getComponentBefore(Container aContainer,    Component aComponent)
```

## Example

In the following code shows how to use FocusTraversalPolicy.getComponentBefore(Container aContainer, Component aComponent) method.

```java title=Example.java
import java.awt.Component;
import java.awt.Container;
import java.awt.FocusTraversalPolicy;
import java.awt.GridLayout;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
 public Main() {
     setLayout(new GridLayout(6, 1));
     add(new JButton("A"));
     add(new JButton("D"));
     add(new JButton("C"));
     add(new JButton("E"));
     add(new JButton("B"));
     add(new JButton("F"));
 }
 publicstaticvoid main(String[] args) {
     JFrame frame = new JFrame();
     frame.setFocusTraversalPolicy(new AlphaButtonPolicy());
     frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
     frame.setContentPane(new Main());
     frame.setSize(400, 300);
     frame.setVisible(true);
 }
}
class AlphaButtonPolicy extends FocusTraversalPolicy {
  private SortedMap getSortedButtons(Container focusCycleRoot) {
    if (focusCycleRoot == null) {
      thrownew IllegalArgumentException("focusCycleRoot can't be null");
    }
    SortedMap result = new TreeMap(); // Will sort all buttons by text.
    sortRecursive(result, focusCycleRoot);
    return result;
  }
  privatevoid sortRecursive(Map buttons, Container container) {
    for (int i = 0; i < container.getComponentCount(); i++) {
      Component c = container.getComponent(i);
      if (c instanceof JButton) { // Found another button to sort.
        buttons.put(((JButton) c).getText(), c);
      }
      if (c instanceof Container) { // Found a container to search.
        sortRecursive(buttons, (Container) c);
      }
    }
  }
  // The rest of the code implements the FocusTraversalPolicy interface.
public Component getFirstComponent(Container focusCycleRoot) {
    SortedMap buttons = getSortedButtons(focusCycleRoot);
    if (buttons.isEmpty()) {
      return null;
    }
    return (Component) buttons.get(buttons.firstKey());
  }
  public Component getLastComponent(Container focusCycleRoot) {
    SortedMap buttons = getSortedButtons(focusCycleRoot);
    if (buttons.isEmpty()) {
      return null;
    }
    return (Component) buttons.get(buttons.lastKey());
  }
  public Component getDefaultComponent(Container focusCycleRoot) {
    return getFirstComponent(focusCycleRoot);
  }
  public Component getComponentAfter(Container focusCycleRoot, Component aComponent) {
    if (!(aComponent instanceof JButton)) {
      return null;
    }
    SortedMap buttons = getSortedButtons(focusCycleRoot);
    // Find all buttons after the current one.
    String nextName = ((JButton) aComponent).getText() + "\0";
    SortedMap nextButtons = buttons.tailMap(nextName);
    if (nextButtons.isEmpty()) { // Wrapped back to beginning
if (!buttons.isEmpty()) {
        return (Component) buttons.get(buttons.firstKey());
      }
      return null; // Degenerate case of no buttons.
    }
    return (Component) nextButtons.get(nextButtons.firstKey());
  }
  public Component getComponentBefore(Container focusCycleRoot, Component aComponent) {
    if (!(aComponent instanceof JButton)) {
      return null;
    }
    SortedMap buttons = getSortedButtons(focusCycleRoot);
    SortedMap prevButtons = // Find all buttons before this one.
    buttons.headMap(((JButton) aComponent).getText());
    if (prevButtons.isEmpty()) { // Wrapped back to end.
if (!buttons.isEmpty()) {
        return (Component) buttons.get(buttons.lastKey());
      }
      return null; // Degenerate case of no buttons.
    }
    return (Component) prevButtons.get(prevButtons.lastKey());
  }
}
```
