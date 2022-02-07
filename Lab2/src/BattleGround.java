
import pokemons.*;
import ru.ifmo.se.pokemon.Battle;

public class BattleGround {
    public static void main(String[] args) {
        Battle b = new Battle();
        Marshtomp Marsh = new Marshtomp("Petya", 1);
        b.addAlly(Marsh);
        b.go();
    }
}


