import jakarta.jms.*;
import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;

import java.io.Serializable;

public class Player implements Serializable {
    private String name;
    private static String url = ActiveMQConnection.DEFAULT_BROKER_URL;
    private static String queueName = "POTATO_QUEUE"; // Nombre de la cola para nuestro juego.
    private int id; // Identificador único para cada jugador.

    public Player(String name, int id) {
        this.name = name;
        this.id = id;
    }

    // Método para "aventar" la papa a otro jugador.
    public void throwPotato(Potato potato) {
        try {
            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queueName);

            MessageProducer producer = session.createProducer(destination);

            // Se configura la conexión para permitir el envío de cualquier paquete.
            connectionFactory.setTrustAllPackages(true);

            ObjectMessage message = session.createObjectMessage();
            message.setObject(potato); // Establecemos el objeto papa a enviar.

            System.out.println(this.name + " está aventando la papa con ID: " + potato.id);
            producer.send(message);

            producer.close();
            session.close();
            connection.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }

    // Método para verificar si otro jugador ha aventado una papa.
    public void checkForPotato() {
        try {
            ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
            Connection connection = connectionFactory.createConnection();
            connection.start();

            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Destination destination = session.createQueue(queueName);

            MessageConsumer consumer = session.createConsumer(destination);

            // Espera recibir un mensaje durante un tiempo máximo (por ejemplo, 5 segundos).
            ObjectMessage message = (ObjectMessage) consumer.receive(5000);

            if (message != null) {
                Potato potato = (Potato) message.getObject();
                System.out.println(this.name + " ha recibido la papa con ID: " + potato.id);

                // Verifica si el tiempo para "caerse" es 0.
                if (potato.time_to_burn <= 0) {
                    System.out.println("¡La papa se ha caído! " + this.name + " ha perdido.");
                    // Aquí podrías terminar el juego o manejar la derrota.
                } else {
                    // Si aún tiene tiempo, decrementa y avienta de nuevo.
                    potato.time_to_burn--;
                    throwPotato(potato);
                }
            }

            consumer.close();
            session.close();
            connection.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}

