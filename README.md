# :crystal_ball: Love-Me-Like-You-Do :sparkles:

## :gift: This All For Final :tada:

### :capricorn: MY FAVOURITE :stars:
![This is picture.](/Images/Inspiration_n_love/duo.jpg "Go To Dream!")

### :minidisc: MY WORK :thought_balloon:
* Art-Work -> My_Beginner_work :beginner:

### :hourglass_flowing_sand: Want To Know About Mid-Term <-b714063-> :hourglass_flowing_sand:

### Software Construction Lecture :trident:
* Read 8th chapters in slied **08 I/O** finished  18:43 On 10/09/2023 :books:
    ```
    -> read อ่านทีละตัว ส่วนถ้าใช้ readline อ่านได้เลยทีละบรรทัด ค่าที่อ่านได้เป็น String ทั้งสิ้น ตัวเลขก็เป็น String แต่มีวิธีอ่านเป็นตัวเลขด้วย Integer.parseInt(string) อะไรก็ว่าไป
    -> มี InputSteamReader/FileReader ใช้อ่านจากหน้าจอ และไฟล์ตามลำดับ
    -> printWriter/BufferWriter/print&&Buffer ใช้เขียนไฟล์ ความเร็วเรียงจากหน้ามาหลัง ทำงานด้วยกันก็ยิ่งเร็ว
    -> การปิดไฟล์ สำคัญมาก!!!
    -> แล้วก็มีการเขียน obj เขียนได้นะ แต่เปิดขึ้นมายังไงไม่รู้ขึ้นมาเป็นรหัส something 
    -> Serialization[เขียน เป็น Binary] Deserialization อ่าน
    ```
### Computer Architecture :children_crossing:
* Read 11st chapters in slide **11 Memory Protection** finished 11:40 On 13/09/2023 :hotsprings:
    ```
    -> Privilege Levels จะกล่าวเกี่ยวกับว่า Privilege มี 2 mode คือ user mode และ kernal mode(Supervisor)
    -> Memory Protection Unit คือ การเช็คข้อมูลว่า สิ่งที่ cpu ร้องขอมา process นี้มีสิทธิ์ที่จะเข้าถึงพื้นที่ไหนบ้าง โดยการตรวจสอบนั้นจะเกิดจาก kernal OS
        ->> โดยภายใน memory protection unit(MPU) จะมี segment registers ที่จะคอยเก็บข้อมูลของ process นั้น
        ->> ข้อมูลของ process จะถูกแบ่งออกเป็นส่วนๆ เมื่อถูกนำมาเก็บใน segment registers ซึ่ง ถูกแบ่งออกได้ 4 ส่วน ได้แก่ 
            ->>> DS : Data Segment 
            ->>> SS : Stack Segment
            ->>> ES : Extra Segment
            ->>> CS : Code Segment
            โดยขนาดของแต่ละ segment นั่นจะถูก fix ไว้แล้ว
    -> Address Space Layout Randomization คือหลักการที่เราจะเปลี่ยนที่อยู่ของข้อมูลตลอด เมื่อเกิดการเข้าถึง โดยใช้ padding นั่นเองงงับ ต่อจากนั่นก็อ่านต่อเองเลย เกริ่นมาแล้ว
    ```