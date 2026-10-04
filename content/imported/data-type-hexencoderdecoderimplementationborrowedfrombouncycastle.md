---
title: Hex encoder/decoder implementation borrowed from BouncyCastle
nav: Hex encoder/decoder implem...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1185
source: https://web.archive.org/web/20140829091447/http://www.java2s.com/Tutorial/Java/0040__Data-Type/HexencoderdecoderimplementationborrowedfromBouncyCastle.htm
---
```java title=Example.java
/*
 * Copyright 2007 Werner Guttmann
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.IOException;
import java.io.OutputStream;
import java.io.ByteArrayOutputStream;
/**
 *
 * @author Johan Lindquist
 * @since 1.1.1
 * @version $Revision$
 */
public final class HexDecoder {
    /**
     * Identifies the data type supported by this decoder.
     */
    public static final String DATA_TYPE = "hexBinary";
    /**
     * Initial size of the decoding table.
     */
    private static final int DECODING_TABLE_SIZE = 128;
    /**
     * Encoding table.
     */
    protected static final byte[] ENCODING_TABLE = {
        (byte) '0', (byte) '1', (byte) '2', (byte) '3',
        (byte) '4', (byte) '5', (byte) '6', (byte) '7',
        (byte) '8', (byte) '9', (byte) 'A', (byte) 'B',
        (byte) 'C', (byte) 'D', (byte) 'E', (byte) 'F'
    };
    /**
     * Decoding table.
     */
    protected static final byte[] DECODING_TABLE = new byte[DECODING_TABLE_SIZE];
    /**
     * Initialize the decoding table.
     */
    protected static void initialiseDecodingTable() {
        for (int i = 0; i < ENCODING_TABLE.length; i++) {
            DECODING_TABLE[ENCODING_TABLE[i]] = (byte) i;
        }
        // deal with lower case letters as well
        DECODING_TABLE['a'] = DECODING_TABLE['A'];
        DECODING_TABLE['b'] = DECODING_TABLE['B'];
        DECODING_TABLE['c'] = DECODING_TABLE['C'];
        DECODING_TABLE['d'] = DECODING_TABLE['D'];
        DECODING_TABLE['e'] = DECODING_TABLE['E'];
        DECODING_TABLE['f'] = DECODING_TABLE['F'];
    }
    static {
        initialiseDecodingTable();
    }
    /**
     * Creates an instance of this class.
     */
    private HexDecoder() {
        // Nothing to do ...
    }
    /**
     * Encodes the input data producing a Hex output stream.
     * @param data The input data to be HEX encoded
     * @param off Initiak offset
     * @param length Initial length of the input data array
     * @param out The {@link OutputStream} instance holding the encoded input data.
     * @return the number of bytes produced.
     * @throws IOException If encoding fails.
     */
    public static int encode(final byte[] data, final int off, final int length,
            final OutputStream out) throws IOException {
        for (int i = off; i < (off + length); i++) {
            int v = data[i] & 0xff;
            out.write(ENCODING_TABLE[(v >>> 4)]);
            out.write(ENCODING_TABLE[v & 0xf]);
        }
        return length * 2;
    }
    /**
     * Indicates whether a given character should be ignored during en-/decoding.
     * @param c The character at question.
     * @return True if the given character should be ignored.
     */
    private static boolean ignore(final char c) {
        return (c == '\n' || c == '\r' || c == '\t' || c == ' ');
    }
    /**
     * Decodes the Hex encoded byte data writing it to the given output stream,
     * whitespace characters will be ignored.
     * @param data The data to be encoded
     * @param off Initial offset.
     * @param length Initial length
     * @param out The {@link OutputStream} instance
     * @return the number of bytes produced.
     * @throws IOException If encoding failed.
     */
    public static int decode(final byte[] data, final int off, final int length,
            final OutputStream out) throws IOException {
        byte b1, b2;
        int outLen = 0;
        int end = off + length;
        while (end > off) {
            if (!ignore((char) data[end - 1])) {
                break;
            }
            end--;
        }
        int i = off;
        while (i < end) {
            while (i < end && ignore((char) data[i])) {
                i++;
            }
            b1 = DECODING_TABLE[data[i++]];
            while (i < end && ignore((char) data[i])) {
                i++;
            }
            b2 = DECODING_TABLE[data[i++]];
            out.write((b1 << 4) | b2);
            outLen++;
        }
        return outLen;
    }
    /**
     * Decodes the Hex encoded String data writing it to the given output stream,
     * whitespace characters will be ignored.
     *
     * @param data The data to be encoded
     * @param out The {@link OutputStream} instance
     * @return the number of bytes produced.
     * @throws IOException If encoding failed.
     */
    public static int decode(final String data, final OutputStream out) throws IOException {
        byte b1, b2;
        int length = 0;
        int end = data.length();
        while (end > 0) {
            if (!ignore(data.charAt(end - 1))) {
                break;
            }
            end--;
        }
        int i = 0;
        while (i < end) {
            while (i < end && ignore(data.charAt(i))) {
                i++;
            }
            b1 = DECODING_TABLE[data.charAt(i++)];
            while (i < end && ignore(data.charAt(i))) {
                i++;
            }
            b2 = DECODING_TABLE[data.charAt(i++)];
            out.write((b1 << 4) | b2);
            length++;
        }
        return length;
    }
    /**
     * Encodes the input data producing a Hex output stream.
     * @param data Input data to encode.
     * @return the number of bytes produced.
     */
    public static String encode(final byte[] data) {
        try {
            final ByteArrayOutputStream out = new ByteArrayOutputStream();
            encode(data, 0, data.length, out);
            out.close();
            return new String(out.toByteArray());
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage(), e);
        }
    }
    /**
     * Decodes the HEX input data producing a output stream.
     * @param data Input data to be decoded.
     * @return A byte array representing the decoded input data.
     */
    public static byte[] decode(final String data) {
        try {
            final ByteArrayOutputStream out = new ByteArrayOutputStream();
            decode(data, out);
            out.close();
            return out.toByteArray();
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage(), e);
        }
    }
}
```

| 2.9.1. | Hexadecimal integer literal |
|---|---|
| 2.9.2. | A hexadecimal literal of type long |
| 2.9.3. | Defining integer literals as octal values |
| 2.9.4. | Decode string to integer |
| 2.9.5. | Convert octal number to decimal number example |
| 2.9.6. | Convert decimal integer to octal number example |
| 2.9.7. | Convert decimal integer to hexadecimal number example |
| 2.9.8. | Parsing and Formatting a Number into Binary |
| 2.9.9. | Convert byte array to Hex String |
| 2.9.10. | Convert the bytes to a hex string representation of the bytes |
| 2.9.11. | Converting hexadecimal strings |
| 2.9.12. | Dumps data in hexadecimal format |
| 2.9.13. | Given a hexstring this will return the byte array corresponding to string |
| 2.9.14. | Hex encoder/decoder implementation borrowed from BouncyCastle |
| 2.9.15. | Returns the hexadecimal value of the supplied byte array |
| 2.9.16. | A custom number formatter that formats numbers as hexadecimal strings. |
| 2.9.17. | Decodes Hex data into octects |
| 2.9.18. | Decodes Base64 data into octects |
| 2.9.19. | Helper function that returns a char from an hex |
| 2.9.20. | Encodes hex octects into Base64 |
| 2.9.21. | Hex encoder and decoder. |
| 2.9.22. | Helper function that dump an array of bytes in hex pair form, without '0x' and space chars |
| 2.9.23. | dump an array of bytes in hex form |
| 2.9.24. | Decode byte array |
