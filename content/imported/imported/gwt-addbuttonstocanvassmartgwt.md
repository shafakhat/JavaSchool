---
title: Add buttons to Canvas (Smart GWT)
nav: Add buttons to Canvas (Sma...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20100503043427/http://www.java2s.com:80/Code/Java/GWT/AddbuttonstoCanvasSmartGWT.htm
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
import com.smartgwt.client.widgets.IButton;
import com.smartgwt.client.widgets.Img;
import com.smartgwt.client.widgets.events.ClickEvent;
import com.smartgwt.client.widgets.events.ClickHandler;
public class Showcase implements EntryPoint{
    public void onModuleLoad() {
       RootPanel.get().add(getViewPanel());
    }
    public Canvas getViewPanel() {
      Canvas canvas = new Canvas();
      final Img myImage = new Img("star_grey.png", 48, 48);
      myImage.setAppImgDir("pieces/48/");
      myImage.setLeft(120);
      myImage.setTop(20);
      canvas.addChild(myImage);
      IButton showBlueButton = new IButton("Show");
      showBlueButton.setLeft(10);
      showBlueButton.setTop(100);
      showBlueButton.setWidth(80);
      showBlueButton.setIconOrientation("right");
      showBlueButton.setIcon("pieces/16/star_blue.png");
      showBlueButton.addClickHandler(new ClickHandler() {
          public void onClick(ClickEvent event) {
              myImage.setSrc("star_blue.png");
          }
      });
      canvas.addChild(showBlueButton);
      IButton showYellowButton = new IButton("Show");
      showYellowButton.setLeft(100);
      showYellowButton.setTop(100);
      showYellowButton.setWidth(80);
      showYellowButton.setIconOrientation("right");
      showYellowButton.setIcon("pieces/16/star_yellow.png");
      showYellowButton.addClickHandler(new ClickHandler() {
          public void onClick(ClickEvent event) {
              myImage.setSrc("star_yellow.png");
          }
      });
      canvas.addChild(showYellowButton);
      IButton showGreenButton = new IButton("Show");
      showGreenButton.setLeft(190);
      showGreenButton.setTop(100);
      showGreenButton.setWidth(80);
      showGreenButton.setIconOrientation("right");
      showGreenButton.setIcon("pieces/16/star_green.png");
      showGreenButton.addClickHandler(new ClickHandler() {
          public void onClick(ClickEvent event) {
              myImage.setSrc("star_green.png");
          }
      });
      canvas.addChild(showGreenButton);
      return canvas;
    }
}
```

SmartGWT.zip( 9,880 k)
1.  Set margin of vertical layout (Smart GWT)
2.  HLayout/VLayout manage the stacked positions and sizes of multiple member components (Smart GWT)
3.  Set layout percentage with * (Smart GWT)
23.  VBoxLayout Example (Ext GWT)
28.  Multi-Spaced horizontal layout (Ext GWT)
