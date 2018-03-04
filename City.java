public class City {
    private double latitude;
    private double longitude;
    private String name;

    public City(double lat, double lon, String n){
        latitude = lat;
        longitude = lon;
        name = n;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public String getName() {
        return name;
    }
}
