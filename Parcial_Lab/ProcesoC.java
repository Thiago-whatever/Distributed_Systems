import java.net.*;
import java.io.*;

public class ProcesoC {
    public static void main(String args[]) {
        DatagramSocket socket = null;
        try {
            int serverPort = 49152;
            socket = new DatagramSocket(serverPort);
            byte[] buffer = new byte[1000]; // buffer encapsulará mensajes
            while (true) {
                System.out.println("Waiting for messages...");
                DatagramPacket request = new DatagramPacket(buffer, buffer.length);
                socket.receive(request);  // bloqueantes

                //System.out.println("Server received a request from " + request.getAddress());
                String m = (new String(request.getData())).trim();
                System.out.println("Mensaje recibido de B: " + m);

                String m_modificado = m + " World!";
                byte[] mC = m_modificado.getBytes();

                DatagramPacket reply = new
                DatagramPacket(mC,
                mC.length,
                request.getAddress(),
                request.getPort());

                socket.send(reply);
                System.out.println("Mensaje enviado a B: " +m_modificado);
            }
        } catch (SocketException e) {
            System.out.println("Socket: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO: " + e.getMessage());
        } finally {
            if (socket != null)
                socket.close();
        }
    }
}