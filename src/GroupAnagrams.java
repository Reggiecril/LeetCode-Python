import java.util.*;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> outList=new ArrayList<>();
        if(strs==null||strs.length==0)
            return outList;
        Map<String,List<String>> map=new HashMap<>();
        for(String str:strs){
            char[] ch=str.toCharArray();
            Arrays.sort(ch);
            String newStr=String.valueOf(ch);
            if (map.containsKey(newStr)){
                map.get(newStr).add(str);
            }else{
                List<String> inList=new ArrayList<>();
                inList.add(str);
                map.put(newStr,inList);
            }

        }
        return new ArrayList<>(map.values());

    }
}
