---
title: Safe UTF
nav: Safe UTF
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1754
source: https://web.archive.org/web/20140811063435/http://www.java2s.com/Tutorial/Java/0120__Development/SafeUTF64Kserializedsize.htm
---
```java title=Example.java
/*
  * JBoss, Home of Professional Open Source
  * Copyright 2005, JBoss Inc., and individual contributors as indicated
  * by the @authors tag. See the copyright.txt in the distribution for a
  * full listing of individual contributors.
  *
  * This is free software; you can redistribute it and/or modify it
  * under the terms of the GNU Lesser General Public License as
  * published by the Free Software Foundation; either version 2.1 of
  * the License, or (at your option) any later version.
  *
  * This software is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  * Lesser General Public License for more details.
  *
  * You should have received a copy of the GNU Lesser General Public
  * License along with this software; if not, write to the Free
  * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
  * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
  */
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
/**
 *
 * A SafeUTF
 *
 * @author <a href="tim.fox@jboss.com">Tim Fox</a>
 * @author <a href="mailto:adrian@jboss.org">Adrian Brock</a>
 * @version $Revision: 1174 $
 *
 * $Id: SafeUTF.java 1174 2006-08-02 14:14:32Z timfox $
 *
 * There is a "bug" in JDK1.4 / 1.5 DataOutputStream.writeUTF()
 * which means it does not work with Strings >= 64K serialized size.
 * See http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4806007
 *
 * We work around this by chunking larger strings into smaller pieces.
 *
 * Note we only support TextMessage and ObjectMessage bodies with serialized length >= 64K
 * We DO NOT support Strings written to BytesMessages or StreamMessages or written as keys or values
 * in MapMessages, or as String properties or other String fields having serialized length >= 64K
 * This is for performance reasons since there is an overhead in coping with large
 * Strings
 *
 */
public class SafeUTF
{
   //Default is 16K chunks
   private static final int CHUNK_SIZE = 16 * 1024;
   private static final byte NULL = 0;
   private static final byte NOT_NULL = 1;
   public static SafeUTF instance = new SafeUTF(CHUNK_SIZE);
   private int chunkSize;
   private int lastReadBufferSize;
   public int getLastReadBufferSize()
   {
      return lastReadBufferSize;
   }
   public SafeUTF(int chunkSize)
   {
      this.chunkSize = chunkSize;
   }
   public void safeWriteUTF(DataOutputStream out, String str) throws IOException
   {
      if (str == null)
      {
         out.writeByte(NULL);
      }
      else
      {
         int len = str.length();
         short numChunks;
         if (len == 0)
         {
            numChunks = 0;
         }
         else
         {
            numChunks = (short)(((len - 1) / chunkSize) + 1);
         }
         out.writeByte(NOT_NULL);
         out.writeShort(numChunks);
         int i = 0;
         while (len > 0)
         {
            int beginCopy = i * chunkSize;
            int endCopy = len <= chunkSize ? beginCopy + len : beginCopy + chunkSize;
            String theChunk = str.substring(beginCopy, endCopy);
            out.writeUTF(theChunk);
            len -= chunkSize;
            i++;
         }
      }
   }
   public String safeReadUTF(DataInputStream in) throws IOException
   {
      boolean isNull = in.readByte() == NULL;
      if (isNull)
      {
         return null;
      }
      short numChunks = in.readShort();
      int bufferSize = chunkSize * numChunks;
      // special handling for single chunk
      if (numChunks == 1)
      {
         // The text size is likely to be much smaller than the chunkSize
         // so set bufferSize to the min of the input stream available
         // and the maximum buffer size. Since the input stream
         // available() can be <= 0 we check for that and default to
         // a small msg size of 256 bytes.
         int inSize = in.available();
         if (inSize <= 0)
         {
            inSize = 256;
         }
         bufferSize = Math.min(inSize, bufferSize);
         lastReadBufferSize = bufferSize;
      }
      StringBuffer buff = new StringBuffer(bufferSize);
      for (int i = 0; i < numChunks; i++)
      {
         String s = in.readUTF();
         buff.append(s);
      }
      return buff.toString();
   }
}
```

| 6.16.1. | Using Unicode in String |
|---|---|
| 6.16.2. | Display special character using Unicode |
| 6.16.3. | Convert from Unicode to UTF-8 |
| 6.16.4. | Convert from UTF-8 to Unicode |
| 6.16.5. | Convert string to UTF8 bytes |
| 6.16.6. | Converts Unicode into something that can be embedded in a java properties file |
| 6.16.7. | Converts the string to the unicode format |
| 6.16.8. | Return an UTF-8 encoded String |
| 6.16.9. | Return an UTF-8 encoded String by length |
| 6.16.10. | Return UTF-8 encoded byte[] representation of a String |
| 6.16.11. | Get UTF String Size |
| 6.16.12. | Return the number of bytes that hold an Unicode char. |
| 6.16.13. | Return the Unicode char which is coded in the bytes at position 0. |
| 6.16.14. | Return the Unicode char which is coded in the bytes at the given position. |
| 6.16.15. | Checks if the String contains only unicode digits or space |
| 6.16.16. | Checks if the String contains only unicode digits. A decimal point is not a unicode digit and returns false. |
| 6.16.17. | Checks if the String contains only unicode letters and space (' '). |
| 6.16.18. | Checks if the String contains only unicode letters or digits. |
| 6.16.19. | Checks if the String contains only unicode letters, digits or space (' '). |
| 6.16.20. | Checks if the String contains only unicode letters. |
| 6.16.21. | Count the number of bytes included in the given char[]. |
| 6.16.22. | Count the number of bytes needed to return an Unicode char. This can be from 1 to 6. |
| 6.16.23. | Count the number of chars included in the given byte[]. |
| 6.16.24. | Decodes values of attributes in the DN encoded in hex into a UTF-8 String. |
| 6.16.25. | Safe UTF: 64K serialized size |
