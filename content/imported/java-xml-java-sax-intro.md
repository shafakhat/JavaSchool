---
title: Java XML Tutorial - Java SAX API Intro
nav: Java XML Tutorial - Java S...
description: Java SAX XML parser stands for Simple API for XML (SAX) parser.
section: Imported - java2s Archive
order: 50321
source: https://www.java2s.com/Tutorials/Java/Java_XML/0030__Java_SAX_Intro.html
---
```java title=Example.java
```

Java SAX XML parser stands for Simple API for XML (SAX) parser.

SAX is an event-driven, serial-access mechanism for accessing XML documents.

This mechanism is frequently used to transmit and receive XML documents.

SAX is a state independent processing, where the handling of an element does not depend on the other elements. StAX is state dependent processing.

SAX is an event-driven model. When using the SAX parser we provide the callback methods, and the parser invokes them as it reads the XML data.

In SAX we cannot go back to an earlier part of the document and we can only process element by element, one by one from the start to the end.

## When to Use SAX

SAX is fast and efficient and it is useful for state-independent filtering. SAX parser calls a method when an element tag is encountered and calls a different method when text is found.

SAX requires much less memory than DOM since SAX does not create an internal tree structure of the XML data, as a DOM does.

## Parsing an XML File Using SAX

In the following we are going to see a demo application which output all SAX events. It is extending DefaultHandler from package org.xml.sax.helpers as follows.

```java title=Example.java
publicclass Main extends DefaultHandler {
```

The following code sets up the parser and gets it started:

```java title=Example.java
    SAXParserFactory spf = SAXParserFactory.newInstance();
    spf.setNamespaceAware(true);
    spf.setValidating(true);
    parser = spf.newSAXParser();
    parser.parse(file, this);
```

These lines of code create a SAXParserFactory instance, as determined by the setting of the javax.xml.parsers.SAXParserFactory system property.

The factory is set up to support XML namespaces by setting setNamespaceAware to true, and then a SAXParser instance is obtained from the factory by newSAXParser() method.

And then it handles the start-document and end-document events:

```java title=Example.java
public void startDocument() {
    System.out.println("Start document: ");
  }
  public void endDocument() {
    System.out.println("End document: ");
  }
```

After that it uses the System.out.println to print message once the method is called by the parser.

When a start tag or end tag is encountered, the name of the tag is passed as a String to the startElement or the endElement method, as appropriate.

When a start tag is encountered, any attributes it defines are passed in an Attributes list.

```java title=Example.java
public void startElement(String uri, String localName, String qname, Attributes attr) {
    System.out.println("Start element: local name: " + localName + " qname: " + qname + " uri: "
        + uri);
  }
```

Characters within the element are passed as an array of characters, along with the number of characters and an offset into the array that points to the first character.

```java title=Example.java
public void characters(char[] ch, int start, int length) {
    System.out.println("Characters: " + new String(ch, start, length));
  }
```

The complete code.

```java title=Example.java
import java.io.File;
import java.io.IOException;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
publicclass Main extends DefaultHandler {
  privatestatic Main handler = null;
  private SAXParser parser = null;
  publicstaticvoid main(String args[]) {
    if (args.length == 0) {
      System.out.println("No file to process. Usage is:" + "\njava TrySAX <filename>");
      return;
    }
    File xmlFile = newFile(args[0]);
    handler = new Main();
    handler.process(xmlFile);
  }
  privatevoid process(File file) {
    SAXParserFactory spf = SAXParserFactory.newInstance();
    spf.setNamespaceAware(true);
    spf.setValidating(true);
    System.out.println("Parser will " + (spf.isNamespaceAware() ? "" : "not ")
        + "be namespace aware");
    System.out.println("Parser will " + (spf.isValidating() ? "" : "not ") + "validate XML");
    try {
      parser = spf.newSAXParser();
      System.out.println("Parser object is: " + parser);
    } catch (SAXException e) {
      e.printStackTrace(System.err);
      System.exit(1);
    } catch (ParserConfigurationException e) {
      e.printStackTrace(System.err);
      System.exit(1);
    }
    System.out.println("\nStarting parsing of " + file + "\n");
    try {
      parser.parse(file, this);
    } catch (IOException e) {
      e.printStackTrace(System.err);
    } catch (SAXException e) {
      e.printStackTrace(System.err);
    }
  }
  publicvoid startDocument() {
    System.out.println("Start document: ");
  }
  publicvoid endDocument() {
    System.out.println("End document: ");
  }
  publicvoid startElement(String uri, String localName, String qname, Attributes attr) {
    System.out.println("Start element: local name: " + localName + " qname: " + qname + " uri: "
        + uri);
  }
  publicvoid endElement(String uri, String localName, String qname) {
    System.out.println("End element: local name: " + localName + " qname: " + qname + " uri: "
        + uri);
  }
  publicvoid characters(char[] ch, int start, int length) {
    System.out.println("Characters: " + new String(ch, start, length));
  }
  publicvoid ignorableWhitespace(char[] ch, int start, int length) {
    System.out.println("Ignorable whitespace: " + new String(ch, start, length));
  }
}
```

The code above generates the following result.

## Error Handler

The parser can generate three kinds of errors:

- a fatal error
- an error
- a warning

When a fatal error occurs, the parser cannot continue.

For nonfatal errors and warnings, default error handler would not generate exceptions and no messages are displayed.

The following line installs the our own error handler.

```java title=Example.java
reader.setErrorHandler(new MyErrorHandler());
```

The MyErrorHandler class implements the standard org.xml.sax.ErrorHandler interface, and defines a method to obtain the exception information that is provided by any SAXParseException.

The complete code.

```java title=Example.java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.ErrorHandler;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.XMLReader;
class MyErrorHandler implements ErrorHandler {
  publicvoid warning(SAXParseException e) throws SAXException {
    show("Warning", e);
    throw (e);
  }
  publicvoid error(SAXParseException e) throws SAXException {
    show("Error", e);
    throw (e);
  }
  publicvoid fatalError(SAXParseException e) throws SAXException {
    show("Fatal Error", e);
    throw (e);
  }
  privatevoid show(String type, SAXParseException e) {
    System.out.println(type + ": " + e.getMessage());
    System.out.println("Line " + e.getLineNumber() + " Column " + e.getColumnNumber());
    System.out.println("System ID: " + e.getSystemId());
  }
}
// Installation and Use of an Error Handler in a SAX Parser
publicclass SAXCheck {
  staticpublicvoid main(String[] arg) throws Exception {
    boolean validate = false;
    validate = true;
    SAXParserFactory spf = SAXParserFactory.newInstance();
    spf.setValidating(validate);
    XMLReader reader = null;
    SAXParser parser = spf.newSAXParser();
    reader = parser.getXMLReader();
    reader.setErrorHandler(new MyErrorHandler());
    InputSource is = new InputSource("test.xml");
    reader.parse(is);
  }
}
```

## XML Schema validation

We can turn on XML Schema validation during parsing with a SAXParser.

```java title=Example.java
import java.io.File;
import javax.xml.XMLConstants;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
publicclass Main {
  publicstaticvoid main(String args[]) throws Exception {
    String language = XMLConstants.W3C_XML_SCHEMA_NS_URI;
    SchemaFactory factory = SchemaFactory.newInstance(language);
    Schema schema = factory.newSchema(newFile("yourSchema"));
    SAXParserFactory spf = SAXParserFactory.newInstance();
    spf.setSchema(schema);
    SAXParser parser = spf.newSAXParser();
    // parser.parse(...);
  }
}
```

## DefaultHandler

The following code shows that when using the DefaultHandler we don't need to implement all methods. We only need to provide the implementation for the methods we care about.

