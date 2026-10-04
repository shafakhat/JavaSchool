---
title: Java AlgorithmConstraints implement
nav: Java AlgorithmConstraints ...
description: publicboolean permits(Set<CryptoPrimitive> primitives, String algorithm, AlgorithmParameters parameters) {
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20210102121729/http://www.java2s.com/ref/java/java-algorithmconstraints-implement.html
---
- java.security
- java.security AlgorithmConstraints GuardedObject KeyPairGenerator KeyStore MessageDigest SecureRandom Security SignedObject

## Description

Java AlgorithmConstraints implement

```java title=Example.java
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.security.AlgorithmConstraints;
import java.security.AlgorithmParameters;
import java.security.CryptoPrimitive;
import java.security.Key;
import java.security.interfaces.RSAKey;
import java.util.Date;
import java.util.Set;

import javax.net.ssl.ExtendedSSLSession;
import javax.net.ssl.SSLParameters;
import javax.net.ssl.SSLServerSocket;
import javax.net.ssl.SSLServerSocketFactory;
import javax.net.ssl.SSLSession;
import javax.net.ssl.SSLSocket;

class SimpleConstraints implementsAlgorithmConstraints {
   publicboolean permits(Set<CryptoPrimitive> primitives, String algorithm, AlgorithmParameters parameters) {
      return permits(primitives, algorithm, null, parameters);
   }/*www.java2s.com*/publicboolean permits(Set<CryptoPrimitive> primitives, Key key) {
      return permits(primitives, null, key, null);
   }

   publicboolean permits(Set<CryptoPrimitive> primitives, String algorithm, Key key, AlgorithmParameters parameters) {
      if (algorithm == null)
         algorithm = key.getAlgorithm();

      if (algorithm.indexOf("RSA") == -1)
         return false;

      if (key != null) {
         RSAKey rsaKey = (RSAKey) key;
         int size = rsaKey.getModulus().bitLength();
         if (size < 2048)
            return false;
      }

      return true;
   }
}

//EchoServerpublicclass Main {

   publicstaticvoid main(String[] arstring) {
      try {
         SSLServerSocketFactory sslServerSocketFactory = (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
         SSLServerSocket sslServerSocket = (SSLServerSocket) sslServerSocketFactory.createServerSocket(9999);
         System.out.println("Waiting for a client ...");
         SSLSocket sslSocket = (SSLSocket) sslServerSocket.accept();

         SSLParameters parameters = sslSocket.getSSLParameters();
         parameters.setAlgorithmConstraints(new SimpleConstraints());

         AlgorithmConstraints constraints = parameters.getAlgorithmConstraints();
         System.out.println("Constraint: " + constraints);

         String endPoint = parameters.getEndpointIdentificationAlgorithm();
         System.out.println("End Point: " + endPoint);

         System.out.println("Local Supported Signature Algorithms");
         if (sslSocket.getSession() instanceofExtendedSSLSession) {
            ExtendedSSLSession extendedSSLSession = (ExtendedSSLSession) sslSocket.getSession();
            String alogrithms[] = extendedSSLSession.getLocalSupportedSignatureAlgorithms();
            for (String algorithm : alogrithms) {
               System.out.println("Algortihm: " + algorithm);
            }
         }

         System.out.println("Peer Supported Signature Algorithms");
         if (sslSocket.getSession() instanceofExtendedSSLSession) {
            String alogrithms[] = ((ExtendedSSLSession) sslSocket.getSession()).getPeerSupportedSignatureAlgorithms();
            for (String algorithm : alogrithms) {
               System.out.println("Algortihm: " + algorithm);
            }
         }

         InputStream inputstream = sslSocket.getInputStream();
         InputStreamReader inputstreamreader = newInputStreamReader(inputstream);
         BufferedReader bufferedreader = newBufferedReader(inputstreamreader);

         SSLSession session = sslSocket.getHandshakeSession();
         if (session != null) {
            System.out.println("Last accessed: " + newDate(session.getLastAccessedTime()));
         }

         String string = null;
         while ((string = bufferedreader.readLine()) != null) {
            System.out.println(string);
            System.out.flush();
         }
      } catch (Exception exception) {
         exception.printStackTrace();
      }
   }

}
```

PreviousNext

## Related

- Java UserPrincipal lookup user by name
- Java UserPrincipal set by FileOwnerAttributeView
- Java UserPrincipalLookupService look up user
- Java GuardedObject create and save
- Java GuardedObject read
