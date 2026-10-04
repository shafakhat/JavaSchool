---
title: Java XML Tutorial - Java DOM Edit
nav: Java XML Tutorial - Java D...
description: DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
section: Imported - java2s Archive
order: 50323
source: https://www.java2s.com/Tutorials/Java/Java_XML/0110__Java_DOM_Edit.html
---
## Attribute

The following code shows how to add attribute to an element.

```java title=Example.java
import java.io.StringWriter;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.DOMImplementation;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    DocumentBuilder builder = factory.newDocumentBuilder();
    DOMImplementation impl = builder.getDOMImplementation();
    Document doc = impl.createDocument(null, null, null);
    Element e1 = doc.createElement("api");
    doc.appendChild(e1);
    Element e2 = doc.createElement("java");
    e1.appendChild(e2);
    e2.setAttribute("url", "http:");
    //transform the DOM for showing the result in console
    DOMSource domSource = new DOMSource(doc);
    Transformer transformer = TransformerFactory.newInstance().newTransformer();
    transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
    transformer.setOutputProperty(OutputKeys.METHOD, "xml");
    transformer.setOutputProperty(OutputKeys.ENCODING, "ISO-8859-1");
    transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
    transformer.setOutputProperty(OutputKeys.INDENT, "yes");
    StringWriter sw = new StringWriter();
    StreamResult sr = new StreamResult(sw);
    transformer.transform(domSource, sr);
    System.out.println(sw.toString());
  }
}
```

The code above generates the following result.

Copying Attributes

```java title=Example.java
public void dupAttributes(Document doc) {
        Element root = doc.getDocumentElement();
        Element personOne = (Element)root.getFirstChild();
        Element personTwo = (Element)personOne.getNextSibling();
        Element personThree = (Element)personTwo.getNextSibling();
        Attr deptAttr = personOne.getAttributeNode("dept");
        personOne.removeAttributeNode(deptAttr);
        String deptString = deptAttr.getValue();
        personTwo.setAttribute("dept",deptString);
        personThree.setAttribute("dept",deptString);
        String mailString = personOne.getAttribute("mail");
        personTwo.setAttribute("mail",mailString);
        String titleString = personOne.getAttribute("title");
        personOne.removeAttribute("title");
        personThree.setAttribute("title",titleString);
    }
```

Deleting Two Attributes

```java title=Example.java
public void delAttribute(Document doc) {
        Element root = doc.getDocumentElement();
        Element person = (Element)root.getFirstChild();
        person.removeAttribute("extension");
        person.removeAttribute("dept");
    }
```

## Element

```java title=Example.java
import java.io.StringWriter;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.DOMImplementation;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    DocumentBuilder builder = factory.newDocumentBuilder();
    DOMImplementation impl = builder.getDOMImplementation();
    Document doc = impl.createDocument(null, null, null);
    Node root = doc.createElement("A");
    doc.appendChild(root);
    Node stanza = doc.createElement("B");
    root.appendChild(stanza);
    Node line = doc.createElement("C");
    stanza.appendChild(line);
    line.appendChild(doc.createTextNode("test"));
    line = doc.createElement("Line");
    stanza.appendChild(line);
    line.appendChild(doc.createTextNode("test"));
    //transform the DOM for showing the result in console
    DOMSource domSource = new DOMSource(doc);
    Transformer transformer = TransformerFactory.newInstance().newTransformer();
    transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
    transformer.setOutputProperty(OutputKeys.METHOD, "xml");
    transformer.setOutputProperty(OutputKeys.ENCODING, "ISO-8859-1");
    transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
    transformer.setOutputProperty(OutputKeys.INDENT, "yes");
    StringWriter sw = new StringWriter();
    StreamResult sr = new StreamResult(sw);
    transformer.transform(domSource, sr);
    System.out.println(sw.toString());
  }
}
```

The code above generates the following result.

The following code shows how to remove an element from parent.

```java title=Example.java
public void deleteFirstElement(Document doc) {
        Element root = doc.getDocumentElement();
        Element child = (Element)root.getFirstChild();
        root.removeChild(child);
    }
```

## Text Node

The following code shows how to add text node to an element.

