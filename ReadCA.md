# :minidisc: COMPUTER-ARCHITECTURE :floppy_disk:
## :calendar: This All For Final :date:
### :ferris_wheel: I THINK I SEE YOU ~ ~ ~ :carousel_horse:
![This is picture.](/Images/Inspiration_n_love/I-Think-I-See-You.jpg "A Sky Full Of Star.")
### Ta Ter Rak Chan Jing :headphones:
* Read 11st chapters in slide **11-Memory Protection** finished 11:40 On 13/09/2023 :hotsprings:
    ```
    > Privilege Levels จะกล่าวเกี่ยวกับว่า Privilege มี 2 mode คือ user mode และ kernal mode(Supervisor)
    > Memory Protection Unit คือ การเช็คข้อมูลว่า สิ่งที่ cpu ร้องขอมา process นี้มีสิทธิ์ที่จะเข้าถึงพื้นที่ไหนบ้าง โดยการตรวจสอบนั้นจะเกิดจาก kernal OS
        > โดยภายใน memory protection unit(MPU) จะมี segment registers ที่จะคอยเก็บข้อมูลของ process นั้น
        > ข้อมูลของ process จะถูกแบ่งออกเป็นส่วนๆ เมื่อถูกนำมาเก็บใน segment registers ซึ่ง ถูกแบ่งออกได้ 4 ส่วน ได้แก่ 
            > DS : Data Segment 
            > SS : Stack Segment
            > ES : Extra Segment
            > CS : Code Segment
            โดยขนาดของแต่ละ segment นั่นจะถูก fix ไว้แล้ว
    > Address Space Layout Randomization คือหลักการที่เราจะเปลี่ยนที่อยู่ของข้อมูลตลอด เมื่อเกิดการเข้าถึง โดยใช้ padding นั่นเองงงับ ต่อจากนั่นก็อ่านต่อเองเลย เกริ่นมาแล้ว
    ```