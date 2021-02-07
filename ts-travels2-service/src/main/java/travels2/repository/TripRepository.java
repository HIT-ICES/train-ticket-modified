package travels2.repository;

import org.springframework.data.repository.CrudRepository;
import travels2.entity.Trip;
import travels2.entity.TripId;

/**
 * @author Lei
 * @version 0.1
 * @date 2021/2/7
 */
public interface TripRepository extends CrudRepository<Trip, TripId> {

    Trip findByTripId(TripId tripId);

    void deleteByTripId(TripId tripId);
}
