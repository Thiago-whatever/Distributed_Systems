

public class Deployer {

    public static void main(String[] args) {
        String [] categories = {"Telecommunications","Banks","Transportation","FoodSupply","Education"};
        System.out.println("hola mundo");
        FloorBroker [] brokers= new FloorBroker[5];
        for(int i = 0; i < 5; i++){
            brokers[i] = new FloorBroker(categories[i]);
            brokers[i].getMessages();
        }
    }
}
