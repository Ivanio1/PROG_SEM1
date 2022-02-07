package pokemons;

import moves.Poison_Sting;
import moves.Rest;
import moves.Thunderbolt;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Staryu extends Pokemon {
    public Staryu(String name,int level){
        super(name,level);
        setStats(30,45,55,70,55,85);
        setType(Type.WATER);
        setMove(new Thunderbolt(),new Poison_Sting(),new Rest());
    }
}

