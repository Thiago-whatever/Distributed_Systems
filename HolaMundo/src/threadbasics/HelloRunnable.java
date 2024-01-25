package threadbasics;

public class HelloRunnable implements Runnable{
    @Override
    public void run(){
        for(int i=0; i<1000; i++)
            System.out.println("Hola soy el hilo (runnable): "+i+" "+ Thread.currentThread().getName());
    }
}
