package client;

public class ClientThread extends Thread{
    public ClientThread(){

    }

    public void run(){
        long suma = 0;
        for(int j = 0; j < 30; j++){
            long startTime = System.currentTimeMillis();
            TCPClient tcpClient = new TCPClient(13); 
            long spentTime = System.currentTimeMillis() -startTime;
            suma+=spentTime;
        }
        
        suma /= 30;
        System.out.println(suma);        
    }
}