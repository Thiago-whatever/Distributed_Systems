import java.net.*;
import java.io.*;

public class ProcesoB {
    public static void main(String args[]) {
        
        try{
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
        DatagramSocket socket = null;
        try {
            // an echo server
            String m = in.readUTF();         // recibo solicitud

            System.out.println("Message received from A: " + clientSocket.getRemoteSocketAddress() + " -- " + m);

            socket = new DatagramSocket();
            byte[] messageB = m.getBytes();

            InetAddress aHost = InetAddress.getByName("localhost");
            int serverPort = 49152;
            DatagramPacket request = new DatagramPacket(messageB, messageB.length, aHost, serverPort);
            socket.send(request);
            System.out.println("Sent message to C: " + m);


            byte[] buffer = new byte[1000];
            DatagramPacket reply = new DatagramPacket(buffer, buffer.length);
            socket.receive(reply);
            String m_modificado = (new String(reply.getData())).trim();
            System.out.println("Reply from C: " + m_modificado);

            System.out.println("Sent message to A: " + m_modificado);
            out.writeUTF(m_modificado);                // envio respuesta

        } catch (EOFException e) {
            System.out.println("EOF:" + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO:" + e.getMessage());
        } finally {
            try {
                clientSocket.close();
                if (socket != null)
                    socket.close();
            } catch (IOException e) {
                System.out.println(e);
            }
        }
    }
}
