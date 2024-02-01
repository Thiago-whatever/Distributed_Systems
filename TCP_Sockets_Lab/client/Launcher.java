package client;

public class Launcher {
    public static void main (String args[]){
        for(int i = 0; i<20; i++){
            ClientThread clientThread = new ClientThread();
            clientThread.start();
        }

        /*
         * Este main no tiene control sobre los otros hilos, de hecho,
         * puede que termine y que hayan varios hilos aun ejecutandose, pues se crean
         * y se "independizan"
         * si aqui midiera el tiempo solo estaria midiendo el tiempo de creacion 
         * de hilos
         * Si pones el join() estas poniendo una barrera, para que todos los hilos
         * regresen al hilo "original", pero esto requeriria tener un arreglo con
         * todos los hilos creados y darle join a cada uno (requiere pensar en sincronizacion)
         * Se propone que cada hilo cuando termine imprima con un print el tiempo que se 
         * tardo en su ejecucion (y no requieres ningun tipo de sincronizacion) y ya con esos
         * podemos pasarlo a un archivo csv y analizarlo.
         * Entre mas carga le metas, la desvest se vuelve mayor
         * TCP tiene un mecanismo de control de velocidad, provoca que cuando esta saturado les diga
         * "no tan rapido", va a afectar y va a dar una desviacion estandar mas alta, pues se vuelve
         * mas caotico
         * 
         * Para medir el tiempo con una variable necesito afuerzas una sincronizacion
         * para poder acceder a esa misma variable
         * Si tenemos un vector, podemos guardarlo, pues podemos controlar que el hilo
         * solo acceda a su casilla dentro del vector, sin embargo, necesito sincronizar en algun 
         * momento. 
         */
        
            
    }
}
