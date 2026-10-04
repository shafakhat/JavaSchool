---
title: Printing indented text
nav: Printing indented text
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2052
source: https://web.archive.org/web/20140217105227/http://www.java2s.com/Tutorial/Java/0120__Development/Printingindentedtext.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.PrintWriter;
/**
 * A helper class for printing indented text
 *
 * @version $Revision: 1.2 $
 */
public class IndentPrinter {
    private int indentLevel;
    private String indent;
    private PrintWriter out;
    public IndentPrinter() {
        this(new PrintWriter(System.out), "  ");
    }
    public IndentPrinter(PrintWriter out) {
        this(out, "  ");
    }
    public IndentPrinter(PrintWriter out, String indent) {
        this.out = out;
        this.indent = indent;
    }
    public void println(Object value) {
        out.print(value.toString());
        out.println();
    }
    public void println(String text) {
        out.print(text);
        out.println();
    }
    public void print(String text) {
        out.print(text);
    }
    public void printIndent() {
        for (int i = 0; i < indentLevel; i++) {
            out.print(indent);
        }
    }
    public void println() {
        out.println();
    }
    public void incrementIndent() {
        ++indentLevel;
    }
    public void decrementIndent() {
        --indentLevel;
    }
    public int getIndentLevel() {
        return indentLevel;
    }
    public void setIndentLevel(int indentLevel) {
        this.indentLevel = indentLevel;
    }
    public void flush() {
        out.flush();
    }
}
```

| 6.59.1. | Prints messages formatted for a specific line width. |
|---|---|
| 6.59.2. | A bean that can be used to keep track of a counter |
| 6.59.3. | Swing Console |
| 6.59.4. | Methods for logging events |
| 6.59.5. | Debug Utility |
| 6.59.6. | A helper class for printing indented text |
| 6.59.7. | Random data for test |
| 6.59.8. | Count Up Down Latch |
| 6.59.9. | A simple logging facility. |
| 6.59.10. | Printing indented text |
