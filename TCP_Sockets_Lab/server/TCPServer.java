package server;

import java.net.*;
import java.io.*;

public class TCPServer {

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
    private AddressBook addressBook;
    private int k;

    public Connection(Socket aClientSocket) {
        try {
            clientSocket = aClientSocket;
            in = new DataInputStream(clientSocket.getInputStream());
            out = new DataOutputStream(clientSocket.getOutputStream());
            addressBook = new AddressBook();
            k = 12;
        } catch (IOException e) {
            System.out.println("Connection:" + e.getMessage());
        }
    }

    @Override
    public void run() {
        try {
            String data = in.readUTF();         // recibo solicitud
            int key = Integer.parseInt(data);
            k = key;
            while(k != -1){
                

                System.out.println("Message received from: " + clientSocket.getRemoteSocketAddress());

                try{
                    
                    String aux = addressBook.getRecord(key).getName();
                    if(aux != null && aux != "")
                        data = "El nombre del usuario con clave "+key+" es: "+aux;
                    else
                        data = "Eres tonto?";
                }catch(Exception e){
                    System.out.println("No enviaste una llave: "+e);
                }

                out.writeUTF(data);                // envio respuesta

                data = in.readUTF();         // recibo solicitud
                key = Integer.parseInt(data);
                k = key;
            }

            if(k == -1){
                try{
                    out.writeUTF("Bye");
                    System.out.println("H9la");

                }catch(IOException e){
                    System.out.println("chin :(");
                }
            }
            

        } catch (EOFException e) {
            System.out.println("EOF:" + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO:" + e.getMessage());
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                System.out.println(e);
            }
        }
    }
}