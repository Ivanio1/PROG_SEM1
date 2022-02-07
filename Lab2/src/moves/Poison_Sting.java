package moves;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Poison_Sting extends PhysicalMove {
    public  Poison_Sting(){
        super(Type.POISON,15,100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect ef = new Effect();
        ef.chance(0.3);
        ef.poison(p);
        p.addEffect(ef);
    }
    @Override
    protected String describe(){
        return ("Использует Poison Sting - Имеет 30% шанс отравить цель");
    }
}
