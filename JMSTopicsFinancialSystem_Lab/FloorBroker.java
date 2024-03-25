import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import jakarta.jms.Connection;
import jakarta.jms.ConnectionFactory;
import jakarta.jms.Destination;
import jakarta.jms.JMSException;
import jakarta.jms.MessageConsumer;
import jakarta.jms.Session;
import jakarta.jms.TextMessage;

public class FloorBroker {

    // URL of the JMS server
    private static String url = ActiveMQConnection.DEFAULT_BROKER_URL;
    // default broker URL is : tcp://localhost:61616"

    // Name of the queue we will receive messages from
    private static String subject = "";

    public FloorBroker(String category){
        this.subject=category;
    }

    public void getMessages() {

        boolean goodByeReceived = false;

        try {
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false /*Transacter*/, Session.AUTO_ACKNOWLEDGE);

            Destination destination = session.createTopic(subject);

            MessageConsumer messageConsumer = session.createConsumer(destination);

            while (!goodByeReceived) {
                System.out.println("Waiting for messages...");
                System.out.println("I'm a floor broker handling "+subject+ " accounts");

                TextMessage textMessage = (TextMessage) messageConsumer.receive();
                if (textMessage != null && !textMessage.getText().equals("Good bye!")) {
                    int level = Integer.parseInt(textMessage.getText());
                    System.out.println("I received bad news of level: "+level);
                    if(level < 5){
                        
                        System.out.println("I have to be patient. There is no such thing as a 'global economic crisis'");
                    }
                    else{
                        System.out.println("Selling! Selling! Selling!");
                    }
                }
                if (textMessage.getText() != null && textMessage.getText().equals("Good bye!")) {
                    goodByeReceived = true;
                    System.out.println("Financial session ended");
                }
            }

            messageConsumer.close();
            session.close();
            connection.close();

        } catch (JMSException e) {
            e.printStackTrace();
        }
    }

    //Proof that (One) FloorBroker receives messages
    // public static void main(String[] args) {
    //     new FloorBroker("Transportation").getMessages();
    // }

}
