package files;

public class Car implements be_the_greatest{
    private Car_status Status;
    private String name="Паровая машина ";

    public Car(Car_status status) {
        this.Status = status;
    }

    public Car_status getStatus() {
        return Status;
    }

    public void setStatus(Car_status status) {
        this.Status = status;
    }

    public void rotation(Car car) {
        if (car.getStatus() == Car_status.Work) {
            System.out.println("Машина работает и издаёт звуки: 'Фут, фут, фут…'! ");
        } else {
            System.out.println("Машина стоит на месте! ");
        }

    }
    @Override
    public void be_the_greatest() {
        System.out.println(this.name+" была самая прекрасная из всех паровых машин, какие только можно себе вообразить. ");
    }
}
