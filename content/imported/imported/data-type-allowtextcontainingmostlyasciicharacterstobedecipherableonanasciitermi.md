---
title: Allow text containing mostly ASCII characters to be decipherable on an ASCII terminal without decoding.
nav: Allow text containing most...
description: Allow text containing mostly ASCII characters to be decipherable on an ASCII terminal without decoding.
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/20091221014805/http://www.java2s.com:80/Code/Java/Data-Type/AllowtextcontainingmostlyASCIIcharacterstobedecipherableonanASCIIterminalwithoutdecoding.htm
---
Allow text containing mostly ASCII characters to be decipherable on an ASCII terminal without decoding.

```java title=Example.java
/*
 * Copyright 2001-2004 The Apache Software Foundation.
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
import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import java.util.BitSet;
/**
 * <p>
 * Similar to the Quoted-Printable content-transfer-encoding defined in <a
 * href="http://www.ietf.org/rfc/rfc1521.txt">RFC 1521</a> and designed to allow text containing mostly ASCII
 * characters to be decipherable on an ASCII terminal without decoding.
 * </p>
 *
 * <p>
 * <a href="http://www.ietf.org/rfc/rfc1522.txt">RFC 1522</a> describes techniques to allow the encoding of non-ASCII
 * text in various portions of a RFC 822 [2] message header, in a manner which is unlikely to confuse existing message
 * handling software.
 * </p>
 *
 * @see <a href="http://www.ietf.org/rfc/rfc1522.txt">MIME (Multipurpose Internet Mail Extensions) Part Two: Message
 *          Header Extensions for Non-ASCII Text</a>
 *
 * @author Apache Software Foundation
 * @since 1.3
 * @version $Id: QCodec.java,v 1.6 2004/05/24 00:24:32 ggregory Exp $
 */
public class QCodec extends RFC1522Codec {
    /**
     * The default charset used for string decoding and encoding.
     */
    private String charset = "UTF8";
    /**
     * BitSet of printable characters as defined in RFC 1522.
     */
    private static final BitSet PRINTABLE_CHARS = new BitSet(256);
    // Static initializer for printable chars collection
    static {
        // alpha characters
        PRINTABLE_CHARS.set(' ');
        PRINTABLE_CHARS.set('!');
        PRINTABLE_CHARS.set('"');
        PRINTABLE_CHARS.set('#');
        PRINTABLE_CHARS.set('$');
        PRINTABLE_CHARS.set('%');
        PRINTABLE_CHARS.set('&');
        PRINTABLE_CHARS.set('\'');
        PRINTABLE_CHARS.set('(');
        PRINTABLE_CHARS.set(')');
        PRINTABLE_CHARS.set('*');
        PRINTABLE_CHARS.set('+');
        PRINTABLE_CHARS.set(',');
        PRINTABLE_CHARS.set('-');
        PRINTABLE_CHARS.set('.');
        PRINTABLE_CHARS.set('/');
        for (int i = '0'; i <= '9'; i++) {
            PRINTABLE_CHARS.set(i);
        }
        PRINTABLE_CHARS.set(':');
        PRINTABLE_CHARS.set(';');
        PRINTABLE_CHARS.set('<');
        PRINTABLE_CHARS.set('>');
        PRINTABLE_CHARS.set('@');
        for (int i = 'A'; i <= 'Z'; i++) {
            PRINTABLE_CHARS.set(i);
        }
        PRINTABLE_CHARS.set('[');
        PRINTABLE_CHARS.set('\\');
        PRINTABLE_CHARS.set(']');
        PRINTABLE_CHARS.set('^');
        PRINTABLE_CHARS.set('`');
        for (int i = 'a'; i <= 'z'; i++) {
            PRINTABLE_CHARS.set(i);
        }
        PRINTABLE_CHARS.set('{');
        PRINTABLE_CHARS.set('|');
        PRINTABLE_CHARS.set('}');
        PRINTABLE_CHARS.set('~');
    }
    private static byte BLANK = 32;
    private static byte UNDERSCORE = 95;
    private boolean encodeBlanks = false;
    /**
     * Default constructor.
     */
    public QCodec() {
        super();
    }
    /**
     * Constructor which allows for the selection of a default charset
     *
     * @param charset
     *                  the default string charset to use.
     *
     * @see <a href="http://java.sun.com/j2se/1.3/docs/api/java/lang/package-summary.html#charenc">JRE character
     *          encoding names</a>
     */
    public QCodec(final String charset) {
        super();
        this.charset = charset;
    }
    protected String getEncoding() {
        return "Q";
    }
    protected byte[] doEncoding(byte[] bytes) throws RuntimeException {
        if (bytes == null) {
            return null;
        }
        byte[] data = QuotedPrintableCodec.encodeQuotedPrintable(PRINTABLE_CHARS, bytes);
        if (this.encodeBlanks) {
            for (int i = 0; i < data.length; i++) {
                if (data[i] == BLANK) {
                    data[i] = UNDERSCORE;
                }
            }
        }
        return data;
    }
    protected byte[] doDecoding(byte[] bytes) throws Exception {
        if (bytes == null) {
            return null;
        }
        boolean hasUnderscores = false;
        for (int i = 0; i < bytes.length; i++) {
            if (bytes[i] == UNDERSCORE) {
                hasUnderscores = true;
                break;
            }
        }
        if (hasUnderscores) {
            byte[] tmp = new byte[bytes.length];
            for (int i = 0; i < bytes.length; i++) {
                byte b = bytes[i];
                if (b != UNDERSCORE) {
                    tmp[i] = b;
                } else {
                    tmp[i] = BLANK;
                }
            }
            return QuotedPrintableCodec.decodeQuotedPrintable(tmp);
        }
        return QuotedPrintableCodec.decodeQuotedPrintable(bytes);
    }
    /**
     * Encodes a string into its quoted-printable form using the specified charset. Unsafe characters are escaped.
     *
     * @param pString
     *                  string to convert to quoted-printable form
     * @param charset
     *                  the charset for pString
     * @return quoted-printable string
     *
     * @throws EncoderException
     *                  thrown if a failure condition is encountered during the encoding process.
     */
    public String encode(final String pString, final String charset) throws Exception {
        if (pString == null) {
            return null;
        }
        try {
            return encodeText(pString, charset);
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e.getMessage());
        }
    }
    /**
     * Encodes a string into its quoted-printable form using the default charset. Unsafe characters are escaped.
     *
     * @param pString
     *                  string to convert to quoted-printable form
     * @return quoted-printable string
     *
     * @throws EncoderException
     *                  thrown if a failure condition is encountered during the encoding process.
     */
    public String encode(String pString) throws Exception {
        if (pString == null) {
            return null;
        }
        return encode(pString, getDefaultCharset());
    }
    /**
     * Decodes a quoted-printable string into its original form. Escaped characters are converted back to their original
     * representation.
     *
     * @param pString
     *                  quoted-printable string to convert into its original form
     *
     * @return original string
     *
     * @throws DecoderException
     *                  A decoder exception is thrown if a failure condition is encountered during the decode process.
     */
    public String decode(String pString) throws Exception {
        if (pString == null) {
            return null;
        }
        try {
            return decodeText(pString);
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e.getMessage());
        }
    }
    /**
     * Encodes an object into its quoted-printable form using the default charset. Unsafe characters are escaped.
     *
     * @param pObject
     *                  object to convert to quoted-printable form
     * @return quoted-printable object
     *
     * @throws EncoderException
     *                  thrown if a failure condition is encountered during the encoding process.
     */
    public Object encode(Object pObject) throws Exception {
        if (pObject == null) {
            return null;
        } else if (pObject instanceof String) {
            return encode((String) pObject);
        } else {
            throw new RuntimeException("Objects of type "
                + pObject.getClass().getName()
                + " cannot be encoded using Q codec");
        }
    }
    /**
     * Decodes a quoted-printable object into its original form. Escaped characters are converted back to their original
     * representation.
     *
     * @param pObject
     *                  quoted-printable object to convert into its original form
     *
     * @return original object
     *
     * @throws DecoderException
     *                  A decoder exception is thrown if a failure condition is encountered during the decode process.
     */
    public Object decode(Object pObject) throws Exception {
        if (pObject == null) {
            return null;
        } else if (pObject instanceof String) {
            return decode((String) pObject);
        } else {
            throw new RuntimeException("Objects of type "
                + pObject.getClass().getName()
                + " cannot be decoded using Q codec");
        }
    }
    /**
     * The default charset used for string decoding and encoding.
     *
     * @return the default string charset.
     */
    public String getDefaultCharset() {
        return this.charset;
    }
    /**
     * Tests if optional tranformation of SPACE characters is to be used
     *
     * @return <code>true</code> if SPACE characters are to be transformed, <code>false</code> otherwise
     */
    public boolean isEncodeBlanks() {
        return this.encodeBlanks;
    }
    /**
     * Defines whether optional tranformation of SPACE characters is to be used
     *
     * @param b
     *                  <code>true</code> if SPACE characters are to be transformed, <code>false</code> otherwise
     */
    public void setEncodeBlanks(boolean b) {
        this.encodeBlanks = b;
    }
}
/*
 * Copyright 2001-2004 The Apache Software Foundation.
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
/**
 * <p>
 * Implements methods common to all codecs defined in RFC 1522.
 * </p>
 *
 * <p>
 * <a href="http://www.ietf.org/rfc/rfc1522.txt">RFC 1522</a>
 * describes techniques to allow the encoding of non-ASCII text in
 * various portions of a RFC 822 [2] message header, in a manner which
 * is unlikely to confuse existing message handling software.
 * </p>
 * @see <a href="http://www.ietf.org/rfc/rfc1522.txt">
 * MIME (Multipurpose Internet Mail Extensions) Part Two:
 * Message Header Extensions for Non-ASCII Text</a>
 * </p>
 *
 * @author Apache Software Foundation
 * @since 1.3
 * @version $Id: RFC1522Codec.java,v 1.2 2004/04/09 22:21:43 ggregory Exp $
 */
