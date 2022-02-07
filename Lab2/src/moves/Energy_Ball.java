package moves;

import ru.ifmo.se.pokemon.*;

public class Energy_Ball extends SpecialMove {
    public Energy_Ball() {

        super(Type.GRASS, 90, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect effect=new Effect();
        effect.chance(0.1);
        effect.stat(Stat.SPECIAL_DEFENSE,-1);
        p.addEffect(effect);
    }
    @Override
    protected String describe() {
        return ("использует Energy Ball - Имеет 10% шанс снизить Специальную защиту цели на одну ступень");
    }
}
