---
title: Java XML Tutorial - Java JAXP Intro
nav: Java XML Tutorial - Java J...
description: The Java API for XML Processing (JAXP) is for processing XML data in the Java.
section: Imported - java2s Archive
order: 50004
source: https://www.java2s.com/Tutorials/Java/Java_XML/index.html
---
- Next »

The Java API for XML Processing (JAXP) is for processing XML data in the Java.

JAXP contains standards Simple API for XML Parsing (SAX), Document Object Model (DOM), and the Streaming API for XML (StAX) standard.

JAXP supports the Extensible Stylesheet Language Transformations (XSLT) standard, and we can use it to convert the XML documents to other formats, such as HTML.

## Packages Overview

The Java SAX and DOM APIs are defined as follows:

Package  Description
---  ---
javax.xml.parsers  The JAXP APIs provide an interface for various SAX and DOM parsers.
org.w3c.dom  DOM related classes
org.xml.sax  SAX APIs.
javax.xml.transform  XSLT APIs that transform XML into other forms.
javax.xml.stream  StAX-specific transformation APIs.

## SAX

The Simple API for XML (SAX) is the event-driven, serial-access parser. It processes the XML document element-by-element.

The SAX API is often used as data filters that do not require an in-memory representation of the XML data.

## DOM

The DOM API builds a tree structure out of the XML document.

We can use the DOM API to manipulate the hierarchy of XML objects.

The entire XML tree is stored in memory by DOM API. It would use more memory than SAX parser

## XSLT

We can use the XSLT APIs defined in javax.xml.transform to write XML data to a file or convert the XML document into other forms, such as HTML or PDF.

## StAX

The StAX APIs defined in javax.xml.stream provide a streaming based, event-driven, pull-parsing API for reading and writing XML documents using Java.

StAX is a simpler than SAX and consumes less memory than DOM.

- Next »
