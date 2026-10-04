---
title: Codec Digest
nav: Codec Digest
description: Imported from the java2s.com archive: Codec Digest
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20061016100624/http://www.java2s.com/Code/Java/Apache-Common/CodecDigest.htm
---
```java title=Example.java
import org.apache.commons.codec.digest.*;
public class DigestUsage{
  public static void main(String args[]){
    DigestUsage codec = new DigestUsage();
    try{
      codec.start();
    }catch(Exception e){
      System.err.println(e);
    }
  }
  public void start(){
    String hashData = "Hello World!!";
    System.err.println("Hello World!! as MD5 16 element hash: "
      + new String(DigestUtils.md5(hashData)));
    System.err.println("Hello World!! as MD5 Hex hash: "
      + DigestUtils.md5Hex(hashData));
    System.err.println("Hello World!! as SHA byte array hash: "
      + new String(DigestUtils.sha(hashData)));
    System.err.println("Hello World!! as SHA Hex hash: "
      + DigestUtils.shaHex(hashData));
  }
}
```

Download: ApacheCodecDigestUsage.zip ( 72 K )
Related examples in the same category
