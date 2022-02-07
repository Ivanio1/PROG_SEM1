package pokemons;
import moves.Swagger;

public class Swampert extends Marshtomp {
    public Swampert(String name,int level){
        super(name,level);
        setStats(100,110,90,85,90,60);
        setMove(new Swagger());
    }
}

