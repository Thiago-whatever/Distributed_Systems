package threadbasics;

public class SynchronizedThread extends Thread{
    private Counter counter;

    public SynchronizedThread(Counter counter){
        this.counter=counter;
    }

    public void run(){
        counter.increase(Thread.currentThread().getName());
    }
}
