# :dizzy: SOFTWARE-CONSTRUCTION-LECTURE :milky_way:
## :hibiscus: This All For Final :blossom:
### :open_file_folder: MY MIND & ME :shipit:
![This is picture.](/Images/Inspiration_n_love/Komi.jpg "Go Faster Faster that you can!!!")
### GOING FAST FASTEST THAT YOU CAN :rocket:

* Read 8th chapters in slide **08-I/O** finished  18:43 On 10/09/2023 :books:
    ```
    > read อ่านทีละตัว ส่วนถ้าใช้ readline อ่านได้เลยทีละบรรทัด ค่าที่อ่านได้เป็น String ทั้งสิ้น ตัวเลขก็เป็น String แต่มีวิธีอ่านเป็นตัวเลขด้วย Integer.parseInt(string) อะไรก็ว่าไป
    > มี InputSteamReader/FileReader ใช้อ่านจากหน้าจอ และไฟล์ตามลำดับ
    > printWriter/BufferWriter/print&&Buffer ใช้เขียนไฟล์ ความเร็วเรียงจากหน้ามาหลัง ทำงานด้วยกันก็ยิ่งเร็ว
    > การปิดไฟล์ สำคัญมาก!!!
    > แล้วก็มีการเขียน obj เขียนได้นะ แต่เปิดขึ้นมายังไงไม่รู้ขึ้นมาเป็นรหัส something 
    > Serialization[เขียน เป็น Binary] Deserialization อ่าน
    ```
* Read 9th chapters in slide **09-exception** finished 18:01 On 20/09/2023 :alien:
    ```
    > Exception ที่อยู่ในบทนี้ส่วนมากจะเป็น Runtime Error
    > Exception เป็น subclass ของ superClass ที่ชื่อว่า Thowable ซึ่งอยู่ใต้ Object อีกที
    > Exception มี 2 ประเภท คือ
        > Uncheck Exception คือประมาณว่า อันนี้อะมันผิดที่ตัวผู้เขียนโค๊ดเอง คือมึงอะเขียนผิดไอ้สาส เพราะฉะนั้นวิธีแก้ก็คือ ไปหาข้อผิดพลาดของโค๊ดที่มึงเขียนผิดแล้วก็แก้ซะ
        > Check Exception แต่อันนี้อะ เราไม่ได้เขียนผิดและ แต่มันอาจจะเกิดจากอะไรก็ตามที่เราควบคุมไม่ได้ ซึ่งวิธีแก้ มี 2 วิธี คือ
            > try/catch
            > throw ถ้าเรา throw exception ประเภท check เราจำเป็นต้อง declare ตรง method signature แต่ถ้าเป็นประเภท uncheck ไม่จำเป็นต้อง declare ที่ method signature
            *** throws แบบนี้อะ จะอยู่ที่บริเวณของ method signature ซึ่ง การที่เราจะ declare แบบนี้อะ ต้องเกิดจาก throw ข้างใน catch ก็ได้หรือจะ declare เองเลยก็ได้แล้วแต่ และเราสามารถ declare กี่ exception ก็ได้
    > การ try/catch catch สามารถมีได้ หลายตัว และ การเรียงลำดับ catch มีความสำคัญ เราควรเอา supclass exception ขึ้น superclass exception ตลอด
    > printStackTrace() คือไอ้ที่ ปริ้นบอกๆๆๆ หลายๆบรรทัดอะ ที่มันจะเป็นชื่อไฟล์อะนะ อันนั้นเอาไว้ใช้เรียงเพื่อไปหาไฟล์ต้นตอได้ จากล่างสุดไปบนสุด 
    > การสร้าง exception ถ้าเรา extends Exception ผลลัพธ์ exception ที่่เราจะได้คือ exception ประเภท Check แต่ถ้าเรา extends RuntimeException ผลลัพธ์ exception ที่่เราจะได้คือ exception ประเภท Uncheck
    > finally จะทำงานเสมอ ต่อให้มี return finally ก็ทำงาน ยกเว้นสิ่งเดียวเท่านั้นที่สามารถหยุด finally ได้ นั่นคือ system.exit(1) ตัวนี้แม่งออกเลย ไม่สนอะไรทั้งนั้น
    ```