---
title: Another Servlet Localization: Currency : Java examples (example source code) » Servlets » I18N
nav: Another Servlet Localizati...
description: Another Servlet Localization: Currency : Java examples (example source code) » Servlets » I18N
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20060411094406/http://www.java2s.com:80/Code/Java/Servlets/AnotherServletLocalizationCurrency.htm
---
Another Servlet Localization: Currency

```java title=Example.java
import java.text.NumberFormat;
import java.util.Locale;
import java.util.ResourceBundle;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class CurrLocaleServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, java.io.IOException {
    //Get the client's Locale
    Locale locale = request.getLocale();
    ResourceBundle bundle = ResourceBundle.getBundle("i18n.WelcomeBundle",
        locale);
    String welcome = bundle.getString("Welcome");
    NumberFormat nft = NumberFormat.getCurrencyInstance(locale);
    String formatted = nft.format(1000000);
    //Display the locale
    response.setContentType("text/html");
    java.io.PrintWriter out = response.getWriter();
    out.println("<html><head><title>" + welcome + "</title></head><body>");
    out.println("<h2>" + bundle.getString("Hello") + " "
        + bundle.getString("and") + " " + welcome + "</h2>");
    out.println("Locale: ");
    out.println(locale.getLanguage() + "_" + locale.getCountry());
    out.println("<br /><br />");
    out.println(formatted);
    out.println("</body></html>");
    out.close();
  } //end doGet
}
```

Related examples in the same category
---
1. Internationalization I18n
2. Servlet Localization
3. Servlet Localization: Date
4. Servlet localization display
