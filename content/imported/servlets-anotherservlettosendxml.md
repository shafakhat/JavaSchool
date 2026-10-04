---
title: Another servlet to Send XML
nav: Another servlet to Send XML
description: public void doGet(HttpServletRequest request, HttpServletResponse response)
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20061018193017/http://www.java2s.com/Code/Java/Servlets/AnotherservlettoSendXML.htm
---
```java title=Example.java
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class SendXml extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
    //get the 'file' parameter
    String fileName = (String) request.getParameter("file");
    if (fileName == null || fileName.equals(""))
      throw new ServletException(
          "Invalid or non-existent file parameter in SendXml servlet.");
    // add the .doc suffix if it doesn't already exist
    if (fileName.indexOf(".xml") == -1)
      fileName = fileName + ".xml";
    String xmlDir = getServletContext().getInitParameter("xml-dir");
    if (xmlDir == null || xmlDir.equals(""))
      throw new ServletException(
          "Invalid or non-existent xmlDir context-param.");
    ServletOutputStream stream = null;
    BufferedInputStream buf = null;
    try {
      stream = response.getOutputStream();
      File xml = new File(xmlDir + "/" + fileName);
      response.setContentType("text/xml");
      response.addHeader("Content-Disposition", "attachment; filename="
          + fileName);
      response.setContentLength((int) xml.length());
      FileInputStream input = new FileInputStream(xml);
      buf = new BufferedInputStream(input);
      int readBytes = 0;
      while ((readBytes = buf.read()) != -1)
        stream.write(readBytes);
    } catch (IOException ioe) {
      throw new ServletException(ioe.getMessage());
    } finally {
      if (stream != null)
        stream.close();
      if (buf != null)
        buf.close();
    }
  }
  public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
    doGet(request, response);
  }
}
```

Related examples in the same category
---
1. Send PDF file
2. Another servlet to Send PDF
3. Send XML
4. Send word document
5. Send mp3
