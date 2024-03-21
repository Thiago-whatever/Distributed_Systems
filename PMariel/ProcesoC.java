import java.net.*;
import java.io.*;

//UDPserver

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
                //C recibe el msj de B
                socket.receive(request);  // bloqueantes

                String msj = (new String(request.getData())).trim();
                System.out.println("Msj recibido de B: " + msj);
                //Modificacion del mensaje
                String msjModif = msj+" de regreso!"; 
                byte[] m = msjModif.getBytes();

                DatagramPacket reply = new DatagramPacket(
                    m, 
                    m.length, 
                    request.getAddress(), 
                    request.getPort());

                System.out.println("Msj enviado a B: " + msjModif);
                System.out.println("Server received a request from " + request.getAddress());

                //C manda a B el msj modificado
                socket.send(reply);
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
