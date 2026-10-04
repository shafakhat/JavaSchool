---
title: Java XML Tutorial - Java DOM Intro
nav: Java XML Tutorial - Java D...
description: A DOM is a standard tree structure, where each node contains one of the components from an XML structure.
section: Imported - java2s Archive
order: 50322
source: https://www.java2s.com/Tutorials/Java/Java_XML/0100__Java_DOM_Intro.html
---
A DOM is a standard tree structure, where each node contains one of the components from an XML structure.

The two most common types of nodes in XML document are element nodes and text nodes.

With Java DOM API we can create nodes, remove nodes, change their contents, and traverse the node hierarchy.

## When to Use DOM

The Document Object Model standard is designed for XML documents manipulation.

DOM was intended to be language-neutral. Java DOM Parser does not take advantage of Java's object-oriented features.

## Mixed-Content Model

Text and elements is intermixed in a DOM hierarchy. That kind of structure is called mixed content in the DOM model.

For example, we have the following xml structure:

```java title=Example.java
<yourTag>This is an <bold>important</bold> test.</yourTag>
```

The hierarchy of DOM nodes is as follows, where each line represents one node:

```java title=Example.java
ELEMENT: yourTag
   + TEXT: This is an
   + ELEMENT: bold
     + TEXT: important
   + TEXT: test.
```

The yourTag element contains text, followed by a sub-element, followed by additional text.

## Types of Nodes

To support mixed content, DOM nodes are very simple. The "content" of the tag element identifies the kind of node it is.

For example, the <yourTag> node content is the name of the element, yourTag.

The DOM Node API defines nodeValue(), nodeType(), and nodeName() methods.

For the element node <yourTag>, nodeName() returns yourTag, while nodeValue() returns null.

For the text node + TEXT: This is an, nodeName() returns #text, and nodeValue() returns "This is an".

## Example

The following code shows how to use DOM parser to parse a xml file and get a org.w3c.dom.Document object.

```java title=Example.java
import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
    DocumentBuilder db = null;
    db = dbf.newDocumentBuilder();
    Document doc = db.parse(newFile("games.xml"));
  }
}
```

## Example 2

The following code shows how to do a DOM dump.

