---
title: MembershipKey and DatagramChannel
nav: MembershipKey and Datagram...
description: NetworkInterface networkInterface = NetworkInterface.getByName("net1");
section: Imported - java2s Archive
order: 1099
source: https://web.archive.org/web/20130820200443/http://java2s.com/Code/Java/JDK-7/MembershipKeyandDatagramChannel.htm
---
```java title=Example.java
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.StandardProtocolFamily;
import java.net.StandardSocketOptions;
import java.nio.channels.DatagramChannel;
import java.nio.channels.MembershipKey;
public class Test {
  public static void main(String[] args) throws Exception {
    NetworkInterface networkInterface = NetworkInterface.getByName("net1");
    DatagramChannel dc = DatagramChannel.open(StandardProtocolFamily.INET);
    dc.setOption(StandardSocketOptions.SO_REUSEADDR, true);
    dc.bind(new InetSocketAddress(8080));
    dc.setOption(StandardSocketOptions.IP_MULTICAST_IF, networkInterface);
    InetAddress group = InetAddress.getByName("180.90.4.12");
    MembershipKey key = dc.join(group, networkInterface);
  }
}
```
