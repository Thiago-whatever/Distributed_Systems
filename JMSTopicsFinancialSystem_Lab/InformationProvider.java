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

            Session session = connection.createSession(false /*Transacter*/, Session.AUTO_ACKNOWLEDGE);
            Destination destination;

            for(int i = 0; i < numMessages; i++){
                numCategory = rand.nextInt(5); //Generates random number between 0 and 4
                subject = categories[numCategory];
                destination = session.createTopic(subject);
                newsLevel = rand.nextInt(10)+1; //Generates random number between 1 and 10

                messageProducer = session.createProducer(destination);
                textMessage = session.createTextMessage();

                textMessage.setText(String.valueOf(newsLevel));
                System.out.println("Sending terrible market news. Level: " +newsLevel+ ". Category: "+subject);
                messageProducer.send(textMessage);
                Thread.sleep(2000);
            }

            for(int i = 0; i<5; i++){
                subject = categories[i];
                destination= session.createTopic(subject);
                messageProducer = session.createProducer(destination);
                textMessage = session.createTextMessage();
                
                textMessage.setText("Good bye!");
                System.out.println("Sending good bye");
                messageProducer.send(textMessage);

                messageProducer.close();
            }

            session.close();
            connection.close();
        } catch (JMSException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
        new InformationProvider().produceMessages(15);
    }
}
