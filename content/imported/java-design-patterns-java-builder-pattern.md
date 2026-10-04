---
title: Java Design Patterns Tutorial - Java Design Pattern - Builder Pattern
nav: Java Design Patterns Tutor...
description: Builder pattern is used to create a complex object using simple objects. It creates the bigger object step by step from small and simple object.
section: Imported - java2s Archive
order: 50115
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0040__Java_Builder_Pattern.html
---
Builder pattern is used to create a complex object using simple objects. It creates the bigger object step by step from small and simple object.

Builder pattern is another creational pattern.

For example, when creating a window as our application's main window, we need to create a menu, a toolbar and then add the menu and toolbar.

For each window we are going to create, we need to create an empty window, create a menu, create a toolbar, install the menu and toolbar to the window.

We can use the builder pattern to hide the implementation of how to create a window.

## Example

```java title=Example.java
class Menu {
}
class ToolBar {
}
class MainWindow {
  Menu menu;
  ToolBar toolBar;
  public Menu getMenu() {
    return menu;
  }
  publicvoid setMenu(Menu menu) {
    this.menu = menu;
  }
  public ToolBar getToolBar() {
    return toolBar;
  }
  publicvoid setToolBar(ToolBar toolBar) {
    this.toolBar = toolBar;
  }
}
class WindowBuilder{
  publicstatic MainWindow createWindow(){
    MainWindow window = new MainWindow();
    Menu menu = new Menu();
    ToolBar toolBar = new ToolBar();
    window.setMenu(menu);
    window.setToolBar(toolBar);
    return window;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MainWindow object = WindowBuilder.createWindow();
  }
}
```

- « Previous
