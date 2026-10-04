---
title: Add row expander (Ext GWT)
nav: Add row expander (Ext GWT)
description: import com.extjs.gxt.ui.client.widget.grid.CheckBoxSelectionModel;
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20100417045057/http://www.java2s.com:80/Code/Java/GWT/AddrowexpanderExtGWT.htm
---
Add row expander (Ext GWT)

```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import com.extjs.gxt.ui.client.Style.HorizontalAlignment;
import com.extjs.gxt.ui.client.core.XTemplate;
import com.extjs.gxt.ui.client.data.BaseModel;
import com.extjs.gxt.ui.client.event.ButtonEvent;
import com.extjs.gxt.ui.client.event.SelectionListener;
import com.extjs.gxt.ui.client.store.ListStore;
import com.extjs.gxt.ui.client.widget.Component;
import com.extjs.gxt.ui.client.widget.ContentPanel;
import com.extjs.gxt.ui.client.widget.LayoutContainer;
import com.extjs.gxt.ui.client.widget.VerticalPanel;
import com.extjs.gxt.ui.client.widget.button.Button;
import com.extjs.gxt.ui.client.widget.grid.CheckBoxSelectionModel;
import com.extjs.gxt.ui.client.widget.grid.ColumnConfig;
import com.extjs.gxt.ui.client.widget.grid.ColumnData;
import com.extjs.gxt.ui.client.widget.grid.ColumnModel;
import com.extjs.gxt.ui.client.widget.grid.Grid;
import com.extjs.gxt.ui.client.widget.grid.GridCellRenderer;
import com.extjs.gxt.ui.client.widget.grid.RowExpander;
import com.extjs.gxt.ui.client.widget.grid.RowNumberer;
import com.extjs.gxt.ui.client.widget.layout.FitLayout;
import com.extjs.gxt.ui.client.widget.table.NumberCellRenderer;
import com.extjs.gxt.ui.client.widget.toolbar.SeparatorToolItem;
import com.extjs.gxt.ui.client.widget.toolbar.ToolBar;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.i18n.client.DateTimeFormat;
import com.google.gwt.i18n.client.NumberFormat;
import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.impl.WindowImplIE.Resources;
import com.google.gwt.user.client.ui.RootPanel;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(new GridPluginsExample());
  }
}
class GridPluginsExample extends LayoutContainer {
  private VerticalPanel panel;
  private GridCellRenderer<Stock> gridNumber;
  private GridCellRenderer<Stock> change;
  public GridPluginsExample() {
    final NumberFormat currency = NumberFormat.getCurrencyFormat();
    final NumberFormat number = NumberFormat.getFormat("0.00");
    final NumberCellRenderer<Grid<Stock>> numberRenderer = new NumberCellRenderer<Grid<Stock>>(currency);
    change = new GridCellRenderer<Stock>() {
      public String render(Stock model, String property, ColumnData config, int rowIndex, int colIndex,
          ListStore<Stock> store, Grid<Stock> grid) {
        double val = (Double) model.get(property);
        String style = val < 0 ? "red" : "green";
        return "<span style='color:" + style + "'>" + number.format(val) + "</span>";
      }
    };
    gridNumber = new GridCellRenderer<Stock>() {
      public String render(Stock model, String property, ColumnData config, int rowIndex, int colIndex,
          ListStore<Stock> store, Grid<Stock> grid) {
        return numberRenderer.render(null, property, model.get(property));
      }
    };
    panel = new VerticalPanel();
    panel.setSpacing(20);
  }
  @Override
  protected void onRender(Element parent, int index) {
    super.onRender(parent, index);
    createExpander();
    add(panel);
  }
  private void createExpander() {
    List<Stock> stocks = getStocks();
    for (Stock s : stocks) {
      s.set(
          "desc",
          "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed metus nibh, sodales a, porta at, vulputate eget, dui. Pellentesque ut nisl. Maecenas tortor turpis, interdum non, sodales non, iaculis ac, lacus. Vestibulum auctor, tortor quis iaculis malesuada, libero lectus bibendum purus, sit amet tincidunt quam turpis vel lacus. In pellentesque nisl non sem. Suspendisse nunc sem, pretium eget, cursus a, fringilla vel, urna.<br/><br/>Aliquam commodo ullamcorper erat. Nullam vel justo in neque porttitor laoreet. Aenean lacus dui, consequat eu, adipiscing eget, nonummy non, nisi. Morbi nunc est, dignissim non, ornare sed, luctus eu, massa. Vivamus eget quam. Vivamus tincidunt diam nec urna. Curabitur velit.");
    }
    List<ColumnConfig> configs = new ArrayList<ColumnConfig>();
    XTemplate tpl = XTemplate.create("<p><b>Company:</b> {name}</p><br><p><b>Summary:</b> {desc}</p>");
    RowExpander expander = new RowExpander();
    expander.setTemplate(tpl);
    configs.add(expander);
    ColumnConfig column = new ColumnConfig();
    column.setId("name");
    column.setHeader("Company");
    column.setWidth(200);
    configs.add(column);
    column = new ColumnConfig();
    column.setId("symbol");
    column.setHeader("Symbol");
    column.setWidth(100);
    configs.add(column);
    column = new ColumnConfig();
    column.setId("last");
    column.setHeader("Last");
    column.setAlignment(HorizontalAlignment.RIGHT);
    column.setWidth(75);
    column.setRenderer(gridNumber);
    configs.add(column);
    column = new ColumnConfig("change", "Change", 100);
    column.setAlignment(HorizontalAlignment.RIGHT);
    column.setRenderer(change);
    configs.add(column);
    column = new ColumnConfig("date", "Last Updated", 100);
    column.setAlignment(HorizontalAlignment.RIGHT);
    column.setDateTimeFormat(DateTimeFormat.getShortDateFormat());
    configs.add(column);
    ListStore<Stock> store = new ListStore<Stock>();
    store.add(stocks);
    ColumnModel cm = new ColumnModel(configs);
    ContentPanel cp = new ContentPanel();
    cp.setHeading("Expander Rows, Collapse and Auto Fill");
    //cp.setIcon(Resources.ICONS.table());
    cp.setAnimCollapse(false);
    cp.setCollapsible(true);
    cp.setLayout(new FitLayout());
    cp.setSize(600, 300);
    Grid<Stock> grid = new Grid<Stock>(store, cm);
    grid.addPlugin(expander);
    grid.getView().setAutoFill(true);
    cp.add(grid);
    panel.add(cp);
  }
  public static List<Stock> getStocks() {
    List<Stock> stocks = new ArrayList<Stock>();
    stocks.add(new Stock("Apple Inc.", "AAPL", 125.64, 123.43));
    stocks.add(new Stock("Cisco Systems, Inc.", "CSCO", 25.84, 26.3));
    stocks.add(new Stock("Google Inc.", "GOOG", 516.2, 512.6));
    stocks.add(new Stock("Intel Corporation", "INTC", 21.36, 21.53));
    stocks.add(new Stock("Level 3 Communications, Inc.", "LVLT", 5.55, 5.54));
    stocks.add(new Stock("Microsoft Corporation", "MSFT", 29.56, 29.72));
    stocks.add(new Stock("Nokia Corporation (ADR)", "NOK", 27.83, 27.93));
    stocks.add(new Stock("Oracle Corporation", "ORCL", 18.73, 18.98));
    stocks.add(new Stock("Starbucks Corporation", "SBUX", 27.33, 27.36));
    stocks.add(new Stock("Yahoo! Inc.", "YHOO", 26.97, 27.29));
    stocks.add(new Stock("Applied Materials, Inc.", "AMAT", 18.4, 18.66));
    stocks.add(new Stock("Comcast Corporation", "CMCSA", 25.9, 26.4));
    stocks.add(new Stock("Sirius Satellite", "SIRI", 2.77, 2.74));
    stocks.add(new Stock("Tellabs, Inc.", "TLAB", 10.64, 10.75));
    stocks.add(new Stock("eBay Inc.", "EBAY", 30.43, 31.21));
    stocks.add(new Stock("Broadcom Corporation", "BRCM", 30.88, 30.48));
    stocks.add(new Stock("CMGI Inc.", "CMGI", 2.14, 2.13));
    stocks.add(new Stock("Amgen, Inc.", "AMGN", 56.22, 57.02));
    stocks.add(new Stock("Limelight Networks", "LLNW", 23, 22.11));
    stocks.add(new Stock("Amazon.com, Inc.", "AMZN", 72.47, 72.23));
    stocks.add(new Stock("E TRADE Financial Corporation", "ETFC", 24.32, 24.58));
    stocks.add(new Stock("AVANIR Pharmaceuticals", "AVNR", 3.7, 3.52));
    stocks.add(new Stock("Gemstar-TV Guide, Inc.", "GMST", 4.41, 4.55));
    stocks.add(new Stock("Akamai Technologies, Inc.", "AKAM", 43.08, 45.32));
    stocks.add(new Stock("Motorola, Inc.", "MOT", 17.74, 17.69));
    stocks.add(new Stock("Advanced Micro Devices, Inc.", "AMD", 13.77, 13.98));
    stocks.add(new Stock("General Electric Company", "GE", 36.8, 36.91));
    stocks.add(new Stock("Texas Instruments Incorporated", "TXN", 35.02, 35.7));
    stocks.add(new Stock("Qwest Communications", "Q", 9.9, 10.03));
    stocks.add(new Stock("Tyco International Ltd.", "TYC", 33.48, 33.26));
    stocks.add(new Stock("Pfizer Inc.", "PFE", 26.21, 26.19));
    stocks.add(new Stock("Time Warner Inc.", "TWX", 20.3, 20.45));
    stocks.add(new Stock("Sprint Nextel Corporation", "S", 21.85, 21.76));
    stocks.add(new Stock("Bank of America Corporation", "BAC", 49.92, 49.73));
    stocks.add(new Stock("Taiwan Semiconductor", "TSM", 10.4, 10.52));
    stocks.add(new Stock("AT&T Inc.", "T", 39.7, 39.66));
    stocks.add(new Stock("United States Steel Corporation", "X", 115.81, 114.62));
    stocks.add(new Stock("Exxon Mobil Corporation", "XOM", 81.77, 81.86));
    stocks.add(new Stock("Valero Energy Corporation", "VLO", 72.46, 72.6));
    stocks.add(new Stock("Micron Technology, Inc.", "MU", 12.02, 12.27));
    stocks.add(new Stock("Verizon Communications Inc.", "VZ", 42.5, 42.61));
    stocks.add(new Stock("Avaya Inc.", "AV", 16.96, 16.96));
    stocks.add(new Stock("The Home Depot, Inc.", "HD", 37.66, 37.79));
    stocks.add(new Stock("First Data Corporation", "FDC", 32.7, 32.65));
    return stocks;
  }
}
class Stock extends BaseModel {
  public Stock() {
  }
  public Stock(String name, String symbol, double open, double last) {
    set("name", name);
    set("symbol", symbol);
    set("open", open);
    set("last", last);
    set("date", new Date());
    set("change", last - open);
  }
  public Stock(String name, double open, double change, double pctChange, Date date, String industry) {
    set("name", name);
    set("open", open);
    set("change", change);
    set("percentChange", pctChange);
    set("date", date);
    set("industry", industry);
  }
  public String getIndustry() {
    return get("industry");
  }
  public void setIndustry(String industry) {
    set("industry", industry);
  }
  public Date getLastTrans() {
    return (Date) get("date");
  }
  public String getName() {
    return (String) get("name");
  }
  public String getSymbol() {
    return (String) get("symbol");
  }
  public double getOpen() {
    Double open = (Double) get("open");
    return open.doubleValue();
  }
  public double getLast() {
    Double open = (Double) get("last");
    return open.doubleValue();
  }
  public double getChange() {
    return getLast() - getOpen();
  }
  public double getPercentChange() {
    return getChange() / getOpen();
  }
  public String toString() {
    return getName();
  }
}
```

Ext-GWT.zip( 4,297 k)
5.  Sortable column (Smart GWT)
