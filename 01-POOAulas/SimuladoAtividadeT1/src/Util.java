import java.util.*;

public class Util {

    public static void clearScreen() {  
        System.out.print("\033[H\033[2J");  
        System.out.flush();  
    }  

    public static Boolean validateString(String value) {
        return value != null && value != "";
    }

    public static Boolean verifyContainsKey(Map<String, Object> mapObj, String key) {
        return (mapObj != null && verifyKey(mapObj, key));
    }

    public static Boolean verifyKey(Map<String, Object> mapObj, String key) {
        return (validateString(key) && mapObj.containsKey(key) && mapObj.get(key) != null && String.valueOf(mapObj.get(key)) != "");
    }

    public static String convertString(Object value, Boolean lower) {
        return (lower) ? String.valueOf(value).toLowerCase() : String.valueOf(value);
    }

    public static Boolean checkList(List<Object> lstValue) {
        return (lstValue != null && lstValue.size() > 0);
    }

    // public String toString(){
    //     return ""
    // }
}
