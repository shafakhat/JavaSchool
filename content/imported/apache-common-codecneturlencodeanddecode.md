---
title: Codec Net
nav: Codec Net
description: public void start() throws EncoderException, DecoderException{
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20061016100615/http://www.java2s.com/Code/Java/Apache-Common/CodecNetURLencodeanddecode.htm
---
Codec Net: URL encode and decode

```java title=Example.java
import org.apache.commons.codec.*;
import org.apache.commons.codec.net.*;
public class NetUsage{
  public static void main(String args[]){
    NetUsage codec = new NetUsage();
    try{
      codec.start();
    }catch(Exception e){
      System.err.println(e);
    }
  }
  public void start() throws EncoderException, DecoderException{
    String urlData1 = "This#is^a&String with reserved @/characters";
    URLCodec encoder = new URLCodec();
    String result = encoder.encode(urlData1);
    System.err.println("URL Encoding result: " + result);
    System.err.println("URL Decoding result: " + encoder.decode(result));
  }
}
```

Download: ApacheCodecNetUsage.zip ( 72 K )
Related examples in the same category
