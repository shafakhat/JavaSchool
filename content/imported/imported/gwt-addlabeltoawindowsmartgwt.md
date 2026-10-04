---
title: Add label to a window (Smart GWT)
nav: Add label to a window (Sma...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20100523193819/http://www.java2s.com:80/Code/Java/GWT/AddlabeltoawindowSmartGWT.htm
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
import com.smartgwt.client.types.Alignment;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.Label;
import com.smartgwt.client.widgets.Window;
import com.smartgwt.client.widgets.events.ClickEvent;
import com.smartgwt.client.widgets.events.ClickHandler;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Canvas canvas = new Canvas();
    final Window window = new Window();
    window.setTitle("Window with footer");
    window.setWidth(200);
    window.setHeight(200);
    window.setCanDragResize(true);
    window.setShowFooter(true);
    Label label = new Label();
    label.setContents("Click Me");
    label.setAlign(Alignment.CENTER);
    label.setPadding(5);
    label.setHeight100();
    label.addClickHandler(new ClickHandler() {
        public void onClick(ClickEvent event) {
            window.setStatus("Click at: " + event.getX() + ", " + event.getY());
        }
    });
    window.addItem(label);
    canvas.addChild(window);
    return canvas;
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Create Custom Dialog
