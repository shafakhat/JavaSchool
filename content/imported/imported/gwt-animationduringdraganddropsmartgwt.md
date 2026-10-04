---
title: Animation during drag and drop (Smart GWT)
nav: Animation during drag and ...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20100921012303/http://www.java2s.com:80/Code/Java/GWT/AnimationduringdraganddropSmartGWT.htm
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
import com.smartgwt.client.types.DragAppearance;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.Img;
import com.smartgwt.client.widgets.layout.HStack;
import com.smartgwt.client.widgets.layout.VStack;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    HStack hStack = new HStack(10);
    hStack.setLayoutMargin(10);
    hStack.setLeft(120);
    hStack.setShowEdges(true);
    hStack.setEdgeImage("edges/blue/6.png");
    hStack.setCanAcceptDrop(true);
    hStack.setAnimateMembers(true);
    hStack.setShowDragPlaceHolder(true);
    hStack.setBorder("1px solid #4040ff");
    hStack.addMember(new DragPiece("cube_blue.png"));
    hStack.addMember(new DragPiece("cube_green.png"));
    hStack.addMember(new DragPiece("cube_yellow.png"));
    VStack vStack = new VStack(10);
    vStack.setLayoutMargin(10);
    vStack.setShowEdges(true);
    vStack.setEdgeImage("edges/green/6.png");
    vStack.setCanAcceptDrop(true);
    vStack.setAnimateMembers(true);
    vStack.setDropLineThickness(4);
    Canvas dropLineProp = new Canvas();
    dropLineProp.setBackgroundColor("#40c040");
    vStack.setDropLineProperties(dropLineProp);
    vStack.addMember(new DragPiece("cube_blue.png"));
    vStack.addMember(new DragPiece("cube_green.png"));
    vStack.addMember(new DragPiece("cube_yellow.png"));
    Canvas main = new Canvas();
    main.addChild(hStack);
    main.addChild(vStack);
    return main;
  }
  private class DragPiece extends Img {
    public DragPiece() {
      setWidth(48);
      setHeight(48);
      setLayoutAlign(Alignment.CENTER);
      setCanDragReposition(true);
      setCanDrop(true);
      setDragAppearance(DragAppearance.TARGET);
      setAppImgDir("pieces/48/");
    }
    public DragPiece(String src) {
      this();
      setSrc(src);
    }
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Click the buttons to move the draggable box above or below the other boxes (Smart GWT)
4.  Drag effect: Translucent, Shadow, Outline (Smart GWT)
