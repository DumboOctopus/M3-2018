import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class DistanceCalculator {
    public static void main(String[] args){
        try{
            FileReader fr = new FileReader("C:/Users/Ibrahim/Desktop/test.txt");
            BufferedReader bf = new BufferedReader(fr);

            List<City> cities = new ArrayList<>();
            String line;
            while((line = bf.readLine()) != null){
                String[] cityInfo = line.split("\t");

                if(!cityInfo[0].equals("USPS")) {
                    double lat = Double.parseDouble(cityInfo[8]);
                    double lon = Double.parseDouble(cityInfo[9]);
                    String name = cityInfo[3];
                    City city = new City(lat, lon, name);

                    cities.add(city);
                }
            }

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

    public static double haversian(double lat1, double lon1, double lat2, double lon2){
        final int R = 6371;

        double latDistance = Math.toRadians(lat2 - lat1);
        double lonDistance = Math.toRadians(lon2 - lon1);

        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        return R * c * 1000;
    }
}
