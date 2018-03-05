/**
 * @author Ahmed Abdalla
 * @date 3-4-2018
 *
 * Models a city
 */
public class City {
    private double latitude;
    private double longitude;
    private String name;

    /**
     * Constructs correct and complete city
     *
     * @param lat latitude
     * @param lon longitude
     * @param n name
     */
    public City(double lat, double lon, String n){
        latitude = lat;
        longitude = lon;
        name = n;
    }

    /**
     * @return latitude
     */
    public double getLatitude() {
        return latitude;
    }

    /**
     * @return longitude
     */
    public double getLongitude() {
        return longitude;
    }

    /**
     * @return name
     */
    public String getName() {
        return name;
    }
}