```java title=Example.java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
publicclass Main {
  publicstaticvoid main(String args[]) throws Exception {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    SAXParser saxParser = factory.newSAXParser();
    DefaultHandler handler = new DefaultHandler() {
      publicvoid startElement(String uri, String localName, String qName,
          Attributes attributes) throws SAXException {
        System.out.println(qName);
      }
      publicvoid characters(char ch[], int start, int length)
          throws SAXException {
        System.out.println(new String(ch, start, length));
      }
    };
    saxParser.parse(args[0], handler);
  }
}
```

The following code handles SAX errors by override the error handler methods from DefaultHandler

```java title=Example.java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.helpers.DefaultHandler;
publicclass Main {
  publicstatic void main(String[] argv) throws Exception {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    factory.setValidating(true);
    SAXParser parser = factory.newSAXParser();
    SaxHandler handler = new SaxHandler();
    parser.parse("sample.xml", handler);
  }
}
class SaxHandler extends DefaultHandler {
  public void startElement(String uri, String localName, String qName, Attributes attrs)
      throws SAXException {
    if (qName.equals("order")) {
    }
  }
  public void error(SAXParseException ex) throws SAXException {
    System.out.println("ERROR: [at " + ex.getLineNumber() + "] " + ex);
  }
  public void fatalError(SAXParseException ex) throws SAXException {
    System.out.println("FATAL_ERROR: [at " + ex.getLineNumber() + "] " + ex);
  }
  public void warning(SAXParseException ex) throws SAXException {
    System.out.println("WARNING: [at " + ex.getLineNumber() + "] " + ex);
  }
}
```

## ContentHandler

The following code chooses to implement the ContentHandler interface and provide implementation for all necessary methods.

It also implements the ErrorHandler interface.

