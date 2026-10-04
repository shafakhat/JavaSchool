---
title: Add click handler for Menu item (Smart GWT)
nav: Add click handler for Menu...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20100427005918/http://www.java2s.com:80/Code/Java/GWT/AddclickhandlerforMenuitemSmartGWT.htm
---
```java title=Example.java
/*
 * SmartGWT (GWT for SmartClient)
 * Copyright 2008 and beyond, Isomorphic Software, Inc.
 *
 * SmartGWT is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License version 3
 * as published by the Free Software Foundation.  SmartGWT is also
 * available under typical commercial license terms - see
 * http://smartclient.com/license
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 */
package com.smartgwt.sample.showcase.client;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.menu.Menu;
import com.smartgwt.client.widgets.menu.MenuButton;
import com.smartgwt.client.widgets.menu.MenuItem;
import com.smartgwt.client.widgets.menu.MenuItemSeparator;
import com.smartgwt.client.widgets.menu.MenuItemStringFunction;
import com.smartgwt.client.widgets.menu.events.ClickHandler;
import com.smartgwt.client.widgets.menu.events.MenuItemClickEvent;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Menu menu = new Menu();
    menu.setShowShadow(true);
    menu.setShadowDepth(10);
    MenuItem newItem = new MenuItem("New", "icons/16/document_plain_new.png", "Ctrl+N");
    MenuItem openItem = new MenuItem("Open", "icons/16/folder_out.png", "Ctrl+O");
    MenuItem saveItem = new MenuItem("Save", "icons/16/disk_blue.png", "Ctrl+S");
    MenuItem saveAsItem = new MenuItem("Save As", "icons/16/save_as.png");
    MenuItem recentDocItem = new MenuItem("Recent Documents", "icons/16/folder_document.png");
    Menu recentDocSubMenu = new Menu();
    MenuItem dataSM = new MenuItem("data.xml");
    dataSM.setChecked(true);
    MenuItem componentSM = new MenuItem("Component Guide.doc");
    MenuItem ajaxSM = new MenuItem("AJAX.doc");
    recentDocSubMenu.setItems(dataSM, componentSM, ajaxSM);
    recentDocItem.setSubmenu(recentDocSubMenu);
    MenuItem exportItem = new MenuItem("Export as...", "icons/16/export1.png");
    Menu exportSM = new Menu();
    exportSM.setItems(
            new MenuItem("XML"),
            new MenuItem("CSV"),
            new MenuItem("Plain text"));
    exportItem.setSubmenu(exportSM);
    MenuItem printItem = new MenuItem("Print", "icons/16/printer3.png", "Ctrl+P");
    printItem.setEnabled(false);
    MenuItemSeparator separator = new MenuItemSeparator();
    final MenuItem activateMenu = new MenuItem("Activate");
    activateMenu.setDynamicTitleFunction(new MenuItemStringFunction() {
        public String execute(final Canvas aTarget, final Menu aMenu, final MenuItem aItem) {
            if (Math.random() > 0.5) {
                return "De-Activate Blacklist";
            } else {
                return "Activate Blacklist";
            }
        }
    });
    activateMenu.addClickHandler(new ClickHandler() {
        public void onClick(final MenuItemClickEvent event) {
            //processStateChangeEvent();
        }
    });
    menu.setItems(activateMenu, newItem, openItem, separator, saveItem, saveAsItem,
            separator, recentDocItem, separator, exportItem, separator, printItem);
    return new MenuButton("File", menu);
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Menu with style
13.  Desktop in a browser (Ext GWT)
