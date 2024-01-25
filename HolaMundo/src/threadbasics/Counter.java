package threadbasics;

public class Counter {
    private int count = 0;

    public Counter(int count){
        this.count = 0;
    }

    public void increase(String threadId){ 
        //la palabra reservada synchronized -> define unas regiones (llamadas regiones criticas)
        //garantiza que el primer hilo tome la llave para entrar a la region, haga lo suyo, se vaya y deje la llave
        //para que el segundo hilo pueda entrar; se ocupa para partes de codigo muy chicos, en estas regiones no hay concurrencias
        //por eso queremos minimizarlas, no tengo condiciones de carrera
        // si la pongo arriba (en el nombre del metodo "private synchronized void increase"), estoy diciendo que la region critica es todo el metodo
        // si la pongo abajo, estoy diciendo que la region critica son solo dos lineas
        // entre más chiquito mejor, pero tambien valdria la pena revisar que es mejor
        for(int i=0;i<10000;i++){
            synchronized(this){
                count++;
                System.out.println(threadId +  " incrementó "+ count);
            }
            
        }

        //Si tenemos el synchronized en el método vamos a tener h1 0-999 y luego h0 1000-1999 o primero h0 y luego h1
        //Si lo tenemos como esta ahorita habria un entrelazamiento muy cañon
    }
}
