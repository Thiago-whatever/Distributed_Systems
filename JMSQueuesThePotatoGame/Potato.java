import java.io.Serializable;

public class Potato implements Serializable{
    public int id;
    public int time_to_burn;

    public Potato(int id, int time_to_burn){
        this.id = id;
        this.time_to_burn = time_to_burn;
    }
}
