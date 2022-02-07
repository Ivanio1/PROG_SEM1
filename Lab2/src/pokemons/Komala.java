package pokemons;

import moves.Blizzard;
import moves.Bubble_Beam;
import moves.Dragon_Dance;
import moves.Waterfall;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Komala extends Pokemon {
        public Komala(String name,int level){
                super(name,level);
                setStats(65,115,65,75,95,65);
                setType(Type.NORMAL);
                setMove(new Waterfall(),new Blizzard(),new Dragon_Dance(),new Bubble_Beam());

        }
}
