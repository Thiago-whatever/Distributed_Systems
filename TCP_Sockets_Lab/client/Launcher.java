package client;

public class Launcher {
    public static void main (String args[]){
        ClientThread clientThread = new ClientThread();
        clientThread.start();
    }
}
