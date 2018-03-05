import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * @author Ahmed Abdalla
 * @date 3-4-2018
 *
 * Calculates distances between all nodes in a globe from a text file
 */
public class DistanceCalculator {

    /**
     * Reads cities from file and outputs distances between all nodes
     *
     * @param args
     */
    public static void main(String[] args){
        try{
            //Creates reader for text file desktop
            FileReader fr = new FileReader("C:/Users/Ibrahim/Desktop/test.txt");
            BufferedReader bf = new BufferedReader(fr);

            List<City> cities = new ArrayList<>();
            String line;
            while((line = bf.readLine()) != null){
                String[] cityInfo = line.split("\t");   //splits all city info into a String[]

                //adds all cities to cities list
                if(!cityInfo[0].equals("USPS"))  {
                    double lat = Double.parseDouble(cityInfo[8]);
                    double lon = Double.parseDouble(cityInfo[9]);
                    String name = cityInfo[3];
                    City city = new City(lat, lon, name);

                    cities.add(city);
                }
            }

            //prints distance between all points to text file
            FileWriter fw = new FileWriter("C:/Users/Ibrahim/Desktop/County_Distances.txt");
            PrintWriter pw = new PrintWriter(fw);
            for(int i = 0; i < cities.size() - 1; i++){
                for(int j = i+1; j < cities.size(); j++){
                    double distance = haversian(cities.get(i).getLatitude(),
                                                cities.get(i).getLongitude(),
                                                cities.get(j).getLatitude(),
                                                cities.get(j).getLongitude());

                    pw.println(cities.get(i).getName() + " --> " + cities.get(j).getName() + " : " + distance);
                }
            }
        }
        catch(IOException e){
            System.err.println("You dun goofed");
            e.printStackTrace();
        }
    }

    /**
     * Uses Haversian method to find distance between two points on a globe
     *
     * @param lat1 latitude of point one
     * @param lon1 longitude of point one
     * @param lat2 latitude of point two
     * @param lon2 longitude of point two
     * @return distance between two points on a glob
     */
    public static double haversian(double lat1, double lon1, double lat2, double lon2){
        final int R = 6371; //radius of Earth

        //distance converted to radians from degrees
        double latDistance = Math.toRadians(lat2 - lat1);
        double lonDistance = Math.toRadians(lon2 - lon1);

        //haversian implementation
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        //value converted to meters
        return R * c * 1000;
    }
}
