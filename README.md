# MID-Term-Test Progress :sunrise_over_mountains:
## Inspiration :shipit:
### MY FAVOURITE :musical_score:
![This is picture.](/Images/Inspiration_n_love/Seraphine_Aquriam.jpg "This is my wife!!!")
### MY WORK :movie_camera:
* You can look my work at Images -> My_Beginner_work :beginner:
### :white_check_mark: Computer Architecture :house_with_garden: status: :white_check_mark:
* ถ้าอยากย้อนดู ประวัติการอ่าน Computer Architecture ให้กด <55c1429> เพื่อดูประวัติ commit เก่าๆได้งับ -O.O- :relaxed:

### :white_check_mark: Data struct :city_sunrise: :white_check_mark:
* ถ้าอยากเห็นย้อนดู ประวัติการอ่าน Data Structure ให้กด เพื่อดูประวัติ commit เก่าๆได้งับ -O.O- :rice_scene:

### Software Construction Lecture :city_sunset:
![This is picture.](/Images/My_Beginner_Work/Screenshot%202023-08-16%20211056.png "Access Modifiers")

* อ่าน Java slide **4 & 6** finished 22:42 On 16/08/2023 :blush:

    ```
    -> Override
        - ถ้าหากว่า มีการสืบทอดจากคลาสแม่มาลูกอะ แล้ว method ทั้งชื่อ กับ parameter เหมือนแม่เลย อันนั้นจะเรียกว่า @override แล้วต้องมาจากคลาสอื่นด้วยนะ
    -> Extend
        - สืบทอดแบบปกติๆ
    -> Abstract
        - ถ้าคลาสแม่ เป็น Abstract method ของแม่จะต้องไม่มีการ ใส่ไส้ข้างใน
        แต่ถ้าลูกเรียกใช้ ลูกต้อง ใส่ไส้ข้างใน
    -> Static 
        - คือถ้าในคลาสนั้นอะ เกิดการใช้ static ตัวคลาสอื่นที่เรียกอะ มีสองทาง คือ เอาชื่อคลาสที่มี static เรียกใช้ กับ สร้าง obj มาเรียก
        - แต่ถ้าแบบว่า เรามีการเรียกใช้ static ในคลาสที่มีการสร้างนั้นอะ ไม่ต้องสร้างอะไร เรียกได้เลย
    -> Constuctor
        - ห้ามเป็น private abstract final native static
        - Constructor ไม่มีการสืบทอด และห้ามการ return รวมถึง recursive
        - ทุกๆ Constructor ที่จะถูกการ extend หรือไม่ได้ก็ตามจะต้องเกิดการ super() or this()
    ```