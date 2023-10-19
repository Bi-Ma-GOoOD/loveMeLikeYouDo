# :zap: TICKING AWAY !!! :zap:

## :trophy: F-I-N-A-L :sparkler:

> :link: Subject That you can see how we so far ^.^
> * :book: [Computer Architecture](#computer-architecture-floppy_disk)
> * :headphones: [Software Construction Lecture](#software-construction-lecture-hotsprings)
> * :guitar: [Data Structure](#data-structure-open_file_folder)

### :stars: SEASON OF MIND :snowflake:
![This is picture.](/Images/Inspiration_n_love/GODS.jpg "GODS!!!!!")

### :clubs: MY WORK :spades:
* My-Work :beginner: [Start Here](Art-Work/My_Beginner_work/) :performing_arts:

### Computer Architecture :floppy_disk:
> * :sunrise_over_mountains: [IF I CAN DREAM](#zap-ticking-away--zap)
><br>แนวข้อสอบปลายภาคแล้วนะะะ สู้ๆ
><br>:question: แนวคำถามเหมือนเดิมเลย: คืออะไร ทำหน้าที่อะไร ทำงานอย่างไร มีอะไรบ้าง มีความสัมพันธ์กันอย่างไร :question:
><br>ประมาณ 10 หัวข้อ จากหัวข้อต่อไปนี้:
>- กลไกการป้องกันหน่วยความจำ (Memory Protection Mechanisms) :heavy_check_mark:
>- หน่วยความจำเสมือน (Virtual Memory) :heavy_check_mark:
>- ตัวควบคุมอุปกรณ์นำเข้าและส่งออก (I/O Controllers)
>- การกำหนดที่อยู่ของอุปกรณ์นำเข้าและส่งออก (Input/Output Address Space)
>- ขั้นตอนการทำงานของคำสั่ง (Instruction Execution Stages)
>- การประมวลผลแบบเป็นลำดับและแบบไปป์ไลน์ (Sequential and Pipelined Execution)
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
    - Privilege Levels : อันนี้เขาจะอธิบายเกี่ยวกับสิทธิ์ในการเข้าถึงแบบทุกเรื่องเลย ไม่ใช่แค่หน่วยความจำอย่างเดียว
        User Mode : สิทธิ์ในการเข้าถึงน้อยสุดเลยยค่า แต่ โปรแกรมที่เราใช้ รวมถึงตัวเราด้วย ก็อยู่ใน Mode นี้นะ
        Kernel Mode(Supervisor Mode) : โหมดนี้แม่งคือ GODS อะแบบเข้าถึงได้ทุกอย่างเพราะเขาต้องคอยจัดการเรื่องทุกๆอย่างเลยแทนเรา อีกอย่างโหมดนี้จะเป็น โหมดที่จะคอยสื่อสาร Hardware แทนเราด้วยนะ เพราะเราทำเองไม่ได้ เขาต้องทำให้ คือจริง Kernel ก็คือ OS นี่แหละ
    - Memory Protection Unit(MPU) : หน่วยนี้คือการเช็คว่า ข้อมูลที่ CPU ร้องขอมาเนี่ยมันถูกจริงๆใช่ไหม เพราะเวลาปกติ CPU เขาร้องขอข้อมูลด้วยการส่งที่อยู่มาอะ ตัว MPU นี่แหละจะเช็คว่า จริงอ่ะป่าววว ซึ่งตัว MPU จะเช็คได้ ก็เกิดจาก Kernel เช่นกัน
        Segment Register : สิ่งนี้คือ หน่วยความจำที่อยู่ใน MPU ที่จะคอยเก็บช่วงของตำแหน่งของ Process นั่นๆ เลย ซึ่งแบ่งได้ 4 ส่วน พวก ES อะไรก็ว่าไป
    - Address Space Layout Randomization(ASLR) : หัวข้อสูดท้ายยแย้ววว อันนี้คือ การสุ่มลำดับที่อยู่ ที่คอยจัดเก็บข้อมูลคับ แค่นั้นเลย โดยใช้ Padding 
        Padding : คือหน่วยความจำว่างเปล่า ที่จะคอยแทรกระหว่าง section ตำแหน่งของข้อมูลต่างๆ ทำให้เกิดการคาดเดาได้ยากอะ ว่าข้อมูลนี้อยู่ที่ไหน
    ```
* Read 12nd chapters in slide **12-Memory Translation** finished 10:51 On 19/10/2023 :recycle:
    ```
    ในบทนี้อะเราจะกล่าวเกี่ยวกับการจัดเก็บข้อมูล แต่มันจัดเก็บข้อมูลแบบเสมือนนั่นก็คือ
    - Virtual Memory : นี่เป็นเหตุผลที่ว่า ทำไมเวลาคอมเราใช้ Ram 100 % ง่ะ จอถึงไม่ฟ้า เพราะว่าการจัดเก็บข้อมูลประเภทนี้ คือ การเก็บข้อมูลแบบเสมือนนั่นเอง ซึ่งสิ่งที่ CPU ร้องขอข้อมูลจากบทที่แล้วอะ ที่ส่งตำแหน่งมาอะ CPU ก็ส่งที่อยู่เสมือนมา และสุดท้ายก็ต้องมีการแปลง เป็นที่อยู่จริง(Physical Memory) ซึ่งขั้นตอนกลางแปลงเนี่ยจะแบ่งได้ตามนี้
        Pages and Frames : ทั้งคู่ คือ หน่วยเก็บข้อมูลย่อยของ Virtual and Physical ตามลำดับ ซึ่งทั้งสองนี้จะมีขนาดข้อมูลที่เท่ากันนะ ซึ่ง frames อะเปรียบเสมือน Memory Block เลย แบบเก็บเป็น Block เลยอะ ใน เฟรมๆ เดียว
        Page Tables : คือตัวแปลงจาก Virtual->Physical งับ ซึ่ง 1 Process : 1 Page Table
        Page Tables Entries(PTEs) : สิ่งนี้จะอยู่ใน Page Tables และสิ่งนี้แหละที่คอยเก็บว่า page เลขที่เท่านี้จะถูกเก็บไว้ใน Frame ไหน เพราะ PTEs เขาเก็บเลข Frame เอาไว้
        Translation Lookaside Buffer(TLB) : อันนี้อยู่ใน PTEs อีกทีงับ อันนี้เขาจะมีหน้าที่แบบว่า ช่วยให้ตัวของ Page Table เนี่ยแปลงไวขึ้น แบบว่าจะมึทั้ง TLB Hit และ TLB Miss เลย คล้ายๆ Cache
        Memory Management Units(MMUs) : อันนี้คือตัวสุดท้ายที่แบบว่า คอยทำทุกอย่างเลย เป็นตัวตรงกลางที่อยู่ระหว่าง CPU และ Address Bus คือ 4 หัวข้อที่กล่าวมาข้างบนอะ ถูกตัวนี้แหละ ที่ทั้งแปลง และเช็คอะไรต่างๆ ตัวนี้เป็น Hardware นะงับ
    ```

### Software Construction Lecture :hotsprings:
> * :izakaya_lantern: [ROYALTY](#zap-ticking-away--zap)


### Data Structure :open_file_folder:
> * :milky_way: [ANOTHER DIMENSION](#zap-ticking-away--zap)
