---
title: Java XML Tutorial - Java StAX
nav: Java XML Tutorial - Java S...
description: StAX was created to address limitations in the SAX and DOM APIs.
section: Imported - java2s Archive
order: 50325
source: https://www.java2s.com/Tutorials/Java/Java_XML/0300__Java_StAX_Intro.html
---
```java title=Example.java
```

StAX was created to address limitations in the SAX and DOM APIs.

The StAX APIs allow us to ask for the next event (pull the event) and allows state to be stored in procedural fashion.

There are two programming models for XML parsing: streaming and the document object model (DOM).

The DOM model involves creating in-memory objects representing an entire document tree. DOM trees can be navigated freely. The cost is a large memory footprint. This is OK for small documents, but memory consumption can escalate quickly as document becomes larger.

Streaming refers to a programming model in which XML data are parsed serially. We can only see the XML data at one location at a time in the document. The implication is that we need to know the XML structure before reading the XML document. Streaming models for XML processing are useful when there is memory limitation.

## Pull Parsing vs Push Parsing

We do streaming pull parsing when we want to get (pulls) XML data.

We do streaming push parsing when the parser sends the data whether or not the client is ready to use it at that time.

A StAX pull parser can filter XML documents and ignore elements unnecessary.

StAX is a bidirectional API by which we can read and write XML documents. SAX is read only.

SAX is a push API, whereas StAX is pull.

## Example

This program demonstrates how to use a StAX parser. It prints all hyperlinks links of an XHTML web page.

```java title=Example.java
import java.io.InputStream;
import java.net.URL;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamConstants;
import javax.xml.stream.XMLStreamReader;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    URL url = new URL("http://www.w3c.org");
    InputStream in = url.openStream();
    XMLInputFactory factory = XMLInputFactory.newInstance();
    XMLStreamReader parser = factory.createXMLStreamReader(in);
    while (parser.hasNext()) {
      int event = parser.next();
      if (event == XMLStreamConstants.START_ELEMENT) {
        if (parser.getLocalName().equals("a")) {
          String href = parser.getAttributeValue(null, "href");
          if (href != null)
            System.out.println(href);
        }
      }
    }
  }
}
```

## Example 2

The following code shows how to load XML document with XML stream reader.

```java title=Example.java
import java.io.File;
import java.io.FileInputStream;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamConstants;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamReader;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    File file = newFile("yourXML.xml");
    FileInputStream inputStream = new FileInputStream(file);
    XMLInputFactory inputFactory = XMLInputFactory.newInstance();
    XMLStreamReader reader = inputFactory.createXMLStreamReader(inputStream);
    System.out.println(reader.getVersion());
    System.out.println(reader.isStandalone());
    System.out.println(reader.standaloneSet());
    System.out.println(reader.getEncoding());
    System.out.println(reader.getCharacterEncodingScheme());
    parseRestOfDocument(reader);
  }
  privatestaticvoid parseRestOfDocument(XMLStreamReader reader)
      throws XMLStreamException {
    while (reader.hasNext()) {
      int type = reader.next();
      switch (type) {
      case XMLStreamConstants.START_ELEMENT:
        System.out.println(reader.getLocalName());
        if (reader.getNamespaceURI() != null) {
          String prefix = reader.getPrefix();
          if (prefix == null) {
            prefix = "[None]";
          }
          System.out.println("prefix = '" + prefix + "', URI = '"
              + reader.getNamespaceURI() + "'");
        }
        if (reader.getAttributeCount() > 0) {
          for (int i = 0; i < reader.getAttributeCount(); i++) {
            System.out.println("Attribute (name = '"
                + reader.getAttributeLocalName(i) + "', value = '"
                + reader.getAttributeValue(i) + "')");
            String attURI = reader.getAttributeNamespace(i);
            if (attURI != null) {
              String attPrefix = reader.getAttributePrefix(i);
              if (attPrefix == null || attPrefix.equals("")) {
                attPrefix = "[None]";
              }
              System.out.println("prefix=" + attPrefix + ",URI=" + attURI);
            }
          }
        }
        break;
      case XMLStreamConstants.END_ELEMENT:
        System.out.println("XMLStreamConstants.END_ELEMENT");
        break;
      case XMLStreamConstants.CHARACTERS:
        if (!reader.isWhiteSpace()) {
          System.out.println("CD:" + reader.getText());
        }
        break;
      case XMLStreamConstants.DTD:
        System.out.println("DTD:" + reader.getText());
        break;
      case XMLStreamConstants.SPACE:
        System.out.println(" ");
        break;
      case XMLStreamConstants.COMMENT:
        System.out.println(reader.getText());
        break;
      default:
        System.out.println(type);
      }
    }
  }
}
```

