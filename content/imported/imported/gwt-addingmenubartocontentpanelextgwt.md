---
title: Adding menu bar to ContentPanel (Ext GWT)
nav: Adding menu bar to Content...
description: Imported from the java2s.com archive: Adding menu bar to ContentPanel (Ext GWT)
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20100630150946/http://www.java2s.com:80/Code/Java/GWT/AddingmenubartoContentPanelExtGWT.htm
---
```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import com.extjs.gxt.ui.client.widget.ContentPanel;
import com.extjs.gxt.ui.client.widget.LayoutContainer;
import com.extjs.gxt.ui.client.widget.layout.FlowData;
import com.extjs.gxt.ui.client.widget.menu.Menu;
import com.extjs.gxt.ui.client.widget.menu.MenuBar;
import com.extjs.gxt.ui.client.widget.menu.MenuBarItem;
import com.extjs.gxt.ui.client.widget.menu.MenuItem;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.ui.RootPanel;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(new MenuBarExample());
  }
}
class MenuBarExample extends LayoutContainer {
  @Override
  protected void onRender(Element parent, int index) {
    super.onRender(parent, index);
    Menu menu = new Menu();
    MenuItem item1 = new MenuItem("New");
    menu.add(item1);
    MenuItem item2 = new MenuItem("Open File");
    menu.add(item2);
    Menu sub = new Menu();
    sub.add(new MenuItem("readme.txt"));
    sub.add(new MenuItem("helloworld.txt"));
    item2.setSubMenu(sub);
    MenuBar bar = new MenuBar();
    bar.setBorders(true);
    bar.setStyleAttribute("borderTop", "none");
    bar.add(new MenuBarItem("File", menu));
    Menu sub2 = new Menu();
    sub2.add(new MenuItem("Cut"));
    sub2.add(new MenuItem("Copy"));
    MenuBarItem edit = new MenuBarItem("Edit", sub2);
    bar.add(edit);
    ContentPanel panel = new ContentPanel();
    panel.setHeading("MenuBar Example");
    panel.setTopComponent(bar);
    panel.setSize(400, 300);
    add(panel, new FlowData(10));
  }
}
```

Ext-GWT.zip( 4,297 k)
3.  ToolBar overflow (Ext GWT)
