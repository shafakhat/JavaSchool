---
title: Java Utililty Methods Activation Mimetype Check
nav: Java Utililty Methods Acti...
description: The list of methods to do Activation Mimetype Check are organized into topic(s).
section: Imported - java2s Archive
order: 50012
source: https://www.java2s.com/example/java-utility-method/activation-mimetype-check-index-0.html
---
List of utility methods to do Activation Mimetype Check

## Description

The list of methods to do Activation Mimetype Check are organized into topic(s).

## Method

MimeTypecopyMimeType(final MimeType original) copy Mime Type

```java title=Example.java
returnnewMimeType(original.getPrimaryType(), original.getSubType());
```

MimeTypecreateWildcard() create Wildcard

```java title=Example.java
try {
    returnnewMimeType("*/*");
} catch (Exception e) {
    return null;
```

booleanequal(String string1, String string2) Returns true if the given MIME type strings are considered equivalent because their types and subtypes match (parameters are not considered in the comparison).

```java title=Example.java
if (string1 == null && string2 == null)
    return true;
if (string1 == null || string2 == null)
    return false;
MimeType mimeType1 = newMimeType(string1);
MimeType mimeType2 = newMimeType(string2);
return mimeType1.match(mimeType2);
```

StringgetContentType(String filename) get Content Type

```java title=Example.java
if (filename == null || filename.length() == 0) {
    return"application/octet-stream";
String contentType;
if (filename.endsWith(".html") || filename.endsWith(".htm")) {
    contentType = "text/html";
} elseif (filename.endsWith(".js")) {
    contentType = "text/javascript";
...
```

StringgetContentType(String filePath) Returns the mime type of the given file.

```java title=Example.java
FileTypeMap map = MimetypesFileTypeMap.getDefaultFileTypeMap();
return map.getContentType(filePath);
```

StringgetContentTypeFromFileName(String fileName) get Content Type From File Name

```java title=Example.java
FileTypeMap map = FileTypeMap.getDefaultFileTypeMap();
if (map instanceofMimetypesFileTypeMap) {
    try {
        ((MimetypesFileTypeMap) map).addMimeTypes("image/png png PNG");
    } catch (Exception ignored) {
return map.getContentType(fileName);
...
```

StringgetMimeType(final String filename) get Mime Type

```java title=Example.java
if (filename == null) {
    return null;
return mimeMap.getContentType(filename);
```

StringgetMimetype(String filename) get Mimetype

```java title=Example.java
return mimeMap.getContentType(filename);
```

StringgetMimeTypeForFileName(String filename) get Mime Type For File Name

```java title=Example.java
String mimeType = mimeTypes.getContentType(filename);
if (mimeType != null) {
    return mimeType;
} else {
    return GENERIC_MIME_TYPE;
```

voidinit() Init the mime type list

```java title=Example.java
mimeTypes.addMimeTypes("application/vnd.ms-excel xls xlt");
mimeTypes.addMimeTypes("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet xlsx");
mimeTypes.addMimeTypes("application/msword doc dot");
mimeTypes.addMimeTypes("application/vnd.openxmlformats-officedocument.wordprocessingml.document docx");
mimeTypes.addMimeTypes("application/pdf pdf");
mimeTypes.addMimeTypes("application/rtf rtf");
mimeTypes.addMimeTypes("text/csv csv");
mimeTypes.addMimeTypes("application/vnd.ms-powerpoint ppt pps pot");
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