```java title=Example.java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.Attributes;
import org.xml.sax.ContentHandler;
import org.xml.sax.ErrorHandler;
import org.xml.sax.InputSource;
import org.xml.sax.Locator;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.XMLReader;
publicclass Main {
  staticpublicvoid main(String[] arg) throws Exception {
    String filename = "yourXML.xml";
    // Create a new factory that will create the parser.
    SAXParserFactory spf = SAXParserFactory.newInstance();
    // Create the XMLReader to be used to parse the document.
    SAXParser parser = spf.newSAXParser();
    XMLReader reader = parser.getXMLReader();
    // Specify the error handler and the content handler.
    reader.setErrorHandler(new MyErrorHandler());
    reader.setContentHandler(new MyContentHandler());
    // Use the XMLReader to parse the entire file.
    InputSource is = new InputSource(filename);
    reader.parse(is);
  }
}
class MyContentHandler implements ContentHandler {
  private Locator locator;
  /**
   * The name and of the SAX document and the current location within the
   * document.
   */publicvoid setDocumentLocator(Locator locator) {
    this.locator = locator;
    System.out.println("-" + locator.getLineNumber() + "---Document ID: "
        + locator.getSystemId());
  }
  /** The parsing of a document has started.. */publicvoid startDocument() {
    System.out.println("-" + locator.getLineNumber()
        + "---Document parse started");
  }
  /** The parsing of a document has completed.. */publicvoid endDocument() {
    System.out.println("-" + locator.getLineNumber()
        + "---Document parse ended");
  }
  /** The start of a namespace scope */publicvoid startPrefixMapping(String prefix, String uri) {
    System.out.println("-" + locator.getLineNumber()
        + "---Namespace scope begins");
    System.out.println("     " + prefix + "=\"" + uri + "\"");
  }
  /** The end of a namespace scope */publicvoid endPrefixMapping(String prefix) {
    System.out.println("-" + locator.getLineNumber()
        + "---Namespace scope ends");
    System.out.println("     " + prefix);
  }
  /** The opening tag of an element. */publicvoid startElement(String namespaceURI, String localName, String qName,
      Attributes atts) {
    System.out.println("-" + locator.getLineNumber()
        + "---Opening tag of an element");
    System.out.println("       Namespace: " + namespaceURI);
    System.out.println("      Local name: " + localName);
    System.out.println("  Qualified name: " + qName);
    for (int i = 0; i < atts.getLength(); i++) {
      System.out.println("       Attribute: " + atts.getQName(i) + "=\""
          + atts.getValue(i) + "\"");
    }
  }
  /** The closing tag of an element. */publicvoid endElement(String namespaceURI, String localName, String qName) {
    System.out.println("-" + locator.getLineNumber()
        + "---Closing tag of an element");
    System.out.println("       Namespace: " + namespaceURI);
    System.out.println("      Local name: " + localName);
    System.out.println("  Qualified name: " + qName);
  }
  /** Character data. */publicvoid characters(char[] ch, int start, int length) {
    System.out.println("-" + locator.getLineNumber() + "---Character data");
    showCharacters(ch, start, length);
  }
  /** Ignorable whitespace character data. */publicvoid ignorableWhitespace(char[] ch, int start, int length) {
    System.out.println("-" + locator.getLineNumber() + "---Whitespace");
    showCharacters(ch, start, length);
  }
  /** Processing Instruction */publicvoid processingInstruction(String target, String data) {
    System.out.println("-" + locator.getLineNumber()
        + "---Processing Instruction");
    System.out.println("         Target: " + target);
    System.out.println("           Data: " + data);
  }
  /** A skipped entity. */publicvoid skippedEntity(String name) {
    System.out.println("-" + locator.getLineNumber() + "---Skipped Entity");
    System.out.println("           Name: " + name);
  }
  /**
   * Internal method to format arrays of characters so the special whitespace
   * characters will show.
   */publicvoid showCharacters(char[] ch, int start, int length) {
    System.out.print("        \"");
    for (int i = start; i < start + length; i++)
      switch (ch[i]) {
      case'\n':
        System.out.print("\\n");
        break;
      case'\r':
        System.out.print("\\r");
        break;
      case'\t':
        System.out.print("\\t");
        break;
      default:
        System.out.print(ch[i]);
        break;
      }
    System.out.println("\"");
  }
}
class MyErrorHandler implements ErrorHandler {
  publicvoid warning(SAXParseException e) throws SAXException {
    show("Warning", e);
    throw (e);
  }
  publicvoid error(SAXParseException e) throws SAXException {
    show("Error", e);
    throw (e);
  }
  publicvoid fatalError(SAXParseException e) throws SAXException {
    show("Fatal Error", e);
    throw (e);
  }
  privatevoid show(String type, SAXParseException e) {
    System.out.println(type + ": " + e.getMessage());
    System.out.println("Line " + e.getLineNumber() + " Column "
        + e.getColumnNumber());
    System.out.println("System ID: " + e.getSystemId());
  }
}
```

## Locator

The following code shows how to access Locator interface from DefaultHandler.

```java title=Example.java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.Attributes;
import org.xml.sax.Locator;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
publicclass Main{
  publicstaticvoid main(String[] args) throws Exception {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    factory.setValidating(true);
    SAXParser parser = factory.newSAXParser();
    parser.parse("sample.xml", new SampleOfXmlLocator());
  }
}
class SampleOfXmlLocator extends DefaultHandler {
  private Locator locator;
  publicvoid setDocumentLocator(Locator locator) {
    this.locator = locator;
  }
  publicvoid startElement(String uri, String localName, String qName, Attributes attrs)
      throws SAXException {
    if (qName.equals("order")) {
      System.out.println("here process element start");
    } else {
      String location = "";
      if (locator != null) {
        location = locator.getSystemId(); // XML-document name;
        location += " line " + locator.getLineNumber();
        location += ", column " + locator.getColumnNumber();
        location += ": ";
      }
      thrownew SAXException(location + "Illegal element");
    }
  }
}
```

- « Previous
