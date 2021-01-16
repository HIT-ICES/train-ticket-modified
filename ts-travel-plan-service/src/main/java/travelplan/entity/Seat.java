package travelplan.entity;

import lombok.Data;

import java.util.Date;

/**
 * @author fdse
 */
@Data
public class Seat {

    private Date travelDate;

    private String trainNumber;

    private String startStation;

    private String destStation;

    private int seatType;


    private Route route;
    private TrainType trainType;


    public Seat(){
        //Default Constructor
    }

}
