---
title: Java Utililty Methods Amazon S3
nav: Java Utililty Methods Amaz...
description: The list of methods to do Amazon S3 are organized into topic(s).
section: Imported - java2s Archive
order: 50017
source: https://www.java2s.com/example/java-utility-method/amazon-s3-index-0.html
---
List of utility methods to do Amazon S3

## Description

The list of methods to do Amazon S3 are organized into topic(s).

## Method

StringwriteStreamToS3File(AWSCredentials credentials, String bucketName, String key, ByteArrayOutputStream stream, String contentType, CannedAccessControlList acl) writeStreamToS3File - Write a given Stream to a specified S3 file, returing a pre-signed URL to the file.

```java title=Example.java
String result = "";
AmazonS3Client conn = new AmazonS3Client(credentials);
ObjectMetadata metadata = new ObjectMetadata();
metadata.setContentType(contentType);
metadata.setContentLength((long) stream.toByteArray().length);
ByteArrayInputStream input = newByteArrayInputStream(stream.toByteArray());
conn.putObject(bucketName, key, (InputStream) input, metadata);
conn.setObjectAcl(bucketName, key, acl);
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
