package pokemons;

import moves.Energy_Ball;
import moves.Facade;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Mudkip extends Pokemon {
    public Mudkip(String name,int level){
        super(name,level);
        setStats(50,70,50,50,50,40);
        setType(Type.WATER);
        setMove(new Facade(),new Energy_Ball());
    }
}

