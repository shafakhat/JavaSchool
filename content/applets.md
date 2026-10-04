---
title: Java Applets
nav: Applets
description: What Java applets were, how they worked, the lifecycle, embedding code, and why the web moved on - with preserved examples.
section: Advanced Java
order: 70
---

## What was an applet?

An **applet** was a small Java program designed to run *inside a web browser*, sandboxed with no access to the local filesystem. From the mid-1990s to around 2010 they brought animation, charts and interactive UIs to pages that were otherwise static HTML.

```text title=then vs now
THEN (1995-2015)                 NOW
----------------                 ---
<applet code="Chart.class">      HTML5 <canvas>, <video>, JS apps
runs in browser JVM plugin        no plugin - browsers removed it
signed applets for full access    WebAssembly / server APIs
Java Web Start (jnlp)             packaged native apps / auto-update
```

> **Warning:** Applets are **dead technology**. Oracle removed the browser plugin (Java 11 era), all major browsers dropped the NPAPI plugin years earlier, and `Applet` itself was deprecated for removal (Java 17) / removed (Java 21 era discussions). Learn applets to **read legacy code**, never to build new UIs.

## The applet lifecycle

```java title=LifeCycle.java
import java.applet.Applet;      // deprecated - legacy reference
import java.awt.Graphics;

// Lifecycle mirrors a servlet: init -> start -> paint* -> stop -> destroy
public class HelloApplet extends Applet {

    private String message;

    @Override
    public void init() {                 // once, after loading
        message = "Hello from the applet!";
    }

    @Override
    public void start() {                // each time the page becomes visible
        // begin animation / threads here
    }

    @Override
    public void paint(Graphics g) {      // redraw requests
        g.drawString(message, 20, 30);
    }

    @Override
    public void stop() {                 // page hidden - pause work
    }

    @Override
    public void destroy() {              // unloading - release resources
    }
}
```

| Phase | Trigger | Typical work |
|---|---|---|
| `init()` | first load | read `<param>` values, build UI |
| `start()` | page shown / return | start threads, timers |
| `paint()` | expose/repaint | draw with `Graphics` |
| `stop()` | page hidden | pause threads |
| `destroy()` | unload | close sockets/files |

## How embedding worked

```html title=page.html (legacy)
<applet code="HelloApplet.class" archive="applet.jar"
        width="400" height="200">
  <param name="speed" value="2">
  Your browser does not support applets.
</applet>
```

- **code** - fully-qualified main class (or **archive** + codepath for jars)
- **width/height** - required; the applet's canvas size
- **param** - per-instance settings read with `getParameter("speed")`
- The browser needed the **Java plugin** (later: JDK's deprecated plugin) - the reason it all collapsed: plugin security holes and the industry's move to HTML5.

## The security sandbox

Unsigned applets ran in a sandbox: no filesystem, no network except back to the serving host, no launching processes, no desktop. That made "download and run" safe-ish in 1998 - and made signed-applet certificate prompts a social-engineering minefield later. The same *idea* survives today in browser sandboxing and WebAssembly's capability model.

## What replaced applets?

| Instead of... | Use today |
|---|---|
| Animated/interactive widget | JavaScript + HTML5 canvas/WebGL |
| Client-side charting | Chart.js, D3, or server-rendered images |
| Rich form logic | Modern frontend framework or server rendering |
| Java Web Start line-of-business app | Native installers, auto-updating desktop (JavaFX still exists) |
| Bulk computation in browser | WebAssembly, or move it to the server |

## JavaFX - the intended successor

JavaFX was Sun/Oracle's replacement for both applets and Swing desktops: CSS styling, FXML layouts, WebView (Chromium), hardware-accelerated scene graph. It runs as **desktop/mobile apps** (and formerly via jfxrt in browsers - also removed). If you need rich Java UI today, JavaFX + Gluon is the living option.

## Legacy applets in the archive

The sidebar's archive section contains preserved java2s applet-era articles and examples (loaded from the Wayback Machine) - useful when you maintain an old codebase that still has `extends Applet` or `<applet>` tags in JSPs.

Related: [AWT & Swing](awt-swing.html) · [Servlets & JSP](servlets-jsp.html)
