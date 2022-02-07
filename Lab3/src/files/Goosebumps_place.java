package files;

import java.lang.reflect.Array;

public enum Goosebumps_place {
    back,
    legs,
    arms,
    stomach;

    public String Name(Goosebumps bumps) {
        String s="";
        if (bumps.getStatus() == Goosebumps_place.back) {
            s= "back";
        }
        if (bumps.getStatus() == Goosebumps_place.legs) {
            s= "legs";}
        if (bumps.getStatus() == Goosebumps_place.arms) {
            s= "arms";}
        if (bumps.getStatus() == Goosebumps_place.stomach) {
            s= "stomach";}
        return s;
    }
}

