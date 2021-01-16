package travel2.entity;

import lombok.Data;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.Date;

/**
 * @author fdse
 */
@Data
public class Seat {
    @Valid
    @NotNull
    private Date travelDate;

    @Valid
    @NotNull
    private String trainNumber;


    @Valid
    @NotNull
    private String startStation;

    @Valid
    @NotNull
    private String destStation;

    @Valid
    @NotNull
    private int seatType;

    // 携带的参数
    private Route route;

    private TrainType trainType;


    public Seat(){
        //Default Constructor
        this.travelDate = new Date();
        this.trainNumber = "";
        this.startStation = "";
        this.destStation = "";
        this.seatType = 0;

        // 新增
        this.route = new Route();
        this.trainType = new TrainType();
    }

    @Override
    public String toString() {
        return "Seat{" +
                "travelDate=" + travelDate +
                ", trainNumber='" + trainNumber + '\'' +
                ", startStation='" + startStation + '\'' +
                ", destStation='" + destStation + '\'' +
                ", seatType=" + seatType +
                ", route=" + route +
                ", trainType=" + trainType +
                '}';
    }
}
