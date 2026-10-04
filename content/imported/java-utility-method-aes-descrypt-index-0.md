---
title: Java Utililty Methods AES Descrypt
nav: Java Utililty Methods AES ...
description: The list of methods to do AES Descrypt are organized into topic(s).
section: Imported - java2s Archive
order: 50014
source: https://www.java2s.com/example/java-utility-method/aes-descrypt-index-0.html
---
List of utility methods to do AES Descrypt

## Description

The list of methods to do AES Descrypt are organized into topic(s).

## Method

byte[]aesDecrypt(byte[] content, Key key) aes Decrypt

```java title=Example.java
return aesCrypt(content, key, Cipher.DECRYPT_MODE);
```

byte[]AESDecrypt(byte[] encrypted, byte[] key, byte[] iv) AES Decrypt

```java title=Example.java
try {
    SecretKeySpec skeySpec = newSecretKeySpec(key, "AES");
    IvParameterSpec ivSpec = newIvParameterSpec(iv);
    Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
    cipher.init(Cipher.DECRYPT_MODE, skeySpec, ivSpec);
    return cipher.doFinal(encrypted);
} catch (InvalidKeyException e) {
    thrownewIllegalArgumentException(
...
```

byte[]aesDecrypt(byte[] input, Key key) aes Decrypt

```java title=Example.java
return aesDecrypt(input, key, IV16);
```

StringaesDecrypt(String encryptStr, String decryptKey) aes Decrypt

```java title=Example.java
return aesDecryptByBytes(parseHexStr2Byte(encryptStr), decryptKey);
```

StringaesDecryptByBytes(byte[] encryptBytes, String decryptKey) aes Decrypt By Bytes

```java title=Example.java
if (encryptBytes == null || decryptKey == null) {
    return null;
try {
    KeyGenerator kgen = KeyGenerator.getInstance("AES");
    kgen.init(128, newSecureRandom(decryptKey.getBytes()));
    Cipher cipher = Cipher.getInstance("AES");
    cipher.init(Cipher.DECRYPT_MODE, newSecretKeySpec(kgen.generateKey().getEncoded(), "AES"));
...
```
