# MID-Term-Test Progress :sunrise_over_mountains:
## Inspiration :shipit:
### MY FAVOURITE :musical_score:
![This is picture.](/Images/Inspiration_n_love/Seraphine_Aquriam.jpg "This is my wife!!!")
### MY WORK :movie_camera:
* You can look my work at Images -> My_Beginner_work :beginner:
### :white_check_mark: Computer Architecture :house_with_garden: status: :white_check_mark:
* ถ้าอยากเห็นว่า ประวัติการอ่าน Computer Architecture ให้กด <55c1429> เพื่อดูประวัติ commit เก่าๆได้งับ -O.O- :relaxed:
### Data struct :city_sunrise:
> :question: แนวข้อสอบกลางภาค :question:
> <br> :fire: ไม่มีแนวครับ อาศัยทำการบ้านแล้วอ่านบทนั้นเอาสู้ๆ :fire:
>- WEEK 1: :heavy_check_mark:
<br>HomeWork2 
>- WEEK 2: :heavy_check_mark:
<br> Lecture02_array_65 
>- WEEK 3: :heavy_check_mark:
<br> Quiz1 
>- WEEK 4: :heavy_check_mark:
<br> Lecture08_Linked_list_66
<br> Quiz2
<br> Lecture09_stack_66
<br> Quiz3
<br> HomeWork (ไอ้นี่ทำหลังสุดเลย พวกตระกูล Homework เนี่ย)
>- WEEK 5: :heavy_check_mark:
<br> Lecture11-recursion-66
<br> Exercise factorial หมู่ 1 และ 200
<br> Exercise recursive
>- WEEK 6: :heavy_check_mark:
<br> Lecture10_search65
<br> Exercise tail recursion
<br> Exercise Ackerman function
<br> Exercise Tower of Hanoi (ทำทีหลังเช่นกัน)
<br> Assignment Hashing
<br> BinarySearch
* Read **Lecture02_array_65** finished 20:29 On 15/08/2023 :calendar:
    ```
    -> Array 1 มิติ
        - การหาจำนวนสมาชิกหรือขนาด Array หาได้จาก Upper - Lower + 1
        - การหาตำแหน่ง Address หาได้จาก loc A[i] = Base + w*(i-L)
    -> Array 2 มิติ
        - การหาจำนวนสมาชิกหรือขนาด Array หาได้จาก (U1-L1+1)*(U2-L2+1)
        - การหาตำแหน่ง Address มี 2 วิธีได้แก่
            - หาโดยใช้ Row แถว เป็นหลัก loc A[i][j] = Base + w[C(i-L1)+(j-L2)]
            - หาโดยใช้ Column หลัก เป็นหลัก loc A[i][j] = Base + w[R(i-L1)+(j-L2)]

    ```
* Read **Lecture08_Linked_list_66** finished 06:30 On 16/08/2023 :bicyclist:
    ```
    -> Linklist ตามโค๊ดที่เราฝึกเลยเวลาน้อยไปที่จะฝึกทั้งหมด แต่เอาพื้นฐานก็ถือว่า ได้แล้วนะ ติดแค่ยังเขียนลบไม่ค่อยเป็น
    ```
* Read **Lecture09_stack_66** finished 07:25 On 16/08/2023 :slot_machine:
    ```
    -> ช่วงแรกๆอะ จะสอนการ pop push แบบ Array ก็ดีนะเดี๋ยวจะเขียนโค๊ดตามไปให้
    -> ช่วงหลังๆนี่ จะเป็นการแบบ แปลง infix->postfix 
    ```
* Read **Lecture11-recursion-66** finished 08:22 On 16/08/2023 :large_blue_circle:
    ```
    -> recursion มีทั้งหมด 4 ประเภท ได้แก่
        -linear คือการเรียกตัวเอง 1 ครั้ง
        -Tail คือการเรียกตัวเองพร้อมกับส่งผลลัพธ์ ไปเป็น พารามิเตอร์ด้วย
        -Binary คือการเรียกตัวเองสองครั้งในฟังค์ขันเดียว เช่น  fibonacci
        -Multiple คือการเรียกตัวเองหลายครั้งในฟังค์ชันเดียว
    -> แล้วก็ Tower of hanoi
    ```
* Read **Lecture10_search65** finished 09:49 On 16/08/2023 :sunglasses:
    ```
    -> มีกล่าวเกี่ยวกับ Big O นิดหน่อย
    -> การหาข้อมูลโดยใช้ Binary Search มีระดับเป็น O(log n)
    -> การหาข้อมูลโดยใช้ Hashing มีระดับเป็น O(1) โดย Hashing อะจะนำข้อมูลไปเป็น Address ซึงมีอยู่ 3 วิธีย่อยคือ 
        - x mod ขนาดของช่อง Hash ถ้าแบบเลขมี 10 ตัว ก็ mod 11 ประมาณนี้
        - Mid Square คือ การยกกำลังค่าของ คีย์ เช่น 12 = 144 เอาค่าตรงกลางอย่างเดียว ตอบ 4
        - Floding การพับ คือเรามีข้อมูลมา แล้วเอามาพับซึ่งจะรู้ได้ไงว่าพับตรงไหน คำตอบ คือ เขาจะบอกหลักสูงสุดมาเองว่า เท่าไร
    -> การชนกันของข้อมูล มีวิธีแก้ใหญ่ 2 อย่างคือ 
        1.Open addressing
            - Linear Probing คือเจอช่องถัดไปถ้าช่องไหนว่างเติมเลย
            - Double Hashing คือการที่เราจะ Hash อีกรอบแต่รอบนี้คือ x mod ขนาดช่อง + 1
        2.Chainning 
            - วิธีแม่งยากเกินไม่รู้จะเขียนโค๊ดยังไงแต่หลักการอะ คือ มึงเติมไปเลยแบบสร้างมาอีกช่องเติมหลังเลยอะ ซ้ำกี่ตัวก็เติมแม่งเท่านั้นแหละ

    ```

### Software Construction Lecture :city_sunset: