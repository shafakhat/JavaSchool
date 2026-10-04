---
title: Java Utililty Methods AES Encrypt
nav: Java Utililty Methods AES ...
description: The list of methods to do AES Encrypt are organized into topic(s).
section: Imported - java2s Archive
order: 50015
source: https://www.java2s.com/example/java-utility-method/aes-encrypt-index-0.html
---
List of utility methods to do AES Encrypt

## Description

The list of methods to do AES Encrypt are organized into topic(s).

## Method

byte[]aesEncrypt(byte[] source, Key key) aes Encrypt

```java title=Example.java
try {
    Cipher cipher = Cipher.getInstance(AES_ALGORITHM_NAME);
    cipher.init(Cipher.ENCRYPT_MODE, key);
    return cipher.doFinal(source);
} catch (Exception e) {
    thrownewIllegalStateException("AES ecnrypt error", e);
```

StringaesEncrypt(String content, String encryptKey) aes Encrypt

```java title=Example.java
return parseByte2HexStr(aesEncryptToBytes(content, encryptKey));
```

StringaesEncrypt(String content, String key) aes Encrypt

```java title=Example.java
try {
    KeyGenerator kgen = KeyGenerator.getInstance("AES");
    kgen.init(128, newSecureRandom(key.getBytes()));
    SecretKey secretKey = kgen.generateKey();
    byte[] enCodeFormat = secretKey.getEncoded();
    SecretKeySpec secretKeySpec = newSecretKeySpec(enCodeFormat, "AES");
    Cipher cipher = Cipher.getInstance("AES");
    byte[] byteContent = content.getBytes("utf-8");
...
```

byte[]aesEncryptBytes(byte[] pBytes, SecretKeySpec pKeySpec, IvParameterSpec ivParameterSpec) aes Encrypt Bytes

```java title=Example.java
Cipher cipher = getAESCipher();
cipher.init(Cipher.ENCRYPT_MODE, pKeySpec, ivParameterSpec);
return cipher.doFinal(pBytes);
```

byte[]aesEncryptToBytes(String content, String encryptKey) aes Encrypt To Bytes

```java title=Example.java
KeyGenerator kgen = KeyGenerator.getInstance("AES");
kgen.init(128, newSecureRandom(encryptKey.getBytes()));
Cipher cipher = Cipher.getInstance("AES");
cipher.init(Cipher.ENCRYPT_MODE, newSecretKeySpec(kgen.generateKey().getEncoded(), "AES"));
return cipher.doFinal(content.getBytes("utf-8"));
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
