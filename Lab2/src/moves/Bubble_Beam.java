package moves;

import ru.ifmo.se.pokemon.*;

public class Bubble_Beam extends SpecialMove {
    public Bubble_Beam(){
        super(Type.WATER,65,100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect effect=new Effect();
        effect.chance(0.1);
        effect.stat(Stat.SPEED,-1);
        p.addEffect(effect);
    }
    @Override
    protected String describe(){
        return ("Использует Bubble Beam - имеет 10% шанс понизить скорость цели на одну ступень");

    }
}
