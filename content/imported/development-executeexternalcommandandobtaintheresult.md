---
title: Execute external command and obtain the result
nav: Execute external command a...
description: BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100626055524/http://www.java2s.com:80/Tutorial/Java/0120__Development/Executeexternalcommandandobtaintheresult.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
  public static void main(String[] args) throws Exception{
    Process process = Runtime.getRuntime().exec("ls -al");
    process.waitFor();
    int exitValue = process.exitValue();
    System.out.println("exitValue = " + exitValue);
    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
    String line = "";
    while ((line = reader.readLine()) != null) {
      System.out.println(line);
    }
  }
}
```
