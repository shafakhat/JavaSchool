---
title: Get socket option
nav: Get socket option
description: Set<SocketOption<?>> socketOptions = socketChannel.supportedOptions();
section: Imported - java2s Archive
order: 1067
source: https://web.archive.org/web/20130821123800/http://java2s.com/Code/Java/JDK-7/Getsocketoption.htm
---
Get socket option

```java title=Example.java
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.net.SocketOption;
import java.net.StandardSocketOptions;
import java.nio.channels.NetworkChannel;
import java.nio.channels.spi.SelectorProvider;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    SelectorProvider provider = SelectorProvider.provider();
    NetworkChannel socketChannel = provider.openSocketChannel();
    SocketAddress address = new InetSocketAddress(3080);
    socketChannel = socketChannel.bind(address);
    Set<SocketOption<?>> socketOptions = socketChannel.supportedOptions();
    System.out.println(socketOptions.toString());
    socketChannel.setOption(StandardSocketOptions.IP_TOS, 3);
    Boolean keepAlive = socketChannel
        .getOption(StandardSocketOptions.SO_KEEPALIVE);
  }
}
```
