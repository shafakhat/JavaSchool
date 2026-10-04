---
title: Java Network Tutorial - IP addresses
nav: Java Network Tutorial - IP...
description: The host argument refers to a computer name or an IP address. The addr argument refers to the parts of an IP address as a byte array.
section: Imported - java2s Archive
order: 50046
source: https://www.java2s.com/Tutorials/Java/Java_Network/index.html
---
Internet protocol uses the IP addresses to deliver packets.

We can use Java InetAddress class to work with IP address.

The following are the methods from InetAddress class.

```java title=Example.java
static InetAddress[] getAllByName(String host)
static InetAddress getByAddress(byte[] addr)
static InetAddress getByAddress(String host, byte[] addr)
static InetAddress getByName(String host)
static InetAddress getLocalHost()
static InetAddress getLoopbackAddress()
```

The host argument refers to a computer name or an IP address. The addr argument refers to the parts of an IP address as a byte array.

If you specify an IPv4 address, addr must be a 4-element byte array.

For IPv6 addresses, it should be a 16-element byte array.

The InetAddress class can resolve the host name to an IP address using DNS.

For a host with multiple IP addresses.

The getAllByName() method returns all addresses as an array of InetAddress objects.

## Example

The following code shows how to create InetAddress.

```java title=Example.java
import java.net.InetAddress;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    // Print www.yahoo.com address details
    printAddressDetails("www.yahoo.com");
    // Print the loopback address details
    printAddressDetails(null);
    // Print the loopback address details using IPv6 format
    printAddressDetails("::1");
  }
  publicstaticvoid printAddressDetails(String host) throws Exception {
    System.out.println("Host '" + host + "' details starts...");
    InetAddress addr = InetAddress.getByName(host);
    System.out.println("Host  IP  Address: " + addr.getHostAddress());
    System.out.println("Canonical  Host  Name: "
        + addr.getCanonicalHostName());
    int timeOutinMillis = 10000;
    System.out.println("isReachable(): "
        + addr.isReachable(timeOutinMillis));
    System.out.println("isLoopbackAddress(): " + addr.isLoopbackAddress());
  }
}
```

The code above generates the following result.

## Socket Address

A socket address has two parts, an IP address and a port number.

InetSocketAddress represents a socket address.

We can use the following constructors to create an object of the InetSocketAddress class:

```java title=Example.java

InetSocketAddress(InetAddress addr,  int port)
InetSocketAddress(int port)
InetSocketAddress(String hostname, int port)
```

If a host name could not be resolved, the socket address will be unresolved, which can be checked using the isUnresolved() method.

To not resolve the address when creating its object, use the following factory method to create the socket address:

```java title=Example.java
static InetSocketAddress createUnresolved(String  host,  int  port)
```

The getAddress() method returns an InetAddress object.

If a host name is not resolved, the getAddress() method returns null.

The following code shows how to create resolved and unresolved InetSocketAddress objects.

```java title=Example.java
import java.net.InetSocketAddress;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    InetSocketAddress addr1 = new InetSocketAddress("::1", 12345);
    printSocketAddress(addr1);
    InetSocketAddress addr2 = InetSocketAddress.createUnresolved("::1",
        12881);
    printSocketAddress(addr2);
  }
  publicstaticvoid printSocketAddress(InetSocketAddress sAddr) {
    System.out.println("Socket  Address: " + sAddr.getAddress());
    System.out.println("Socket Host  Name: " + sAddr.getHostName());
    System.out.println("Socket Port:  " + sAddr.getPort());
    System.out.println("isUnresolved(): " + sAddr.isUnresolved());
    System.out.println();
  }
}
```

The code above generates the following result.
