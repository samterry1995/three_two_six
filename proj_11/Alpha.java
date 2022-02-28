//Samuel Terry 6786350
import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.io.IOException;
import java.util.regex.*;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Alpha {
        public static void main(String [] args) {
        String newWord =  "";
        List<String> words = new ArrayList<String>();
        try {
            Scanner s = new Scanner(new File(args[0]));        
            while (s.hasNext()) {
                Matcher m = Pattern.compile("(^[a-zA-Z]|^\"[a-zA-Z])[a-z]*[\']?[a-z]*[!,.:;?\"]?$").matcher(s.next());
                if (m.find()) {
                    newWord = m.group().replaceAll("([!,.:;?\"]?)", "");
                    newWord = newWord.toLowerCase();
                    words.add(newWord);                   
                }         
            }
            List<String> noDups = words.stream().distinct().collect(Collectors.toList());
            Collections.sort(noDups);
            noDups.forEach(t -> System.out.println(t));
          } 
            catch (IOException e) {
                System.out.println("Error accessing input file!");
          }
    }
}