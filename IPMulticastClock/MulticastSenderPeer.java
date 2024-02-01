import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.SocketException;
import java.util.*;


/**
 * @author Octavio Gutierrez
 */
public class MulticastSenderPeer {

    public static void main(String args[]) {
        MulticastSocket socket = null;
        try {
            InetAddress group = InetAddress.getByName("229.5.6.7"); // destination multicast group
            //tiene que estar en el rango de direcciones multicast, sino hay error
            //CAMBIAR direccion multicast sino va a seguir escuchando todos
            //cuando, por ejemplo, otros equipos estan usando esa direccion (a la hora de revision de proyecto)
            socket = new MulticastSocket(49155);
            socket.joinGroup(group);
            //s.setTimeToLive(10);
            while(true){
                System.out.println("Messages' TTL (Time-To-Live): " + socket.getTimeToLive());
                String currentDate = (new Date()).toString();
                byte[] m = currentDate.getBytes();
                DatagramPacket messageOut = new DatagramPacket(m, m.length, group, 49155);
                //no hay costo de entrada/salida, no hay conexion
                socket.send(messageOut);
                //socket.leaveGroup(group);
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
            
           
        } catch (SocketException e) {
            System.out.println("Socket: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO: " + e.getMessage());
        } finally {
            if (socket != null) socket.close();
        }
    }
}
