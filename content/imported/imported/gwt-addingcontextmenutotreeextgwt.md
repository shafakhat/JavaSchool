---
title: Adding Context Menu to Tree (Ext GWT)
nav: Adding Context Menu to Tre...
description: final TreeStore<ModelData> store = new TreeStore<ModelData>();
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20100821202549/http://www.java2s.com:80/Code/Java/GWT/AddingContextMenutoTreeExtGWT.htm
---
Adding Context Menu to Tree (Ext GWT)

```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import java.io.Serializable;
import java.util.List;
import com.extjs.gxt.ui.client.data.BaseTreeModel;
import com.extjs.gxt.ui.client.data.ModelData;
import com.extjs.gxt.ui.client.event.ButtonEvent;
import com.extjs.gxt.ui.client.event.MenuEvent;
import com.extjs.gxt.ui.client.event.SelectionListener;
import com.extjs.gxt.ui.client.store.TreeStore;
import com.extjs.gxt.ui.client.widget.LayoutContainer;
import com.extjs.gxt.ui.client.widget.button.Button;
import com.extjs.gxt.ui.client.widget.layout.FlowData;
import com.extjs.gxt.ui.client.widget.layout.FlowLayout;
import com.extjs.gxt.ui.client.widget.menu.Menu;
import com.extjs.gxt.ui.client.widget.menu.MenuItem;
import com.extjs.gxt.ui.client.widget.treepanel.TreePanel;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.ui.RootPanel;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(new ContextMenuTreePanelExample());
  }
}
class ContextMenuTreePanelExample extends LayoutContainer {
  private int count = 1;
  @Override
  protected void onRender(Element parent, int pos) {
    super.onRender(parent, pos);
    final Folder model = getTreeModel();
    final TreeStore<ModelData> store = new TreeStore<ModelData>();
    store.add(model.getChildren(), true);
    add(new Button("Reset", new SelectionListener<ButtonEvent>() {
      public void componentSelected(ButtonEvent ce) {
        store.removeAll();
        store.add(model.getChildren(), true);
      }
    }),new FlowData(10));
    final TreePanel<ModelData> tree = new TreePanel<ModelData>(store);
    tree.setDisplayProperty("name");
//    tree.getStyle().setLeafIcon(Resources.ICONS.music());
    tree.setWidth(250);
    Menu contextMenu = new Menu();
    MenuItem insert = new MenuItem();
    insert.setText("Insert Item");
  //  insert.setIcon(Resources.ICONS.add());
    insert.addSelectionListener(new SelectionListener<MenuEvent>() {
      public void componentSelected(MenuEvent ce) {
        ModelData folder = tree.getSelectionModel().getSelectedItem();
        if (folder != null) {
          Folder child = new Folder("Add Child " + count++);
          store.add(folder, child, false);
          tree.setExpanded(folder, true);
        }
      }
    });
    contextMenu.add(insert);
    MenuItem remove = new MenuItem();
    remove.setText("Remove Selected");
    //remove.setIcon(Resources.ICONS.delete());
    remove.addSelectionListener(new SelectionListener<MenuEvent>() {
      public void componentSelected(MenuEvent ce) {
        List<ModelData> selected = tree.getSelectionModel().getSelectedItems();
        for (ModelData sel : selected) {
          store.remove(sel);
        }
      }
    });
    contextMenu.add(remove);
    tree.setContextMenu(contextMenu);
    setLayout(new FlowLayout(8));
    add(tree);
  }
  public static Folder getTreeModel() {
    Folder[] folders = new Folder[] {
        new Folder("Beethoven",
            new Folder[] {
                new Folder("Quartets",
                    new Music[] {
                        new Music("Six String Quartets", "Beethoven", "Quartets"),
                        new Music("Three String Quartets", "Beethoven", "Quartets"),
                        new Music("Grosse Fugue for String Quartets", "Beethoven",
                            "Quartets"),}),
                new Folder("Sonatas", new Music[] {
                    new Music("Sonata in A Minor", "Beethoven", "Sonatas"),
                    new Music("Sonata in F Major", "Beethoven", "Sonatas"),}),
                new Folder("Concertos", new Music[] {
                    new Music("No. 1 - C", "Beethoven", "Concertos"),
                    new Music("No. 2 - B-Flat Major", "Beethoven", "Concertos"),
                    new Music("No. 3 - C Minor", "Beethoven", "Concertos"),
                    new Music("No. 4 - G Major", "Beethoven", "Concertos"),
                    new Music("No. 5 - E-Flat Major", "Beethoven", "Concertos"),}),
                new Folder("Symphonies", new Music[] {
                    new Music("No. 1 - C Major", "Beethoven", "Symphonies"),
                    new Music("No. 2 - D Major", "Beethoven", "Symphonies"),
                    new Music("No. 3 - E-Flat Major", "Beethoven", "Symphonies"),
                    new Music("No. 4 - B-Flat Major", "Beethoven", "Symphonies"),
                    new Music("No. 5 - C Minor", "Beethoven", "Symphonies"),
                    new Music("No. 6 - F Major", "Beethoven", "Symphonies"),
                    new Music("No. 7 - A Major", "Beethoven", "Symphonies"),
                    new Music("No. 8 - F Major", "Beethoven", "Symphonies"),
                    new Music("No. 9 - D Minor", "Beethoven", "Symphonies"),}),}),
        new Folder("Brahms",
            new Folder[] {
                new Folder("Concertos", new Music[] {
                    new Music("Violin Concerto", "Brahms", "Concertos"),
                    new Music("Double Concerto - A Minor", "Brahms", "Concertos"),
                    new Music("Piano Concerto No. 1 - D Minor", "Brahms", "Concertos"),
                    new Music("Piano Concerto No. 2 - B-Flat Major", "Brahms",
                        "Concertos"),}),
                new Folder("Quartets",
                    new Music[] {
                        new Music("Piano Quartet No. 1 - G Minor", "Brahms", "Quartets"),
                        new Music("Piano Quartet No. 2 - A Major", "Brahms", "Quartets"),
                        new Music("Piano Quartet No. 3 - C Minor", "Brahms", "Quartets"),
                        new Music("String Quartet No. 3 - B-Flat Minor", "Brahms",
                            "Quartets"),}),
                new Folder("Sonatas", new Music[] {
                    new Music("Two Sonatas for Clarinet - F Minor", "Brahms", "Sonatas"),
                    new Music("Two Sonatas for Clarinet - E-Flat Major", "Brahms",
                        "Sonatas"),}),
                new Folder("Symphonies", new Music[] {
                    new Music("No. 1 - C Minor", "Brahms", "Symphonies"),
                    new Music("No. 2 - D Minor", "Brahms", "Symphonies"),
                    new Music("No. 3 - F Major", "Brahms", "Symphonies"),
                    new Music("No. 4 - E Minor", "Brahms", "Symphonies"),}),}),
        new Folder("Mozart", new Folder[] {new Folder("Concertos", new Music[] {
            new Music("Piano Concerto No. 12", "Mozart", "Concertos"),
            new Music("Piano Concerto No. 17", "Mozart", "Concertos"),
            new Music("Clarinet Concerto", "Mozart", "Concertos"),
            new Music("Violin Concerto No. 5", "Mozart", "Concertos"),
            new Music("Violin Concerto No. 4", "Mozart", "Concertos"),}),}),};
    Folder root = new Folder("root");
    for (int i = 0; i < folders.length; i++) {
      root.add((Folder) folders[i]);
    }
    return root;
  }
}
class Music extends BaseTreeModel {
  public Music() {
  }
  public Music(String name) {
    set("name", name);
  }
  public Music(String name, String author, String genre) {
    set("name", name);
    set("author", author);
    set("genre", genre);
  }
  public String getName() {
    return (String) get("name");
  }
  public String getAuthor() {
    return (String) get("author");
  }
  public String getGenre() {
    return (String) get("genre");
  }
  public String toString() {
    return getName();
  }
}
class Folder extends BaseTreeModel implements Serializable {
  private static int ID = 0;
  public Folder() {
    set("id", ID++);
  }
  public Folder(String name) {
    set("id", ID++);
    set("name", name);
  }
  public Folder(String name, BaseTreeModel[] children) {
    this(name);
    for (int i = 0; i < children.length; i++) {
      add(children[i]);
    }
  }
  public Integer getId() {
    return (Integer) get("id");
  }
  public String getName() {
    return (String) get("name");
  }
  public String toString() {
    return getName();
  }
}
```

Ext-GWT.zip( 4,297 k)
1.  Use TreeListener
2.  Create Tree With Pending Item
