
package moves;

import ru.ifmo.se.pokemon.*;

public class Swagger extends StatusMove {
    public Swagger() {
        super(Type.NORMAL, 0, 85);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect ef = new Effect();
        ef.stat(Stat.ATTACK, 2);
        ef.confuse(p);
        p.addEffect(ef);
    }
    @Override
    protected String describe() {
        return ("Использует Swagger - Увеличивает атаку цели на два этапа и сбивает цель с толку");
    }
}
