---
title: Java Design Patterns Tutorial - Java Design Pattern - Adapter Pattern
nav: Java Design Patterns Tutor...
description: We use the adapter in real life a lot. For example, we use a memory card adapter to connect a memory card and a computer since the computer only support one type of memor
section: Imported - java2s Archive
order: 50117
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0060__Java_Adapter_Pattern.html
---
```java title=Example.java
```

We use the adapter in real life a lot. For example, we use a memory card adapter to connect a memory card and a computer since the computer only support one type of memory card and our card is not compatible with the computer.

Adapter is a converter between two incompatible entities. Adapter pattern is a structural pattern.

In Java design pattern, Adapter pattern works as a bridge between two incompatible interfaces.

By using the adapter pattern we can unify the two incompatible interfaces.

## Example

First we create a Player interface to play any time of media files.

MyPlayer is the adapter, it unifies the interface of playing media files.

```java title=Example.java
interface Player {
   publicvoid play(String type, String fileName);
}/*www.java2s.com*/interface AudioPlayer {
   publicvoid playAudio(String fileName);
}
interface VideoPlayer {
   publicvoid playVideo(String fileName);
}
class MyAudioPlayer implements AudioPlayer {
   @Override
   publicvoid playAudio(String fileName) {
      System.out.println("Playing. Name: "+ fileName);
   }
}
class MyVideoPlayer implements VideoPlayer {
   @Override
   publicvoid playVideo(String fileName) {
      System.out.println("Playing. Name: "+ fileName);
   }
}
class MyPlayer implements Player {
   AudioPlayer audioPlayer = new MyAudioPlayer();
   VideoPlayer videoPlayer = new MyVideoPlayer();
   public MyPlayer(){
   }
   @Override
   publicvoid play(String audioType, String fileName) {
      if(audioType.equalsIgnoreCase("avi")){
         videoPlayer.playVideo(fileName);
      }elseif(audioType.equalsIgnoreCase("mp3")){
         audioPlayer.playAudio(fileName);
      }
   }
}
publicclass Main{
   publicstaticvoid main(String[] args) {
      MyPlayer myPlayer = new MyPlayer();
      myPlayer.play("mp3", "h.mp3");
      myPlayer.play("avi", "me.avi");
   }
}
```

The code above generates the following result.

- « Previous
