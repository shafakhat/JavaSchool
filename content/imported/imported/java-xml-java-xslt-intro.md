---
title: Java XML Tutorial - Java XSLT
nav: Java XML Tutorial - Java X...
description: The Extensible Stylesheet Language Transformations (XSLT) standard defines class for addressing XML data with XPath and for transforming the data to other forms.
section: Imported - java2s Archive
order: 50324
source: https://www.java2s.com/Tutorials/Java/Java_XML/0200__Java_XSLT_Intro.html
---
```java title=Example.java
```

The Extensible Stylesheet Language Transformations (XSLT) standard defines class for addressing XML data with XPath and for transforming the data to other forms.

JAXP includes an interpreting implementation of XSLT.

## XSL, XSLT, and XPath

The Extensible Stylesheet Language (XSL) has three major subcomponents:

Component  Description
---  ---
XSL-FO  The Formatting Objects standard. We can define font sizes, page layouts, and other aspects of object rendering.
XSLT  It defines a transformation from XML into some other format. For example, use XSLT to produce HTML from XML document.
XPath  XPath is a specification language we can use to create a path to an element.

## JAXP Transformation Packages

Here is a description of the packages for the JAXP Transformation APIs:

Package  Description
---  ---
javax.xml.transform  This package defines the factory class to return a Transformer object. We can configure the Transformer with input and output objects, and invoke its transform() method to do the transformation.
javax.xml.transform.dom  Defines the DOMSource and DOMResult classes for using a DOM as an input to or output in a transformation.
javax.xml.transform.sax  Defines the SAXSource and SAXResult classes for using a SAX as input or output in a transformation.
javax.xml.transform.stream  Defines the StreamSource and StreamResult classes for using an I/O stream as an input to or output in transformation.

An XPath expression specifies a pattern to select a set of XML nodes.

XSLT templates can use those patterns to select nodes and apply transformations.

With XPath expression we can refer elements text and attributes. The XPath specification defines seven kinds of nodes:

- Root
- Element
- Text
- Attribute
- Comment
- Processing instruction
- Namespace

## XPath Addressing

An XML document is a tree-structured collection of nodes.

XPath use path notation to address the node in XML.

- The forward slash / is a path separator.
- An absolute path from the document root starts with / .
- A relative path can start with anything else.
- A double period .. indicates the parent node.
- A single period . indicates the current node.

In XPath /h1/h2 selects all h2 elements that lie under an h1 element.

To select a specific h2 element, we use square brackets [] to index.

For example, /h1[4]/h2[5] would select the fifth h2 element under the fourth h1 element.

To refer to an attribute, prefix the attribute name with an @ sign. For example, @type refers to the type attribute.

h1/@type selects the type attribute of the h1 element.

## XPath Expressions

XPath expressions can use the wild cards, operators, and its own functions.

The expression @type="unordered" specifies an attribute named type whose value is unordered.

The expression h1[@type="unordered"] selects all h1 elements whose type attribute value is unordered.

## Example

Suppose we have a phone data stored in the following XML document.

```java title=Example.java

<PHONEBOOK>
<PERSON>
 <NAME>Joe Wang</NAME>
 <EMAIL>joe@yourserver.com</EMAIL>
 <TELEPHONE>202-999-9999</TELEPHONE>
 <WEB>www.java2s.com</WEB>
</PERSON>
<PERSON>
 <NAME>Karol</name>
 <EMAIL>karol@yourserver.com</EMAIL>
 <TELEPHONE>306-999-9999</TELEPHONE>
 <WEB>www.java2s.com</WEB>
</PERSON>
<PERSON>
 <NAME>Green</NAME>
 <EMAIL>green@yourserver.com</EMAIL>
 <TELEPHONE>202-414-9999</TELEPHONE>
 <WEB>www.java2s.com</WEB>
</PERSON>
</PHONEBOOK>
```

And we would transform the XML above using the following XSLT to a HTML file.

