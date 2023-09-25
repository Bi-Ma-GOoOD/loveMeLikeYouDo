# :minidisc: COMPUTER-ARCHITECTURE :floppy_disk:
## :calender: This All For Final :date:
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
* Read 12nd chapters in slide **12-Memory Translation** finished 19:30 On 24/09/2023 :ocean:
    ```
    > Memory Address Translation อันนี้เขาประมาณว่าแบบ ในคอมอะมีการใช้ พื้นที่จำลองขึ้นมา พอมีการขอเข้าถึงข้อมูลนั้นในหน่วยความจำจริงๆ ต้องมีการแปลงจาก virtual->physical ผ่าน memory translation
    > Virtual Memory จะมีส่วนประกอบทั้งหมด 5 ส่วน ได้แก่
        > Pages and Frames ส่วนนี้คือ pages จะใช้เรียกหน่วยพื้นที่ใน virtual mem ส่วน frames จะใช้เรียกหน่วนพื้นที่ที่เก็บอยู่ในหน่วยความจำจริง(physical mem)
        > Page Tables คือการที่เราแปลงว่า virtual mem นี้อะงับ เขาจะไปเก็บข้อมูลที่ไหนใน physical mem โดยทุกๆ โปรแกรมอะงับ จะมี page tables ของตัวเอง โดยเราจะแปลงจาก pages -> frame
        > Page Table Entries(PTEs) อะงับ เขาจะเก็บว่า page นี้จาก virtual อะงับ จะเอาไปเก็บใน Physical Address ไหน
        > Translation Lookaside Buffer(TLB) กล่าวง่ายๆ น้องคือตัวเก็บข้อมูล frame แค่นั้นเลยงับ โดยตัว TLB ตัวนี้อะ เขาจะพยายามช่วยลด overhead การเข้าถึงข้อมูล  จาก virtual->physical คือน้องอยากจะพยายามช่วยให้ตัวของ page tables อะคับ แยกได้ว่า เออ virtual นี้ควรอยู่ใน physical นี้นะโดยใช้เวลาให้น้อยลงอะงับอยากให้ไว ว่างั้นแหละ
        > Memory Management Units(MMUs) คือ Hardware ที่สั่งให้ส่วนประกอบข้างต้นที่กล่าวมาอะงับ ทำงาน แค่นี้เลยงับ
    ```