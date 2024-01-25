package threadbasics;
public class Main {
    public static void main(String[] args) throws Exception {

        /*try{
            HelloThread hilo1 = new HelloThread();
            Thread hilo2 = new Thread(new HelloRunnable());
            //Thread.sleep(5000);//hago que espere un hilo, mas no sincronizo (es peligroso usarlo, mejor no lo uses)
            hilo1.start(); //creo el hilo
            hilo1.join(); // sincronización por barrera: una vez hecha el fork, lo que hace el join es que regresa a la siguiente instrucción
            //del hilo del que se hizo fork en primer lugar, habria que tener un timeout. Se corre el main, se hace el nuevo hilo y el join lo que hace
            //es que se hace todo lo que este en el nuevo hilo y luego regresa al main (el main durante el tiempo estaba en pausa)
             * Si pongo primero hilo1.start();hilo2.start(); hilo1.join(); hilo2.join(); lo que tendria es un entrelazamiento entre los dos hilos
             * generados en el main y al final regresa al main. 
             */
            /*hilo2.start();
            System.out.println("Hola soy hilo: "+ Thread.currentThread().getName());
        }catch (Exception e){
            System.out.println(e);
        }*/

        try{
            Counter counter = new Counter(0);
            SynchronizedThread hilo1= new SynchronizedThread(counter);
            SynchronizedThread hilo2= new SynchronizedThread(counter);
            hilo1.start();
            hilo2.start();
            //condicion de carrera (Foto 7:18 22/01/2024)
            //si pusieramos un hilo1.join antes seria un parche mal hecho -> estarias serializando la ejecucion y no estas aprovechando los hilos
        }catch(Exception e){
            System.out.println(e);
        }
        
    }
}
