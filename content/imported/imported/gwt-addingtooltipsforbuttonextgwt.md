---
title: Adding tooltips for Button (Ext GWT)
nav: Adding tooltips for Button...
description: btn.setToolTip(new ToolTipConfig("Information", "Prints the current document"));
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20101207174144/http://www.java2s.com:80/Code/Java/GWT/AddingtooltipsforButtonExtGWT.htm
---
Adding tooltips for Button (Ext GWT)

```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import com.extjs.gxt.ui.client.widget.LayoutContainer;
import com.extjs.gxt.ui.client.widget.button.Button;
import com.extjs.gxt.ui.client.widget.layout.FlowData;
import com.extjs.gxt.ui.client.widget.tips.ToolTipConfig;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.ui.RootPanel;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(new ToolTipsExample());
  }
}
class ToolTipsExample extends LayoutContainer {
  @Override
  protected void onRender(Element parent, int pos) {
    super.onRender(parent, pos);
    Button btn = new Button("Print");
    btn.setToolTip(new ToolTipConfig("Information", "Prints the current document"));
    add(btn, new FlowData(10));
  }
}
```

Ext-GWT.zip( 4,297 k)
1.  Tooltip component for GWT
2.  Add buttons to ToolStrip(ToolBar) (Smart GWT)