```java title=Example.java
import java.io.StringWriter;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.bootstrap.DOMImplementationRegistry;
import org.w3c.dom.ls.DOMImplementationLS;
import org.w3c.dom.ls.LSOutput;
import org.w3c.dom.ls.LSSerializer;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
    dbf.setNamespaceAware(true);
    DocumentBuilder db = dbf.newDocumentBuilder();
    Document doc = db.newDocument();
    Element root = doc.createElementNS(null, "person"); // Create Root Element
    Element item = doc.createElementNS(null, "name"); // Create element
    item.appendChild(doc.createTextNode("Jeff"));
    root.appendChild(item); // Attach element to Root element
    item = doc.createElementNS(null, "age"); // Create another Element
    item.appendChild(doc.createTextNode("28"));
    root.appendChild(item); // Attach Element to previous element down tree
    item = doc.createElementNS(null, "height");
    item.appendChild(doc.createTextNode("1.80"));
    root.appendChild(item); // Attach another Element - grandaugther
    doc.appendChild(root); // Add Root to Document
    DOMImplementationRegistry registry = DOMImplementationRegistry
        .newInstance();
    DOMImplementationLS domImplLS = (DOMImplementationLS) registry
        .getDOMImplementation("LS");
    LSSerializer ser = domImplLS.createLSSerializer(); // Create a serializer
// for the DOM
    LSOutput out = domImplLS.createLSOutput();
    StringWriter stringOut = new StringWriter(); // Writer will be a String
    out.setCharacterStream(stringOut);
    ser.write(doc, out); // Serialize the DOM
    System.out.println("STRXML = " + stringOut.toString()); // DOM as a String
  }
}
```

The code above generates the following result.

The following code shows how to edit text by insertion and replacement.

```java title=Example.java
public void edit3(Document doc) {
        int count;
        int offset;
        Element root = doc.getDocumentElement();
        Element place = (Element)root.getFirstChild();
        Text name = (Text)place.getFirstChild().getFirstChild();
        Text directions = (Text)place.getLastChild().getFirstChild();
        offset = 7;
        name.insertData(offset," black");
        offset = 5;
        count = 4;
        directions.replaceData(offset,count,"right");
    }
```

Modifying Text by Cutting and Pasting

```java title=Example.java
public void edit(Document doc) {
        int length;
        int count;
        int offset;
        Element root = doc.getDocumentElement();
        Element place = (Element)root.getFirstChild();
        Text name = (Text)place.getFirstChild().getFirstChild();
        Text directions = (Text)place.getLastChild().getFirstChild();
        length = name.getLength();
        count = 4;
        offset = length - 4;
        name.deleteData(offset,count);
        length = directions.getLength();
        count = 6;
        offset = length - count;
        String bridge = directions.substringData(offset,count);
        name.appendData(bridge);
        count = 5;
        offset = 4;
        directions.deleteData(offset,count);
    }
```

Modifying Text by Replacement

```java title=Example.java
public void edit(Document doc) {
        Element root = doc.getDocumentElement();
        Element place = (Element)root.getFirstChild();
        Text name = (Text)place.getFirstChild().getFirstChild();
        Text directions = (Text)place.getLastChild().getFirstChild();
        name.setData("AAA");
        directions.setData("BBB");
    }
```

## Comment

The following code shows how to create comments node for XML.

```java title=Example.java
import java.io.File;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Comment;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    factory.setValidating(true);
    factory.setExpandEntityReferences(false);
    Document doc = factory.newDocumentBuilder().parse(newFile("filename"));
    Element element = doc.getDocumentElement();
    Comment comment = doc.createComment("A Document Comment");
    element.getParentNode().insertBefore(comment, element);
  }
}
```

## Processing Instruction

The following code shows how to add ProcessingInstruction.

```java title=Example.java
public void addProcessingInstruction(Document doc) {
        Element root = doc.getDocumentElement();
        Element folks = (Element)root.getLastChild();
        ProcessingInstruction pi;
        pi = (ProcessingInstruction)doc.createProcessingInstruction(
            "validate",
            "phone=\"lookup\"");
        root.insertBefore(pi,folks);
    }
```

## CDATA

The following code shows how to add CDATA to XML document.

```java title=Example.java
publicvoid addCDATA(Document doc) {
        Element root = doc.getDocumentElement();
        Element place = (Element)root.getFirstChild();
        Element directions = (Element)place.getLastChild();
        String dirtext =">>>\n" +
            "<<<\n" +
            "&&&\n" +
            "<><><>.";
        CDATASection dirdata = doc.createCDATASection(dirtext);
        directions.replaceChild(dirdata,directions.getFirstChild());
    }
```

## Clone

```java title=Example.java
public void duplicatePerson(Document doc) {
        Element root = doc.getDocumentElement();
        Element origPerson = (Element)root.getFirstChild();
        Element newPerson = (Element)origPerson.cloneNode(true);
        root.appendChild(newPerson);
    }
```

- « Previous
