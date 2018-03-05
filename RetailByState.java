import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class RetailByState {
    public static void main(String[] args){
        try{
            FileReader fr = new FileReader("C:/Users/Ibrahim/Desktop/test.txt");
            BufferedReader bf = new BufferedReader(fr);

            int num = 0;
            String line;
            while((line = bf.readLine()) != null){
                String[] storeInfo = line.split("\t");

                num += Integer.parseInt(storeInfo[1]);
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