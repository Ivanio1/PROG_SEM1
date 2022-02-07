package moves;

import ru.ifmo.se.pokemon.*;

public class Focus_Energy extends StatusMove {
    public  Focus_Energy(){
        super(Type.NORMAL,0,0);
    }
    @Override
    protected void applySelfEffects(Pokemon p) {
        Effect ef = new Effect();
        ef.chance(+Math.random());
        ef.stat(Stat.SPECIAL_ATTACK,+1);
        p.addEffect(ef);
    }
    @Override
    protected String describe(){
        return ("Использует Focus Energy - Увеличивает шанс покемона нанести критический удар");
    }
}
