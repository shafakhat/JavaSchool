---
title: Java Utililty Methods AES
nav: Java Utililty Methods AES
description: byte[]aesHandler(byte[] toBeHandleData, String password, boolean isEncrypt) aes Handler
section: Imported - java2s Archive
order: 50013
source: https://www.java2s.com/example/java-utility-method/aes-index-0.html
---
List of utility methods to do AES

## Description

The list of methods to do AES are organized into topic(s).

## Method

CipheraesCipher() aes Cipher

```java title=Example.java
returnCipher.getInstance("AES/CCM/NoPadding", "BC");
```

byte[]aesCrypt(byte[] content, Key key, int crypt) aes Crypt

```java title=Example.java
try {
    Cipher cipher = Cipher.getInstance(AES_CIPER_ALGRITHM);
    cipher.init(crypt, key);
    return cipher.doFinal(content);
} catch (Exception e) {
    e.printStackTrace();
return content;
...
```

byte[]aesHandler(byte[] toBeHandleData, String password, boolean isEncrypt) aes Handler

```java title=Example.java
try {
    SecretKeySpec e = newSecretKeySpec(toKey(password), "AES");
    Cipher cipher = Cipher.getInstance("AES/CFB8/NoPadding");
    IvParameterSpec initialParameter = newIvParameterSpec(IV);
    cipher.init(isEncrypt ? 1 : 2, e, initialParameter);
    return cipher.doFinal(toBeHandleData);
} catch (Exceptionvar6) {
    return null;
...
```

SecretKeyaesKey(int keySize) aes Key

```java title=Example.java
KeyGenerator kgen = KeyGenerator.getInstance("AES");
kgen.init(keySize);
return kgen.generateKey();
```

voidaesStoreKeyToFile(Key secretKey, String path) aes Store Key To File

```java title=Example.java
try {
    Path store = Paths.get(path);
    Files.write(store, secretKey.getEncoded());
} catch (Exception e) {
    e.printStackTrace();
```

StringcreateSessionKey() Creates random session keys

```java title=Example.java
KeyGenerator gen = KeyGenerator.getInstance("AES");
gen.init(128);
byte[] original = gen.generateKey().getEncoded();
String s = DatatypeConverter.printBase64Binary(original);
return s;
```

Stringdecrypt(String encryptedText, String key) decrypt

```java title=Example.java
try {
    byte[] encrypted = BaseEncoding.base64Url().decode(encryptedText);
    Cipher cipher = Cipher.getInstance("AES");
    cipher.init(Cipher.DECRYPT_MODE, getAesKey(key));
    byte[] plain = cipher.doFinal(encrypted);
    if (plain == null || plain.length <= 8) {
        thrownewRuntimeException("wrong encrypted text.");
    byte[] data = newbyte[plain.length - 8];
    System.arraycopy(plain, 8, data, 0, data.length);
    returnnewString(data, "ISO-8859-1");
} catch (InvalidKeyException e) {
    thrownewRuntimeException(e);
} catch (NoSuchAlgorithmException e) {
    thrownewRuntimeException(e);
} catch (NoSuchPaddingException e) {
    thrownewRuntimeException(e);
} catch (IllegalBlockSizeException e) {
    thrownewRuntimeException(e);
} catch (BadPaddingException e) {
    thrownewRuntimeException(e);
} catch (UnsupportedEncodingException e) {
    thrownewRuntimeException(e);
```

Stringdecrypt_aes(String key, String initVector, String encrypted) decrypaes

```java title=Example.java
try {
    IvParameterSpec iv = newIvParameterSpec(initVector.getBytes("UTF-8"));
    SecretKeySpec skeySpec = newSecretKeySpec(key.getBytes("UTF-8"), "AES");
    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
    cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv);
    byte[] original = cipher.doFinal(DatatypeConverter.parseBase64Binary(encrypted));
    returnnewString(original);
} catch (Exception ex) {
...
```

StringencryptAes(String value) encrypt Aes

```java title=Example.java
Key key = generateKey();
Cipher c = Cipher.getInstance(ALGORITHM);
c.init(Cipher.ENCRYPT_MODE, key);
byte[] encryptedBytes = c.doFinal(value.getBytes());
String encryptedValue = DatatypeConverter.printBase64Binary(encryptedBytes);
return encryptedValue;
```

StringencryptDecrypt(int mode, String data, String key, String salt, String iv) Encrypts and decrypts a string.

```java title=Example.java
KeySpec pbeKeySpec = newPBEKeySpec(key.toCharArray(), DatatypeConverter.parseBase64Binary(salt),
        ITERATIONS, KEY_LENGTH);
SecretKey secretKey = getSecretKey(pbeKeySpec);
Cipher cipher = getCipher();
cipher.init(mode, secretKey, newIvParameterSpec(DatatypeConverter.parseBase64Binary(iv)));
if (mode == DECRYPT_MODE) {
    returnnewString(cipher.doFinal(DatatypeConverter.parseBase64Binary(data)), StandardCharsets.UTF_8);
} else {
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
