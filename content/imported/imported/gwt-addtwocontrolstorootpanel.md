---
title: Add two controls to RootPanel
nav: Add two controls to RootPa...
description: Imported from the java2s.com archive: Add two controls to RootPanel
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20091010112400/http://www.java2s.com:80/Code/Java/GWT/AddtwocontrolstoRootPanel.htm
---
```java title=Example.java
package com.java2s.gwt.client;
import com.google.gwt.core.client.*;
import com.google.gwt.user.client.ui.*;
public class GWTClient implements EntryPoint{
   public void onModuleLoad() {
      final Button button = new Button("Click me");
      final Label label = new Label();
      button.addClickListener(new ClickListener() {
         public void onClick(Widget sender) {
            if (label.getText().equals(""))
               label.setText("Hello World!");
            else
               label.setText("");
         }
      });
      RootPanel.get("slot1").add(button);
      RootPanel.get("slot2").add(label);
   }
}
```

GWT-inTable.zip( 2 k)
1.  Use RootPanel to Load New Page
