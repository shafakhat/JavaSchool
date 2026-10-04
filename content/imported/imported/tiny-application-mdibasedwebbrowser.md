---
title: MDI based web browser
nav: MDI based web browser
description: JInternalFrame frame = new JInternalFrame("Browser", // title
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20061018210623/http://www.java2s.com/Code/Java/Tiny-Application/MDIbasedwebbrowser.htm
---
```java title=Example.java
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDesktopPane;
import javax.swing.JEditorPane;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.JToolBar;
import javax.swing.event.HyperlinkEvent;
import javax.swing.event.HyperlinkListener;
public class MDIWebBrowser extends JFrame {
  JDesktopPane desktopPane = new JDesktopPane();
  public MDIWebBrowser() {
    super("MDI Web Browser");
    createNewWindow();
    Container contentPane = getContentPane();
    contentPane.add(desktopPane);
    JMenu fileMenu = new JMenu("File");
    fileMenu.add(new NewWindowAction());
    fileMenu.addSeparator();
    fileMenu.add(new ExitAction());
    fileMenu.setMnemonic('F');
    JMenuBar menuBar = new JMenuBar();
    menuBar.add(fileMenu);
    setJMenuBar(menuBar);
  }
  private void createNewWindow() {
    JInternalFrame frame = new JInternalFrame("Browser", // title
        true, // resizable
        true, // closable
        true, // maximizable
        true); // iconifiable
    WebBrowserPane browserPane = new WebBrowserPane();
    WebToolBar toolBar = new WebToolBar(browserPane);
    Container contentPane = frame.getContentPane();
    contentPane.add(toolBar, BorderLayout.NORTH);
    contentPane.add(new JScrollPane(browserPane), BorderLayout.CENTER);
    frame.setSize(320, 240);
    // move JInternalFrame to prevent it from obscuring others
    int offset = 30 * desktopPane.getAllFrames().length;
    frame.setLocation(offset, offset);
    desktopPane.add(frame);
    frame.setVisible(true);
  }
  private class NewWindowAction extends AbstractAction {
    public NewWindowAction() {
      putValue(Action.NAME, "New Window");
      putValue(Action.SHORT_DESCRIPTION, "Create New Web Browser Window");
      putValue(Action.MNEMONIC_KEY, new Integer('N'));
    }
    public void actionPerformed(ActionEvent event) {
      createNewWindow();
    }
  }
  private class ExitAction extends AbstractAction {
    public ExitAction() {
      // set name, description and mnemonic key
      putValue(Action.NAME, "Exit");
      putValue(Action.SHORT_DESCRIPTION, "Exit Application");
      putValue(Action.MNEMONIC_KEY, new Integer('x'));
    }
    public void actionPerformed(ActionEvent event) {
      System.exit(0);
    }
  }
  public static void main(String args[]) {
    MDIWebBrowser browser = new MDIWebBrowser();
    browser.setDefaultCloseOperation(EXIT_ON_CLOSE);
    browser.setSize(640, 480);
    browser.setVisible(true);
  }
}
class WebToolBar extends JToolBar implements HyperlinkListener {
  private WebBrowserPane webBrowserPane;
  private JButton backButton;
  private JButton forwardButton;
  private JTextField urlTextField;
  public WebToolBar(WebBrowserPane browser) {
    super("Web Navigation");
    webBrowserPane = browser;
    webBrowserPane.addHyperlinkListener(this);
    urlTextField = new JTextField(25);
    urlTextField.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        try {
          URL url = new URL(urlTextField.getText());
          webBrowserPane.goToURL(url);
        }catch (MalformedURLException urlException) {
          urlException.printStackTrace();
        }
      }
    });
    backButton = new JButton("back");
    backButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        URL url = webBrowserPane.back();
        urlTextField.setText(url.toString());
      }
    });
    forwardButton = new JButton("forward");
    forwardButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        URL url = webBrowserPane.forward();
        urlTextField.setText(url.toString());
      }
    });
    add(backButton);
    add(forwardButton);
    add(urlTextField);
  }
  public void hyperlinkUpdate(HyperlinkEvent event) {
    if (event.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
      URL url = event.getURL();
      webBrowserPane.goToURL(url);
      urlTextField.setText(url.toString());
    }
  }
}
class WebBrowserPane extends JEditorPane {
  private List history = new ArrayList();
  private int historyIndex;
  public WebBrowserPane() {
    setEditable(false);
  }
  public void goToURL(URL url) {
    displayPage(url);
    history.add(url);
    historyIndex = history.size() - 1;
  }
  public URL forward() {
    historyIndex++;
    if (historyIndex >= history.size())
      historyIndex = history.size() - 1;
    URL url = (URL) history.get(historyIndex);
    displayPage(url);
    return url;
  }
  public URL back() {
    historyIndex--;
    if (historyIndex < 0)
      historyIndex = 0;
    URL url = (URL) history.get(historyIndex);
    displayPage(url);
    return url;
  }
  private void displayPage(URL pageURL) {
    try {
      setPage(pageURL);
    }
    catch (IOException ioException) {
      ioException.printStackTrace();
    }
  }
}
```

Related examples in the same category
---
1. Brower based on JEditorPane
2. Drag and drop web browser
3. Tabbed Web browser
