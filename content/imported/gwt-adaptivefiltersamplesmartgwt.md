---
title: Adaptive Filter Sample (Smart GWT)
nav: Adaptive Filter Sample (Sm...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20100417105728/http://www.java2s.com:80/Code/Java/GWT/AdaptiveFilterSampleSmartGWT.htm
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
import com.google.gwt.user.client.Timer;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.data.DSRequest;
import com.smartgwt.client.data.DSResponse;
import com.smartgwt.client.data.DataSource;
import com.smartgwt.client.data.fields.DataSourceBooleanField;
import com.smartgwt.client.data.fields.DataSourceDateField;
import com.smartgwt.client.data.fields.DataSourceEnumField;
import com.smartgwt.client.data.fields.DataSourceFloatField;
import com.smartgwt.client.data.fields.DataSourceIntegerField;
import com.smartgwt.client.data.fields.DataSourceLinkField;
import com.smartgwt.client.data.fields.DataSourceTextField;
import com.smartgwt.client.util.SC;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.Label;
import com.smartgwt.client.widgets.form.validator.FloatPrecisionValidator;
import com.smartgwt.client.widgets.form.validator.FloatRangeValidator;
import com.smartgwt.client.widgets.grid.ListGrid;
import com.smartgwt.client.widgets.grid.ListGridField;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Canvas canvas = new Canvas();
    final ServerCountLabel serverCountLabel = new ServerCountLabel();
    ItemSupplyXmlDS supplyXmlDS = new ItemSupplyXmlDS(SC.generateID()) {
      // this approach logs simulated server trips for DataSources with
      // clientOnly:true
      // so that no server is required. Since this example has a clientOnly
      // datasource that loads data
      // from a static xml, use the simulated server trips getClientOnlyResponse
      // override point.
      // If working with a real server that returns data dynamically based on
      // start/end row, override
      // transformResponse instead.
      @Override
      public DSResponse getClientOnlyResponse(DSRequest request) {
        DSResponse response = super.getClientOnlyResponse(request);
        int totalRows = response.getTotalRows();
        int startRow = response.getStartRow();
        int endRow = response.getEndRow();
        serverCountLabel.incrementAndUpdate(totalRows, startRow, endRow);
        serverCountLabel.setBackgroundColor("ffff77");
        new Timer() {
          public void run() {
            serverCountLabel.setBackgroundColor("ffffff");
          }
        }.schedule(500);
        return response;
      }
    };
    // when working with a server that dynamically returns the response based on
    // start row, end row,
    // use can override transformResponse instead of getClientOnlyResponse
    /*
     * protected void transformResponse(DSResponse response, DSRequest request,
     * Object data) { int totalRows = response.getTotalRows(); int startRow =
     * response.getStartRow(); int endRow = response.getEndRow();
     * serverCountLabel.incrementAndUpdate(totalRows, startRow, endRow);
     * serverCountLabel.setBackgroundColor("ffff77"); new Timer() { public void
     * run() { serverCountLabel.setBackgroundColor("ffffff"); } }.schedule(500); }
     */
    final ListGrid supplyItemGrid = new ListGrid();
    supplyItemGrid.setWidth(500);
    supplyItemGrid.setHeight(300);
    supplyItemGrid.setAlternateRecordStyles(true);
    supplyItemGrid.setAutoFetchData(true);
    supplyItemGrid.setShowFilterEditor(true);
    supplyItemGrid.setFilterOnKeypress(true);
    supplyItemGrid.setFetchDelay(500);
    supplyItemGrid.setDataSource(supplyXmlDS);
    ListGridField skuField = new ListGridField("SKU", 100);
    ListGridField nameField = new ListGridField("itemName", 150);
    ListGridField descriptionField = new ListGridField("description", 250);
    ListGridField categoryField = new ListGridField("category", 100);
    supplyItemGrid.setFields(skuField, nameField, descriptionField, categoryField);
    canvas.addChild(supplyItemGrid);
    canvas.addChild(serverCountLabel);
    return canvas;
  }
  class ServerCountLabel extends Label {
    private int count = 0;
    ServerCountLabel() {
      setContents("<b>Number of server trips : 0</b>");
      setTop(320);
      setPadding(10);
      setWidth(500);
      setHeight(30);
      setBorder("1px solid black");
    }
    public void incrementAndUpdate(int totalRows, int startRow, int endRow) {
      count++;
      setContents("<b>Number of server trips: " + count + "<br/>Total rows in this filter set: "
          + totalRows + "<br/>Last range of records returned: " + startRow + " to " + endRow
          + "</b>");
    }
  }
}
class SupplyCategoryXmlDS extends DataSource {
  private static SupplyCategoryXmlDS instance = null;
  public static SupplyCategoryXmlDS getInstance() {
    if (instance == null) {
      instance = new SupplyCategoryXmlDS("supplyCategoryDS");
    }
    return instance;
  }
  public SupplyCategoryXmlDS(String id) {
    setID(id);
    setRecordXPath("/List/supplyCategory");
    DataSourceTextField itemNameField = new DataSourceTextField("categoryName", "Item", 128, true);
    itemNameField.setPrimaryKey(true);
    DataSourceTextField parentField = new DataSourceTextField("parentID", null);
    parentField.setHidden(true);
    parentField.setRequired(true);
    parentField.setRootValue("root");
    parentField.setForeignKey("supplyCategoryDS.categoryName");
    setFields(itemNameField, parentField);
    setDataURL("ds/test_data/supplyCategory.data.xml");
    setClientOnly(true);
  }
}
class ItemSupplyXmlDS extends DataSource {
  private static ItemSupplyXmlDS instance = null;
  public static ItemSupplyXmlDS getInstance() {
    if (instance == null) {
      instance = new ItemSupplyXmlDS("supplyItemDS");
    }
    return instance;
  }
  public ItemSupplyXmlDS(String id) {
    setID(id);
    setRecordXPath("/List/supplyItem");
    DataSourceIntegerField pkField = new DataSourceIntegerField("itemID");
    pkField.setHidden(true);
    pkField.setPrimaryKey(true);
    DataSourceTextField itemNameField = new DataSourceTextField("itemName", "Item Name", 128, true);
    DataSourceTextField skuField = new DataSourceTextField("SKU", "SKU", 10, true);
    DataSourceTextField descriptionField = new DataSourceTextField("description", "Description",
        2000);
    DataSourceTextField categoryField = new DataSourceTextField("category", "Category", 128, true);
    categoryField.setForeignKey("supplyCategoryDS.categoryName");
    DataSourceEnumField unitsField = new DataSourceEnumField("units", "Units", 5);
    unitsField.setValueMap("Roll", "Ea", "Pkt", "Set", "Tube", "Pad", "Ream", "Tin", "Bag", "Ctn",
        "Box");
    DataSourceFloatField unitCostField = new DataSourceFloatField("unitCost", "Unit Cost", 5);
    FloatRangeValidator rangeValidator = new FloatRangeValidator();
    rangeValidator.setMin(0);
    rangeValidator.setErrorMessage("Please enter a valid (positive) cost");
    FloatPrecisionValidator precisionValidator = new FloatPrecisionValidator();
    precisionValidator.setPrecision(2);
    precisionValidator.setErrorMessage("The maximum allowed precision is 2");
    unitCostField.setValidators(rangeValidator, precisionValidator);
    DataSourceBooleanField inStockField = new DataSourceBooleanField("inStock", "In Stock");
    DataSourceDateField nextShipmentField = new DataSourceDateField("nextShipment", "Next Shipment");
    setFields(pkField, itemNameField, skuField, descriptionField, categoryField, unitsField,
        unitCostField, inStockField, nextShipmentField);
    setDataURL("ds/test_data/supplyItem.data.xml");
    setClientOnly(true);
  }
}
class CountryXmlDS extends DataSource {
  private static CountryXmlDS instance = null;
  public static CountryXmlDS getInstance() {
    if (instance == null) {
      instance = new CountryXmlDS("countryDS");
    }
    return instance;
  }
  public CountryXmlDS(String id) {
    setID(id);
    setRecordXPath("/List/country");
    DataSourceIntegerField pkField = new DataSourceIntegerField("pk");
    pkField.setHidden(true);
    pkField.setPrimaryKey(true);
    DataSourceTextField countryCodeField = new DataSourceTextField("countryCode", "Code");
    countryCodeField.setRequired(true);
    DataSourceTextField countryNameField = new DataSourceTextField("countryName", "Country");
    countryNameField.setRequired(true);
    DataSourceTextField capitalField = new DataSourceTextField("capital", "Capital");
    DataSourceTextField governmentField = new DataSourceTextField("government", "Government", 500);
    DataSourceBooleanField memberG8Field = new DataSourceBooleanField("member_g8", "G8");
    DataSourceTextField continentField = new DataSourceTextField("continent", "Continent");
    continentField.setValueMap("Europe", "Asia", "North America", "Australia/Oceania",
        "South America", "Africa");
    DataSourceDateField independenceField = new DataSourceDateField("independence", "Nationhood");
    DataSourceFloatField areaField = new DataSourceFloatField("area", "Area (km&amp;sup2;)");
    DataSourceIntegerField populationField = new DataSourceIntegerField("population", "Population");
    DataSourceFloatField gdpField = new DataSourceFloatField("gdp", "GDP ($M)");
    DataSourceLinkField articleField = new DataSourceLinkField("article", "Info");
    setFields(pkField, countryCodeField, countryNameField, capitalField, governmentField,
        memberG8Field, continentField, independenceField, areaField, populationField, gdpField,
        articleField);
    setDataURL("ds/test_data/country.data.xml");
    setClientOnly(true);
  }
}
```

SmartGWT.zip( 9,880 k)