abstract class RFC1522Codec {
    /**
     * Applies an RFC 1522 compliant encoding scheme to the given string of text with the
     * given charset. This method constructs the "encoded-word" header common to all the
     * RFC 1522 codecs and then invokes {@link #doEncoding(byte [])} method of a concrete
     * class to perform the specific enconding.
     *
     * @param text a string to encode
     * @param charset a charset to be used
     *
     * @return RFC 1522 compliant "encoded-word"
     *
     * @throws EncoderException thrown if there is an error conidition during the Encoding
     *  process.
     * @throws UnsupportedEncodingException thrown if charset is not supported
     *
     * @see <a href="http://java.sun.com/j2se/1.3/docs/api/java/lang/package-summary.html#charenc">JRE character
     *          encoding names</a>
     */
    protected String encodeText(final String text, final String charset)
     throws Exception, UnsupportedEncodingException
    {
        if (text == null) {
            return null;
        }
        StringBuffer buffer = new StringBuffer();
        buffer.append("=?");
        buffer.append(charset);
        buffer.append('?');
        buffer.append(getEncoding());
        buffer.append('?');
        byte [] rawdata = doEncoding(text.getBytes(charset));
        buffer.append(new String(rawdata, "US-ASCII"));
        buffer.append("?=");
        return buffer.toString();
    }
    /**
     * Applies an RFC 1522 compliant decoding scheme to the given string of text. This method
     * processes the "encoded-word" header common to all the RFC 1522 codecs and then invokes
     * {@link #doEncoding(byte [])} method of a concrete class to perform the specific deconding.
     *
     * @param text a string to decode
     *
     * @throws DecoderException thrown if there is an error conidition during the Decoding
     *  process.
     * @throws UnsupportedEncodingException thrown if charset specified in the "encoded-word"
     *  header is not supported
     */
    protected String decodeText(final String text)
     throws Exception, UnsupportedEncodingException
    {
        if (text == null) {
            return null;
        }
        if ((!text.startsWith("=?")) || (!text.endsWith("?="))) {
            throw new RuntimeException("RFC 1522 violation: malformed encoded content");
        }
        int termnator = text.length() - 2;
        int from = 2;
        int to = text.indexOf("?", from);
        if ((to == -1) || (to == termnator)) {
            throw new RuntimeException("RFC 1522 violation: charset token not found");
        }
        String charset = text.substring(from, to);
        if (charset.equals("")) {
            throw new RuntimeException("RFC 1522 violation: charset not specified");
        }
        from = to + 1;
        to = text.indexOf("?", from);
        if ((to == -1) || (to == termnator)) {
            throw new RuntimeException("RFC 1522 violation: encoding token not found");
        }
        String encoding = text.substring(from, to);
        if (!getEncoding().equalsIgnoreCase(encoding)) {
            throw new RuntimeException("This codec cannot decode " +
                encoding + " encoded content");
        }
        from = to + 1;
        to = text.indexOf("?", from);
        byte[] data = text.substring(from, to).getBytes("US-ASCII");
        data = doDecoding(data);
        return new String(data, charset);
    }
    /**
     * Returns the codec name (referred to as encoding in the RFC 1522)
     *
     * @return name of the codec
     */
    protected abstract String getEncoding();
    /**
     * Encodes an array of bytes using the defined encoding scheme
     *
     * @param bytes Data to be encoded
     *
     * @return A byte array containing the encoded data
     *
     * @throws EncoderException thrown if the Encoder encounters a failure condition
     *  during the encoding process.
     */
    protected abstract byte[] doEncoding(byte[] bytes) throws Exception;
    /**
     * Decodes an array of bytes using the defined encoding scheme
     *
     * @param bytes Data to be decoded
     *
     * @return a byte array that contains decoded data
     *
     * @throws DecoderException A decoder exception is thrown if a Decoder encounters a
     *  failure condition during the decode process.
     */
    protected abstract byte[] doDecoding(byte[] bytes) throws Exception;
}
class QuotedPrintableCodec {
  /**
   * The default charset used for string decoding and encoding.
   */
  private String charset = "UTF8";
  /**
   * BitSet of printable characters as defined in RFC 1521.
   */
  private static final BitSet PRINTABLE_CHARS = new BitSet(256);
  private static byte ESCAPE_CHAR = '=';
  private static byte TAB = 9;
  private static byte SPACE = 32;
  // Static initializer for printable chars collection
  static {
      // alpha characters
      for (int i = 33; i <= 60; i++) {
          PRINTABLE_CHARS.set(i);
      }
      for (int i = 62; i <= 126; i++) {
          PRINTABLE_CHARS.set(i);
      }
      PRINTABLE_CHARS.set(TAB);
      PRINTABLE_CHARS.set(SPACE);
  }
  /**
   * Default constructor.
   */
  public QuotedPrintableCodec() {
      super();
  }
  /**
   * Constructor which allows for the selection of a default charset
   *
   * @param charset
   *                  the default string charset to use.
   */
  public QuotedPrintableCodec(String charset) {
      super();
      this.charset = charset;
  }
  /**
   * Encodes byte into its quoted-printable representation.
   *
   * @param b
   *                  byte to encode
   * @param buffer
   *                  the buffer to write to
   */
  private static final void encodeQuotedPrintable(int b, ByteArrayOutputStream buffer) {
      buffer.write(ESCAPE_CHAR);
      char hex1 = Character.toUpperCase(Character.forDigit((b >> 4) & 0xF, 16));
      char hex2 = Character.toUpperCase(Character.forDigit(b & 0xF, 16));
      buffer.write(hex1);
      buffer.write(hex2);
  }
  /**
   * Encodes an array of bytes into an array of quoted-printable 7-bit characters. Unsafe characters are escaped.
   *
   * <p>
   * This function implements a subset of quoted-printable encoding specification (rule #1 and rule #2) as defined in
   * RFC 1521 and is suitable for encoding binary data and unformatted text.
   * </p>
   *
   * @param printable
   *                  bitset of characters deemed quoted-printable
   * @param bytes
   *                  array of bytes to be encoded
   * @return array of bytes containing quoted-printable data
   */
  public static final byte[] encodeQuotedPrintable(BitSet printable, byte[] bytes) {
      if (bytes == null) {
          return null;
      }
      if (printable == null) {
          printable = PRINTABLE_CHARS;
      }
      ByteArrayOutputStream buffer = new ByteArrayOutputStream();
      for (int i = 0; i < bytes.length; i++) {
          int b = bytes[i];
          if (b < 0) {
              b = 256 + b;
          }
          if (printable.get(b)) {
              buffer.write(b);
          } else {
              encodeQuotedPrintable(b, buffer);
          }
      }
      return buffer.toByteArray();
  }
  /**
   * Decodes an array quoted-printable characters into an array of original bytes. Escaped characters are converted
   * back to their original representation.
   *
   * <p>
   * This function implements a subset of quoted-printable encoding specification (rule #1 and rule #2) as defined in
   * RFC 1521.
   * </p>
   *
   * @param bytes
   *                  array of quoted-printable characters
   * @return array of original bytes
   * @throws DecoderException
   *                  Thrown if quoted-printable decoding is unsuccessful
   */
  public static final byte[] decodeQuotedPrintable(byte[] bytes) throws Exception {
      if (bytes == null) {
          return null;
      }
      ByteArrayOutputStream buffer = new ByteArrayOutputStream();
      for (int i = 0; i < bytes.length; i++) {
          int b = bytes[i];
          if (b == ESCAPE_CHAR) {
              try {
                  int u = Character.digit((char) bytes[++i], 16);
                  int l = Character.digit((char) bytes[++i], 16);
                  if (u == -1 || l == -1) {
                      throw new RuntimeException("Invalid quoted-printable encoding");
                  }
                  buffer.write((char) ((u << 4) + l));
              } catch (ArrayIndexOutOfBoundsException e) {
                  throw new RuntimeException("Invalid quoted-printable encoding");
              }
          } else {
              buffer.write(b);
          }
      }
      return buffer.toByteArray();
  }
  /**
   * Encodes an array of bytes into an array of quoted-printable 7-bit characters. Unsafe characters are escaped.
   *
   * <p>
   * This function implements a subset of quoted-printable encoding specification (rule #1 and rule #2) as defined in
   * RFC 1521 and is suitable for encoding binary data and unformatted text.
   * </p>
   *
   * @param bytes
   *                  array of bytes to be encoded
   * @return array of bytes containing quoted-printable data
   */
  public byte[] encode(byte[] bytes) {
      return encodeQuotedPrintable(PRINTABLE_CHARS, bytes);
  }
  /**
   * Decodes an array of quoted-printable characters into an array of original bytes. Escaped characters are converted
   * back to their original representation.
   *
   * <p>
   * This function implements a subset of quoted-printable encoding specification (rule #1 and rule #2) as defined in
   * RFC 1521.
   * </p>
   *
   * @param bytes
   *                  array of quoted-printable characters
   * @return array of original bytes
   * @throws DecoderException
   *                  Thrown if quoted-printable decoding is unsuccessful
   */
  public byte[] decode(byte[] bytes) throws Exception {
      return decodeQuotedPrintable(bytes);
  }
  /**
   * Encodes a string into its quoted-printable form using the default string charset. Unsafe characters are escaped.
   *
   * <p>
   * This function implements a subset of quoted-printable encoding specification (rule #1 and rule #2) as defined in
   * RFC 1521 and is suitable for encoding binary data.
   * </p>
   *
   * @param pString
   *                  string to convert to quoted-printable form
   * @return quoted-printable string
   *
   * @throws EncoderException
   *                  Thrown if quoted-printable encoding is unsuccessful
   *
   * @see #getDefaultCharset()
   */
  public String encode(String pString) throws Exception {
      if (pString == null) {
          return null;
      }
      try {
          return encode(pString, getDefaultCharset());
      } catch (UnsupportedEncodingException e) {
          throw new RuntimeException(e.getMessage());
      }
  }
  /**
   * Decodes a quoted-printable string into its original form using the specified string charset. Escaped characters
   * are converted back to their original representation.
   *
   * @param pString
   *                  quoted-printable string to convert into its original form
   * @param charset
   *                  the original string charset
   * @return original string
   * @throws DecoderException
   *                  Thrown if quoted-printable decoding is unsuccessful
   * @throws UnsupportedEncodingException
   *                  Thrown if charset is not supported
   */
  public String decode(String pString, String charset) throws Exception, UnsupportedEncodingException {
      if (pString == null) {
          return null;
      }
      return new String(decode(pString.getBytes("US-ASCII")), charset);
  }
  /**
   * Decodes a quoted-printable string into its original form using the default string charset. Escaped characters are
   * converted back to their original representation.
   *
   * @param pString
   *                  quoted-printable string to convert into its original form
   * @return original string
   * @throws DecoderException
   *                  Thrown if quoted-printable decoding is unsuccessful
   * @throws UnsupportedEncodingException
   *                  Thrown if charset is not supported
   * @see #getDefaultCharset()
   */
  public String decode(String pString) throws Exception {
      if (pString == null) {
          return null;
      }
      try {
          return decode(pString, getDefaultCharset());
      } catch (UnsupportedEncodingException e) {
          throw new RuntimeException(e.getMessage());
      }
  }
  /**
   * Encodes an object into its quoted-printable safe form. Unsafe characters are escaped.
   *
   * @param pObject
   *                  string to convert to a quoted-printable form
   * @return quoted-printable object
   * @throws EncoderException
   *                  Thrown if quoted-printable encoding is not applicable to objects of this type or if encoding is
   *                  unsuccessful
   */
  public Object encode(Object pObject) throws Exception {
      if (pObject == null) {
          return null;
      } else if (pObject instanceof byte[]) {
          return encode((byte[]) pObject);
      } else if (pObject instanceof String) {
          return encode((String) pObject);
      } else {
          throw new RuntimeException("Objects of type "
              + pObject.getClass().getName()
              + " cannot be quoted-printable encoded");
      }
  }
  /**
   * Decodes a quoted-printable object into its original form. Escaped characters are converted back to their original
   * representation.
   *
   * @param pObject
   *                  quoted-printable object to convert into its original form
   * @return original object
   * @throws DecoderException
   *                  Thrown if quoted-printable decoding is not applicable to objects of this type if decoding is
   *                  unsuccessful
   */
  public Object decode(Object pObject) throws Exception {
      if (pObject == null) {
          return null;
      } else if (pObject instanceof byte[]) {
          return decode((byte[]) pObject);
      } else if (pObject instanceof String) {
          return decode((String) pObject);
      } else {
          throw new RuntimeException("Objects of type "
              + pObject.getClass().getName()
              + " cannot be quoted-printable decoded");
      }
  }
  /**
   * Returns the default charset used for string decoding and encoding.
   *
   * @return the default string charset.
   */
  public String getDefaultCharset() {
      return this.charset;
  }
  /**
   * Encodes a string into its quoted-printable form using the specified charset. Unsafe characters are escaped.
   *
   * <p>
   * This function implements a subset of quoted-printable encoding specification (rule #1 and rule #2) as defined in
   * RFC 1521 and is suitable for encoding binary data and unformatted text.
   * </p>
   *
   * @param pString
   *                  string to convert to quoted-printable form
   * @param charset
   *                  the charset for pString
   * @return quoted-printable string
   *
   * @throws UnsupportedEncodingException
   *                  Thrown if the charset is not supported
   */
  public String encode(String pString, String charset) throws UnsupportedEncodingException {
      if (pString == null) {
          return null;
      }
      return new String(encode(pString.getBytes(charset)), "US-ASCII");
  }
}
```

1.  Checks whether the character is ASCII 7 bit.
2.  Checks whether the character is ASCII 7 bit printable.
3.  Checks whether the character is ASCII 7 bit control.
4.  Checks whether the character is ASCII 7 bit alphabetic.
5.  Checks whether the character is ASCII 7 bit alphabetic upper case.
6.  Checks whether the character is ASCII 7 bit alphabetic lower case.
7.  Checks whether the character is ASCII 7 bit numeric.
8.  Checks whether the character is ASCII 7 bit numeric and character.
9.  Removes control characters (char < = 32) from both ends returning null if the String is empty ("") after the trim or if it is null
10.  Removes control characters (char < = 32) from both ends returning an empty String ("") if the String is empty ("") after the trim or if it is null.
11.  Get 7-bit ASCII character array from input String.
12.  Test if the character is a digit <digit> ::= '0'  '1'  '2'  '3'  '4'  '5'  '6'  '7'  '8'  '9'
13.  Test if the current character is a digit <digit> ::= '0'  '1'  '2'  '3'  '4'  '5'  '6'  '7'  '8'  '9'
14.  Test if the current character is a new line.
15.  Test if the current character is a space.
16.  Test if the current character is an Alpha character : <alpha> ::= [0x41-0x5A]  [0x61-0x7A]
17.  Test if the current character is an Ident character
18.  Test if the current character is equal to a specific character.
19.  Test if the current string is a digit <digit> ::= '0'  '1'  '2'  '3'  '4'  '5'  '6'  '7'  '8'  '9'
20.  Removes spaces (char <= 32) from both start and ends of this bytes array
21.  Removes spaces (char <= 32) from end of this String with escape, handling null by returning null
22.  Removes spaces (char <= 32) from end of this String, handling null by returning null
23.  Removes spaces (char <= 32) from end of this array by index, handling null by returning null
24.  Removes spaces (char <= 32) from end of this array ny position, handling null by returning null
25.  Removes spaces (char <= 32) from end of this array, handling null by returning null
26.  Removes spaces (char <= 32) from start of this String, handling null by returning null
27.  Removes spaces (char <= 32) from start of this array, handling null by returning null
28.  Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127].
