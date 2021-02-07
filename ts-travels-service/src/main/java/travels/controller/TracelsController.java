package travels.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import travels.entity.TravelInfo;
import travels.service.TravelsService;

import static org.springframework.http.ResponseEntity.ok;

/**
 * @author Lei
 * @version 0.1
 * @date 2021/2/7
 */
@RestController
@RequestMapping("/api/v1/travelsservice")
public class TracelsController {

    @Autowired
    private TravelsService service;

    @CrossOrigin(origins = "*")
    @PostMapping(value = "/trips")
    public HttpEntity<?> createTrip(@RequestBody TravelInfo routeIds, @RequestHeader HttpHeaders headers) {
        // null
        return new ResponseEntity<>(service.create(routeIds, headers), HttpStatus.CREATED);
    }

    @CrossOrigin(origins = "*")
    @PutMapping(value = "/trips")
    public HttpEntity updateTrip(@RequestBody TravelInfo info, @RequestHeader HttpHeaders headers) {
        // Trip
        return ok(service.update(info, headers));
    }

    @CrossOrigin(origins = "*")
    @DeleteMapping(value = "/trips/{tripId}")
    public HttpEntity deleteTrip(@PathVariable String tripId, @RequestHeader HttpHeaders headers) {
        // string
        return ok(service.delete(tripId, headers));
    }
}
