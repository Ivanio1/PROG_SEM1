package moves;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Blizzard extends SpecialMove {
    public  Blizzard(){
        super(Type.ICE,110,70);
    }
    @Override
    protected void applyOppEffects(Pokemon p){
        Effect effect=new Effect();
        effect.chance(0.1);
        effect.freeze(p);
        p.addEffect(effect);
    }
    @Override
    protected String describe(){
        return ("Использует Blizzard - Имеет 10% шанс заморозить цель");
    }
}
