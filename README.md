# MID-Term-Test Progress :sunrise_over_mountains:
## Inspiration :shipit:
### MY FAVOURITE :musical_score:
![This is picture.](/Images/Inspiration_n_love/Seraphine_Aquriam.jpg "This is my wife!!!")
### MY WORK :movie_camera:
* You can look my work at Images -> My_Beginner_work :beginner:
### Computer Architecture :house_with_garden:
**Computer Architecture จะมีทั้งหมด 10 สไลด์ที่จะต้องอ่านสอบ**
> แนวข้อสอบกลางภาค
><br>:question: แนวคำถาม: คืออะไร ทำหน้าที่อะไร ทำงานอย่างไร มีอะไรบ้าง มีความสัมพันธ์กันอย่างไร :question:
> <br>ประมาณ 10 หัวข้อ จากหัวข้อต่อไปนี้:
>- วิวัฒนาการของระบบคอมพิวเตอร์ :heavy_check_mark:
>- องค์ประกอบของระบบคอมพิวเตอร์ :heavy_check_mark:
>- องค์ประกอบของหน่วยประมวลผลกลาง (CPU) :heavy_check_mark:
>- หน่วยความจำใน CPU (Registers) :heavy_check_mark:
>- ภาษาแอสเซมบลี (Assembly Language) :heavy_check_mark:
>- ชุดคำสั่ง (Instruction Set) :heavy_check_mark:
>- วงจรการทำงานของคำสั่ง (Instruction Cycle) :heavy_check_mark:
>- สถาปัตยกรรมชุดคำสั่งที่พบบ่อย (Common ISAs) :heavy_check_mark:
>- วิธีการระบุที่อยู่ (Addressing Modes) :heavy_check_mark: 
>- ลำดับชั้นหน่วยความจำ (Memory Hierarchy) :heavy_check_mark:
>- ความใกล้เคียงกันของข้อมูล (Locality) :heavy_check_mark:
>- ผลที่เกิดขึ้นเมื่อมีการร้องขอข้อมูลจากแคช (Cache Events) :heavy_check_mark:
>- คุณสมบัติของหน่วยความจำ (Memory Properties) ที่ต้องรักษาไว้ :heavy_check_mark:
>- หน่วยของแคช (Cache Lines, Cache Sets) :heavy_check_mark:
>- วิธีกำหนดที่อยู่แคช (Cache Placement Policies) :heavy_check_mark:
>- วิธีแทนที่แคช (Cache Replacement Policies) :heavy_check_mark:
>- วิธีเขียนแคช (Cache Write Policies) :heavy_check_mark:
>- ตัววัดประสิทธิภาพแคช (Cache Performance Metrics) :heavy_check_mark:
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
* Read 3rd chapter in slide **3 Assembly** finished 09:40 am on 13/08/2023 :part_alternation_mark:
    ```
    -> บทนี้ช่วงแรกๆจะอธิบายว่า Assembly คืออะไร syntax เป็นยังไง
    -> ช่วงกลางจะเป็นแบบว่า วิธีใช้ วิธีแปลงโค๊ดด้วย symbol tables 
    -> แล้วก็ท้ายสุดก็ ข้อดี ข้อเสีย
    ```
* Read 4th chapter of slide **4 Instruction Set** finished 15:31 pm On 13/08/2023 :diamond_shape_with_a_dot_inside:
    ```
    -> ในบทนี้จะบอกว่า Instruction Set มีอะไรบ้างที่แบบ Data tran, Arithmatic.. ก็ว่ากันไป
    -> บอกเกี่ยวกับว่า Instruction format มี 2 แบบคือ fixed ขนาด && Variable (ไม่ fixed)
    -> Insturetion Cycle : fetch->decode->exe->store (loop)
    -> CISC && RISC 
    ```
* Read 5th chapter of slide **5 Addressing Modes** finished 17:43 pm On 13/08/2023 :mount_fuji:
    ```
    -> ช่วงแรกเขาจะกล่าวถึงว่า Information Set มีอะไรบ้าง
        - มี Data Tran: Move, Load, Store
        - มี Arithmatic: Add, ....
        - มี Logical: And, Or, Compare...
        - มี Branching: Uncondition, Condition/jne||je, Call Func
        - มี Machine con: Halt, No Operation, Software Interrupt
    -> Machine Code ประกอบด้วย Addressing Mode-Opcode-operand 
    -> แล้วเขาก็จะกล่าวต่อมาว่า ใน Addressing Mode ว่ามีอะไรบ้าง อ่านเอาเองมีทั้งหมด 5 รูปแบบสู้ๆ
    ```
* Read 6th chapter of slide **6 Memory-Hierarchy** finished 18:36 pm On 13/08/2023 :sparkles:
    ```
    -> บทนี้จะกล่าวเกี่ยวกับ ลำดับขั้นของความจุต่างๆ ได้แก่ Primary Storage && Secondary Storge
    -> Locality -> Temporal && Spartial
        อ่าน Locality เพิ่มเติมที่ https://pepewitch.medium.com/
    ```
* Read 7th chapter of slide **7 Memory Levels** finished 22:15 pm On 13/08/2023 :postbox:
    ```
    -> บทนี้จะกล่าวถึงประเภทต่างๆ คือแบบประมาณรูปแบบอะตัวแม่ใหญ่ เช่นแบบ
        - Register -> Geneal Purpose && Special Purpose
        - Cache -> L1, L2, L3
        - SRAM ใช้กับ Regiter & Cache || DRAM ใช้กับ Main Memory
        - SSD || HDD 
        - Magnetic Drive && Magnetic Solid State Drive
    ```
* Read 8th chapter of slide **8 Cache** finished 09:55 am On 14/08/2023 :cactus:
    ```
    -> ในช่วงต้นจะกล่าวถึงความหมายของ Cache ว่า แบบเออ Tag ใน Cache จะเก็บที่อยู่จริง(Address) จาก Memory
    -> Storage Condider มี Locality && Special
    -> Cache Events มี Cache Hit && Cache Miss
    -> Memory Properties
        - Coherences อัปเดตค่า cache ทุกค่าถ้าหากมีการเปลี่ยนแปลง ยกเว้น main memory
        - Consistency อัปเดตหมด
    ```
* Read 9th chapter of slide **9 Cache Organization** finished 13:58 pm On 14/08/2023 :police_car:
    ```
    -> Cache Line เป็นหน่วยย่อยของ Cache Set 
    -> Placement Policies มี 3 ประเภท ได้แก่
        - Direct Mapped
        - Set-associative
        - Fully-associative
    -> Replacement Policies มี 2 ประเภท ได้แก่
        - First in , First out
        - Least Recent Use
    -> Write Policies
        - Write through Cpu ส่งอัปเดตค่าทั้งใน Cache และ Mem
        - Write back Cpu update Cache and Cache update Mem later
    ```
* Read 10th chapter of slide **10 Cache Metrics** finished 14:16 pm On 14/08/2023 :musical_note:
    ```
    ->Average Memory Access Time = (Cache Hit rate * Hit time)+(Cache Miss rate * Miss penalty)
        - Cache Hit คือ อัตราการเกิด Cache Hit
        - Cache Miss คือ อัตราการเกิด Cache Miss
        - Hit time คือ เวลาที่ Cpu นำข้อมูลหลังจาก เกิด Cache Hit
        - Miss penalty คือ เวลาที่ Cpu ต้องนำข้อมูลมาจาก Ram เมื่อเกิด Cache Miss
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