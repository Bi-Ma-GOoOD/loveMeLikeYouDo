# MID-Term-Test Progress :sunrise_over_mountains:
## Inspiration :shipit:
### MY FAVOURITE :musical_score:
![This is picture.](/Images/Inspiration_n_love/Seraphine_Aquriam.jpg "This is my wife!!!")
### MY WORK :movie_camera:
* You can look my work at Images -> My_Beginner_work :beginner:
### Computer Architecture :house_with_garden:
**Computer Architecture จะมีทั้งหมด 10 สไลด์ที่จะต้องอ่านสอบ**
> แนวข้อสอบกลางภาค
> <br>ประมาณ 10 หัวข้อ จากหัวข้อต่อไปนี้:
>- วิวัฒนาการของระบบคอมพิวเตอร์ :white_check_mark:
>- องค์ประกอบของระบบคอมพิวเตอร์ :white_check_mark:
>- องค์ประกอบของหน่วยประมวลผลกลาง (CPU) :white_check_mark:
>- หน่วยความจำใน CPU (Registers) :white_check_mark:
>- ภาษาแอสเซมบลี (Assembly Language) :white_check_mark:
>- ชุดคำสั่ง (Instruction Set) :white_check_mark:
>- วงจรการทำงานของคำสั่ง (Instruction Cycle) :white_check_mark:
>- สถาปัตยกรรมชุดคำสั่งที่พบบ่อย (Common ISAs) :white_check_mark:
>- วิธีการระบุที่อยู่ (Addressing Modes)
>- ลำดับชั้นหน่วยความจำ (Memory Hierarchy)
>- ความใกล้เคียงกันของข้อมูล (Locality)
>- ผลที่เกิดขึ้นเมื่อมีการร้องขอข้อมูลจากแคช (Cache Events)
>- คุณสมบัติของหน่วยความจำ (Memory Properties) ที่ต้องรักษาไว้
>- หน่วยของแคช (Cache Lines, Cache Sets)
>- วิธีกำหนดที่อยู่แคช (Cache Placement Policies)
>- วิธีแทนที่แคช (Cache Replacement Policies)
>- วิธีเขียนแคช (Cache Write Policies)
>- ตัววัดประสิทธิภาพแคช (Cache Performance Metrics)
><br>แนวคำถาม: คืออะไร ทำหน้าที่อะไร ทำงานอย่างไร มีอะไรบ้าง มีความสัมพันธ์กันอย่างไร
* Read 1st chapter in slide **1 Introduction** finished NULL On 28/07/2023 :triangular_flag_on_post:
    ```
    -> ยุคสมัยแรกของคอม คอมมีขนาดใหญ่มากเท่าห้องเลย และใช้ vacuum tubes ในการส่งข้อมูล
    -> ยุคสมัยที่สองของคอม มีการใช้ Transitors ในการส่งข้อมูลแทน ทำให้คอมเล็กลง
    -> ยุคสมัยที่สามของคม มีการใช้ วงจรรวม(Integrated circuits)
    -> ยุคที่สี่ของคอม เกิดการใช้คอมส่วนบุคคลทำให้บุคคลธรรมดาสามารถจับต้องได้ในราคาที่สามารถเข้าถึงได้
    -> ยุคที่ห้าของคอม คือการพัฒนา Processor และส่วนต่างๆให้มีความรวดเร็วและมีขนาดเล็กมากขึ้น
    -> ส่วนประกอบคอม Cpu-Mem-In/Out-Bus system
    -> วิธีต่างๆที่สามารถทำให้คอมมีประสิทธิภาพที่มากขึ้น
    ```
* Read 2nd chapter in slide **2 Components** finished NULL on 08/08/2023 :rainbow:
    ```
    -> บทนี้จะกล่าวเกี่ยวกับ แบบว่า Cpu->ALU-o-Register-o-Control Unit-o-Cache-o-Main Memory-o-I/O Devices
    -> แล้วก็อธิบายเกี่ยวกับส่วนประกอบของในของแต่ละส่วนคับผม
    ```
* Read 3rd chapter in slide **3 Assembly** finished 09:40 Am on 13/08/2023 :part_alternation_mark:
    ```
    -> บทนี้ช่วงแรกๆจะอธิบายว่า Assembly คืออะไร syntax เป็นยังไง
    -> ช่วงกลางจะเป็นแบบว่า วิธีใช้ วิธีแปลงโค๊ดด้วย symbol tables 
    -> แล้วก็ท้ายสุดก็ ข้อดี ข้อเสีย
    ```
* Read 4th chapter of slide **4 Instruction Set** finished 15:31 Pm On 13/08/2023 :diamond_shape_with_a_dot_inside:
    ```
    -> ในบทนี้จะบอกว่า Instruction Set มีอะไรบ้างที่แบบ Data tran, Arithmatic.. ก็ว่ากันไป
    -> บอกเกี่ยวกับว่า Instruction format มี 2 แบบคือ fixed ขนาด && Variable (ไม่ fixed)
    -> Insturetion Cycle : fetch->decode->exe->store (loop)
    -> CISC && RISC 
    ```
### Data struct :city_sunrise:
**Code ที่เห็นอ้างอิงตาม slide ของอาจารย์ทั้งหมด สำหรับวิชา Data-Structure**
* Read 1st chapter in slide **Lecture2_66** at NULL On 26/07/2023 :partying_face:
    ```
    -> Signed magnitude representation หน้า 15
    -> 1's complement system หน้า 16
    -> 2's complement system หน้า 17
    -> การบวกลบเลขฐาน หน้า 18
    -> ตัวอย่างการใช้ IEEE-754 หน้า 29(สร้างขึ้นมาเอง)
    ```
* Read 2nd chapter in slide **Lecture02-array-65** at NULL On 29/07/2023 :moyai:
    ```
    -> การคำนวณ Array ขนาด 1 มิติ หน้า 14 
    -> การคำนวณหาตำแหน่งข้อมูลใน Array ขนาด 1 มิติ หน้า 15 - 18
    -> การคำนวณ Array ขนาด 2 มิติ หน้า 23 
    -> การคำนวณหาตำแหน่งข้อมูลใน Array ขนาด 2 มิติ หน้า 29 - 32
    -> การคำนวณ Array ขนาด 3 มิติ หน้า 41 (ใน slide ไม่มีการหาตำแหน่ง Array 3 มิติง่ะ) 
    ```
* Read 3rd chapter in slide **Lecture05-pointer_66** at NULL On 10/08/2023 :point_up_2:
    ```
    -> เรื่องหลักๆจะเกี่ยวกับ Pointer เป็นหลัก การเอากำหนดค่า เรียกค่า และการใช้ Pointer กับ Array 
    -> ส่วน 10 หน้าสุดท้ายจะเป็นการอธิบายเกี่ยวกับ การบวก Address 
    ```