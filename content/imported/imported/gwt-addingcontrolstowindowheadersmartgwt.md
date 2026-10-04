---
title: Adding controls to window header (Smart GWT)
nav: Adding controls to window ...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20100721155952/http://www.java2s.com:80/Code/Java/GWT/AddingcontrolstowindowheaderSmartGWT.htm
---
Adding controls to window header (Smart GWT)

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
import com.smartgwt.client.types.HeaderControls;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.Window;
import com.smartgwt.client.widgets.form.DynamicForm;
import com.smartgwt.client.widgets.form.fields.SelectItem;
import com.smartgwt.client.widgets.form.fields.events.ChangedEvent;
import com.smartgwt.client.widgets.form.fields.events.ChangedHandler;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Canvas canvas = new Canvas();
    final StatusCanvas statusReportCanvas = new StatusCanvas();
    statusReportCanvas.setPadding(5);
    statusReportCanvas.setWidth100();
    statusReportCanvas.setHeight100();
    DynamicForm systemSelector = new DynamicForm();
    systemSelector.setWidth(75);
    systemSelector.setNumCols(1);
    systemSelector.setLayoutAlign(Alignment.CENTER);
    SelectItem selectFont = new SelectItem();
    selectFont.setName("selectFont");
    selectFont.setWidth(120);
    selectFont.setShowTitle(false);
    selectFont.setValueMap("Development", "Staging", "Production");
    selectFont.setDefaultValue("Development");
    selectFont.addChangedHandler(new ChangedHandler() {
        public void onChanged(ChangedEvent event) {
            statusReportCanvas.setNewStatus((String)event.getValue());
        }
    });
    systemSelector.setItems(selectFont);
    final Window window = new Window();
    window.setTitle("Status");
    window.setWidth(300);
    window.setHeight(200);
    window.setCanDragReposition(true);
    window.setCanDragResize(true);
    window.setHeaderControls(HeaderControls.CLOSE_BUTTON, HeaderControls.MINIMIZE_BUTTON, HeaderControls.HEADER_LABEL,  systemSelector);
    window.addItem(statusReportCanvas);
    statusReportCanvas.setNewStatus("Development");
    canvas.addChild(window);
    return canvas;
}
class StatusCanvas extends Canvas {
    public void setNewStatus(String system) {
        setContents(system + ": <span style='color:green;font-weight:bold'>Normal</span><br>");
    }
}
}
```

SmartGWT.zip( 9,880 k)
1.  Create Custom Dialog
