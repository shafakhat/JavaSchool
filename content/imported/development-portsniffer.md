---
title: Port Sniffer
nav: Port Sniffer
description: System.out.println("SerialPortEvent.OUTPUT_BUFFER_EMPTY occurred");
section: Imported - java2s Archive
order: 1984
source: https://web.archive.org/web/20140829083114/http://www.java2s.com/Tutorial/Java/0120__Development/PortSniffer.htm
---
```java title=Example.java
import java.io.*;
import javax.comm.*;
import java.util.*;
public class PortSniffer SerialPortEventListener
{
    static Enumeration ports;
    static CommPortIdentifier pID;
    InputStream inStream;
    SerialPort serPort;
    public PortSniffer() throws Exception
    {
        serPort = (SerialPort)pID.open("PortSniffer",2000);
        inStream = serPort.getInputStream();
        serPort.addEventListener(this);
        serPort.notifyOnDataAvailable(true);
        serPort.notifyOnBreakInterrupt(true);
        serPort.notifyOnCarrierDetect(true);
        serPort.notifyOnCTS(true);
        serPort.notifyOnDataAvailable(true);
        serPort.notifyOnDSR(true);
        serPort.notifyOnFramingError(true);
        serPort.notifyOnOutputEmpty(true);
        serPort.notifyOnOverrunError(true);
        serPort.notifyOnParityError(true);
        serPort.notifyOnRingIndicator(true);
        serPort.setSerialPortParams(9600, SerialPort.DATABITS_8,
        SerialPort.STOPBITS_1,
        SerialPort.PARITY_NONE);
    }
    public void serialEvent(SerialPortEvent event)
    {
        switch(event.getEventType())
        {
            case SerialPortEvent.BI:
                System.out.println("SerialPortEvent.BI occurred");
            case SerialPortEvent.OE:
                System.out.println("SerialPortEvent.OE occurred");
            case SerialPortEvent.FE:
                System.out.println("SerialPortEvent.FE occurred");
            case SerialPortEvent.PE:
                System.out.println("SerialPortEvent.PE occurred");
            case SerialPortEvent.CD:
                System.out.println("SerialPortEvent.CD occurred");
            case SerialPortEvent.CTS:
                System.out.println("SerialPortEvent.CTS occurred");
            case SerialPortEvent.DSR:
                System.out.println("SerialPortEvent.DSR occurred");
            case SerialPortEvent.RI:
                System.out.println("SerialPortEvent.RI occurred");
            case SerialPortEvent.OUTPUT_BUFFER_EMPTY:
                System.out.println("SerialPortEvent.OUTPUT_BUFFER_EMPTY occurred");
                break;
            case SerialPortEvent.DATA_AVAILABLE:
                System.out.println("SerialPortEvent.DATA_AVAILABLE occurred");
                byte[] readBuffer = new byte[20];
                try
                {
                    while (inStream.available() > 0)
                    {
                        int numBytes = inStream.read(readBuffer);
                    }
                    System.out.print(new String(readBuffer));
                 }catch (IOException ioe)
                {
                    System.out.println("Exception " + ioe);
                }
                break;
        }
    }
    public static void main(String[] args)throws Exception{
        ports = CommPortIdentifier.getPortIdentifiers();
        while(ports.hasMoreElements())
        {
            pID = (CommPortIdentifier)ports.nextElement();
            System.out.println("Port " + pID.getName());
            if (pID.getPortType() == CommPortIdentifier.PORT_SERIAL)
            {
                if (pID.getName().equals("COM1"))
                {
                    PortSniffer pSniffer = new PortSniffer();
                    System.out.println("COM1 found");
                }
            }
        }
    }
}
```

| 6.53.1. | Port Finder |
|---|---|
| 6.53.2. | Port Reader |
| 6.53.3. | Port Sniffer |
| 6.53.4. | Port Writer |
