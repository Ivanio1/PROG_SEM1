package files;

public class Goosebumps {
    private String name = "Мурашки";
    private Goosebumps_place Status;

    public Goosebumps(Goosebumps_place place) {
        this.Status = place;
    }

    public Goosebumps_place getStatus() {
        return Status;
    }

    public void run(int n, Goosebumps bumps) {
        if (n == 1) {
            if (bumps.getStatus() == Goosebumps_place.back) {
                System.out.println(this.name + " побежали по спине.");
            }
            if (bumps.getStatus() == Goosebumps_place.legs) {
                System.out.println(this.name + " побежали по ногам.");
            }
            if (bumps.getStatus() == Goosebumps_place.arms) {
                System.out.println(this.name + " побежали по рукам.");
            }
            if (bumps.getStatus() == Goosebumps_place.stomach) {
                System.out.println(this.name + " побежали по животу.");
            }
        }
    }
}
