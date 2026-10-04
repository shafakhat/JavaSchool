---
title: Java IO Tutorial - Java Jar file
nav: Java IO Tutorial - Java Ja...
description: JAR (Java Archive) is a file format based on the ZIP file format.
section: Imported - java2s Archive
order: 50219
source: https://www.java2s.com/Tutorials/Java/Java_io/0830__Java_io_Jar_File.html
---
```java title=Example.java
« Previous
```

- Next »

## JAR File Format

JAR (Java Archive) is a file format based on the ZIP file format.

It is used to bundle resources, class files, sound files, images, etc. for a Java application or applet. It also provides data compression.

A JAR file as a special kind of a ZIP file. You can digitally sign the contents of a JAR file to provide security. It provides a platform-independent file format.

You can use the JAR API to manipulate a JAR file in a Java program.

A JAR file can have an optional META-INF directory to contain files and directories containing information about application configuration.

## META-INF directory

The following table lists the entries in a META-INF directory.

Name  Type  Purpose
---  ---  ---
MANIFEST.MF  File  It contains extension and package related data.
INDEX.LIST  File  It contains location information of packages. Class loaders use it to speed up the class searching and loading process.
X.SF  File  X is the base file name. It stores the signature for the jar file.
X.DSA  File  X is the base file name. It stores the digital signature of the corresponding signature file.
/services  Directory  This directory contains all service provider configuration files.

## Jar tools

The JDK ships a jar tool to create and manipulate JAR files. You can also create and manipulate a JAR file using the Java API using classes in the java.util.jar package.

The JAR API has some new classes to deal with a manifest file. The Manifest class represents a manifest file.

To create a JAR file using the jar tool, many command-line options are available.

The following code lists the command-line options for the jar tool.

Option  Description
---  ---
-c  Create a new JAR file.
-u  Update an existing JAR file.
-x  Extract a named file or all files from a JAR file.
-t  List the table of contents of a JAR file.
-f  Specify the JAR file name.
-m  Include the manifest information from the specified file.
-M  Do not create a manifest file.
-i  Generate index information for the specified JAR file. It creates an INDEX.LIST file in JAR file under the META-INF directory.
-0  Do not compress the entries in the JAR file. Only store them. The option value is zero, which means zero compression.
-e  Add the specified class name as the value for the Main-Class entry in the main section of the manifest file.
-v  Generate verbose output on the standard output
-C  Change to the specified directory and include the following files in a JAR file. Note that the option is in uppercase (C). The lowercase (c) is used to indicate the create JAR file option.

## Creating a JAR File

Use the following command to create a test.jar JAR file with two class files called A.class and B.class:

```java title=Example.java

jar cf test.jar  A.class B.class
```

In the above command, the option c indicates that we are creating a new JAR file and the option f indicates that we are specifying a JAR file name, which is test.jar.

At the end of the command, we can specify one or more file names or directory names to include in the JAR file.

To view the contents of the test.jar file, execute the following command:

```java title=Example.java

jar tf test.jar
```

The option t indicates that we are interested in the table of contents of a JAR file.

The option f indicates that we are specifying the JAR file name, which is test.jar in this case.

The above command will generate the following output:

```java title=Example.java

META-INF/
META-INF/MANIFEST.MF A.class
B.class
```

jar command had automatically created two extra things for you: one directory called META-INF and a file named MANIFEST.MF in the META-INF directory.

The following command will create a test.jar file by including everything in the current working directory.

```java title=Example.java

jar cf test.jar  *
```

The following command will create a JAR file with all class files in the book/archives directory and all images from the book/images directory.

```java title=Example.java

jar cf test.jar  book/archives/*.class  book/images
```

We can specify a manifest file using the command-line option while creating a JAR file.

The manifest file is a text file that contains all manifest entries for your JAR file.

The manifest file must have a blank line at the end of the file. Otherwise, the last entry in the manifest file will not be processed.

The following command will use a manifest.txt file while creating test.jar file including all files and sub-directories in the current directory.

```java title=Example.java

jar cfm test.jar manifest.txt *
```

The order of the options used in the above command matters. f occurs before m, we must specify the JAR file name, test.jar, before the manifest file name manifest.txt.

You can rewrite the above command as follows:

```java title=Example.java

jar cmf manifest.txt test.jar *
```

## Updating a JAR File

Use the option u to update an existing JAR file entries or its manifest file.

The following command will add a C.class file to an existing test.jar file:

```java title=Example.java

jar uf  test.jar  C.class
```

Suppose we have a test.jar file and we want to change the Main-Class entry in its manifest file to HelloWorld class. You can do that by using the following command:

```java title=Example.java

jar ufe  test.jar HelloWorld
```

In this command, the option u indicates that we are updating a JAR file; the option f indicates that we are specifying the JAR file name, which is test.jar, and the option e indicates that we are specifying the Main-Class entry's value as HelloWorld for the MANIFEST.MF file in test.jar file.

## Indexing a JAR File

We can generate an index file for JAR file. It is used to speed up class loading.

We must use the option i with the jar command in a separate command, after creating a JAR file.

```java title=Example.java

jar i test.jar
```

This command will add a META-INF/INDEX.LIST file to the test.jar file. We can verify it by listing the table of contents of the test.jar file by using the following command:

```java title=Example.java

jar tf test.jar
```

## Extracting a JAR File

To extract all or some entries from a JAR file, use the option x with the jar command.

To extract all entries from a test.jar file

```java title=Example.java

jar xf  test.jar
```

The option x extracts the entries from the JAR file.

The option f specifies the file name, which is test.jar.

The above command will extract all entries from test.jar file in the current working directory.

It will create the same directory structure as it exists in the test.jar file.

To extract individual entries from a JAR file, list them at the end of the command. The entries should be separated by a space.

The following command will extract A.class and book/HelloWorld.class entries from a test.jar file:

```java title=Example.java

jar xf  test.jar A.class  book/HelloWorld.class
```

To extract all class files from a book directory, you can use the following command:

```java title=Example.java

jar xf  test.jar  book/*.class
```

## Listing JAR File Contents

Use the option t with the jar command to list the table of contents of a JAR file on the standard output.

```java title=Example.java

jar tf test.jar
```

- Next »
- « Previous
