package client;

public class Launcher {
    public static void main (String args[]){
        for(int i = 0; i<20; i++){
            ClientThread clientThread = new ClientThread();
            clientThread.start();
        }

        
        
            
    }
}
