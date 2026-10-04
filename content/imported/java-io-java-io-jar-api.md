---
title: Java IO Tutorial - Java Jar API
nav: Java IO Tutorial - Java Ja...
description: JAR API includes classes for working with a manifest file. An object of the Manifest class represents a manifest file. You create a Manifest object in your code as follow
section: Imported - java2s Archive
order: 50221
source: https://www.java2s.com/Tutorials/Java/Java_io/0850__Java_io_Jar_API.html
---
## JAR API

JAR API includes classes for working with a manifest file. An object of the Manifest class represents a manifest file. You create a Manifest object in your code as follows:

```java title=Example.java
Manifest manifest = new Manifest();
```

We can read entries from a manifest file and write entries to it.

To add an entry into a main section, get an instance of the Attributes class using the getMainAttributes() method from Manifest class and keep adding a name-value pair to it using its put() method.

The following code adds some attributes to the main section of a manifest object. The known attribute names are defined as constants in the Attributes.Name class.

For example, the constant Attributes.Name.MANIFEST_VERSION represents the Manifest-Version attribute name.

```java title=Example.java
Manifest manifest = new Manifest();
Attributes  mainAttribs = manifest.getMainAttributes(); mainAttribs.put(Attributes.Name.MANIFEST_VERSION, "1.0"); mainAttribs.put(Attributes.Name.MAIN_CLASS, "com.java2s.Main"); mainAttribs.put(Attributes.Name.SEALED, "true");
```

Adding an individual entry to the manifest file is a little more complex than adding the main entry.

The following code shows you how to add an individual entry to a Manifest object:

```java title=Example.java
Map<String,Attributes> attribsMap = manifest.getEntries();
Attributes attribs  = new Attributes();
Attributes.Name name = new Attributes.Name("Sealed");
attribs.put(name, "false");
attribsMap.put("com/java2s/archives/", attribs);
```

To add a manifest file to a JAR file, specify it in one of the constructors of the JarOutputStream class.

For example, the following code creates a jar output stream to create a test.jar file with a Manifest object:

```java title=Example.java
Manifest manifest = new Manifest();
JarOutputStream jos  = new JarOutputStream(new BufferedOutputStream(
new FileOutputStream("test.jar")), manifest);
```

The following code creates a JAR file that includes a manifest file.

```java title=Example.java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Map;
import java.util.jar.Attributes;
import java.util.jar.JarEntry;
import java.util.jar.JarOutputStream;
import java.util.jar.Manifest;
import java.util.zip.Deflater;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Manifest manifest = getManifest();
    String jarFileName = "jartest.jar";
    String[] entries = new String[2];
    entries[0] = "images/logo.bmp";
    entries[1] = "com/java2s/Test.class";
    createJAR(jarFileName, entries, manifest);
  }
  publicstaticvoid createJAR(String jarFileName, String[] jarEntries,
      Manifest manifest) {
    try (JarOutputStream jos = new JarOutputStream(new BufferedOutputStream(
        new FileOutputStream(jarFileName)), manifest)) {
      jos.setLevel(Deflater.BEST_COMPRESSION);
      for (int i = 0; i < jarEntries.length; i++) {
        File entryFile = newFile(jarEntries[i]);
        if (!entryFile.exists()) {
          return;
        }
        JarEntry je = new JarEntry(jarEntries[i]);
        jos.putNextEntry(je);
        addEntryContent(jos, jarEntries[i]);
        jos.closeEntry();
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  publicstaticvoid addEntryContent(JarOutputStream jos, String entryFileName)
      throws IOException, FileNotFoundException {
    BufferedInputStream bis = new BufferedInputStream(new FileInputStream(
        entryFileName));
    byte[] buffer = newbyte[1024];
    int count = -1;
    while ((count = bis.read(buffer)) != -1) {
      jos.write(buffer, 0, count);
    }
    bis.close();
  }
  publicstatic Manifest getManifest() {
    Manifest manifest = new Manifest();
    Attributes mainAttribs = manifest.getMainAttributes();
    mainAttribs.put(Attributes.Name.MANIFEST_VERSION, "1.0");
    mainAttribs.put(Attributes.Name.MAIN_CLASS, "com.java2s.Test");
    mainAttribs.put(Attributes.Name.SEALED, "true");
    Map<String, Attributes> attribsMap = manifest.getEntries();
    Attributes a1 = getAttribute("Sealed", "false");
    attribsMap.put("com/java2s/", a1);
    Attributes a2 = getAttribute("Content-Type", "image/bmp");
    attribsMap.put("images/logo.bmp", a2);
    return manifest;
  }
  publicstatic Attributes getAttribute(String name, String value) {
    Attributes a = new Attributes();
    Attributes.Name attribName = new Attributes.Name(name);
    a.put(attribName, value);
    return a;
  }
}
```

To read the entries from a manifest file of a JAR file, get the object of the Manifest class using the getManifest() class of the JarInputStream as follows:

```java title=Example.java
JarInputStream jis = new JarInputStream(new FileInputStream("jartest.jar"));
Manifest manifest = jis.getManifest();
if (manifest !=  null)  {
    Attributes  mainAttributes = manifest.getMainAttributes();
    String  mainClass = mainAttributes.getValue("Main-Class");
    Map<String, Attributes> entries  = manifest.getEntries();
}
```

## Accessing Resources from a JAR File

You can construct a URL object by using the reference of a resource in a JAR file.

The JAR file URL syntax is

```java title=Example.java
jar:<url>!/{entry}
```

The following URL refers to an images/logo.bmp JAR entry in a test.jar file on www.java2s.com using the HTTP protocol:

```java title=Example.java
jar:http:/test.jar!/images/logo.bmp
```

The following URL refers to an images/logo.bmp JAR entry in a test.jar file on the local file system in the c:\jarfiles\ directory using the file protocol:

```java title=Example.java
jar:file:/c:/jarfiles/test.jar!/images/logo.bmp
```

To read the images/logo.bmp file from a JAR file in the classpath, you can get an input stream object using a class object as follows:

```java title=Example.java
// Assuming that the   Test   class is in the   CLASSPATH
Class cls = Test.class;
InputStream in = cls.getResourceAsStream("/images/logo.bmp")
```

You can also get a URL object for an entry in your JAR file, which is in your classpath as follows:

```java title=Example.java
URL  url = cls.getResource("/images/logo.bmp");
```

- « Previous
