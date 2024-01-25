package threadbasics;

public class HelloThread extends Thread{
    @Override
    public void run(){
        for(int i = 0; i< 1000; i++)
            System.out.println("Hola soy el hilo (extends): "+i+" " + Thread.currentThread().getName());
    }
}
