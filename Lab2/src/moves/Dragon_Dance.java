package moves;

import ru.ifmo.se.pokemon.*;

public class Dragon_Dance extends StatusMove {
    public  Dragon_Dance(){
        super(Type.DRAGON,0,0);
    }
    @Override
    protected void applySelfEffects(Pokemon p) {
        Effect effect=new Effect();
        effect.stat(Stat.SPEED,+1);
        effect.stat(Stat.ATTACK,+1);
        p.addEffect(effect);
    }
    @Override
    protected String describe(){
        return ("Использует Dragon Dance - Повышает свою Атаку и Скорость на одну ступень каждую");
    }
}
