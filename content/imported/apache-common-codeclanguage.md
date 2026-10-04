---
title: Codec Language
nav: Codec Language
description: public void start() throws EncoderException, DecoderException{
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20061016100618/http://www.java2s.com/Code/Java/Apache-Common/CodecLanguage.htm
---
Codec Language

```java title=Example.java
import org.apache.commons.codec.*;
import org.apache.commons.codec.language.*;
public class LanguageUsage{
  public static void main(String args[]){
    LanguageUsage codec = new LanguageUsage();
    try{
      codec.start();
    }catch(Exception e){
      System.err.println(e);
    }
  }
  public void start() throws EncoderException, DecoderException{
    String word1 = "Wilson";
    String word2 = "Wylson";
    String foreignWord1 = "Otto";
    String foreignWord2 = "Auto";
    Soundex sndx = new Soundex();
    DoubleMetaphone doubleMetaphone = new DoubleMetaphone();
    System.err.println("Soundex Code for Wilson is: " + sndx.encode("Wilson"));
    System.err.println("Soundex Code for Wylson is: " + sndx.encode("Wylson"));
    // Use the StringEncoderComparator to compare these two Strings
    StringEncoderComparator comparator1 = new StringEncoderComparator(sndx);
    System.err.println("Are Wilson and Wylson same based on Soundex? "
      + comparator1.compare("Wilson", "Wylson"));
    System.err.println("Are Auto and Otto same based on Soundex? "
      + comparator1.compare("Auto", "Otto"));
    StringEncoderComparator comparator2 =
      new StringEncoderComparator(doubleMetaphone);
    System.err.println("Are Auto and Otto same based on DoubleMetaphone? "
      + comparator2.compare("Auto", "Otto"));
    System.err.println("Double Metaphone primary code for Schmidt: " +
      doubleMetaphone.doubleMetaphone("Schmidt"));
    System.err.println("Double Metaphone secondary code for Schmidt: " +
      doubleMetaphone.doubleMetaphone("Schmidt", true));
  }
}
```

Download: ApacheCodecLanguageUsage.zip ( 73 K )
Related examples in the same category
