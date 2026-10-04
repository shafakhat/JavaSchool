---
title: Adding shadow to a Label (Smart GWT)
nav: Adding shadow to a Label (...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20100628173220/http://www.java2s.com:80/Code/Java/GWT/AddingshadowtoaLabelSmartGWT.htm
---
Adding shadow to a Label (Smart GWT)

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
import com.smartgwt.client.widgets.Label;
import com.smartgwt.client.widgets.Slider;
import com.smartgwt.client.widgets.events.DrawEvent;
import com.smartgwt.client.widgets.events.DrawHandler;
import com.smartgwt.client.widgets.events.ValueChangedEvent;
import com.smartgwt.client.widgets.events.ValueChangedHandler;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Canvas canvas = new Canvas();
    final Label label = new Label("EXAMPLE_TEXT");
    label.setWidth(250);
    label.setPadding(10);
    label.setLeft(160);
    label.setTop(20);
    label.setBackgroundColor("white");
    label.setBorder("1px solid #c0c0c0");
    label.setCanDragReposition(true);
    label.setShowShadow(true);
    label.setShadowSoftness(10);
    label.setShadowOffset(5);
    label.setKeepInParentRect(true);
    final Slider softness = new Slider("Softness");
    softness.setMinValue(1);
    softness.setMaxValue(10);
    softness.setNumValues(11);
    softness.setShowRange(false);
    softness.setLabelWidth(20);
    softness.setValue(10);
    softness.addDrawHandler(new DrawHandler() {
        public void onDraw(DrawEvent event) {
            softness.addValueChangedHandler(new ValueChangedHandler() {
                public void onValueChanged(ValueChangedEvent event) {
                    label.setShadowSoftness(event.getValue());
                    label.updateShadow();
                }
            });
        }
    });
    final Slider offset = new Slider("Offset");
    offset.setMinValue(0);
    offset.setMaxValue(20);
    offset.setNumValues(21);
    offset.setShowRange(false);
    offset.setLabelWidth(20);
    offset.setLeft(60);
    offset.setValue(5);
    offset.addDrawHandler(new DrawHandler() {
        public void onDraw(DrawEvent event) {
            offset.addValueChangedHandler(new ValueChangedHandler() {
                public void onValueChanged(ValueChangedEvent event) {
                    label.setShadowOffset(event.getValue());
                    label.updateShadow();
                }
            });
        }
    });
    canvas.addChild(softness);
    canvas.addChild(offset);
    canvas.addChild(label);
    return canvas;
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Change style for Label
2.  Change the Label layer (Smart GWT)
3.  Turn on Label border and change the background color (Smart GWT)
