---
title: ProcessBuilder
nav: ProcessBuilder
description: ProcessBuilder proc = new ProcessBuilder("notepad.exe", "testfile");
section: Imported - java2s Archive
order: 1808
source: https://web.archive.org/web/20140816205721/http://www.java2s.com/Tutorial/Java/0120__Development/ProcessBuilderstartandmanageprocessesprograms.htm
---
```java title=Example.java
import java.io.IOException;
public class MainClass {
  public static void main(String args[]) throws IOException {
    ProcessBuilder proc = new ProcessBuilder("notepad.exe", "testfile");
    proc.start();
  }
}
```
