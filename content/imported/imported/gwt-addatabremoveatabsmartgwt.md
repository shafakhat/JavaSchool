---
title: Add a tab, remove a tab (Smart GWT)
nav: Add a tab, remove a tab (S...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20100422205935/http://www.java2s.com:80/Code/Java/GWT/AddatabremoveatabSmartGWT.htm
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
import com.smartgwt.client.types.Side;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.IButton;
import com.smartgwt.client.widgets.Img;
import com.smartgwt.client.widgets.events.ClickEvent;
import com.smartgwt.client.widgets.events.ClickHandler;
import com.smartgwt.client.widgets.layout.HLayout;
import com.smartgwt.client.widgets.layout.VLayout;
import com.smartgwt.client.widgets.tab.Tab;
import com.smartgwt.client.widgets.tab.TabSet;
import com.smartgwt.client.widgets.tab.events.CloseClickHandler;
import com.smartgwt.client.widgets.tab.events.TabCloseClickEvent;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    final TabSet topTabSet = new TabSet();
    topTabSet.setTabBarPosition(Side.TOP);
    topTabSet.setTabBarAlign(Side.LEFT);
    topTabSet.setWidth(400);
    topTabSet.setHeight(200);
    Tab tTab1 = new Tab("Blue", "pieces/16/pawn_blue.png");
    tTab1.setCanClose(true);
    Img tImg1 = new Img("pieces/48/pawn_blue.png", 48, 48);
    tTab1.setPane(tImg1);
    Tab tTab2 = new Tab("Green", "pieces/16/pawn_green.png");
    Img tImg2 = new Img("pieces/48/pawn_green.png", 48, 48);
    tTab2.setPane(tImg2);
    topTabSet.addTab(tTab1);
    topTabSet.addTab(tTab2);
    topTabSet.addCloseClickHandler(new CloseClickHandler() {
        public void onCloseClick(TabCloseClickEvent event) {
            Tab tab = event.getTab();
            System.out.println("");
        }
    });
    HLayout buttons = new HLayout();
    buttons.setMembersMargin(15);
    IButton addButton = new IButton("Add Tab");
    addButton.addClickHandler(new ClickHandler() {
        public void onClick(ClickEvent event) {
            String title = topTabSet.getTabs().length % 2 == 0 ? "Yellow" : "Green";
            String iconType = topTabSet.getTabs().length % 2 == 0 ? "pawn" : "cube";
            Tab tTab = new Tab(title, "pieces/16/" + iconType + "_" + title.toLowerCase() + ".png");
            tTab.setCanClose(true);
            Img tImg = new Img("pieces/48/" + iconType + "_" + title.toLowerCase() + ".png", 48, 48);
            tTab.setPane(tImg);
            topTabSet.addTab(tTab);
        }
    });
    IButton removeButton = new IButton("Remove Tab");
    removeButton.addClickHandler(new ClickHandler() {
        public void onClick(ClickEvent event) {
            topTabSet.removeTab(topTabSet.getTabs().length - 1);
        }
    });
    buttons.addMember(addButton);
    buttons.addMember(removeButton);
    VLayout vLayout = new VLayout();
    vLayout.setMembersMargin(15);
    vLayout.addMember(topTabSet);
    vLayout.addMember(buttons);
    vLayout.setHeight("auto");
    return vLayout;
  }
}
```

SmartGWT.zip( 9,880 k)
