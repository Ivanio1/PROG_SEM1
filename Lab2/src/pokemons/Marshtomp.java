package pokemons;

import moves.*;
import ru.ifmo.se.pokemon.Type;

public class Marshtomp extends Mudkip {
    public Marshtomp(String name,int level){
        super(name,level);
        setStats(70,85,70,60,70,50);
        setType(Type.GROUND);
        setMove(new Dazzling_Gleam());
    }
}

