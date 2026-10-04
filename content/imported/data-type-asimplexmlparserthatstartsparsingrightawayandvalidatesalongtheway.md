---
title: A simple XML parser that starts parsing right away and validates along the way.
nav: A simple XML parser that s...
description: A simple XML parser that starts parsing right away and validates along the way.
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20111125121359/http://java2s.com/Code/Java/Data-Type/AsimpleXMLparserthatstartsparsingrightawayandvalidatesalongtheway.htm
---
A simple XML parser that starts parsing right away and validates along the way.

```java title=Example.java
//Copyright 2007-2008 David Yu dyuproject@gmail.com
//------------------------------------------------------------------------
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//http://www.apache.org/licenses/LICENSE-2.0
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.
//package com.dyuproject.util.xml;
import java.io.IOException;
import java.io.InputStreamReader;
/**
 * A simple XML parser that starts parsing right away and validates along the way.
 *
 * @author David Yu
 * @created Sep 17, 2008
 */
public final class XMLParser
{
    private static final int STATE_EL_STARTING = 1;
    private static final int STATE_EL_STARTED = 2;
    private static final int STATE_EL_ENDING = 3;
    private static final int STATE_EL_ENDED = 4;
    private static final int STATE_EL_ATTR_NAME_START = 5;
    private static final int STATE_EL_ATTR_VALUE_START = 6;
    private static final int STATE_EL_ATTR_VALUE_END = 7;
    private static final int STATE_EL_TEXT = 8;
    private static final int STATE_COMMENT_STARTING = 9;
    private static final int STATE_COMMENT_DASH_START = 10;
    private static final int STATE_COMMENT_STARTED = 11;
    private static final int STATE_COMMENT_DASH_END = 12;
    private static final int STATE_COMMENT_ENDING = 13;
    private static final int STATE_IGNORE = 14;
    private static final int STATE_CDATA_STARTING = 15;
    private static final int STATE_CDATA_STARTED = 16;
    private static final int STATE_CDATA_ENDING = 17;
    private static final int STATE_CDATA_ENDED = 18;
    private static int __defaultBufferSize = 4096;
    public static void setDefaultBufferSize(int size)
    {
        __defaultBufferSize = size;
    }
    /**
     * Lazily parses the given {@code reader} using the default buffer size
     * {@link #__defaultBufferSize}.  The parsing can be terminated by
     * the {@link LazyHandler} {@code handler} at any point.
     */
    public static void parse(InputStreamReader reader, LazyHandler handler,
            boolean includeInnerText) throws IOException
    {
        parse(reader, handler, includeInnerText, __defaultBufferSize);
    }
    /**
     * Lazily parses the given {@code reader}.  The parsing can be terminated by
     * the {@link LazyHandler} {@code handler} at any point.
     */
    public static void parse(InputStreamReader reader, LazyHandler handler,
            boolean includeInnerText, int bufferSize) throws IOException
    {
        if(handler==null)
            throw new IllegalArgumentException("LazyHandler arg must not be null.");
        char[] cbuf = new char[bufferSize];
        int offset = 0;
        int len = 0;
        int state = 0;
        int stateBeforeComment = 0;
        int mark = -1;
        int elwsMark = -1;
        int nsMark = -1;
        String attrName = null;
        String attrValue = null;
        boolean dq = true;
        boolean searchRoot = true;
        while((len = reader.read(cbuf, offset, cbuf.length-offset))!=-1)
        {
            for(int i=0; i<len; i++, offset++)
            {
                char c = cbuf[offset];
                switch(c)
                {
                    case '<':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --< comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case 0:
                                state = STATE_EL_STARTING;
                                mark = offset;
                                continue;
                            case STATE_EL_ENDED:
                            case STATE_EL_STARTED:
                                stateBeforeComment = state;
                                state = STATE_EL_STARTING;
                                mark = offset;
                                continue;
                            case STATE_EL_TEXT:
                                stateBeforeComment = state;
                                state = STATE_EL_STARTING;
                                if(mark!=-1 && includeInnerText)
                                {
                                    handler.characters(cbuf, mark+1, offset-mark-1);
                                }
                                mark = offset;
                                continue;
                        }
                        continue;
                    case '>':
                        switch(state)
                        {
                            case STATE_IGNORE:
                                if(stateBeforeComment==0)
                                    state = 0;
                                continue;
                            case STATE_EL_TEXT:// uncommented text
                            case STATE_COMMENT_STARTED:
                                continue;
                            case STATE_CDATA_ENDING:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_ENDING:
                                state = STATE_EL_ENDED;
                                if(!handler.endElement())
                                    return;
                                elwsMark = -1;
                                continue;
                            case STATE_EL_ATTR_NAME_START:
                            case STATE_EL_STARTING:
                                if(elwsMark==-1)
                                {
                                    String name = null;
                                    String namespace = null;
                                    if(nsMark==-1)
                                        name = new String(cbuf, mark+1, offset-mark-1).trim();
                                    else
                                    {
                                        namespace = new String(cbuf, mark+1, nsMark-mark-1).trim();
                                        name = new String(cbuf, nsMark+1, offset-nsMark-1).trim();
                                    }
                                    if(searchRoot)
                                    {
                                        if(!handler.rootElement(name, namespace))
                                            return;
                                        searchRoot = false;
                                    }
                                    else if(!handler.startElement(name, namespace))
                                        return;
                                }
                                nsMark = -1;
                                elwsMark = -1;
                                state = STATE_EL_STARTED;
                                mark = -1;
                                continue;
                            case STATE_COMMENT_ENDING:
                                state = stateBeforeComment;
                                continue;
                            case STATE_CDATA_ENDED:
                                state = STATE_EL_TEXT;
                                if(mark!=-1 && includeInnerText)
                                {
                                    handler.characters(cbuf, mark+1, offset-2-mark-1);
                                }
                                mark = offset;
                                continue;
                        }
                        continue;
                    case '/':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --/ comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_ATTR_NAME_START:
                                mark = -1;
                                state = STATE_EL_ENDING;
                                continue;
                            case STATE_EL_STARTED:
                                state = STATE_EL_TEXT;
                                mark = offset-1;
                                continue;
                            case STATE_EL_STARTING:
                                if(mark+1!=offset)
                                {
                                    String name = null;
                                    String namespace = null;
                                    if(nsMark==-1)
                                        name = new String(cbuf, mark+1, offset-mark-1).trim();
                                    else
                                    {
                                        namespace = new String(cbuf, mark+1, nsMark-mark-1).trim();
                                        name = new String(cbuf, nsMark+1, offset-nsMark-1).trim();
                                    }
                                    if(searchRoot)
                                    {
                                        if(!handler.rootElement(name, namespace))
                                            return;
                                        searchRoot = false;
                                    }
                                    else if(!handler.startElement(name, namespace))
                                        return;
                                }
                                state = STATE_EL_ENDING;
                                elwsMark = -1;
                                nsMark = -1;
                                mark = -1;
                                continue;
                        }
                        continue;
                    case ':':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --: comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_STARTING:
                                if(nsMark!=-1)
                                    throw new IOException("invalid xml.");
                                nsMark = offset;
                                continue;
                        }
                        continue;
                    case '?':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --? comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_STARTING:
                                // uncommented text
                                if(stateBeforeComment==STATE_EL_TEXT)
                                    continue;
                                state = STATE_COMMENT_STARTING;
                                mark = -1;
                                continue;
                        }
                        continue;
                    case '!':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --! comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_STARTING:
                                state = STATE_COMMENT_STARTING;
                                mark = -1;
                                continue;
                        }
                        continue;
                    case '[':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --[ comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_COMMENT_STARTING:
                                state = STATE_CDATA_STARTING;
                                if(mark!=-1 && includeInnerText)
                                {
                                    handler.characters(cbuf, mark+1, offset-2-mark-1);
                                }
                                mark = -1;
                                continue;
                            case STATE_CDATA_STARTING:
                                state = STATE_CDATA_STARTED;
                                mark = offset;
                                continue;
                        }
                        continue;
                    case ']':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --[ comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_CDATA_STARTED:
                                state = STATE_CDATA_ENDING;
                                continue;
                            case STATE_CDATA_ENDING:
                                state = STATE_CDATA_ENDED;
                                continue;
                        }
                        continue;
                    case '-':
                        switch(state)
                        {
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_STARTING:
                                state = STATE_COMMENT_DASH_START;
                                continue;
                            case STATE_COMMENT_DASH_START:
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_COMMENT_STARTED:
                                state = STATE_COMMENT_DASH_END;
                                continue;
                            case STATE_COMMENT_DASH_END:
                                state = STATE_COMMENT_ENDING;
                                continue;
                            case STATE_COMMENT_ENDING:// handle ---- text
                                state = STATE_COMMENT_STARTED;
                                continue;
                        }
                        continue;
                    case '=':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --= comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_ATTR_NAME_START:
                                state = STATE_EL_ATTR_VALUE_START;
                                attrName = new String(cbuf, mark+1, offset-mark-1).trim();
                                mark = -1;
                                continue;
                        }
                        continue;
                    case '\'':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --' comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_ATTR_VALUE_START:
                                dq = false;
                                state = STATE_EL_ATTR_VALUE_END;
                                mark = offset;
                                continue;
                            case STATE_EL_ATTR_VALUE_END:
                                if(dq)
                                    continue;
                                state = STATE_EL_STARTING;
                                attrValue = new String(cbuf, mark+1, offset-mark-1).trim();
                                handler.attribute(attrName, attrValue);
                                attrName = null;
                                attrValue = null;
                                mark = -1;
                                continue;
                        }
                        continue;
                    case '"':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_ENDING://handle --" comments
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_ATTR_VALUE_START:
                                dq = true;
                                state = STATE_EL_ATTR_VALUE_END;
                                mark = offset;
                                continue;
                            case STATE_EL_ATTR_VALUE_END:
                                if(!dq)
                                    continue;
                                state = STATE_EL_STARTING;
                                attrValue = new String(cbuf, mark+1, offset-mark-1).trim();
                                handler.attribute(attrName, attrValue);
                                attrName = null;
                                attrValue = null;
                                mark = -1;
                                continue;
                        }
                        continue;
                    case ' ':
                    case '\t':
                    case '\r':
                    case '\n':
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_EL_STARTING:
                                state = STATE_EL_ATTR_NAME_START;
                                if(elwsMark==-1)
                                {
                                    String name = null;
                                    String namespace = null;
                                    if(nsMark==-1)
                                        name = new String(cbuf, mark+1, offset-mark-1).trim();
                                    else
                                    {
                                        namespace = new String(cbuf, mark+1, nsMark-mark-1).trim();
                                        name = new String(cbuf, nsMark+1, offset-nsMark-1).trim();
                                    }
                                    if(searchRoot)
                                    {
                                        if(!handler.rootElement(name, namespace))
                                            return;
                                        searchRoot = false;
                                    }
                                    else if(!handler.startElement(name, namespace))
                                        return;
                                }
                                nsMark = -1;
                                elwsMark = offset;
                                mark = offset;
                                continue;
                        }
                        continue;
                    default:
                        switch(state)
                        {
                            case STATE_COMMENT_STARTED:
                            case STATE_IGNORE:
                                continue;
                            case STATE_COMMENT_DASH_END:
                            case STATE_COMMENT_ENDING:
                                state = STATE_COMMENT_STARTED;
                                continue;
                            case STATE_CDATA_ENDING:
                            case STATE_CDATA_ENDED:
                                state = STATE_CDATA_STARTED;
                                continue;
                            case STATE_EL_STARTED:
                                state = STATE_EL_TEXT;
                                if(includeInnerText)
                                    mark = offset-1;
                                continue;
                            case STATE_COMMENT_STARTING:
                                if(stateBeforeComment!=0)
                                    throw new IOException("invalid xml.");
                                mark = -1;
                                state = STATE_IGNORE;
                                continue;
                            case STATE_COMMENT_DASH_START:
                                throw new IOException("invalid xml.");
                        }
                        continue;
                }
            }
            if(mark==-1)
                offset = 0;
            else
            {
                if(state==STATE_EL_TEXT || state==STATE_CDATA_STARTED)
                {
                    if(includeInnerText)
                        handler.characters(cbuf, mark+1, offset-mark-2);
                    offset = 0;
                    mark = -1;
                }
                else
                {
                    // move to the front
                    int copyLen = offset - mark;
                    System.arraycopy(cbuf, mark, cbuf, 0, copyLen);
                    offset = len;
                    mark = 0;
                }
            }
        }
    }
}
interface LazyHandler
{
    /**
     * Callback that gets called only once upon traversing the root xml element.
     */
    public boolean rootElement(String name, String namespace);
    /**
     * Callback after traversing the start of xml elements (E.g &lt;foo&gt;).
     */
    public boolean startElement(String name, String namespace);
    /**
     * Callback after traversing the end of xml elements (E.g &lt;/foo&gt; or
     * /&gt;).
     */
    public boolean endElement();
    /**
     * Callback after traversing the attributes of an element.
     */
    public void attribute(String name, String value);
    /**
     * Callback after traversing the text content of an element.
     */
    public void characters(char[] data, int start, int length);
}
/*
//Copyright 2007-2008 David Yu dyuproject@gmail.com
//------------------------------------------------------------------------
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//http://www.apache.org/licenses/LICENSE-2.0
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.
//package com.dyuproject.util.xml;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import junit.framework.TestCase;
//* @author David Yu
//* @created Sep 18, 2008
public class XMLParserTest extends TestCase
{
  static final String prefix = "com/dyuproject/util/xml/";
  static URL getResource(String resource)
  {
      return Thread.currentThread().getContextClassLoader().getResource(prefix + resource);
  }
  public void testNamespace() throws Exception
  {
      String url = "http://open.login.yahooapis.com/openid20/www.yahoo.com/xrds";
      HttpURLConnection con = (HttpURLConnection)new URL(url).openConnection();
      con.setRequestMethod("GET");
      con.setDefaultUseCaches(false);
      con.setInstanceFollowRedirects(false);
      con.setDoInput(true);
      con.connect();
      SimpleHandler handler = new SimpleHandler();
      InputStreamReader reader = new InputStreamReader(con.getInputStream());
      try
      {
          XMLParser.parse(reader, handler, true);
          Node xrds = handler.getNode();
          assertEquals("xrds", xrds.getNamespace());
          Node xrd = xrds.getNode("xrd");
          Node service = xrd.getNode("service");
          assertTrue(0!=service.getNodes("type").size());
          assertEquals("xrds", service.getLastNode().getNamespace());
      }
      finally
      {
          reader.close();
          con.disconnect();
      }
  }
  public void testSimple() throws Exception
  {
      SimpleHandler handler = new SimpleHandler();
      InputStreamReader reader = new InputStreamReader(getResource("simple.xml").openStream());
      try
      {
          XMLParser.parse(reader, handler, true);
          Node root = handler.getNode();
          assertEquals("root", root.getName());
          Node foo = root.getNode("foo");
          assertNotNull(foo);
          assertEquals(foo.getText().toString(), "baz");
          Node bar = foo.getNode("bar");
          assertNotNull(bar);
      }
      finally
      {
          reader.close();
      }
  }
  public void testTrimAndCDATA() throws Exception
  {
      SimpleHandler handler = new SimpleHandler();
      InputStreamReader reader = new InputStreamReader(getResource("xrds").openStream());
      try
      {
          XMLParser.parse(reader, handler, true);
          Node xrds = handler.getNode();
          assertEquals("xrds", xrds.getNamespace());
          Node xrd = xrds.getNode("xrd");
          Node service = xrd.getNode("service");
          assertTrue(0!=service.getNodes("type").size());
          assertEquals("xrds", service.getLastNode().getNamespace());
          Node foo = xrds.getNode("FOO");
          assertNotNull(foo);
          assertEquals(foo.getText().toString(), "I am a cdata text. yep\nyep");
          System.err.println(foo.getText().toString());
      }
      finally
      {
          reader.close();
      }
  }
  public void testSiteXrds() throws Exception
  {
      SimpleHandler handler = new SimpleHandler();
      InputStreamReader reader = new InputStreamReader(getResource("site-xrds").openStream());
      try
      {
          XMLParser.parse(reader, handler, true);
          Node xrds = handler.getNode();
          assertNotNull(xrds);
          assertEquals("xrds", xrds.getNamespace());
          assertEquals("XRDS", xrds.getName());
          Node signature = xrds.getNode("Signature");
          assertNotNull(signature);
          assertEquals("ds", signature.getNamespace());
          Node xrd = xrds.getNode("XRD");
          assertNotNull(xrd);
          Node canonicalID = xrd.getNode("CanonicalID");
          assertNotNull(canonicalID);
          assertEquals("dyuproject.com", canonicalID.getText().toString());
          Node service = xrd.getNode("Service");
          assertNotNull(service);
          Node uri = service.getNode("URI");
          assertNotNull(uri);
          assertEquals("https://www.google.com/a/dyuproject.com/o8/ud?be=o8", uri.getText().toString());
      }
      finally
      {
          reader.close();
      }
  }
}
*/
```

1.  Date parser for ISO 8601 format
2.  Date Utils
3.  Date To String
4.  Perform date validations
5.  ISO 8601 date parsing utility.
6.  Parses a string representing a date by trying a variety of different parsers.
7.  Parses a time period into a long. Translates possible [msec  sec  min  h] suffixes
8.  A method to get the current date as an array of components 0 = year, 1 = month, 2 = day
9.  ISO 8601 date parsing utility. Designed for parsing the ISO subset used in Dublin Core, RSS 1.0, and Atom.