## XMLStreamWriter

The following code shows how to output xml with XMLStreamWriter.

```java title=Example.java
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamWriter;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    XMLOutputFactory factory = XMLOutputFactory.newInstance();
    XMLStreamWriter writer = factory.createXMLStreamWriter(System.out);
    writer.writeStartDocument("1.0");
    writer.writeStartElement("catalog");
    writer.writeStartElement("book");
    writer.writeAttribute("id", "1");
    writer.writeStartElement("code");
    writer.writeCharacters("I01");
    writer.writeEndElement();
    writer.writeStartElement("title");
    writer.writeCharacters("This is the title");
    writer.writeEndElement();
    writer.writeStartElement("price");
    writer.writeCharacters("$2.95");
    writer.writeEndElement();
    writer.writeEndDocument();
    writer.flush();
    writer.close();
  }
}
```

The code above generates the following result.

## XMLEventReader

```java title=Example.java
import java.io.FileReader;
import java.io.Reader;
import java.util.Iterator;
import javax.xml.namespace.QName;
import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.events.Attribute;
import javax.xml.stream.events.Characters;
import javax.xml.stream.events.EndElement;
import javax.xml.stream.events.StartElement;
import javax.xml.stream.events.XMLEvent;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    XMLInputFactory factory = XMLInputFactory.newInstance();
    Reader fileReader = new FileReader("Source.xml");
    XMLEventReader reader = factory.createXMLEventReader(fileReader);
    while (reader.hasNext()) {
      XMLEvent event = reader.nextEvent();
      if (event.isStartElement()) {
        StartElement element = (StartElement) event;
        System.out.println("Start Element: " + element.getName());
        Iterator iterator = element.getAttributes();
        while (iterator.hasNext()) {
          Attribute attribute = (Attribute) iterator.next();
          QName name = attribute.getName();
          String value = attribute.getValue();
          System.out.println("Attribute name/value: " + name + "/" + value);
        }
      }
      if (event.isEndElement()) {
        EndElement element = (EndElement) event;
        System.out.println("End element:" + element.getName());
      }
      if (event.isCharacters()) {
        Characters characters = (Characters) event;
        System.out.println("Text: " + characters.getData());
      }
    }
  }
}
```

## XMLEventWriter

```java title=Example.java
import java.util.Arrays;
import java.util.List;
import javax.xml.stream.XMLEventFactory;
import javax.xml.stream.XMLEventWriter;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.events.Attribute;
import javax.xml.stream.events.Characters;
import javax.xml.stream.events.EndDocument;
import javax.xml.stream.events.EndElement;
import javax.xml.stream.events.StartDocument;
import javax.xml.stream.events.StartElement;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    XMLOutputFactory outputFactory = XMLOutputFactory.newInstance();
    XMLEventWriter writer = outputFactory.createXMLEventWriter(System.out);
    XMLEventFactory xmlEventFactory = XMLEventFactory.newInstance();
    StartDocument startDocument = xmlEventFactory.createStartDocument("UTF-8", "1.0");
    writer.add(startDocument);
    StartElement startElement = xmlEventFactory.createStartElement("", "", "My-list");
    writer.add(startElement);
    Attribute attribute = xmlEventFactory.createAttribute("version", "1");
    List attributeList = Arrays.asList(attribute);
    List nsList = Arrays.asList();
    StartElement startElement2 = xmlEventFactory.createStartElement("", "", "Item",
        attributeList.iterator(), nsList.iterator());
    writer.add(startElement2);
    StartElement codeSE = xmlEventFactory.createStartElement("", "", "code");
    writer.add(codeSE);
    Characters codeChars = xmlEventFactory.createCharacters("I001");
    writer.add(codeChars);
    EndElement codeEE = xmlEventFactory.createEndElement("", "", "code");
    writer.add(codeEE);
    StartElement nameSE = xmlEventFactory.createStartElement(" ", " ", "name");
    writer.add(nameSE);
    Characters nameChars = xmlEventFactory.createCharacters("a name");
    writer.add(nameChars);
    EndElement nameEE = xmlEventFactory.createEndElement("", "", "name");
    writer.add(nameEE);
    StartElement contactSE = xmlEventFactory.createStartElement("", "", "contact");
    writer.add(contactSE);
    Characters contactChars = xmlEventFactory.createCharacters("another name");
    writer.add(contactChars);
    EndElement contactEE = xmlEventFactory.createEndElement("", "", "contact");
    writer.add(contactEE);
    EndDocument ed = xmlEventFactory.createEndDocument();
    writer.add(ed);
    writer.flush();
    writer.close();
  }
}
```

