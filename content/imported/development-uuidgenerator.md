---
title: UUID generator
nav: UUID generator
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1993
source: https://web.archive.org/web/20140829083649/http://www.java2s.com/Tutorial/Java/0120__Development/UUIDgenerator.htm
---
```java title=Example.java
/*
 * Copyright 2004,2005 The Apache Software Foundation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Random;
/**
 */
public class UUIDGenerator {
    private static String baseUUID = null;
    private static long incrementingValue = 0;
    private static Random myRand = null;
    /**
     * MD5 a random string with localhost/date etc will return 128 bits
     * construct a string of 18 characters from those bits.
     *
     * @return string
     */
    public static String getUUID() {
        if (baseUUID == null) {
            getInitialUUID();
        }
        long i = ++incrementingValue;
        if(i >= Long.MAX_VALUE || i < 0){
            incrementingValue = 0;
            i = 0;
        }
        return baseUUID + System.currentTimeMillis() + i;
    }
    protected static synchronized void getInitialUUID() {
        if (baseUUID != null) {
            return;
        }
        if (myRand == null) {
            myRand = new Random();
        }
        long rand = myRand.nextLong();
        String sid;
        try {
            sid = InetAddress.getLocalHost().toString();
        } catch (UnknownHostException e) {
            sid = Thread.currentThread().getName();
        }
        StringBuffer sb = new StringBuffer();
        sb.append(sid);
        sb.append(":");
        sb.append(Long.toString(rand));
        MessageDigest md5 = null;
        try {
            md5 = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            //todo have to be properly handled
        }
        md5.update(sb.toString().getBytes());
        byte[] array = md5.digest();
        StringBuffer sb2 = new StringBuffer();
        for (int j = 0; j < array.length; ++j) {
            int b = array[j] & 0xFF;
            sb2.append(Integer.toHexString(b));
        }
        int begin = myRand.nextInt();
        if (begin < 0) begin = begin * -1;
        begin = begin % 8;
        baseUUID = sb2.toString().substring(begin, begin + 18).toUpperCase();
    }
}
```

| 6.54.1. | Get a unique identifier Using java.rmi.dgc.VMID |
|---|---|
| 6.54.2. | Using java.util.UUID |
| 6.54.3. | Using java.util.concurrent.AtomicLong: A numerical id, start at zero and increment by one. |
| 6.54.4. | Create your own basic UUID |
| 6.54.5. | Random GUID |
| 6.54.6. | Session ID generator |
| 6.54.7. | Generates a UUID |
| 6.54.8. | ID generator |
| 6.54.9. | Generator for Globally unique Strings |
| 6.54.10. | Generates random UUIDs |
| 6.54.11. | UUID generator |
