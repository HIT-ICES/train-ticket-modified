package travels2.service;

import edu.fudan.common.util.Response;
import org.springframework.http.HttpHeaders;
import travels2.entity.TravelInfo;

/**
 * @author Lei
 * @version 0.1
 * @date 2021/2/7
 */
public interface Travels2Service {
    Response create(TravelInfo info, HttpHeaders headers);

    Response update(TravelInfo info, HttpHeaders headers);

    Response delete(String tripId, HttpHeaders headers);
}
