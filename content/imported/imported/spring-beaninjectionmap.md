---
title: Bean Injection
nav: Bean Injection
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20090226184121/http://www.java2s.com:80/Code/Java/Spring/BeanInjectionMap.htm
---
Bean Injection: Map

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="ftpDownloader" class="FtpDownloader"/>
    <bean id="httpDownloader" class="HttpDownloader"/>
    <bean id="sftpDownaloader" class="SftpDownloader"/>
    <bean id="downloadManager" class="DownloadManager">
        <property name="downloaders">
            <map>
                <entry key="ftp" value-ref="ftpDownloader"/>
                <entry key="http" value-ref="httpDownloader"/>
                <entry key="sftp" value-ref="sftpDownaloader"/>
            </map>
        </property>
    </bean>
</beans>
File: Main.java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Component;
public class Main {
  public static void main(String[] args) throws Exception {
    XmlBeanFactory xbf = new XmlBeanFactory(new ClassPathResource("context.xml"));
    DownloadManager dm = (DownloadManager)xbf.getBean("downloadManager");
    String uri = "http://www.java2s.com";
    dm.download(uri);
  }
}
class DownloadManager {
  private static final Pattern URI_PATTERN = Pattern.compile("^([^:]*):/(.*)$");
  private Map<String, Downloader> downloaders;
  void download(String uri) {
      Matcher matcher = URI_PATTERN.matcher(uri);
      if (matcher.matches()) {
          String scheme = matcher.group(1);
          String path = matcher.group(2);
          Downloader downloader = this.downloaders.get(scheme);
          if (downloader != null) {
              downloader.download(path);
          }
      }
  }
  public void setDownloaders(Map<String, Downloader> downloaders) {
      this.downloaders = downloaders;
  }
}
@Component
class SftpDownloader implements Downloader {
    public byte[] download(String uri) {
        System.out.println("SFTP Downloading " + uri);
        return new byte[0];
    }
}
@Component
 class HttpDownloader implements Downloader {
    public byte[] download(String uri) {
        System.out.println("HTTP Downloading " + uri);
        return new byte[0];
    }
}
@Component
 class FtpDownloader implements Downloader {
    public byte[] download(String uri) {
        System.out.println("FTP Downloading " + uri);
        return new byte[0];
    }
}
interface Downloader {
    byte[] download(final String uri);
}
```

Spring-BeanInjectionMap.zip( 2,601 k)
1.  Property Setting: URL
2.  PropertySetting: String Array
3.  Property Setting: Stream From URL
4.  Property Setting: Properties
5.  Property Setting: Integer
6.  Property Setting: File
7.  Property Setting: Class type
8.  Property Setting: Byte Array
9.  Property Setting: Boolean
10.  Property Setting: BigDecimal
11.  Properties Setting: Date
12.  Load property File In Context
13.  lazy init
14.  Fill Value To List
15.  Fill Map
16.  Fill Set
17.  Fill Properties
18.  Fill List To Another List
19.  Fill Calendar Object To List
20.  Create List Map In Context
21.  Bean Injection Collection: Set
22.  Bean Injection: Collection Properties
23.  Bean Injection Collection: Map
24.  Bean Injection Collection: List