```java title=Example.java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.ErrorHandler;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
publicclass Main{
  staticpublicvoid main(String[] arg) throws Exception{
    String filename = "input.xml";
    boolean validate = true;
    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
    dbf.setValidating(validate);
    dbf.setNamespaceAware(true);
    dbf.setIgnoringElementContentWhitespace(true);
    DocumentBuilder builder = dbf.newDocumentBuilder();
    builder.setErrorHandler(new MyErrorHandler());
    InputSource is = new InputSource(filename);
    Document doc = builder.parse(is);
    TreeDumper td = new TreeDumper();
    td.dump(doc);
  }
}
class TreeDumper {
    publicvoid dump(Document doc) {
        dumpLoop((Node)doc,"");
    }
    privatevoid dumpLoop(Node node,String indent) {
        switch(node.getNodeType()) {
        case Node.CDATA_SECTION_NODE:
            System.out.println(indent + "CDATA_SECTION_NODE");
            break;
        case Node.COMMENT_NODE:
            System.out.println(indent + "COMMENT_NODE");
            break;
        case Node.DOCUMENT_FRAGMENT_NODE:
            System.out.println(indent + "DOCUMENT_FRAGMENT_NODE");
            break;
        case Node.DOCUMENT_NODE:
            System.out.println(indent + "DOCUMENT_NODE");
            break;
        case Node.DOCUMENT_TYPE_NODE:
            System.out.println(indent + "DOCUMENT_TYPE_NODE");
            break;
        case Node.ELEMENT_NODE:
            System.out.println(indent + "ELEMENT_NODE");
            break;
        case Node.ENTITY_NODE:
            System.out.println(indent + "ENTITY_NODE");
            break;
        case Node.ENTITY_REFERENCE_NODE:
            System.out.println(indent + "ENTITY_REFERENCE_NODE");
            break;
        case Node.NOTATION_NODE:
            System.out.println(indent + "NOTATION_NODE");
            break;
        case Node.PROCESSING_INSTRUCTION_NODE:
            System.out.println(indent + "PROCESSING_INSTRUCTION_NODE");
            break;
        case Node.TEXT_NODE:
            System.out.println(indent + "TEXT_NODE");
            break;
        default:
            System.out.println(indent + "Unknown node");
            break;
        }
        NodeList list = node.getChildNodes();
        for(int i=0; i<list.getLength(); i++)
            dumpLoop(list.item(i),indent + "   ");
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

## Error handler

The following code shows how to handle error when parsing the XML with DOM parser.

```java title=Example.java
import java.io.IOException;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.xml.sax.ErrorHandler;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
publicclass DOMCheck {
  staticpublicvoid main(String[] arg) {
    boolean validate = true;
    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
    dbf.setValidating(validate);
    dbf.setNamespaceAware(true);
    try {
      DocumentBuilder builder = dbf.newDocumentBuilder();
      builder.setErrorHandler(new MyErrorHandler());
      InputSource is = new InputSource("person.xml");
      Document doc = builder.parse(is);
    } catch (SAXException e) {
      System.out.println(e);
    } catch (ParserConfigurationException e) {
      System.err.println(e);
    } catch (IOException e) {
      System.err.println(e);
    }
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
    System.out.println("Line " + e.getLineNumber() + " Column " + e.getColumnNumber());
    System.out.println("System ID: " + e.getSystemId());
  }
}
```

## Example 3

The following code shows how to recursively visit all nodes in a DOM tree.

import java.io.File; /*w w w . j a v a 2s .c o m*/ import javax.xml.parsers.DocumentBuilderFactory; import org.w3c.dom.Document; import org.w3c.dom.Node; import org.w3c.dom.NodeList; public class Main { public static void main(String[] argv) throws Exception{ DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance(); factory.setValidating(true); factory.setExpandEntityReferences(false); Document doc = factory.newDocumentBuilder().parse(new **File**("file.xml")); visit(doc, 0); } public static void visit(Node node, int level) { NodeList list = node.getChildNodes(); for (int i = 0; i < list.getLength(); i++) { Node childNode = list.item(i); visit(childNode, level + 1); } } }

## Example 4

The following code shows how to convert an XML Fragment into a DOM Fragment

import java.io.File; import java.io.StringReader; //from w w w .j av a 2s . c om import javax.xml.parsers.DocumentBuilderFactory; import org.w3c.dom.Document; import org.w3c.dom.DocumentFragment; import org.w3c.dom.Element; import org.w3c.dom.Node; import org.xml.sax.InputSource; public class Main { public static void main(String[] argv) throws Exception { DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance(); factory.setValidating(true); Document doc = factory.newDocumentBuilder().parse(new **File**("infilename.xml")); String fragment = "<fragment>aaa</fragment>"; factory = DocumentBuilderFactory.newInstance(); Document d = factory.newDocumentBuilder().parse(new InputSource(new StringReader(fragment))); Node node = doc.importNode(d.getDocumentElement(), true); DocumentFragment docfrag = doc.createDocumentFragment(); while (node.hasChildNodes()) { docfrag.appendChild(node.removeChild(node.getFirstChild())); } Element element = doc.getDocumentElement(); element.appendChild(docfrag); } }

## Example 5

The following code shows how to parse an XML string: Using DOM and a StringReader.

import java.io.StringReader; /* ww w . jav a2 s. c o m*/ import javax.xml.parsers.DocumentBuilder; import javax.xml.parsers.DocumentBuilderFactory; import org.w3c.dom.CharacterData; import org.w3c.dom.Document; import org.w3c.dom.Element; import org.w3c.dom.Node; import org.w3c.dom.NodeList; import org.xml.sax.InputSource; public class Main { public static void main(String arg[]) throws Exception{ String xmlRecords = "<data><employee><name>A</name>" + "<title>Manager</title></employee></data>"; DocumentBuilder db = DocumentBuilderFactory.newInstance().newDocumentBuilder(); InputSource is = new InputSource(); is.setCharacterStream(new StringReader(xmlRecords)); Document doc = db.parse(is); NodeList nodes = doc.getElementsByTagName("employee"); for (int i = 0; i < nodes.getLength(); i++) { Element element = (Element) nodes.item(i); NodeList name = element.getElementsByTagName("name"); Element line = (Element) name.item(0); System.out.println("Name: " + getCharacterDataFromElement(line)); NodeList title = element.getElementsByTagName("title"); line = (Element) title.item(0); System.out.println("Title: " + getCharacterDataFromElement(line)); } } public static String getCharacterDataFromElement(Element e) { Node child = e.getFirstChild(); if (child instanceof CharacterData) { CharacterData cd = (CharacterData) child; return cd.getData(); } return ""; } }

The code above generates the following result. Next »« Previous
