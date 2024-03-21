import java.net.*;
import java.io.*;
//TCPserver

//Para que funcione como esperamos, necesitamos que el ProcesoB funcione como servidor TCP y como cliente UDP
public class ProcesoB {

    public static void main(String args[]) {
        try {
            int serverPort = 49152;
            ServerSocket listenSocket = new ServerSocket(serverPort);
            while (true) {
                System.out.println("Waiting for messages...");
                Socket clientSocket = listenSocket.accept();  // Listens for a connection to be made to this socket and accepts it. The method blocks until a connection is made.
                Connection c = new Connection(clientSocket);
                c.start();
            }
        } catch (IOException e) {
            System.out.println("Listen :" + e.getMessage());
        }
    }

}

class Connection extends Thread {
    private DataInputStream in;
    private DataOutputStream out;
    private Socket clientSocket;

    public Connection(Socket aClientSocket) {
        try {
            clientSocket = aClientSocket;
            in = new DataInputStream(clientSocket.getInputStream());
            out = new DataOutputStream(clientSocket.getOutputStream());
        } catch (IOException e) {
            System.out.println("Connection:" + e.getMessage());
        }
    }

    @Override
    public void run() {
        try {
            //Recepcion solicitud del proceso A
            String data = in.readUTF(); 
            System.out.println("Message received from A: " + data);
            
            //Envío de datos al proceso C via UDP
            byte[] msj = data.getBytes();
            InetAddress address = InetAddress.getByName("localhost");
            int portC = 49152; // Tiene que ser el mismo puerto que el proceso C
            DatagramSocket socketUDP = new DatagramSocket();
            DatagramPacket packet = new DatagramPacket(msj, msj.length, address, portC);
            socketUDP.send(packet);
            
            // Recepción de la respuesta de C
            byte[] bufReceive = new byte[1000];
            DatagramPacket packetReceive = new DatagramPacket(bufReceive, bufReceive.length);
            socketUDP.receive(packetReceive);
            String received = new String(packetReceive.getData(), 0, packetReceive.getLength());
            
            // Envío de la respuesta modificada de vuelta al proceso A
            out.writeUTF(received); // Envío respuesta modificada al proceso A
            System.out.println("Message received from C: " + received);

            socketUDP.close();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                System.out.println(e);
            }
        }
    }

    // public void run() {
    //     try {
    //         // an echo server
    //         String data = in.readUTF();// recibo solicitud

    //         System.out.println("Message received from: " + clientSocket.getRemoteSocketAddress());

    //         //Aqui lo que quiero es enviarle data al proceso C mediante UDP
    //         //Luego voy a recibir otro mensaje del proceso c
    //         //esa respuesta la quiero mandar al proceso a
    //         //out.writeUTF(data);// envio respuesta

    //     } catch (EOFException e) {
    //         System.out.println("EOF:" + e.getMessage());
    //     } catch (IOException e) {
    //         System.out.println("IO:" + e.getMessage());
    //     } finally {
    //         try {
    //             clientSocket.close();
    //         } catch (IOException e) {
    //             System.out.println(e);
    //         }
    //     }
    // }
}