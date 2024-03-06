import jakarta.jms.Connection;
import jakarta.jms.ConnectionFactory;
import jakarta.jms.Destination;
import jakarta.jms.JMSException;
import jakarta.jms.MessageProducer;
import jakarta.jms.Session;
import jakarta.jms.TextMessage;

import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import java.util.Random;

public class InformationProvider {

    private static String url = ActiveMQConnection.DEFAULT_BROKER_URL;
    // default broker URL is : tcp://localhost:61616"|


    private static String subject = ""; // Queue Name. You can create any/many queue names as per your requirement.

    private static String [] categories = {"Telecommunications","Banks","Transportation","FoodSupply","Education"};


    public void produceMessages(int numMessages) {
        MessageProducer messageProducer;
        TextMessage textMessage;
        Random rand = new Random();
        int numCategory=0, newsLevel=0;

        try {

            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
            Connection connection = connectionFactory.createConnection();
            connection.start();

            numCategory = rand.nextInt(5); //Generates random number between 0 and 4
            subject = categories[numCategory];
            Session session = connection.createSession(false /*Transacter*/, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(subject);

            messageProducer = session.createProducer(destination);
            textMessage = session.createTextMessage();


            for(int i = 0; i < numMessages; i++){
                newsLevel = rand.nextInt(10)+1; //Generates random number between 1 and 10

                textMessage.setText(newsLevel +" I have to be patient. There is no such thing as a 'global economic crisis'");
                System.out.println("Sending the following message: " + textMessage.getText());
                messageProducer.send(textMessage);
            }

            textMessage.setText("Good bye!");
            System.out.println("Sending the following message: " + textMessage.getText());
            messageProducer.send(textMessage);

            messageProducer.close();
            session.close();
            connection.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
        new InformationProvider().produceMessages(5);
    }
}
