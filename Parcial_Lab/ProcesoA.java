import java.net.*;
import java.io.*;

public class ProcesoA {
    public static void main(String args[]) {
        Socket s = null;

        try{
            int serverPort = 49152;
            s = new Socket("localhost", serverPort);

            DataInputStream in = new DataInputStream(s.getInputStream());
            DataOutputStream out = new DataOutputStream(s.getOutputStream());

            String m = "Hello";
            out.writeUTF(m);
            
            String m_modificado = in.readUTF();
            System.out.println("Received: " + m_modificado);

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
