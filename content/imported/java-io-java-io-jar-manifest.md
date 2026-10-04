---
title: Java IO Tutorial - Java Jar Manifest
nav: Java IO Tutorial - Java Ja...
description: A JAR file may optionally contain a manifest file named MANIFEST.MF in the META-INF directory.
section: Imported - java2s Archive
order: 50220
source: https://www.java2s.com/Tutorials/Java/Java_io/0840__Java_io_Jar_Manifest.html
---
```java title=Example.java
```

## Manifest File

A JAR file may optionally contain a manifest file named MANIFEST.MF in the META-INF directory.

The manifest file contains information about the JAR file and its entries.

A manifest file can contain information about the CLASSPATH setting for the JAR file, and its main entry class.

The main entry class is a class with the main() method to start a stand-alone application, version information about packages, etc.

A manifest file is divided into sections separated by a blank line. Each section contains name-value pairs. A new line separates each name-value pair. A colon separates a name and its corresponding value.

A manifest file must end with a new line. The following is a sample manifest file:

```java title=Example.java
Manifest-Version: 1.0
Created-By: 1.8.0_20-ea-b05 (Oracle Corporation)
Main-Class: com.java2s.Main
Profile:  compact1
```

The above manifest file has one section with four attributes:

- Manifest-Version
- Created-By
- Main-Class
- Profile

## Sections in Jar Manifest File

There are two kinds of sections in a manifest file: the main section and the individual section.

A blank line must separate any two sections. Entries in the main section apply to the entire JAR file. Entries in the individual section apply to a particular entry.

An attribute in an individual section overrides the same attribute in the main section.

An individual entry starts with a "Name" attribute, whose value is the name of the entry in the JAR file and it is followed by other attributes for that entry.

```java title=Example.java
Manifest-Version: 1.0
Created-By: 1.6.0  (Sun  Microsystems Inc.)
Main-Class: com.java2s.Main
Sealed: true
Name: book/data/
Sealed: false
Name: images/logo.bmp
Content-Type: image/bmp
```

The manifest file above contains three sections: one main section and two individual sections.

There is a blank line between the two sections.

The first individual section indicates that the package book/data is not sealed. This individual section attribute of "Sealed: false" will override the main section's attribute of "Sealed: true".

The second individual section is for an entry called images/logo.bmp. It states that the content type of the entry is an image of bmp type.

## Values in Jar Manifest File

The jar command can create a default manifest file and add it to the JAR file. The default manifest file contains only two attributes: Manifest-Version and Created-By.

You can use the option M to tell the jar tool to omit the default manifest file.

The following command will create a test.jar file without adding a default manifest file:

```java title=Example.java
jar cMf test.jar  *
```

The jar command gives you an option to customize the contents of the manifest file.

The option m specifies our file that has the contents for the manifest file.

The jar command will read the name-value pairs from the specified manifest file and add them to the MANIFEST.MF file.

Suppose you have a file named manifest.txt with one attribute entry in it. Make sure to add a new line at the end of the file. The file's contents are as follows:

```java title=Example.java
Main-Class: com.java2s.Main
```

To add the Main-Class attribute value from manifest.txt file in a new test.jar file by including all class files in the current working directory, you execute the following command:

```java title=Example.java
jar cfm test.jar manifest.txt *.class
```

When you specify the option m, you must also specify the manifest file name. The order in which you specify the new JAR file name and the manifest file name must match the order of options m and f.

For example, you can change the above command by specifying the f and m options in a different order as follows:

```java title=Example.java
jar cmf manifest.txt test.jar  *.class
```

This command will add a manifest file with the following contents to the test.jar file:

```java title=Example.java
Manifest-Version: 1.0
Created-By: 1.8.0_20-ea (Oracle Corporation)
Main-Class: com.java2s.Main
```

If you do not specify the Manifest-Version and Created-By attribute in your manifest file, the tool adds them. It defaults the Manifest-Version to 1.0. The Created-By is defaulted to the JDK version you use.

## Main class

The following code shows how to run a Java program by using the java command and specifying the class name that has the main() method as follows:

```java title=Example.java
java com.java2s.Main
```

com.java2s is the package name.

We can run a jar file using the -jar option with the java command as follows:

```java title=Example.java
java -jar test.jar
```

When you run the above command, the JVM will look for the value of the Main-Class attribute in the MANIFEST.MF file in the test.jar file and attempt to run that class.

If you have not included a Main-Class attribute in the test.jar file, the above command will generate an error.

We can also add the Main-Class attribute value in the manifest file without creating our own manifest file.

Use the option e with the jar tool when you create/update a jar file.

The following command will add com.java2s.Main as the value of the Main-Class in the MANIFEST.MF file in the test.jar file:

```java title=Example.java
jar cfe   test.jar com.java2s.Main *.class
```

The following command will add com.java2s.Main as the value of the Main-Class in the MANIFEST.MF file in an existing test.jar file by using the option u for update:

```java title=Example.java
jar ufe  test.jar com.java2s.Main
```

## Class Path

You can set the CLASSPATH for a JAR file in its manifest file. The attribute name is called Class-Path, which you must specify in a custom manifest file. It is a space-separated list of jar files, zip files, and directories. The Class-Path attribute in a manifest file looks like

```java title=Example.java
Class-Path: Main.jar  file:/c:/book/  http:/tutorial.jar
```

The above entry has three items for the CLASSPATH: a JAR file Main.jar, a directory using the file protocol file:/c:/book/, and another JAR file using a HTTP protocol http://www.java2s.com/tutorial.jar.

A directory name must end with a forward slash. Suppose this Class-Path setting is included in the manifest file for the test.jar file. When you run the test.jar file using the following java command, this CLASSPATH will be used to search and load classes.

```java title=Example.java
java -jar test.jar
```

When you run a JAR file with the -jar option using the java command, any CLASSPATH setting outside the manifest file of the JAR file (test.jar file in the above case) is ignored.

Another use of the Class-Path attribute is to generate an index of all packages using the option i of the jar tool.

The following command will generate an index for all packages in all JAR files listed in the Class-Path attribute of the manifest file in the test.jar file:

```java title=Example.java
jar i test.jar
```

## Sealing a Package in a JAR File

Sealing a package in a JAR file means that all classes declared in that package must be archived in the same JAR file.

To seal a package in a JAR file, include two attributes: Name and Sealed. The value for the Name attribute is the name of the package and the Sealed attribute has value as true.

The following entries in a manifest file will seal a package named com.java2s. The package name must end with a forward slash (/).

```java title=Example.java
Name: com/java2s/ Sealed: true
```

By default, all packages in a JAR file are not sealed. If you want to seal the JAR file itself, you can include a Sealed attributed, as shown:

```java title=Example.java
Sealed: true
```

Sealing the JAR file will seal all packages in that JAR file. However, you can override it by not sealing a package individually.

The following entries in a manifest file will seal all packages in the JAR file, except the book/tutorial/ package:

```java title=Example.java
Sealed: true
Name: book/tutorial/
Sealed: false
```

- « Previous
