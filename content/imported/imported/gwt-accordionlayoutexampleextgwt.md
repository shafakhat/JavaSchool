---
title: Accordion Layout Example (Ext GWT)
nav: Accordion Layout Example (...
description: import com.extjs.gxt.ui.client.widget.layout.AccordionLayout;
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20100618041203/http://www.java2s.com:80/Code/Java/GWT/AccordionLayoutExampleExtGWT.htm
---
Accordion Layout Example (Ext GWT)

```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import com.extjs.gxt.ui.client.data.BaseModelData;
import com.extjs.gxt.ui.client.data.ModelData;
import com.extjs.gxt.ui.client.data.ModelIconProvider;
import com.extjs.gxt.ui.client.store.TreeStore;
import com.extjs.gxt.ui.client.util.IconHelper;
import com.extjs.gxt.ui.client.widget.ContentPanel;
import com.extjs.gxt.ui.client.widget.layout.AccordionLayout;
import com.extjs.gxt.ui.client.widget.layout.FitLayout;
import com.extjs.gxt.ui.client.widget.treepanel.TreePanel;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.ui.AbstractImagePrototype;
import com.google.gwt.user.client.ui.RootPanel;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    //setLayout(new FlowLayout(10));
    ContentPanel panel = new ContentPanel();
    panel.setHeading("AccordionLayout");
    panel.setBodyBorder(false);
    panel.setLayout(new AccordionLayout());
    //panel.setIcon(Resources.ICONS.accordion());
    ContentPanel cp = new ContentPanel();
    cp.setAnimCollapse(false);
    cp.setHeading("Online Users");
    cp.setLayout(new FitLayout());
    panel.add(cp);
    TreeStore<ModelData> store = new TreeStore<ModelData>();
    TreePanel<ModelData> tree = new TreePanel<ModelData>(store);
    tree.setIconProvider(new ModelIconProvider<ModelData>() {
      public AbstractImagePrototype getIcon(ModelData model) {
        if (model.get("icon") != null) {
          return IconHelper.createStyle((String) model.get("icon"));
        } else {
          return null;
        }
      }
    });
    tree.setDisplayProperty("name");
    ModelData m = newItem("Family", null);
    store.add(m, false);
    store.add(m, newItem("Darrell", "user"), false);
    store.add(m, newItem("Maro", "user-girl"), false);
    store.add(m, newItem("Lia", "user-kid"), false);
    store.add(m, newItem("Alec", "user-kid"), false);
    store.add(m, newItem("Andrew", "user-kid"), false);
    tree.setExpanded(m, true);
    m = newItem("Friends", null);
    store.add(m, false);
    store.add(m, newItem("Bob", "user"), false);
    store.add(m, newItem("Mary", "user-girl"), false);
    store.add(m, newItem("Sally", "user-girl"), false);
    store.add(m, newItem("Jack", "user"), false);
    tree.setExpanded(m, true);
    cp.add(tree);
    cp = new ContentPanel();
    cp.setAnimCollapse(false);
    cp.setBodyStyleName("pad-text");
    cp.setHeading("Settings");
    cp.addText("DUMMY_TEXT_SHORT");
    panel.add(cp);
    cp = new ContentPanel();
    cp.setAnimCollapse(false);
    cp.setBodyStyleName("pad-text");
    cp.setHeading("Stuff");
    cp.addText("DUMMY_TEXT_SHORT");
    panel.add(cp);
    cp = new ContentPanel();
    cp.setAnimCollapse(false);
    cp.setBodyStyleName("pad-text");
    cp.setHeading("More Stuff");
    cp.addText("DUMMY_TEXT_SHORT");
    panel.add(cp);
    panel.setSize(200, 325);
    RootPanel.get().add(panel);
  }
  private ModelData newItem(String text, String iconStyle) {
    ModelData m = new BaseModelData();
    m.set("name", text);
    m.set("icon", iconStyle);
    return m;
  }
}
```

Ext-GWT.zip( 4,297 k)
