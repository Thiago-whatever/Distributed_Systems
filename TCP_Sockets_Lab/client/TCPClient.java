package client;

import java.net.*;
import java.io.*;

public class TCPClient {
    public int numSolicitudes;

    public TCPClient(int numSolicitudes){
        this.numSolicitudes=numSolicitudes;
        main();
    }

    public void main() {

        Socket s = null;

        try {
            int serverPort = 49152;

            s = new Socket("localhost", serverPort);
            //s = new Socket("127.0.0.1", serverPort);
            DataInputStream in = new DataInputStream(s.getInputStream());
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            for (int i = 0; i< numSolicitudes; i++){
                out.writeUTF("2");            // UTF is a string encoding
                String data = in.readUTF();
                System.out.println("Received: " + data);
            }
            out.writeUTF("-1");
            String data = in.readUTF();
            System.out.println("Received: "+data);
            

            

        } catch (UnknownHostException e) {
            System.out.println("Sock:" + e.getMessage());
        } catch (EOFException e) {
            System.out.println("EOF:" + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO:" + e.getMessage());
        } finally {
            if (s != null) try {
                s.close();
            } catch (IOException e) {
                System.out.println("close:" + e.getMessage());
            }
        }
    }
}