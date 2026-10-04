---
title: Adding icon to tab bar (Ext GWT)
nav: Adding icon to tab bar (Ex...
description: ajax1.setAutoLoad(new RequestBuilder(RequestBuilder.GET, GWT.getHostPageBaseURL() + "data/ajax1.html"));
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20100422211009/http://www.java2s.com:80/Code/Java/GWT/AddingicontotabbarExtGWT.htm
---
```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import com.extjs.gxt.ui.client.Style.Scroll;
import com.extjs.gxt.ui.client.event.ComponentEvent;
import com.extjs.gxt.ui.client.event.Events;
import com.extjs.gxt.ui.client.event.Listener;
import com.extjs.gxt.ui.client.widget.LayoutContainer;
import com.extjs.gxt.ui.client.widget.TabItem;
import com.extjs.gxt.ui.client.widget.TabPanel;
import com.extjs.gxt.ui.client.widget.VerticalPanel;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.core.client.GWT;
import com.google.gwt.http.client.RequestBuilder;
import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.RootPanel;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(new BasicTabExample());
  }
}
class BasicTabExample extends LayoutContainer {
  @Override
  protected void onRender(Element parent, int pos) {
    super.onRender(parent, pos);
    VerticalPanel vp = new VerticalPanel();
    vp.setSpacing(10);
    String txt = "SHORT";
    TabPanel folder = new TabPanel();
    folder.setWidth(450);
    folder.setAutoHeight(true);
    TabItem shortText = new TabItem("Short Text");
    shortText.addStyleName("pad-text");
    shortText.addText(txt);
    folder.add(shortText);
    TabItem longText = new TabItem("Long Text");
    longText.addStyleName("pad-text");
    longText.addText(txt + "<br>" + txt);
    folder.add(longText);
    TabPanel panel = new TabPanel();
    panel.setPlain(true);
    panel.setSize(450, 250);
    TabItem normal = new TabItem("Normal");
    normal.addStyleName("pad-text");
    normal.addText("Just a plain old tab");
    panel.add(normal);
    TabItem iconTab = new TabItem("Icon Tab");
    //iconTab.setIcon(Resources.ICONS.table());
    iconTab.addStyleName("pad-text");
    iconTab.addText("Just a plain old tab with an icon");
    panel.add(iconTab);
    TabItem ajax1 = new TabItem("Ajax Tab");
    ajax1.setScrollMode(Scroll.AUTO);
    ajax1.addStyleName("pad-text");
    ajax1.setAutoLoad(new RequestBuilder(RequestBuilder.GET, GWT.getHostPageBaseURL() + "data/ajax1.html"));
    panel.add(ajax1);
    TabItem eventTab = new TabItem("Event Tab");
    eventTab.addListener(Events.Select, new Listener<ComponentEvent>() {
      public void handleEvent(ComponentEvent be) {
        Window.alert("Event Tab Was Selected");
      }
    });
    eventTab.addStyleName("pad-text");
    eventTab.addText("I am tab 4's content. I also have an event listener attached.");
    panel.add(eventTab);
    TabItem disabled = new TabItem("Disabled");
    disabled.setEnabled(false);
    panel.add(disabled);
    vp.add(folder);
    vp.add(panel);
    add(vp);
  }
}
```

Ext-GWT.zip( 4,297 k)
