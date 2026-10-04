---
title: Add Image to Canvas (Smart GWT)
nav: Add Image to Canvas (Smart...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20100411202823/http://www.java2s.com:80/Code/Java/GWT/AddImagetoCanvasSmartGWT.htm
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
import com.google.gwt.user.client.Random;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.IButton;
import com.smartgwt.client.widgets.Img;
import com.smartgwt.client.widgets.events.ClickEvent;
import com.smartgwt.client.widgets.events.ClickHandler;
import com.smartgwt.client.widgets.layout.VLayout;
public class Showcase implements EntryPoint{
    public void onModuleLoad() {
       RootPanel.get().add(getViewPanel());
    }
    public Canvas getViewPanel() {
      VLayout layout = new VLayout();
      layout.setMembersMargin(10);
      final Canvas cubeBin = new Canvas("cubeBin");
      cubeBin.setTop(40);
      cubeBin.setWidth(400);
      cubeBin.setHeight(300);
      cubeBin.setShowEdges(true);
      IButton button = new IButton();
      button.setTitle("Create");
      button.setIcon("pieces/16/cube_blue.png");
      button.addClickHandler(new ClickHandler() {
          public void onClick(ClickEvent event) {
              final Img img = new Img();
              img.setLeft(Random.nextInt(340));
              img.setTop(Random.nextInt(240));
              img.setWidth(48);
              img.setHeight(48);
              img.setParentElement(cubeBin);
              img.setSrc("pieces/48/cube_blue.png");
              img.addClickHandler(new ClickHandler() {
                  public void onClick(ClickEvent event) {
                      img.destroy();
                  }
              });
              img.draw();
          }
      });
      layout.addMember(button);
      layout.addMember(cubeBin);
      return layout;
  }
}
```

1.  Image widget that overcomes PNG browser incompatabilities
---  ---
2.  Use GWT Resource To Load Images
3.  Load image