The code above generates the following result.

## StreamFilter

```java title=Example.java
import java.io.FileInputStream;
import javax.xml.namespace.QName;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamReader;
import javax.xml.stream.events.XMLEvent;
publicclass Main implements javax.xml.stream.StreamFilter {
  publicstaticvoid main(String[] args) throws Exception {
    String filename = "yourXML.xml";
    XMLInputFactory xmlif = null;
    xmlif = XMLInputFactory.newInstance();
    xmlif.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES,
        Boolean.TRUE);
    xmlif.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES,
        Boolean.FALSE);
    xmlif.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, Boolean.TRUE);
    xmlif.setProperty(XMLInputFactory.IS_COALESCING, Boolean.TRUE);
    System.out.println("FACTORY: " + xmlif);
    System.out.println("filename = " + filename);
    FileInputStream fis = new FileInputStream(filename);
    XMLStreamReader xmlr = xmlif.createFilteredReader(
        xmlif.createXMLStreamReader(fis), new Main());
    int eventType = xmlr.getEventType();
    printEventType(eventType);
    while (xmlr.hasNext()) {
      eventType = xmlr.next();
      printEventType(eventType);
      printName(xmlr, eventType);
      printText(xmlr);
      if (xmlr.isStartElement()) {
        printAttributes(xmlr);
      }
      printPIData(xmlr);
    }
  }
  publicstaticfinal String getEventTypeString(int eventType) {
    switch (eventType) {
    case XMLEvent.START_ELEMENT:
      return"START_ELEMENT";
    case XMLEvent.END_ELEMENT:
      return"END_ELEMENT";
    case XMLEvent.PROCESSING_INSTRUCTION:
      return"PROCESSING_INSTRUCTION";
    case XMLEvent.CHARACTERS:
      return"CHARACTERS";
    case XMLEvent.COMMENT:
      return"COMMENT";
    case XMLEvent.START_DOCUMENT:
      return"START_DOCUMENT";
    case XMLEvent.END_DOCUMENT:
      return"END_DOCUMENT";
    case XMLEvent.ENTITY_REFERENCE:
      return"ENTITY_REFERENCE";
    case XMLEvent.ATTRIBUTE:
      return"ATTRIBUTE";
    case XMLEvent.DTD:
      return"DTD";
    case XMLEvent.CDATA:
      return"CDATA";
    }
    return"UNKNOWN_EVENT_TYPE";
  }
  privatestaticvoid printEventType(int eventType) {
    System.out.print("EVENT TYPE(" + eventType + "):");
    System.out.println(getEventTypeString(eventType));
  }
  privatestaticvoid printName(XMLStreamReader xmlr, int eventType) {
    if (xmlr.hasName()) {
      System.out.println("HAS NAME: " + xmlr.getLocalName());
    } else {
      System.out.println("HAS NO NAME");
    }
  }
  privatestaticvoid printText(XMLStreamReader xmlr) {
    if (xmlr.hasText()) {
      System.out.println("HAS TEXT: " + xmlr.getText());
    } else {
      System.out.println("HAS NO TEXT");
    }
  }
  privatestaticvoid printPIData(XMLStreamReader xmlr) {
    if (xmlr.getEventType() == XMLEvent.PROCESSING_INSTRUCTION) {
      System.out.println(" PI target = " + xmlr.getPITarget());
      System.out.println(" PI Data = " + xmlr.getPIData());
    }
  }
  privatestaticvoid printAttributes(XMLStreamReader xmlr) {
    if (xmlr.getAttributeCount() > 0) {
      System.out.println("\nHAS ATTRIBUTES: ");
      int count = xmlr.getAttributeCount();
      for (int i = 0; i < count; i++) {
        QName name = xmlr.getAttributeName(i);
        String namespace = xmlr.getAttributeNamespace(i);
        String type = xmlr.getAttributeType(i);
        String prefix = xmlr.getAttributePrefix(i);
        String value = xmlr.getAttributeValue(i);
        System.out.println("ATTRIBUTE-PREFIX: " + prefix);
        System.out.println("ATTRIBUTE-NAMESP: " + namespace);
        System.out.println("ATTRIBUTE-NAME:   " + name.toString());
        System.out.println("ATTRIBUTE-VALUE:  " + value);
        System.out.println("ATTRIBUTE-TYPE:  " + type);
      }
    } else {
      System.out.println("HAS NO ATTRIBUTES");
    }
  }
  publicboolean accept(XMLStreamReader reader) {
    if (!reader.isStartElement() && !reader.isEndElement()) {
      return false;
    } else {
      return true;
    }
  }
}
```

- « Previous
