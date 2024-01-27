package server;

public class AddressBook {
    private Person [] bookPersons;
    private int total;
    private int count;

    public AddressBook(int total){
        this.total = total;
        count = 0;
        bookPersons = new Person[total];
    }

    public void add (){
        try{
            bookPersons[count] = new Person();
            count ++;
        }catch(Exception e){
            System.out.println("No se pudo agregar la persona al directorio: "+e);
        }
    }

    public void add(int id, String nombre){
        try{
            bookPersons[count] = new Person(id,nombre);
            count ++;
        }catch(Exception e){
            System.out.println("No se pudo agregar la persona al directorio: "+e);
        }
    }

    public int Count(){
        return count-1;
    }

    public Person getRecord(int key){
        Person res = null;
        boolean band = false;
        int i = 0;

        while(!band && i<total && i <= count){
            if(bookPersons[i].getId()==key){
                res = bookPersons[i];
                band = true;
            }
            else
                i++;
        }

        return res;
    }

    public String toString(){
        StringBuilder res = new StringBuilder();
        Person aux;
        for (int i = 0; i<=total-1; i++){
            aux=bookPersons[i];
            if(aux != null)
                res.append("Key: "+ aux.getId()+ " con Nombre: "+aux.getName()+"\n");
        }
        return res.toString();
    }
}
