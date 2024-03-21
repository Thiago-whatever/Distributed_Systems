import java.net.*;
import java.io.*;
//TCPclient
//envía un mensaje al ProcesoB vía TCP
public class ProcesoA {

    public static void main(String args[]) {

        Socket s = null;
        String msj = "Hola";

        try {
            int serverPort = 49152;

            s = new Socket("localhost", serverPort);
            //s = new Socket("127.0.0.1", serverPort);
            DataInputStream in = new DataInputStream(s.getInputStream());
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            
            System.out.println("Msj a B: " + msj);
            out.writeUTF(msj);

            String data = in.readUTF();
            System.out.println("Received: " + data);

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