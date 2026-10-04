---
title: Java java.awt.FocusTraversalPolicy
nav: Java java.awt.FocusTravers...
description: A FocusTraversalPolicy defines the order in which Components with a particular focus cycle root are traversed. Instances can apply the policy to arbitrary focus cycle roo
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FocusTraversalPolicy/Java_java_awt_FocusTraversalPolicy.htm
---
In this chapter you will learn:

- Get to know java.awt.FocusTraversalPolicy
- JDK Version for java.awt.FocusTraversalPolicy
- Constructors from java.awt.FocusTraversalPolicy
- Methods from java.awt.FocusTraversalPolicy

### Description

A FocusTraversalPolicy defines the order in which Components with a particular focus cycle root are traversed. Instances can apply the policy to arbitrary focus cycle roots, allowing themselves to be shared across Containers. They do not need to be reinitialized when the focus cycle roots of a Component hierarchy change.

The core responsibility of a FocusTraversalPolicy is to provide algorithms determining the next and previous Components to focus when traversing forward or backward in a UI. Each FocusTraversalPolicy must also provide algorithms for determining the first, last, and default Components in a traversal cycle.

First and last Components are used when normal forward and backward traversal, respectively, wraps. The default Component is the first to receive focus when traversing down into a new focus traversal cycle. A FocusTraversalPolicy can optionally provide an algorithm for determining a Window's initial Component.

The initial Component is the first to receive focus when a Window is first made visible. FocusTraversalPolicy takes into account focus traversal policy providers.

When searching for first/last/next/previous Component, if a focus traversal policy provider is encountered, its focus traversal policy is used to perform the search operation.

### Since

```java title=Example.java
1.4
```

### Constructor

Constructor and Description
FocusTraversalPolicy()

### Method

Modifier and Type  Method and Description
---  ---
abstract Component  getComponentAfter(Container aContainer, Component aComponent) Returns the Component that should receive the focus after aComponent.
abstract Component  getComponentBefore(Container aContainer, Component aComponent) Returns the Component that should receive the focus before aComponent.
abstract Component  getDefaultComponent(Container aContainer) Returns the default Component to focus.
abstract Component  getFirstComponent(Container aContainer) Returns the first Component in the traversal cycle.
Component  getInitialComponent(Window window) Returns the Component that should receive the focus when a Window is made visible for the first time.
abstract Component  getLastComponent(Container aContainer) Returns the last Component in the traversal cycle.

#### Next chapter...

What you will learn in the next chapter:

- Get to know FocusTraversalPolicy.FocusTraversalPolicy()
- Syntax for FocusTraversalPolicy() constructor from FocusTraversalPolicy
- Example - FocusTraversalPolicy.FocusTraversalPolicy()
