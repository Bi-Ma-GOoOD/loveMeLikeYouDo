# :zap: TICKING AWAY !!! :zap:

## :trophy: F-I-N-A-L :sparkles:

> :link: Subject That you can see how we so far ^.^
> * :book: [Computer Architecture](#computer-architecture-floppy_disk) :pencil2:
> * :headphones: [Software Construction Lecture](#software-construction-lecture-hotsprings) :notes:
> * :guitar: [Data Structure](#data-structure-open_file_folder) :microphone:

### :stars: SEASON OF MIND :snowflake:
![This is picture.](/Images/Inspiration_n_love/GODS.jpg "GODS!!!!!")

### :clubs: MY WORK :spades:
* My-Work :beginner: [Start Here](Art-Work/My_Beginner_work/) :performing_arts:

### Computer Architecture :floppy_disk:
> * :sunrise_over_mountains: [IF I CAN DREAM](#zap-ticking-away--zap) :sunrise:
><br>แนวข้อสอบปลายภาคแล้วนะะะ สู้ๆ
><br>:question: แนวคำถามเหมือนเดิมเลย: คืออะไร ทำหน้าที่อะไร ทำงานอย่างไร มีอะไรบ้าง มีความสัมพันธ์กันอย่างไร :question:
><br>ประมาณ 10 หัวข้อ จากหัวข้อต่อไปนี้:
>- กลไกการป้องกันหน่วยความจำ (Memory Protection Mechanisms) :heavy_check_mark:
>- หน่วยความจำเสมือน (Virtual Memory) :heavy_check_mark:
>- ตัวควบคุมอุปกรณ์นำเข้าและส่งออก (I/O Controllers) :heavy_check_mark:
>- การกำหนดที่อยู่ของอุปกรณ์นำเข้าและส่งออก (Input/Output Address Space) :heavy_check_mark:
>- ขั้นตอนการทำงานของคำสั่ง (Instruction Execution Stages) :heavy_check_mark:
>- การประมวลผลแบบเป็นลำดับและแบบไปป์ไลน์ (Sequential and Pipelined Execution) :heavy_check_mark:
>- อันตรายของการทำงานแบบไปป์ไลน์ (Pipeline Hazards)
>- ประเภทของมัลติโพรเซสซิง (Types of Multiprocessing)
>- ประเภทของการทำงานแบบขนาน (Parallelism)
>- สถาปัตยกรรมของหน่วยความจำ (Memory Architectures)
>- ประเภทของการเชื่อมต่อ (Types of Interconnects)
>- ประเภทของการทำงานแบบหลายเธรด (Types of Multithreading)
>- กลไกที่ทำให้หน่วยความจำตรงกัน (Memory Synchronization Mechanisms)
>- โมเดลความสม่ำเสมอของหน่วยความจำ (Memory Consistency Models)
>- โปรโตคอลความเชื่อมโยงกันของหน่วยความจำ (Memory Coherence Protocols)
>- ตัววัดประสิทธิภาพ (Performance Metrics)
>- สิ่งที่ต้องแลกมาเพื่อประสิทธิภาพ (Performance Trade-offs)

* Read 11st chapters in slide **11-Memory Protection** finished 09:54 On 19/10/2023 :alien:
    ```
    คือในบทนี้อะ เราจะกล่าวเกี่ยวกับ สิทธิ์และการเข้าถึงพื้นที่ในหน่วยความจำของแต่ละ Process แบบที่ควรจะเป็นอะ ซึ่งแบ่งได้ ดังนี้
    --> Privilege Levels : อันนี้เขาจะอธิบายเกี่ยวกับสิทธิ์ในการเข้าถึงแบบทุกเรื่องเลย ไม่ใช่แค่หน่วยความจำอย่างเดียว
            User Mode : สิทธิ์ในการเข้าถึงน้อยสุดเลยยค่า แต่ โปรแกรมที่เราใช้ รวมถึงตัวเราด้วย ก็อยู่ใน Mode นี้นะ
            Kernel Mode(Supervisor Mode) : โหมดนี้แม่งคือ GODS อะแบบเข้าถึงได้ทุกอย่างเพราะเขาต้องคอยจัดการเรื่องทุกๆอย่างเลยแทนเรา อีกอย่างโหมดนี้จะเป็น โหมดที่จะคอยสื่อสาร Hardware แทนเราด้วยนะ เพราะเราทำเองไม่ได้ เขาต้องทำให้ คือจริง Kernel ก็คือ OS นี่แหละ
    --> Memory Protection Unit(MPU) : หน่วยนี้คือการเช็คว่า ข้อมูลที่ CPU ร้องขอมาเนี่ยมันถูกจริงๆใช่ไหม เพราะเวลาปกติ CPU เขาร้องขอข้อมูลด้วยการส่งที่อยู่มาอะ ตัว MPU นี่แหละจะเช็คว่า จริงอ่ะป่าววว ซึ่งตัว MPU จะเช็คได้ ก็เกิดจาก Kernel เช่นกัน
            Segment Register : สิ่งนี้คือ หน่วยความจำที่อยู่ใน MPU ที่จะคอยเก็บช่วงของตำแหน่งของ Process นั่นๆ เลย ซึ่งแบ่งได้ 4 ส่วน พวก ES อะไรก็ว่าไป
    --> Address Space Layout Randomization(ASLR) : หัวข้อสูดท้ายยแย้ววว อันนี้คือ การสุ่มลำดับที่อยู่ ที่คอยจัดเก็บข้อมูลคับ แค่นั้นเลย โดยใช้ Padding 
            Padding : คือหน่วยความจำว่างเปล่า ที่จะคอยแทรกระหว่าง section ตำแหน่งของข้อมูลต่างๆ ทำให้เกิดการคาดเดาได้ยากอะ ว่าข้อมูลนี้อยู่ที่ไหน
    ```
* Read 12nd chapters in slide **12-Memory Translation** finished 10:51 On 19/10/2023 :recycle:
    ```
    ในบทนี้อะเราจะกล่าวเกี่ยวกับการจัดเก็บข้อมูล แต่มันจัดเก็บข้อมูลแบบเสมือนนั่นก็คือ
    -->Virtual Memory : นี่เป็นเหตุผลที่ว่า ทำไมเวลาคอมเราใช้ Ram 100 % ง่ะ จอถึงไม่ฟ้า เพราะว่าการจัดเก็บข้อมูลประเภทนี้ คือ การเก็บข้อมูลแบบเสมือนนั่นเอง ซึ่งสิ่งที่ CPU ร้องขอข้อมูลจากบทที่แล้วอะ ที่ส่งตำแหน่งมาอะ CPU ก็ส่งที่อยู่เสมือนมา และสุดท้ายก็ต้องมีการแปลง เป็นที่อยู่จริง(Physical Memory) ซึ่งขั้นตอนกลางแปลงเนี่ยจะแบ่งได้ตามนี้
            Pages and Frames : ทั้งคู่ คือ หน่วยเก็บข้อมูลย่อยของ Virtual and Physical ตามลำดับ ซึ่งทั้งสองนี้จะมีขนาดข้อมูลที่เท่ากันนะ ซึ่ง frames อะเปรียบเสมือน Memory Block เลย แบบเก็บเป็น Block เลยอะ ใน เฟรมๆ เดียว
            Page Tables : คือตัวแปลงจาก Virtual->Physical งับ ซึ่ง 1 Process : 1 Page Table
            Page Tables Entries(PTEs) : สิ่งนี้จะอยู่ใน Page Tables และสิ่งนี้แหละที่คอยเก็บว่า page เลขที่เท่านี้จะถูกเก็บไว้ใน Frame ไหน เพราะ PTEs เขาเก็บเลข Frame เอาไว้
            Translation Lookaside Buffer(TLB) : อันนี้อยู่ใน PTEs อีกทีงับ อันนี้เขาจะมีหน้าที่แบบว่า ช่วยให้ตัวของ Page Table เนี่ยแปลงไวขึ้น แบบว่าจะมึทั้ง TLB Hit และ TLB Miss เลย คล้ายๆ Cache
            Memory Management Units(MMUs) : อันนี้คือตัวสุดท้ายที่แบบว่า คอยทำทุกอย่างเลย เป็นตัวตรงกลางที่อยู่ระหว่าง CPU และ Address Bus คือ 4 หัวข้อที่กล่าวมาข้างบนอะ ถูกตัวนี้แหละ ที่ทั้งแปลง และเช็คอะไรต่างๆ ตัวนี้เป็น Hardware นะงับ
    ```
* Read 13rd chapters in slide **13-IO System** finished 15:57 On 19/10/2023 :fire:
    ```
    คือบทนี้อะงับเราจะพูดเกี่ยวกับตัวของ Input/Output System ซึ่งแบ่งได้หลักๆ ตามนี้
    --> I/O Controller : ตัวนี้จะเป็นตัวกลางที่อยู่ระหว่าง CPU และ Devices คอยเชื่อมเข้าหากัน แบบไม่ต้องให้ CPU เหนื่อย ซึ่งตัวของ I/O Controllers อะไม่จำเป็นที่จะต้องมี 1 Devices : 1 Controller นะ คือ 1 Controller อะ อาจจะควบคุมหลายอุปกรณ์ก็ได้แล้วแต่เยย ซึ่งจะมีส่วนประกอบทั้งหมด 5 ส่วน ได้แก่
            Address Decoder : จะเป็นตัวถอดรหัสของตัว Device กับ ที่อยู่ของ CPU ที่ส่งมาว่า ที่อยู่นี้อะที่ส่งมาอะ คุณกดปุ่มอะไรคุณบอกผมสิ อะไรประมาณนี้
            Control Unit : ส่วนนี้ง่ายๆนะ มันคือ ส่วนควบคุมของ Device เลย ซึ่่งบางที่อาจจะไปควบคุม ส่วนอื่นๆด้วย ถ้าหาก Device นี้มีการเข้าถึงข้อมูลส่วนอื่นๆ
            Control Register : ตัวนี้เอาไว้คอยเก็บคำสั่งงับ
            Status Register : ตัวนี้เอาไว้เช็คว่า เออ Device นี้ยังทำงานปกติอยู่อ่ะป่าววฮื่อ
            Data Register : อันนี้คือ การเก็บข้อมูลของ Device งับ เช่น ผู้ใช้งานกดปุ่ม คีย์บอดร์ ตัว Data นี่แหละที่เก็บข้อมูลไว้ว่า ผู้ใช้กดปุ่มไรบ้าง
    --> I/O Interface : อันนี้คือ ง่ายๆเลยนะงับ น้องคือ port ที่อยู่ระหว่างการเชื่อมของ Device และ I/O Controller ซึ่งแบ่งได้ 2 ประเภทงับ ได้แก่
            Serial Interface : คือการส่งข้อมูล 1 bit : 1 cycle ช้าแต่ไม่ค่อยมีข้อผิดพลาด
            Parallel Interface : คือการส่งข้อมูล หลาย bits : 1 cycle เร็วแต่อาจจะมีข้อผิดพลาด เพราะในช่วงเวลาเดียวกัน มีการส่งข้อมูลหลาย bits
    --> I/O Address Space : การเก็บข้อมูลของ I/O แบ่งได้ 2 รูปแบบงับ งือ
            Memory Mapped : คือ ตัวที่อยู่ของ I/O อะใช้พื้นที่รวมกันเลยไม่ได้มีการแบ่ง แบบว่าตัวของ I/O อะเขาอยู่ในช่วงที่หน่วยความจำจัดไว้ให้แล้ว ข้อดีคือ เข้าถึงข้อมูลได้ง่าย แต่มีความปลอดภัยต่ำ
            Isolated : ส่วนอันนี้ง่ะ คือ ตัวที่ของ I/O กับ ที่อยู่ของหน่วยความจำอะ แยกกันเก็บเลย เพราะฉะนั้นข้อดีคือ มีความปลอดภัยสูงเพราะแยกกันเก็บ แต่ข้อเสียคือ ต้องมีคำสั่งพิเศษในการเข้าถึงข้อมูล เพราะถ้าหากมี Address ที่ต้องการเข้าถึงอะ ที่อยู่เลขเดียวกันเลย แต่เราต้องการเข้าถึง ที่อยู่ของ 
            I/O อะ เราก็ต้องมีคำสั่งพิเศษ เพื่อป้องกันเอาไว้
        
    ```
* Read 14th chapters in slide **14-Pipelinning** finished 22:59 On 19/10/2023 :ramen:
    ```
    ในบทนี้เราจะกล่าวเกี่ยวกัว การรัน รันยังไงไปดู
    --> Instruction Execute Stages : คือขั้นตอนของการทำ Cycle ซึ่งแบ่งได้ 4 แต่ว่าเราจะเขียนไป 5 เลย ก็คือ
            Ins Fetch(IF) : การนำข้อมูลจาก Ram ไปใส่ไว้ใน IR(Instruction Register)
            Ins Decode(ID) : การถอดรหัสของคำสั่ง ซึ่งการถอดรหัสนี้ถูกกระทำโดย Control Unit
            Op Fetch(OF) : หลังจากการถอดคำสั่งแล้วอะ บางทีเราต้องการค่าจากที่อื่นด้วยก่อน ประมวลผลฉะนั้นเลยมีขั้นตอนนี้นี่แล
            Ins Execute(IE) : ขั้นตอนนี้การประมวลผลเลยงับ แล้วเอาค่าไปใส่ไว้ใน Register
            Op Store(OP) : การเก็บผลลัพธ์ที่ได้จากการประมวลผลงับ
    --> Instruction Execution : อันนี้อะ คือขั้นตอนของการกระทำการประมวลผล ซึ่งจะมี 2 รูปแบบได้แก่
            Sequantial Exe : คือการรัน 1 คำสั่งให้เสร็จ พอเสร็จแล้วคำสั่งต่อไปค่อยทำงาน ซึ่งถ้าหากใน 1 คำสั่งมี 5 ขั้นตอนก็รอให้ทำแต่ละขั้นตอนจนเสร็จอะ ซึ่งวิธีนี้ไม่ค่อยดีนะ มันจะนำไปสู่การใช้ทรัพยากรที่ไม่คุ้มค่า Underutilization
            Piplined Exe : ส่วนอันนี้ แนวคิดเขาคือว่า เอ๊ะ ถ้าหากว่า ในช่วงที่ process กำลังประมวลผลอยู่อะ แปลว่า Instruction ที่เป็นในส่วนของ Fetch Decode อะไรพวกนี้อะ ก็ว่างอะดิ ฉะนั้นแนวคิดก็คือ ถ้าหากว่า Instruction ที่ว่างอะให้ทำงานต่อเลย จึงทำให้เกิดการใช้ทรัพยากรอย่างคุ้มค่านั่นเองงับ
    ```

### Software Construction Lecture :hotsprings:
> * :izakaya_lantern: [ROYALTY](#zap-ticking-away--zap) :fireworks:


### Data Structure :open_file_folder:
> * :milky_way: [ANOTHER DIMENSION](#zap-ticking-away--zap) :dizzy: