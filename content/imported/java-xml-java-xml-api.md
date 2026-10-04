---
title: Java XML Tutorial - Java XML API
nav: Java XML Tutorial - Java X...
description: SAXParserFactory Creates an instance of the parser determined by the system property, javax.xml.parsers.SAXParserFactory.
section: Imported - java2s Archive
order: 50320
source: https://www.java2s.com/Tutorials/Java/Java_XML/0020__Java_XML_API.html
---
```java title=Example.java
```

## SAX APIs

Here is a summary of the key SAX APIs:

Class  Usage
---  ---
SAXParserFactory  Creates an instance of the parser determined by the system property, javax.xml.parsers.SAXParserFactory.
SAXParser  The SAXParser interface defines several overloaded of parse() methods.
SAXReader  The SAXParser wraps a SAXReader and is returned from SAXParser's getXMLReader() method.
DefaultHandler  DefaultHandler implements the ContentHandler, ErrorHandler, DTDHandler, and EntityResolver interfaces. By using DefaultHandler we can override only the ones that we need to.
ContentHandler  This interface defines the call back methods, such as startDocument, endDocument, startElement, and endElement. These method are invoked when an XML tag is recognized. It also defines the methods characters() which is invoked when the parser encounters the text in an XML element. It defines processingInstruction() which is invoked when the parser encounters the inline processing instruction.
ErrorHandler  It uses error(), fatalError(), and warning() methods to response to various parsing errors. The default error handler only throws an exception for fatal errors and ignores validation errors.
DTDHandler  Used to processe a DTD
EntityResolver  Its resolveEntity() method is used to identify data.

We usually implement most of the ContentHandler methods.

To provide a more robust implementation we may implement the methods from ErrorHandler.

## SAX Packages

The SAX parser is defined in the packages listed in the following Table .

Packages  Description
---  ---
org.xml.sax  Defines the SAX interfaces.
org.xml.sax.ext  Defines SAX extensions used for more advanced SAX processing.
org.xml.sax.helpers  Defines helper classes for SAX APIs.
javax.xml.parsers  Defines the SAXParserFactory class, which returns the SAXParser.

## DOM APIs

javax.xml.parsers.DocumentBuilderFactory class returns a DocumentBuilder instance.

We use DocumentBuilder instance to produce a Document object out of an XML document.

The builder is determined by the system property javax.xml.parsers.DocumentBuilderFactory.

The newDocument() method from DocumentBuilder can create an empty Document that implements the org.w3c.dom.Document interface.

We can use one of the builder's parse methods to create a Document from existing XML document.

## DOM Packages

The Document Object Model implementation is defined in the packages listed in the following Table .

Package  Description
---  ---
org.w3c.dom  Defines the DOM programming interfaces for XML documents.
javax.xml.parsers  Defines the DocumentBuilderFactory class and the DocumentBuilder class.

## XSLT APIs

A TransformerFactory creates a Transformer object.

The XSLT APIs are defined in the packages shown in the following Table .

Package  Description
---  ---
javax.xml.transform  Defines the TransformerFactory and Transformer classes. We can invoke transform() method from the transformer object to do the transformation.
javax.xml.transform.dom  Classes to create input and output objects from a DOM.
javax.xml.transform.sax  Classes to create input objects from a SAX parser and output objects from a SAX event handler.
javax.xml.transform.stream  Classes to create input objects and output objects from an I/O stream.

## StAX APIs

StAX provides an alternative to SAX and DOM parsers for developers.

StAX can do high-performance stream filtering, processing, and modification with less memory.

StAX is a standard, bidirectional pull parser interface for streaming XML processing.

StAX offers a simpler programming model than SAX and is more memory efficient than DOM.

StAX can parse and modify XML streams as events.

## StAX Packages

The StAX APIs are defined in the packages shown in the following Table.

Package  Description
---  ---
javax.xml.stream  Defines the XMLStreamReader interface which iterates over the elements of an XML document. Defines the XMLStreamWriter interface which specifies how the XML should be written.
javax.xml.transform.stax  Provides StAX-specific transformation APIs.

- « Previous
