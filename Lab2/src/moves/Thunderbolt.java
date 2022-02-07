package moves;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Thunderbolt extends SpecialMove {
    public  Thunderbolt(){
        super(Type.ELECTRIC,90,100);
    }
    @Override
    protected void applyOppEffects(Pokemon p){
        Effect ef = new Effect();
        ef.chance(0.1);
        ef.paralyze(p);
        p.addEffect(ef);
    }
    @Override
    protected String describe(){
        return ("Использует Thunderbolt - Имеет 10% шанс парализовать цель");
    }
}
