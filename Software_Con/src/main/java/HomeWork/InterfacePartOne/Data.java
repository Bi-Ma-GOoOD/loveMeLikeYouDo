/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.InterfacePartOne;

public class Data {
    public static double min(MeasurableForLeast[] objects){
        double min = 9999999;

        for(MeasurableForLeast obj : objects)
            if(obj.getMeasureForLeast() < min) {
                min = obj.getMeasureForLeast();
            }

        return min;
    }
    public static void sort(Comparable[] a) {
        for (int i = 0; i < a.length - 1; i++) {// i แบ่งส่วนเรียงแล้วกับยังไม่เรียง
            int minPos = i;
            for (int j = i + 1; j < a.length; j++) { // วนลูปหาค่าน้อยสุด
                if ((a[j].compareTo(a[minPos]) < 0)){
                    minPos = j;
                }
            }
            // สลับข้อมูลใน minPos และ i ทําให้ข้อมูลใน minPos ไปอยู่ส่วนที่เรียงแล้ว
            Comparable temp = a[minPos];
            a[minPos] = a[i];
            a[i] = temp;
        }
    }
}
