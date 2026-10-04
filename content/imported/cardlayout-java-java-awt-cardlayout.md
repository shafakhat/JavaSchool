---
title: Java java.awt.CardLayout
nav: Java java.awt.CardLayout
description: A CardLayout object is a layout manager for a container. It treats each component in the container as a card. Only one card is visible at a time, and the container acts a
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/Java_java_awt_CardLayout.htm
---
In this chapter you will learn:

- Get to know java.awt.CardLayout
- JDK Version for java.awt.CardLayout
- Constructors from java.awt.CardLayout
- Methods from java.awt.CardLayout

### Description

A CardLayout object is a layout manager for a container. It treats each component in the container as a card. Only one card is visible at a time, and the container acts as a stack of cards. The first component added to a CardLayout object is the visible component when the container is first displayed. The ordering of cards is determined by the container's own internal ordering of its component objects. CardLayout defines a set of methods that allow an application to flip through these cards sequentially, or to show a specified card. The addLayoutComponent(java.awt.Component, java.lang.Object) method can be used to associate a string identifier with a given card for fast random access.

### Since

```java title=Example.java
JDK1.0
```

### Constructor

Constructor and Description
---
CardLayout() Creates a new card layout with gaps of size zero.
CardLayout(int hgap, int vgap) Creates a new card layout with the specified horizontal and vertical gaps.

### Method

Modifier and Type  Method and Description
---  ---
void  addLayoutComponent(Component comp, Object constraints) Adds the specified component to this card layout's internal table of names.
void  addLayoutComponent(String name, Component comp) Deprecated. replaced by addLayoutComponent(Component, Object) .
void  first(Container parent) Flips to the first card of the container.
int  getHgap() Gets the horizontal gap between components.
float  getLayoutAlignmentX(Container parent) Returns the alignment along the x axis.
float  getLayoutAlignmentY(Container parent) Returns the alignment along the y axis.
int  getVgap() Gets the vertical gap between components.
void  invalidateLayout(Container target) Invalidates the layout, indicating that if the layout manager has cached information it should be discarded.
void  last(Container parent) Flips to the last card of the container.
void  layoutContainer(Container parent) Lays out the specified container using this card layout.
Dimension  maximumLayoutSize(Container target) Returns the maximum dimensions for this layout given the components in the specified target container.
Dimension  minimumLayoutSize(Container parent) Calculates the minimum size for the specified panel.
void  next(Container parent) Flips to the next card of the specified container.
Dimension  preferredLayoutSize(Container parent) Determines the preferred size of the container argument using this card layout.
void  previous(Container parent) Flips to the previous card of the specified container.
void  removeLayoutComponent(Component comp) Removes the specified component from the layout.
void  setHgap(int hgap) Sets the horizontal gap between components.
void  setVgap(int vgap) Sets the vertical gap between components.
void  show(Container parent, String name) Flips to the component that was added to this layout with the specified name , using addLayoutComponent .
String  toString() Returns a string representation of the state of this card layout.

#### Next chapter...

What you will learn in the next chapter:

- Get to know CardLayout.CardLayout()
- Syntax for CardLayout() constructor from CardLayout
- Example - CardLayout.CardLayout()
