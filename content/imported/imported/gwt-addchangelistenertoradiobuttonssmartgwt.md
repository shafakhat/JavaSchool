---
title: Add change listener to Radio buttons (Smart GWT)
nav: Add change listener to Rad...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20111124233228/http://java2s.com/Code/Java/GWT/AddchangelistenertoRadiobuttonsSmartGWT.htm
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
import java.util.LinkedHashMap;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.HTMLFlow;
import com.smartgwt.client.widgets.form.DynamicForm;
import com.smartgwt.client.widgets.form.fields.RadioGroupItem;
import com.smartgwt.client.widgets.form.fields.events.ChangedEvent;
import com.smartgwt.client.widgets.form.fields.events.ChangedHandler;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    final HTMLFlow textBox = new HTMLFlow("EXAMPLE_TEXT");
    textBox.setLeft(100);
    textBox.setWidth(300);
    textBox.setStyleName("exampleStyleOnline");
    LinkedHashMap<String, String> styleMap = new LinkedHashMap<String, String>();
    styleMap.put("exampleStyleOnline", "Online");
    styleMap.put("exampleStyleLegal", "Legal");
    styleMap.put("exampleStyleCode", "Code");
    styleMap.put("exampleStyleInformal", "Informal");
    RadioGroupItem style = new RadioGroupItem();
    style.setDefaultValue("exampleStyleOnline");
    style.setShowTitle(false);
    style.setValueMap(styleMap);
    style.addChangedHandler(new ChangedHandler() {
        public void onChanged(ChangedEvent event) {
            textBox.setStyleName((String)event.getValue());
            textBox.markForRedraw();
        }
    });
    DynamicForm controls = new DynamicForm();
    controls.setFields(style);
    Canvas canvas = new Canvas();
    canvas.addChild(textBox);
    canvas.addChild(controls);
    return canvas;
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Use RadioButtonGroup
