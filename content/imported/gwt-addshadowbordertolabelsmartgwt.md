---
title: Add shadow border to label (Smart GWT)
nav: Add shadow border to label...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20100615030620/http://www.java2s.com:80/Code/Java/GWT/AddshadowbordertolabelSmartGWT.htm
---
Add shadow border to label (Smart GWT)

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
import com.smartgwt.client.types.DragAppearance;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.Label;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Canvas canvas = new Canvas();
    final Label label1 = createLabel();
    final Label label2 = createLabel();
    final Label label3 = createLabel();
    label1.setEdgeImage("corners/flat_100.png");
    label1.setEdgeSize(30);
    label1.setEdgeOffset(14);
    label2.setLeft(100);
    label2.setTop(80);
    label2.setEdgeImage("corners/ridge_28.png");
    label2.setEdgeSize(28);
    label2.setEdgeOffset(18);
    label3.setLeft(200);
    label3.setTop(160);
    label3.setEdgeImage("corners/glow_35.png");
    label3.setEdgeSize(35);
    label3.setEdgeOffset(25);
    canvas.addChild(label1);
    canvas.addChild(label2);
    canvas.addChild(label3);
    return canvas;
  }
  private Label createLabel() {
    Label label = new Label("EXAMPLE_TEXT");
    label.setWidth(250);
    label.setPadding(8);
    label.setBackgroundColor("white");
    label.setCanDragReposition(true);
    label.setDragAppearance(DragAppearance.TARGET);
    label.setShowEdges(true);
    label.setEdgeShowCenter(true);
    label.setKeepInParentRect(true);
    return label;
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Change style for Label
2.  Change the Label layer (Smart GWT)
3.  Turn on Label border and change the background color (Smart GWT)
