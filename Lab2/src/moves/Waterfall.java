package moves;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Waterfall extends PhysicalMove {
    public Waterfall() {
        super(Type.WATER, 80, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect ef = new Effect();
        ef.chance(0.2);
        ef.flinch(p);
        p.addEffect(ef);
    }
    @Override
    protected String describe() {
        return ("Использует Waterfall - Имеет 20% шанс заставить цель вздрогнуть");
    }
}
