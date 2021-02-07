package travels.service;

import edu.fudan.common.util.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import travels.entity.TravelInfo;
import travels.entity.Trip;
import travels.entity.TripId;
import travels.repository.TripRepository;

/**
 * @author Lei
 * @version 0.1
 * @date 2021/2/7
 */
@Service
public class TravelsServiceImpl implements TravelsService{

    @Autowired
    private TripRepository repository;


    @Override
    public Response create(TravelInfo info, HttpHeaders headers) {
        TripId ti = new TripId(info.getTripId());
        if (repository.findByTripId(ti) == null) {
            Trip trip = new Trip(ti, info.getTrainTypeId(), info.getStartingStationId(),
                    info.getStationsId(), info.getTerminalStationId(), info.getStartingTime(), info.getEndTime());
            trip.setRouteId(info.getRouteId());
            repository.save(trip);
            return new Response<>(1, "Create trip:" + ti.toString() + ".", null);
        } else {
            return new Response<>(1, "Trip " + info.getTripId().toString() + " already exists", null);
        }
    }

    @Override
    public Response update(TravelInfo info, HttpHeaders headers) {
        TripId ti = new TripId(info.getTripId());
        if (repository.findByTripId(ti) != null) {
            Trip trip = new Trip(ti, info.getTrainTypeId(), info.getStartingStationId(),
                    info.getStationsId(), info.getTerminalStationId(), info.getStartingTime(), info.getEndTime());
            trip.setRouteId(info.getRouteId());
            repository.save(trip);
            return new Response<>(1, "Update trip:" + ti.toString(), trip);
        } else {
            return new Response<>(1, "Trip" + info.getTripId().toString() + "doesn 't exists", null);
        }
    }

    @Override
    public Response delete(String tripId, HttpHeaders headers) {
        TripId ti = new TripId(tripId);
        if (repository.findByTripId(ti) != null) {
            repository.deleteByTripId(ti);
            return new Response<>(1, "Delete trip:" + tripId + ".", tripId);
        } else {
            return new Response<>(0, "Trip " + tripId + " doesn't exist.", null);
        }
    }
}