```java title=Example.java

<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">
<html>
<head>
<title>Directory</title>
</head>
<body>
<table border="1">
<tr>
 <th>Name</th>
 <th>Telephone</th>
 <th>Email</th>
</tr>
<xsl:for-each select="PHONEBOOK/PERSON">
 <xsl:sort/>
 <tr>
  <td><xsl:value-of select="NAME"/></td>
  <td><xsl:value-of select="TELEPHONE"/></td>
  <td><xsl:value-of select="EMAIL"/></td>
 </tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
```

From the code above we can see that the data would be transformed to a HTML table.

We use the following code to do the transformation.

```java title=Example.java
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String args[]) throws Exception {
    StreamSource source = new StreamSource(args[0]);
    StreamSource stylesource = new StreamSource(args[1]);
    TransformerFactory factory = TransformerFactory.newInstance();
    Transformer transformer = factory.newTransformer(stylesource);
    StreamResult result = new StreamResult(System.out);
    transformer.transform(source, result);
  }
}
```

## Example 2

The following code shows how to transform xml with StAX parsers.

```java title=Example.java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
/*fromwww.java2s.com*/import javax.xml.XMLConstants;
import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    SchemaFactory sf = SchemaFactory
        .newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
    System.out.println("schema factory instance obtained is " + sf);
    Schema schema = sf.newSchema(newFile(args[0]));
    System.out.println("schema obtained is = " + schema);
    Validator validator = schema.newValidator();
    String fileName = args[1].toString();
    String fileName2 = args[2].toString();
    javax.xml.transform.Result xmlResult = new javax.xml.transform.stax.StAXResult(
        XMLOutputFactory.newInstance().createXMLStreamWriter(
            new FileWriter(fileName2)));
    javax.xml.transform.Source xmlSource = new javax.xml.transform.stax.StAXSource(
        getXMLEventReader(fileName));
    validator.validate(new StreamSource(args[1]));
    validator.validate(xmlSource, xmlResult);
  }
  privatestatic XMLEventReader getXMLEventReader(String filename)
      throws Exception {
    XMLInputFactory xmlif = null;
    XMLEventReader xmlr = null;
    xmlif = XMLInputFactory.newInstance();
    xmlif.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES,
        Boolean.TRUE);
    xmlif.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES,
        Boolean.FALSE);
    xmlif.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, Boolean.TRUE);
    xmlif.setProperty(XMLInputFactory.IS_COALESCING, Boolean.TRUE);
    FileInputStream fis = new FileInputStream(filename);
    xmlr = xmlif.createXMLEventReader(filename, fis);
    return xmlr;
  }
}
```

## Example 3

The following code uses the DOMSource as the transform input.

```java title=Example.java
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
//www.java2s.comimport javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    DocumentBuilder builder = factory.newDocumentBuilder();
    Document document = builder.parse(new InputSource(new InputStreamReader(new FileInputStream(
        "inputFile.xml"))));
    Transformer xformer = TransformerFactory.newInstance().newTransformer();
    xformer.setOutputProperty(OutputKeys.METHOD, "xml");
    xformer.setOutputProperty(OutputKeys.INDENT, "yes");
    xformer.setOutputProperty("http://xml.apache.org/xslt;indent-amount", "4");
    xformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
    Source source = new DOMSource(document);
    Result result = new StreamResult(newFile("result.xml"));
    xformer.transform(source, result);
  }
}
```

## Example 4

The following code shows how to change a specific element using XPath.

```java title=Example.java
//fromwww.java2s.comimport java.io.File;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Document doc = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(
        new InputSource("data.xml"));
    XPath xpath = XPathFactory.newInstance().newXPath();
    NodeList nodes = (NodeList) xpath.evaluate("//employee/name[text()='old']", doc,
        XPathConstants.NODESET);
    for (int idx = 0; idx < nodes.getLength(); idx++) {
      nodes.item(idx).setTextContent("new value");
    }
    Transformer xformer = TransformerFactory.newInstance().newTransformer();
    xformer.transform(new DOMSource(doc), new StreamResult(newFile("data_new.xml")));
  }
}
```

- « Previous
