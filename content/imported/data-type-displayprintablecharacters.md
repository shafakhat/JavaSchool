---
title: Display printable Characters
nav: Display printable Characters
description: Imported from the java2s.com archive: Display printable Characters
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DisplayprintableCharacters.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    for (int i = 32; i < 127; i++) {
      System.out.write(i);
      // break line after every eight characters.
 if (i % 8 == 7)
        System.out.write('\n');
      else
        System.out.write('\t');
    }
    System.out.write('\n');
  }
}
java title=Example.java
! " # $ % & '
  ( ) * + , - . /
  0 1 2 3 4 5 6 7
  8 9 : ; < = > ?
  @ A B C D E F G
  H I J K L M N O
  P Q R S T U V W
  X Y Z [ \ ] ^ _
  ` a b c d e f g
  h i j k l m n o
  p q r s t u v w
  x y z { | } ~
```
