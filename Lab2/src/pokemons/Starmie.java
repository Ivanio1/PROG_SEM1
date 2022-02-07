package pokemons;

import moves.Focus_Energy;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Starmie extends Staryu {
    public Starmie(String name,int level){
        super(name,level);
        setStats(60,75,85,100,85,115);
        setType(Type.PSYCHIC);
        setMove(new Focus_Energy());
    }
}

