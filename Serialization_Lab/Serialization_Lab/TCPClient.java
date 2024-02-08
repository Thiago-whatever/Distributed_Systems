package Serialization_Lab;
import java.net.*;
import java.io.*;

public class TCPClient {

    public static void main(String args[]) throws ClassNotFoundException {

        Socket s = null;
        Person me = new Person(1980,"Octavio");

        try {
            int serverPort = 49152;

            s = new Socket("localhost", serverPort);
            //s = new Socket("127.0.0.1", serverPort);
            ObjectInputStream in = new ObjectInputStream(s.getInputStream());
            ObjectOutputStream out = new ObjectOutputStream(s.getOutputStream());

            out.writeObject(me);            // UTF is a string encoding

            me = (Person) in.readObject();

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