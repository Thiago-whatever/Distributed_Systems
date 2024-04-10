public class PotatoGame {

    public static void main(String[] args) {
        // Crear dos jugadores
        Player player1 = new Player("Jugador 1", 1);
        Player player2 = new Player("Jugador 2", 2);

        // Crear dos papas con tiempos aleatorios para "caerse"
        Potato potato1 = new Potato(1, (int) (Math.random() * 10) + 1);
        Potato potato2 = new Potato(2, (int) (Math.random() * 10) + 1);

        // Iniciar el juego aventando las papas
        new Thread(() -> player1.throwPotato(potato1)).start();
        new Thread(() -> player2.throwPotato(potato2)).start();

        // Los jugadores comienzan a verificar si reciben la papa.
        new Thread(player1::checkForPotato).start();
        new Thread(player2::checkForPotato).start();
    }
}
