---
title: Adding tooltip based help information next to a field (Smart GWT)
nav: Adding tooltip based help ...
description: Adding tooltip based help information next to a field (Smart GWT)
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20100925015934/http://www.java2s.com:80/Code/Java/GWT/AddingtooltipbasedhelpinformationnexttoafieldSmartGWT.htm
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
import com.google.gwt.i18n.client.NumberFormat;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.data.DataSource;
import com.smartgwt.client.data.fields.DataSourceBooleanField;
import com.smartgwt.client.data.fields.DataSourceDateField;
import com.smartgwt.client.data.fields.DataSourceFloatField;
import com.smartgwt.client.data.fields.DataSourceIntegerField;
import com.smartgwt.client.data.fields.DataSourceLinkField;
import com.smartgwt.client.data.fields.DataSourceTextField;
import com.smartgwt.client.types.Alignment;
import com.smartgwt.client.types.Autofit;
import com.smartgwt.client.types.ListGridFieldType;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.IButton;
import com.smartgwt.client.widgets.events.ClickEvent;
import com.smartgwt.client.widgets.events.ClickHandler;
import com.smartgwt.client.widgets.grid.CellFormatter;
import com.smartgwt.client.widgets.grid.ListGrid;
import com.smartgwt.client.widgets.grid.ListGridField;
import com.smartgwt.client.widgets.grid.ListGridRecord;
import com.smartgwt.client.widgets.layout.HLayout;
import com.smartgwt.client.widgets.layout.VLayout;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    VLayout layout = new VLayout(15);
    final ListGrid countryGrid = new ListGrid();
    countryGrid.setWidth(750);
    countryGrid.setHeight(224);
    countryGrid.setAlternateRecordStyles(true);
    countryGrid.setDataSource(CountryXmlDS.getInstance());
    countryGrid.setAutoFetchData(true);
    countryGrid.setAutoFitData(Autofit.HORIZONTAL);
    //allow users to add formula and summary fields
    //accessible in the grid header context menu
    countryGrid.setCanAddFormulaFields(true);
    countryGrid.setCanAddSummaryFields(true);
    ListGridField countryCodeField = new ListGridField("countryCode", "Flag", 50);
    countryCodeField.setAlign(Alignment.CENTER);
    countryCodeField.setType(ListGridFieldType.IMAGE);
    countryCodeField.setImageURLPrefix("flags/16/");
    countryCodeField.setImageURLSuffix(".png");
    countryCodeField.setCanSort(false);
    ListGridField nameField = new ListGridField("countryName", "Country");
    ListGridField capitalField = new ListGridField("capital", "Capital");
    ListGridField populationField = new ListGridField("population", "Population");
    populationField.setCellFormatter(new CellFormatter() {
        public String format(Object value, ListGridRecord record, int rowNum, int colNum) {
            if (value == null) return null;
            try {
                NumberFormat nf = NumberFormat.getFormat("0,000");
                return nf.format(((Number) value).longValue());
            } catch (Exception e) {
                return value.toString();
            }
        }
    });
    ListGridField areaField = new ListGridField("area", "Area (km&sup2;)");
    areaField.setType(ListGridFieldType.INTEGER);
    areaField.setCellFormatter(new CellFormatter() {
        public String format(Object value, ListGridRecord record, int rowNum, int colNum) {
            if (value == null) return null;
            String val = null;
            try {
                NumberFormat nf = NumberFormat.getFormat("0,000");
                val = nf.format(((Number) value).longValue());
            } catch (Exception e) {
                return value.toString();
            }
            return val + "km&sup2";
        }
    });
    ListGridField gdpField = new ListGridField("gdp", "GDP");
    gdpField.setAlign(Alignment.RIGHT);
    gdpField.setCellFormatter(new CellFormatter() {
        public String format(Object value, ListGridRecord record, int rowNum, int colNum) {
            if (value == null) return null;
            try {
                NumberFormat nf = NumberFormat.getFormat("0,000");
                return "$" + nf.format(((Number) value).longValue());
            } catch (Exception e) {
                return value.toString();
            }
        }
    });
    countryGrid.setFields(countryCodeField, nameField, capitalField, populationField, areaField, gdpField);
    layout.addMember(countryGrid);
    HLayout buttonLayout = new HLayout(15);
    IButton formulaButton = new IButton("Show Formula Builder");
    formulaButton.setAutoFit(true);
    formulaButton.addClickHandler(new ClickHandler() {
        public void onClick(ClickEvent event) {
            countryGrid.addFormulaField();
        }
    });
    IButton summaryBuilder = new IButton("Show Summary Builder");
    summaryBuilder.setAutoFit(true);
    summaryBuilder.addClickHandler(new ClickHandler() {
        public void onClick(ClickEvent event) {
            countryGrid.addSummaryField();
        }
    });
    buttonLayout.addMember(formulaButton);
    buttonLayout.addMember(summaryBuilder);
    layout.addMember(buttonLayout);
    return layout;
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
      continentField.setValueMap("Europe", "Asia", "North America", "Australia/Oceania", "South America", "Africa");
      DataSourceDateField independenceField = new DataSourceDateField("independence", "Nationhood");
      DataSourceFloatField areaField = new DataSourceFloatField("area", "Area (km&amp;sup2;)");
      DataSourceIntegerField populationField = new DataSourceIntegerField("population", "Population");
      DataSourceFloatField gdpField = new DataSourceFloatField("gdp", "GDP ($M)");
      DataSourceLinkField articleField = new DataSourceLinkField("article", "Info");
      setFields(pkField, countryCodeField, countryNameField, capitalField, governmentField,
              memberG8Field, continentField, independenceField, areaField, populationField,
              gdpField, articleField);
      setDataURL("ds/test_data/country.data.xml");
      setClientOnly(true);
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Tooltip component for GWT
2.  Add buttons to ToolStrip(ToolBar) (Smart GWT)
