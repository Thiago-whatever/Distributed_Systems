package server;

public class pruebas {
    public static void main(String args[]) {
        AddressBook addressBook = new AddressBook(10);
        for(int i = 0; i<=5; i++){
            addressBook.add();
        }

        addressBook.add(13, "Mariel");
        addressBook.add(14,"China");
        addressBook.add(15,"Santiago");
        addressBook.add(18,"Angel");

        System.out.println("La cantidad de personas guardadas en el directorio es: "+addressBook.Count());
        System.out.println("La persona con id" + 13 + " se llama: "+addressBook.getRecord(13).getName());
        System.out.println(addressBook.toString());
    }
}
