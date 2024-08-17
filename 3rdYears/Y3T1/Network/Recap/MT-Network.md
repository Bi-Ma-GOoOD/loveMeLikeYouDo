# MT-Network

# Chapter 1: Introduction

- What is the Internet?
    - Internet or Inter Connection Network: คือ เครือข่ายที่ใช้เชื่อมเครือข่ายของแต่ละบริษัทให้สามารถสื่อสารผ่านเครือข่ายเดียวกันได้ เพราะในตอนนั้นแต่ละบริษัทมีเครือข่ายเป็นของตนเอง
    - Internet Standards
        - Defacto Standard: เป็นข้อยอมรับที่ทุกคนยอมรับกันในที่สุด โดยไม่ผ่านการบังคับ เช่น HTTP, TCP, IP, FTP เป็นต้น
            - RFC [Request for Comment]: เป็นเอกสารเพื่ออธิบายว่า อะไรเป็น standard, Protocols และ Technologies ของ Internet (TCP/IP) ในปี 1969
            - IETF [Internet Engineering Task Force]: เป็นองค์กรที่คอยช่วยเหลือและสนับสนุนความเป็นมาตรฐานการสื่อสารของ Internet ผ่าน Protocols
- What is protocol
    - Protocols: เป็นขั้นตอน หรือ กระบวนการสื่อสาร / การแลกเปลี่ยนข้อมูลระหว่าง Devices ซึ่งจริงๆ แล้วน้องก็คือ ภาษาเหมือนที่เราใช้สื่อสารกันทั่วไปนี่แหละ แต่ว่า Protocols ก็เป็นภาษาที่ใช้คุยกันระหว่าง Devices ต่อให้ทั้ง 2 Devices นั้นจะมี software ที่ต่างกันก็ตาม
    - Wed browser: คือการใช้ HTTP (Hypertext Transfer Protocols) สื่อสารกันระหว่าง Web ในการส่งไฟล์อย่าง HTML (Hyper Text Markup Language) แต่การส่งหากันได้นั้นจะต้องมี TCP ในการอนุญาตเพื่อส่งไฟล์ก่อน
        - TCP REQUEST → TCP CONNECT → GET LINK → FILE (HTML) →
- Network Edge
    - Network Edge: Host, Access Network, Physical media
        - Host: ผู้รับและผู้ส่งสัญญาณ ณ ปลายทางของ Network นั้นๆ
        - Access Network: คือตัวเชื่อม Network จาก User และ Core Network
        - Physical Media: คือ ตัวสายที่ใช้ส่งสัญญาณอะ มี หลักๆ 3 ประเภท ได้แก่
            - Wire
            - Wireless
            - Radio Waves
    - Network Edge
        - Host: ผู้รับสัญญาณ และ ผู้ส่งสัญญาณ
        - servers ส่วนมากจะเป็น Data Center ที่จะคอยส่งข้อมูลมาให้
    - Access Network: คือ sub-network ที่จะคอยเชื่อม Device ของ User กับ Core Network ซึ่งมันเปรียบเสมือนทางด่วนที่ถูกโยงกันงับ
        - ประเภทของ Access Network:
            1. Residential access net (Home): Wire - Cable or DSL
            2. Institutional access networks (school, company): Wire - DSL
            3. Mobile access networks (Wi-Fi, 4G/5G): Wire + Wireless
            4. Data center networks (DCNs)
                1. Data center มีมากมายทั่วโลก เพราะน้องมีหน้าที่เพื่อทำให้ Bandwidth มีความสูงมากขึ้นและลดการ Dalay ของ ISP ต้นทาง ทำให้ต้องมีหลายที่ ด้วยสิ่งนี้เองทำให้เวลาเราใช้ Application อะไรก็สามารถที่จะใช้ได้อย่าง smooth และนอกจากนี้ด้วยความที่ DCNs ต้องมีหลายที่เพื่อลด Delay จากตัวของ ISP ทำให้การเชื่อมต่อระหว่าง User มาที่ตัวของ DCNs สร้างได้เป็นระบบประสาทโครงข่ายขนาดใหญ่
    - Wire Access Netwok: เชื่อมต่อ Network แบบใช้เส้นในการรับและส่งญญาณ Internet
        1. DSL (Digital Subcriber Line): คือ สายโทรศัพท์มักใช้กับตึกหรืออาคารในที่ทำงาน ทำให้สามารถส่งข้อมูลที่มีความ reliable มากกว่าสาย Cable แต่ข้อเสียก็คือ สามารถใช้งานได้ทีละอย่างเท่านั้น จะโทรก็โทร จะใช้เน็ตก็ใช้ ไม่เหมือนสาย Cable ที่สามารถทำงานพร้อมกันได้ เพราะแบ่งเป็น ช่วงสัญญาณไว้แล้ว
        2. Cable - Based Access: ใช้สายที่ชื่อว่า Coaxial Cables ในการรับและส่งสัญญาณ โดยสายนี้จะมี Bandwidth ที่ลดลงหากว่ามีเพื่อนบ้านของเราใช้สายเดียวกับเรา โดยสาย Coaxial มีขนาดที่เล็กว่า DSL แต่ก็ดีกว่า เพราะสามารถส่งได้ทั้งสัญญาณ TV และสัญญาณได้ในเวลาเดียวกัน อีกทั้งยังมี อัตราการ Download ที่สูง แต่ก็มีอัตราการ Upload ที่่ต่ำ นอกจากนี้สาย Coaxial ยังมีการใช้ FDM (Frequency Division Multiplexing) ในการแบ่งช่วงความถี่ของสัญญาณให้มีหลายเลนมากยิ่งขึ้นทำให้สามารถใช้ประสิทธิภาพของ Bandwidth ได้ดียิ่งขึ้น แต่ข้อเสียคือ แบ่งเยอะก็ช้าลงเพราะต้องหารไปเรื่อยๆ
    - Wireless Access Network: คือการ share network ผ่านอากาศทำให้ได้ใช้พร้อมกันได้หลายคน แต่ Cable จะใช้ได้แค่คนเดียวเท่านั้น หรือว่าต้องมีการเชือมต่อสายถึงจะใช้ได้
        - Wireless local area networks (LAN): Wi-Fi
        - Wide-area cellular access networks: เสาส่งสัญญาณ
    - Physical Media Property
        - Guided Media: มีทิศทางการส่งชัดเจน เช่น Cable, Fiber
        - Unguided Media: มีทิศทางที่กระจายไร้ทิศทาง เช่น Radio
        - Fully Duplex: สัญญาณที่ส่งไปสามารถเป็นได้ทั้งขาไปและกลับ เช่น เวลาเราคุยโทรศัพท์ เราสามารถเป็นได้ทั้งผู้ฟังและผู้พูดได้ในเวลาเดียวกัน เพราะข้อมูลถูกส่งพร้อมกันจากทั้งสองฝั่งไม่ได้ต้องรอกัน
        - Half Duplex: สัญญาณที่ส่งไปสามารถไปได้แค่ขาเดียว เลือกเอาระหว่าง ไป และ กลับ เช่น เวลาเราคุย walkie talkie
        - Twisted pair (TP): เป็นสายทองแดงที่พันกันเป็นคู่ นิยมใช้เป็น สายโทรศัพท์บ้าน สาย Lan สาย DSL เป็นสายที่ดีกว่า UTP
        - Untwisted pair (UTP): เป็นสายทองแดงที่ไม่ได้พันกัน นิยมใช้กับ โทรศัพท์ที่อยู่ในอาคารทำงาน
        
        ---
        
        - Crosstalk Phenomenon: เป็นเหตุการณ์ที่สายทองแดงนั้นมีการพันไม่แน่นพอจนทำให้สัญญาณจากสายอื่นๆ หรือว่า สัญญาณรบกวนจากแม่เหล็กภายนอกสามารถมารบกวนข้อมูลที่ส่งมาในสายนี้ได้ ทำให้ข้อมูลที่ได้เกิดความผิดเพื้ยน เพราะมีกระแสไฟฟ้ามาทำลายสัญญาณนั่นเอง
    - Type of Physical Media
        - Coaxial Cable: เป็นสายต่อหลักของ Capable Access ที่มีการแบ่ง channel
        - Fiber Optic Cable: วิ่งด้วยแสง ซึ่งไวกว่าสาย Coaxial Cable แน่นอน ทำให้ Fiber Optic มีความเร็วที่สูงกว่าและมี Bandwidth ที่มากกว่า และนอกจากนี้สาย Fiber Optic ยังมีกลไกการป้องกัน Bit-Flip อีกด้วย
        - Wireless Radio: พูดง่ายๆ น้องคือ คลื่นสัญญาณวิทยุทุกรูปแบบ AM/FM radio to cellular networks, Wi-Fi, Bluetooth, and satellite communications.
        - Radio Link: อันนี้เหมือนเป็นแบบ เชื่อมต่อด้วย จุดต่อจุดอะ แบบระบุจำเพาะเอาไว้แล้วว่าถ้าเชื่อมจากจุดนี้แล้ว ต้องไปต่อที่จุดไหนอะ
    
    ---
    
    > Router กับ Modem ต่างกันตรงที่
    > 
    > 
    > Router: คือ คนที่คอยหาเส้นทางในการส่งข้อมูลของ Devices ภายในบริเวณนั้นๆ นอกจากนี้ยังมีการเช็คความผิดพลาดของข้อมูลอีกด้วยว่าข้อมูลที่ส่งมาถูกไหมมีอะไรตกหล่นหรือป่าว แล้วค่อยหาว่า Devices ไหนกันที่จะเป็นคนได้รับข้อมูลนี้
    > 
    > Modem: คือ เหมือนสะพานที่เชื่อมระหว่าง Devices ของบ้านเรากับ Network นอกจากนี้น้องยังคอยแปลงสัญญาณ 01 หรือที่เรียกว่า Analog/Digital Signal เพื่อให้ Devices ของเราเข้าใจอีกด้วย เหมือนเป็น Gateway
    > 
    > ---
    > 
    
    > สูตรการหา Packet transmission Delay
    > 
    > 
    > L = packet length bits (bits)
    > 
    > R = link transmission rate (bits/sec)
    > 
    > $$
    > Packet-Transmission-Delay = L/R
    > $$
    > 
- Network Core
    - มี 3 เรื่องหลักๆ คือ
        - Packet Switching
            - Packet-switching: คือการส่ง packet แต่ละ packet ผ่าน router ไปเรื่อยๆ จนไปถึงปลายทาง การส่ง packet ไปยัง router หนึ่งๆ แล้วส่งต่อไปอีกเป็นทอดๆ เราเรียกว่า “HOP”
            - Network core มี 2 กลไกหลักๆ คือ
                - Forwarding (Local Action) aka switching: คือการที่ว่า หาเส้นทางทั้งหมดที่เป็นไปได้ว่า packet ที่ส่งมาเนี่ยมีปลายทางคือที่ไหน แล้ว ระหว่างทางไปอะ มีเส้นทางไหนบ้าง
                - Routing (Global Action): คือการหาเส้นทางที่ดีที่สุด เช่น ทางที่สั้นที่สุด หรือ ทางที่มี congestion traffic น้อย
            - Packet Switching มี 2 หลักการ ได้แก่
                - Store and Forward: คือการที่ Router จะรอรับข้อมูล bit ของ packet นั้นๆ มาจนครบก่อน แล้วค่อยส่งต่อไป มันคือ store พอครบก็ forward
                - Queueing: อันนี้คือ ประมาณว่า ในขณะที่ Router กำลังหาทางที่จะส่ง packet นั้นๆ ไปยัง router อื่นๆ ก็ต้องมีการใช้ Routing Algorithm แต่ว่าระหว่างที่ Router ใช้ Algo นี้อยู่อะ ข้อมูลมันก็ไหลเข้ามาเรื่อยๆ จนบางทีก็ต้องเกิดการรอ Queue พอรอไปนานมากๆ Router ก็ไม่มีพื้นที่เพียงพอจะเก็บข้อมูลอีกต่อไป Buffer เต็ม ดังนั้น Router จึงทำการ drop packet ทิ้งเพื่อรักษาสถานภาพการทำงานของตัวเองเอาไว้ ด้วยเหตุนี้เองจึงเป็นที่มาของ packet loss ทำให้เมื่อข้อมูลถูกส่งไปที่ปลายทางแล้วอะ มีโอกาสที่จะต้อง retransmission ใหม่ เพราะข้อมูลบางส่วนมันหายไป bit loss นั่นเอง
        - Circuit Switching
            - Circuit-switching: คือการที่ถ้าหากว่าเราต้องการจะส่งข้อมูลหากัน จะเกิดการทำ Call - Setup ระหว่างตัวของ Host → Destination โดยการทำ call - setup นั่นจะทำให้คุณได้ใช้งาน Bandwidth ได้อย่างเต็มที่นอกจากนี้ยังมี Latency ต่ำอีกด้วย เพราะว่า Call - setup เหมือนแบบเราจองเส้นทางให้คุณแล้วอะ ไม่ใช่แค่เส้นทางนะ พื้นที่ก็จองไว้ให้แล้วเรียบร้อย เหมือน private เลยอะ แต่ข้อเสียคือ ใช้ทรัพยากรไม่คุ้มค่า รองรับหลาย user ไม่ไหว และอีกอย่างการทำ Circuit Switching มันแพง
                
                <aside>
                💡 ส่วนมาก Circuit Switching มักใช้กับ การใช้โทรหากัน
                
                </aside>
                
                - รูปแบบการทำงานของ Circuit Switching มี 2 รูปแบบคือ
                    - Frequency Division Multiplexing: ถูกแบ่งตามคลื่นความที่ให้แต่ละ User แต่การแบ่งแบบนี้จะทำให้ค่าของ Bandwidth ถูกหารตามจำนวน User ณ ตอนนั้นด้วย
                        - ข้อดี: ใช้นานเท่าไหร่ก็ได้
                        - ข้อเสีย: ส่งได้น้อยมากๆ ถ้าหากว่า Bandwidth ถูกหารด้วยจำนวน User ที่เยอะ
                    - Time Division Multiplexing: ถูกหารด้วยเวลา เหมือน Round Robin
                        - ข้อดี: ผู้ใช้งานทุกคนสามารถส่งข้อมูลได้ตาม Bandwidth สูงสุดที่กำหนดเอาไว้
                        - ข้อเสีย: ถ้าหากมี User เยอะคนที่ส่งคนแรกที่ยังส่งไม่หมดอาจจะต้องรอนาน เพราะต้องเอาเวลาไปให้คนอื่นๆด้วย
        - Internet Structure
            - คำถามเริ่มจากที่ว่า “ISP สามารถรองรับคนใช้งานเป็นล้านๆคนได้อย่างไร”
                - ขั้นตอนที่ 1: Tired Network: การเข้าแบบแบ่งเป็นชั้นๆ
                    - Access ISPs: ให้บริการกับกลุ่มธุรกิจขนาดใหญ่ แบบบริษัท อะไรงี้
                    - Transit ISPs: เป็น ISPs ขนาดใหญ่ที่มี Bandwidth ที่สูงกว่าอันแรก คอยทำหน้าที่เป็นตัวรับส่งข้อมูลระหว่าง ISPs ที่เข้าถึง และเครือข่ายอื่นๆ ทำหน้าที่เหมือนเป็น Highway
                    - Content Delivery Network (CDNs): ทำหน้าที่ในการส่ง content เช่น Video, websites ที่มีประสิทธิภาพมาก
                        
                        <aside>
                        💡 บริษัทที่เป็น CDNs เองก็อย่างเช่น Google, Microsoft, Akamai, Facebook
                        
                        </aside>
                        
                - ขั้นตอนที่ 2: คืออย่างอันแรกอะ เรามี Global ISPs ก็คือมี ISPs แค่อันเดียวเลย แต่ว่าอันนี้คือ เออแล้วถ้ามีหลาย ISPs หล่ะจะทำยังไง เราเลยมีหลัการใช้ Peering มาเชื่อมต่อและส่งข้อมูลระหว่าง ISPs กันเอง
                    - Peering คือ การจัดการแลกเปลี่ยนการรับส่งข้อมูล โดย ISP จะตกลงให้เส้นทางกับลูกค้า หากันและกันในแบบที่ฟรีไม่เสียค่าใช้จ่าย
                - ขั้นตอนที่ 3: Internet Exchange Points (IXPs): คือการตั้งสำนักงานของ ISP ที่มีการเชื่อมต่อหลายๆ ISP และ Network เข้าด้วย ช่วยให้สามารถแลกเปลี่ยนการรับส่งข้อมูลระหว่างเครือข่ายเกิดขึ้นได้อย่างประสิทธิภาพ โดยไม่ต้องพึ่งพา Global ISPs ขนาดใหญ่อีกต่อไป
                - ถ้าไล่เป็นขั้นๆ จะได้
                    - Tier 1 ISP: ผู้ให้บริการอินเตอร์เน็ตแบบ ข้ามทวีป ข้ามมหาสมุทร เช่น NTT
                    - IXP: เป็นตัวเชื่อม อย่างที่บอกไป
                    - Regional ISP: ผู้ให้บริการอินเตอร์เน็ตแบบ ระดับทวีป แต่ไม่ได้ข้ามนะ
                    - Access ISP: ผู้ให้บริการอินเตอร์ระดับประเทศนั้นๆ เช่น AIS, TRUE, DTAC
                        - Tier 1 ISP / CDNs → IXP → Regional ISP → Access ISP
                - สูตรการหาความน่าจะเป็นต่อจำนวนผู้ใช้ N คนในการส่งข้อมูลพร้อมกัน โดยที่ไม่มีคนอื่นส่งด้วยแล้วนอกจาก N คนนี้
                    
                    $$
                    x = C(n, k) * [pow(p, k) * pow(1-p, n -k)]
                    $$
                    
- Performance
    - Packet Delay:
        
        $$
        Dnodal = Dproc + Dqueue + Dtrans + Dprop
        $$
        
        - Delay processing: คือความเร็วในการแปลงข้อมูลจาก Analog เป็น bit และนอกจานนี้ยังมีการเช็คสถานะ bits ต่างๆ
            - L / A = Length bit, A = Convert analog to digital at a
        - Delay Queue: คือ เวลาที่ packet จะต้องรอที่ router ปัจจุบันก่อนจะถูกส่งต่อไป
            - L / Q = Length bit, Q = เวลาที่ใช้รอ
        - Delay Transmission: คือเวลาที่ใช้ในการส่งทั้ง packet ข้าม link โดยจะขึ้นอยู่กับขนาดของ packet และ ความกว้างของ Bandwidth
            - L/R = Length bit, R = ส่งด้วยความเร็ว R bit (bps)
        - Delay Propagation: คือ เวลาที่เราใช้ส่ง bit 1-bit ผ่านบนเส้น physical media
            - D/S = Distance (KM), S = ความเร็วแสง หรือว่า propagation speed
        - Traffic Intensity
            - a = average packet arrival rate
            - L = packet length (bits)
            - R = link bandwidth (bit transmission rate)
            
            $$
            value = L * a/R
            $$
            
            - ถ้า value เข้าใกล้ 0 = ถนนโล่ง
            - ถ้า value เข้าใกล้ 1 = ถนนเริ่มมีความแออัดทางจราจร
            - ถ้า value มากกว่า 1 = ถนนระเบิด เตรียมตัว packet loss ได้เลย
    - Packet Loss:
        - Packet Loss: จะเกิดขึ้นเมื่อ buffer ที่คอยเก็บข้อมูล bit ของ Router เต็มจนต้องเกิดการ Replacement Policy หรืออาจจะมีการขอ retransmission เพื่อขอข้อมูลอีกรอบจากการที่ตัวเองได้ drop packet ทิ้งไป
    - Packet Throughput:
        - Scenario 1: Rsent < Rrecieve
            - จะเกิดคอขวดที่ Rsent เพราะมีขนาดท่อที่เล็กกว่า Rreceive ทำให้ Rreceive เกิดการว่างงานได้เพราะตัวเองรับได้เร็วกว่าข้อมูลที่ส่งมาซะอีก
        - Scenario 2: Rsent > Rrecieve
            - จะเกิดคอขวดที่ Rrecieve เพราะตัวเองมีขนาดท่อที่เล็กกว่าของ Rsent ทำให้ข้อมูลที่ส่งมาเกิดการกระจุดตัวที่ Rrecieve ซึ่งอาจส่งผลให้ข้อมูลเกิดการสูญหายได้
- Security
    - Network Security
        - Packet Interception (sniffing): การแอบดู หรือ ดักจับข้อมูลนั้นๆ ซึ่ง Wireshark ก็ทำแบบนั้น
        - Fake Identity: การปลอมตัวเป็นคนรับสารแล้วขโมยข้อมูลส่วนนั้นไป
        - Denial of Service (Dos): เป็นการโจมตี server จาก host หลายๆ host พร้อมกัน
    - Line of defense
        - Authentication: การยืนยันตัวตน
        - Confidentiality: การเข้ารหัสเพื่อดูข้อมูล
        - Integrity checks: การเช็คว่าไฟล์นั้นๆ ที่ส่งมา รวมไปถึงข้อมูลที่ส่งมานั้นจริง หรือ ปลอม
        - Access Restrictions: การเข้าถึงข้อมูลแบบ ต้องมีอะไรแสดงว่าเรานี่แหละมีสิทธิ์ที่จะดูได้
        - Firewalls: เป็นเหมือนยามที่คอยดูว่า packet ที่เข้ามาหรือว่าส่งออกไปมีความอันตรายไหม
- Protocol layers, Service models
    - Layers มีไว้ทำไม
        - เพราะแต่ละ layer จะมีแนวทางในเชิงที่แยกกันทำงานได้ในส่วนของตนเอง จากนั้นจึงนำมาทำงานร่วมกัน และนอกจากนี้ยังสามารถแก้ไขแต่ละ layer ได้ง่าย โดยประชน์ของ layer มี
            - Modularity: แต่ละ layer ทำงานในส่วนของตนเอง ทำให้ง่ายต่อความเข้าใจในการพัฒนาทีและส่วนหรือซ่อมบำรุง
            - Scalability: ปรับเพิ่มอะไรได้ง่าย โดยไม่ส่งผลกระทบต่อ layer อื่นๆ
    - Layered Internet protocol stack
        - Application (Message): ทำหน้าที่ติดต่อกับ User โดยตรง
            - HTTP, IMAP, SMTP, DNS
                - Presentation: ขั้นตอนนี้เหมือนแบบว่า เราแปลงข้อมูลที่ได้จาก Application มาแปลงเป็น ASCII หรือ Unicode จากนั้นเอาผลลัพธ์ที่ได้ไปทำการ encryption และส่งส่วนนี้ไปที่ชั้นต่อไป
                - Session: เป็นตัวที่จะคอยเชื่อมการทำงานระหว่าง Application และคอยแลกเปลี่ยนข้อมูลกัน หรือหยุดเชื่อมต่อกันระหว่าง Devices ต่างๆ ที่ได้มีการสนทนากัน
        - Transport (Segment): ทำหน้าที่ในการส่งข้อมูลที่น่าเชื่อถือระหว่าง Application ที่ต่าง Host กันซึ่งจะมีการแตกข้อความใหญ่เป็นชิ้นเล็กๆ เพื่อเป็นการส่งที่มีลำดับและถูกต้อง
            - TCP, UDP
        - Network (Datagram): จะทำการ Routing path เพื่อหาเส้นทางที่ดีที่สุดระหว่าง Source → Destination
            - IP, Routing Protocols, ICMP, ARP
        - Link (Frame): ในชั้นนี้จะมีการทำ Encapsule data และใส่ Address Header นอกจากนี้ยังมีการเช็ค bit error อีกด้วย รวมไปถึงการใส่ Unique Identification ของ Devices นั้นๆ เพื่อส่งลงไปใน Network
            - Ethernet, 802.11(Wi-Fi), PPP
        - physical: ทำการส่งข้อมูล bits ผ่าน Physical link
            - Wire, Wireless, Radio Wave
    - ความแตกต่างระหว่าง Switch and Router
        - Switch: จะมีกระบวนการทำงานถึงแค่ layer ที่ 2 นับจากล่างสุด การทำงานของ Switch คือการที่เราส่งข้อมูลแบบจำเพาะเจาะจงให้คนนั้นหลาย เปรียบเสมือนคนโบกรถกลางสี่แยก แต่ประเด็นคือ คนนี้เขารู้หมดเลยว่า แต่ละคนควรจะไปไหน ประมาณนี้
        - Router: จะมีกระบวนการทำงานถึง layer ที่ 3 เพราะหา best path จากการใช้ Routing Algorithm

# Chapter 2: Application

- Principles of network applications
    - Client-server paradigm
        - Server
            - จะทำงานตลอดเวลา, IP Address ที่แน่นอน, ส่วนใหญ่ Server จะตั้งอยู่ที่ Data Center
        - Clients
            - จะทำอะไรต้องมีการติดต่อสื่อสารกับ Server, สามารถเปิด/ปิด การเชื่อมต่อกับ Server ได้, มี IP Address ที่เปลี่ยนแปลงตลอด, Client จะไม่สื่อสารกันเอง
    - P2P Architecture: Peer to Peer
        - คือ Network ส่วนบุคคลที่สามารถสื่อสารกันได้โดยตรงโดยไม่ต้องผ่านตัวของ Central Server เลย
            - Devices ใน Network นี้เป็นได้ทั้ง Client และ Server
            - สามารถกระจายไฟล์และข้อมูลต่างๆได้ โดยไม่ต้องผ่าน Server ที่อาจจะมีการขอดูสิทธิ์เข้าถึงพื้นที่ต่างๆ
            - ปรับขยายได้ง่าย
            - เสี่ยงต่อการโดนคุกคามจากไฟล์ที่ติด Malware ได้ง่าย
        - Application ที่ใช้ P2P
            - การ shared file, music, video กันเอง ผ่าน BitTorrent
            - การทำ document editing online
            - Game online ที่มีใครคนใดคนนึงเป็นหัวห้อง
    - IPC - Inter Process Communication
        - น้องคือคนที่ควบคุมการทำงานของ process ที่มีการทำงานเกี่ยวกับ network ทุกๆอย่าง ไม่ว่าจะเป็นการ ขอเข้าถึงพื้นที่ร่วมกันเพื่อทำการอ่าน หรือ เขียนลงในพื้นที่นั้นๆ การส่งข้อมูลที่จะผ่าน socket การแยก process เพื่อให้งานเสร็จไวขึ้น
    - Socket
        - น้องคือ คนที่สามารถแลกเปลี่ยนข้อมูลกันระหว่าง Devices จบเลย คือทุกอย่างที่มีการสื่อสารกันผ่าน Network น้องคนนี้รับจบ น้องเป็นเหมือนพื้นที่ที่จะมีการเก็บข้อมูลที่ได้รับมา หรือว่าที่จะส่งไปเพื่อเตรียม Exchange Data
    - Addressing Processes
        - ทุกๆ process จะมีเลข IP Address เป็นของตัวเองเพื่อใช้ในการอ้างอิงเพื่อขอเข้าถึงพื้นที่ต่างๆ ตามสิทธิ์ที่ตัวเองได้รับ นอกจากนี้แต่ละ Process ยังต้องมีการกำหนด port number ของตัวเองอดีด้วย เพราะว่าเมื่อข้อมูลที่ถูก Exchange data มาแล้วผ่าน socket ตัวของ socket ก็จะหาว่าข้อมูลนี้ควรไปอยู่ที่ Process ไหนผ่านตัวของ port number นี่แหละ
    - สิ่งที่ Application Layer ต้องการจาก Transport Layer
        - Data integrity: ความถูกต้องของข้อมูล ข้อมูลต้องมาและไปแบบครบๆ ไม่มีขาดหาย
        - Throughput: มีการกำหนด minimum bandwidth ที่ชัดเจนเพื่อป้องกันการสูญหายของข้อมูล
        - Timing: เวลาที่ใช้ในการเข้าถึง หรือ ส่งข้อมูล (Delay)
        - Security: ความปลอดภัย เช่น การเข้ารหัส
    - Internet transport protocols services
        - หัวข้อนี้จะอยู่ในการทำงานของ Transport Layer แบ่งออกหลักได้ 2 ตัว คือ
            - TCP - Transmission Control Protocol: File Transfer, E-mail, Web - browsing
                - การส่งข้อมูลมีความน่าเชื่อถือ
                - มีการส่งข้อมูลที่พอดีทั้งผู้ส่งและผู้รับสามารถรับได้แบบไม่เกิดปัญหา Rs = Rc
                - มีการควบคุมการจราจรของการส่งข้อมูล
                - ต้องมีการจองพื้นที่การติดต่อสื่อสารกันก่อน
            - UDP - User Datagram Protocol: Online Gaming, Streaming Media และ DNS Lookups
                - เหมาะแก่การส่งข้อมูลแบบ real - time สำหรับ App ที่ต้องกรความเร็ว แต่ก็มีโอกาสเกิด Error ด้วยเช่นกัน แต่ก็เป็น Error ที่รับได้
            
            <aside>
            💡 ในช่วงแรก การส่งข้อมูลผ่าน TCP นั้นไม่ปลอดภัยทำให้มีการดักจับข้อมูลไปใช้ได้ เมื่อเป็นเช่นนั้น จึงเกิดน้อง TLS - Transport Layer Security ขึ้นมา เอาไว้ใช้กับ Application Layer เพื่อเป็นการกำหนดการ Encryption เอาไว้เลย
            
            </aside>
            
- Web and HTTP
    - HTTP Connections มี 2 ประเภท ได้แก่
        - Non - persistent HTTP: ทุกๆ obj ที่มีการส่งมาจะต้องมีการเริ่ม HTTP connect อีกรอบนึง นั่นหมายความว่า ถ้ามี 11 obj ต้องทำ HTTP connect ถึง 11 รอบมันเสียเวลา
            - Round Trip Time: คือเวลาที่เราส่ง Respond ไปหา Server และ Server ตอบกลับมาเวลาทั้งหมดที่ใช้คือ ตัวนี้ และมีสูตรว่า
                - วิธีการคำนวณหาค่า non-persistent HTTP response time
                
                $$
                response time = 2RTT + fileTransmissionTime
                $$
                
        - Persistent HTTP: เลยมีประเภทนี้ขึ้นมา คือ Server ไม่ต้องปิดเปิดค้างไว้เลย
    - MIME: Multipurpose Internet Mail Extensions
        - น้องคือคนที่จะบอกว่า format ของ file ว่า file ที่ส่งผ่าน network มาคืออะไร แบบน้องทำหน้าที่ในการติดป้ายบอกชื่อ file นั้นๆ ให้คอมรู้ว่าข้อมูลที่ส่งมาเป็นประเภทอะไร
        - น้องมี 2 ส่วน คือ
            - Main Type: แบ่งประเภทข้อมูลแบบกว้างว่าเป็นอะไรเช่น Text, Video, Sound, Image
            - Sub Type: เป็นการระบุจำเพาะของ format file จาก Main type เช่น Mp4, JPG, HTML
                - เช่น Text/HTML, Video/Mp4 ประมาณนี้
    - HTTP Request Messages
        - POST Method: การกรอกข้อความเยอะๆลงใน web
        - GET Method: การกดเข้า link
        - HEAD Method: การกดเข้า link เหมือนกันแต่ข้อมูลที่ได้จะมาแค่ส่วนของ Head ส่วนของ Body ที่เป็น HTML ไม่ได้มาด้วย
        - PUT Method: การเอา file ไปวางใน server แต่ส่วนมากคนที่ทำจะเป็นคนที่ได้รับอนุญาติไม่ได้ทำได้ทั่วไป
    - HTTP Respond Status Codes
        - 200 (OK): สถานะคำขอปกติ สามารถทำตามคำขอนี้ได้
        - 301 (Move Permanently): obj บน server ไม่มีการเปลี่ยนแปลงส่ง obj ไปได้เลย
        - 400 (Bad Request): ผู้ใช้งานพิมพ์อะไรมาไม่รู้เรื่อง
        - 404 (Not Found): ไม่พบ file บน server นี้
        - 505: HTTP Version not found
    - State Full Vs State Less ของ HTTP
        - State Full: คือการที่ Server เก็บทั้ง request และ respond เอาไว้ทำให้เวลาได้รับคำสั่งอะไรมา ต้องมีการเช็คกับแคชที่ตัวเองเก็บไว้ก่อนมีไหม ถ้ามีก็ส่งเลย แต่ถ้าไม่มีก็ต้องรอ operation แล้วก็ค่อยส่งไป แต่โดยปกติแล้วแคชที่เก็บไว้จะไม่ค่อยมีประโยชน์เท่าไรเพราะว่า request มีการเปลี่ยนแปลงจาก client ตลอด ยกเว้นซะจากว่า client คนนั้นจะทำอยู่อย่างเดียวเรื่อยๆ บนหน้า webpage
        - State Less: อันนี้คือ Server ไม่เก็บอะไรทั้งสิ้นทั้ง request และ respond ต่อให้เซิฟจะล่ม หรือ client จะตายก็ไม่ส่งผลเพราะพอเข้ามาก็เหมือนเริ่มทำงานใหม่ทุกครั้ง ดังนั้นจึงง่ายต่อการ Scalability ไม่เหมือน State Full ที่ขยายได้ยากนอกจากนี้ถ้าหากว่า Client เกิดคอมดับหรือขาดการติดต่อระหว่างทาง แล้ว Client กลับมาใหม่ มีโอกาสที่ Client ไม่รู้ว่าตอนนี้ Server ทำอะไรอยู่เพราะ Server เก็บ State เอาไว้
            
            <aside>
            💡 เพราะว่า State Less ไม่มีการเก็บอะไรทั้งสิ้นจึงเกิด Cookie ขึ้นมา
            
            </aside>
            
    - Cookies
        - Cookies คืออะไร
            - น้องคือ text file เล็กๆที่เก็บข้อมูลการท่องเว็บไซต์ของเราเอง และถูกเก็บไว้ในเครื่องของเรา เพราเวลาเราเข้าเว็บไซต์อะไรตัวคอมของเราเองจะแปะ Cookie ไปด้วยเพื่อบอกว่า เออนี่เป็นตัวเรานะเราเคยเข้ามาแล้วรอบนึง ดังนั้นกิจกรรมที่เราทำบนเว็บนั้นๆจึงจะยังอยู่เพราะ Cookie ของเรานั่นเอง
        - Cookies ทำงานอย่างไร
            - Website sends cookie: เมื่อคุณเข้าเว็บไซต์ไหนเป็นครั้งแรก เว็บไซต์นั่นจะส่งคุกกี้กลับมาให้เราด้วย
            - Browser store cookie: บราวเซอร์ของเราจะเก็บคุกกี้เอาไว้ในคอมของเรา
            - Cookie sent back to visited: เมื่อเราเข้าเว็บเดิมซ้ำ บราวเซอร์ของเราจะดึงคุกกี้ที่เก็บไว้ในคอมเราส่งไปกับ request ด้วยตอนไปหา web server นั้นๆ
        
        <aside>
        💡 กฎหมายที่ควบคุม Cookies คือ GDPR - EU General Data Protection Regulation
        
        </aside>
        
    - Web caches (AKA proxy servers)
        - Web caches มี 2 ประเภท
            - Client - Side Caches: มีอยู่แล้วใน browser ของเรา และเก็บข้อมูลการท่องเว็บไซต์ไว้บนคอมของเรา
            - Server - Side Caches: สร้างโดย ISP หรือ CDNs โดย web server caches จะถูกตั้งให้อยู่ใกล้ๆกับผู้ใช้งานตามหลักภูมิศาสตร์เพื่อลดระยะเวลาในการเข้าถึง
        - Web caches คืออะไร: น้องคือระบบที่ถูกออกแบบมาเพื่อจัดเก็บข้อมูลชั่วคราโดยข้อมูลนั้นจะเป็นข้อมูลที่ถูกเข้าถึงบ่อยๆ โดยน้องจะทำหน้าที่เป็นตัวกลางระหว่าง เรา กับ original server โดยน้องมีจุดมุ่งหมายหลักในการเพิ่มประสิทธิภาพในการใช้ บราวเซอร์ ของคุณให้เร็วขึ้น โดยถ้าหากว่าข้อมูลที่เราอยากจะเข้ามีใน web caches อยู่แล้วก็ไม่จำเป็นที่จำต้องวิ่งไปหาถึง original server อีกให้เสียเวลา เอาจาก caches ได้เลย
        - Web cache’s benefits:
            - Faster loading time
            - Reduced network traffic
            - Improved offline access
        - Conditional GET
            - คืออะไร: อย่างที่บอกไปว่าเวลาเราเข้า web ไหนจะมีการเก็บ cache เอาไว้ ซึ่งถ้าหากว่าเรามีการเข้าเว็บซ้ำ นี่คือสิ่งที่จะเกิดขึ้น
                - Conditional Check: ถ้าหากว่าเรามีการเข้าเว็บเดิมสิ่งที่เกิดขึ้นคือ เราจะยังไม่ได้รับข้อมูลจาก web cache แต่ว่าตัวของ web cache จะมีการส่ง request ไปหา original server ก่อน นี่คือที่มาของคำว่า “Conditional Get”
                - Modified Date (ETag): จากนั้น request ที่ตัวของ web cache ที่ส่งไปนั้นจะมีการกำกับหมายเลข ETag เอาไว้ด้วยเพื่อบ่งบอกว่า เวอร์ชันข้อมูลที่ web cache เก็บไว้อะ คือเวอร์ชันนี้นะ บน server อะตรงไหม
                - Server Respond: server จะทำการเช็คหมายเลข ETag ว่าตรงไหม
                    - Unmodified: ถ้าตรง หมายความว่า ข้อมูลนี้บน original server ไม่ได้มีการเปลี่ยนแปลงอะ web cache สามารถส่งข้อมูลให้กับ client ได้เลย
                    - Modified: ถ้าไม่ตรง นั่นหมายความว่า ข้อมูลเว็บไซต์ที่บน original server มีการเปลี่ยนแปลงดังนั้น server จะทำการส่งข้อมูลใหม่พร้อมกับแนบ ETag ใหม่ไปด้วย เพื่อที่จะให้ web cache นั้นอัปเดตข้อมูลและทำการส่งข้อมูลไปให้กับ client
    
    จบ HTTP 1.1
    
    ---
    
    - HTTP version 1:
        - จะมีการส่ง obj ที่อยู่ใน HTML แต่ละอันแบบ FCFS ทำให้ข้อมูลที่มีขนาดเล็กๆต้องรอข้อมูลที่มีขนาดใหญ่แสดงผลให้เสร็จก่อน แล้วนอกจากนี้ถ้าเกิดว่า obj ที่มีขนาดใหญ่นั้นดันมี bit loss ก็ต้องเสียเวลาส่งใหม่อีก แล้วไอ้ obj กลุ่มเล็กๆ อะ ก็ต้องให้ไอ้พี่ใหญ่มันทำเสร็จก่อนแล้วตัวเองค่อยต่อ เราเรียกเหตุการ์แบบนี้ว่า HOL - Head of Line Blocking ซึ่งนี่เป็นปัญหามากสำหรับ HTTP version 1.0
    - HTTP version 2.0
        - มีการเพิ่ม priority ของแต่ละ obj เพิ่มเข้ามาทำให้ปัญหาของ HTTP 1.0 ในด้านการส่ง obj นั้นหมดไป
        - น้อง 2.0 จะมีการส่ง obj ไปเลยล่วงหน้าโดยไม่ต้องให้ client ขอก่อน
        - น้อง 2.0 มีการแตก obj ขนาดใหญ่ ให้เหลือเพียงขนาดเล็กๆ
    - HTTP version 3.0
        - เนื่องจากว่าทั้ง 1.0 และ 2.0 ยังมีการใช้เป็นแบบ single TCP connection อยู่ ซึ่งหมายความว่า
            - ถ้าเกิดข้อมูลสูญหายต้องมีการส่งข้อมูลใหม่ทั้งหมด ทำให้การส่งข้อมูลในส่วนอื่นต้องมีการหยุดชะงักเพื่อที่จะต้องส่งข้อมูลคนนี้มาก่อน
            - ไม่มีระบบรักษาความปลอดภัย
        - ดังนั้น 3.0 จึงออกแบบมาเพื่อแก้ไขส่วนตรงนี้และนอกจากนี้ 3.0 ยังมีการเปลี่ยน Transport เป็น UDP เพื่อตอบสนอง client ในปัจจุบันที่มีการใช้ social media กันมากขึ้นทำให้ข้อมูลต้องมีการส่งที่เน้นไว โดยคุณภาพคิดเป็นเรื่องรองลงมา
- E-mail, SMTP, IMAP
    - Email มี 3 ส่วนประกอบสำคัญ คือ
        - User Agent (Mail User Agent): อันนี้คือ software ที่เราใช้อ่าน เขียน และส่ง e-mail นั่นแหละ
            - เช่น Microsoft Outlook, Gmail or Apple Mail
        - Mail Server (Mail Transfer Agent): MTA เป็นชื่อซอฟต์แวร์ที่ Gmail ใช้ดำเนินการทั้งหมดไม่นับ protocol นะ โดยขั้นตอนมีดังนี้
            - Inbound Emails: หมายความว่า พอตัวของ MUA ส่ง email มาแล้วอะ ทุกๆ email จะเข้ามาที่ตัวของ MTA จากนั้น MTA จะพยายามทำทุกวิธีทางเพื่อที่จะได้ส่ง email ไปหาคนที่เราต้องการจะส่งให้ได้
            - Routing and Delivery: ในขั้นตอนนี้ MTA จะใช้หลายเทคนิคมากในการหาเส้นทางที่จะส่ง email ของเราให้กับผู้รับ อย่างเช่น อาจจะใช้ DNS อะไรงี้ในการหาว่าคนรับเนี่ยอยู่ใน Domain name system เดียวกันไหม
            - Queueing and Retries: เมื่อ MTA รู้แล้วว่า คนที่รับ email นี้อยู่ที่ไหน MTA ก็จะมีการส่ง email ไปให้กับคนๆนั้นเลย แต่ถ้าหากว่าคนๆนั้นยังไม่พร้อมที่จะรับ email MTA ก็สามารถที่จะทำการ Queue ข้อความเอาไว้ให้ได้ นอกจากนี้ MTA ยังสามารถที่จะทำการ Retries mechanism email นั้นอีกรอบนึงด้วย เพื่อเป็นการเช็คว่า email ได้ส่งถึงคนๆนั้นแล้ว
            - Security: เป็นสิ่งที่ MTA จะคอยเฝ้าระวังเอาไว้ว่า email ที่ส่งกันเนี่ยมันเป็น spam ไหม หรืออย่างไร
        - SMTP - Simple Mail Transfer Protocol: คือน้อง MTA อะโดยรวมแล้วคือ เขาจัดหาทางให้เราว่า email เราจะไปถึงผู้รับได้อย่างไร แต่ตอนที่ ส่ง หรือ รับ email อะ SMTP เป็นจัดการทั้งหมด
            - Alice → sent mail → SMTP Server (Mail Server) → sent mail → Mail Server → Bob
        - IMAP - Internet Mail Access Protocol: น้องคนนี้คือ คนที่เก็บ email ทุกอย่าง ทุกสถานะ ทุกป้ายกำกับที่เราจัดประเภทเอาไว้ น้องคนนี้เป็นคนจัดการให้เราหมด แม้กระทั้งเวลาเราจะเปิด Mail อะ Browser ก็ต้องมาคุยกับน้องคนนี้เพื่อเปิด Mail เราขึ้นมา
- The Domain Name System (DNS)
    - DNS คืออะไร: น้องเหมือนสมุดเล่มเหลืองที่แบบว่าเรารู้แค่ชื่ออะ น้องก็สามารถเอาชื่อนั้นไปหาว่าอยู่ที่ไหนแล้วส่งเป็นที่อยู่ที่เป็นตัวเลขมาให้เรา เราเลยนำหลักการนี้แหละมาใช้กับ Root Server
    - DNS มี 3 ขั้น เรียงจากใหญ่ → เล็ก ได้แก่
        - Root: Root จะทำงานในขั้นสุดท้ายเพราะขั้นก่อนหน้าก็จัดการได้เหลือเฟืออยู่แล้ว ยกเว้นซะจากว่าจะแปลงจาก String → Numeric ไม่ได้ก็อาจจะมีที่ Root ได้
            - DNSSEC (Domain Name System Security Extension): ทำหน้าที่คอยดูแล Message ที่ส่งไปมาว่ามีความปลอดภัยไหม ซึ่งตอนนี้ message ส่วนมากก็ใส่ HASH เอาไว้อยู่แล้ว
            - ICANN (Internet Corporation for Assigned Names and Numbers): น้องคือคนที่ระบุตำแหน่งและรักษา Database เอาไว้ คือน้องเขารู้ว่าคนที่เข้ามาดูข้อมูลอะ มาจาก DNS ไหนและมี IP - Address ของเครื่องนั้นว่าอยู่ที่ไหน
        - Top Level Domain (TLD): พวก .com .th .edu .net .org
        - Authoritative: อันนี้คือ ชื่อแล้วอะ พวกแบบ [riotgames.com](http://riotgames.com) เนี่ยชื่ออย่างเงี้ย แล้ว .com อะเป็น TLD
    - DHCP - Dynamic Host Configuration Protocol
        - น้องเป็น Network protocol ที่จะ Assign IP - Address แบบ Configuration มาให้เราเพื่อเอาไปท่อง website ต่างๆ โดยมีขั้นตอนดังนี้
            - DHCP Discovery: เครื่องของเราจะไปขอ IP - Address จาก DHCP
            - DHCP Offer: DHCP จะตอบมาโดยให้เราเลือกว่าจะเอา IP - Address อะไร
            - DHCP Request: จากนั้นเราจะส่ง request ไปเพื่อบอกว่าเราเลือก IP - Address นี้แหละ
            - DHCP Acknowledgement: จากนั้น DHCP จะ Assign IP - Address นี้ให้กับเราและเราก็เอา IP - Address นี้ไปท่องเว็บต่อ
    - Query
        - Iterated: Local DNS server ทำงานหนักสุด เพราะต้องคอยไปถามทุกๆตัวกว่าจะได้ข้อมูลมา
        - Recursive: Root server ทำงานหนักสุด เพราะ มีการถามเป็นต่อๆแล้วตอบกลับมาเป็นต่อๆ อีก แล้วจำนวนของ Root server มันมีน้อยอะ ทำให้เขาทำงานหนักสุด
    
    <aside>
    💡 Caching DNS Server มีส่วนช่วยทำให้ Root server นั้นทำงานได้น้อยลงในวิธีการของ Recursive
    
    </aside>
    
    - DNS Record:
        - Type A: บอกแค่ชื่อ host name กับ IP - address
        - Type NS: บอกชื่อ Name Server
        - Type MX: บอกชื่อ Mail Server คล้ายๆ NS นั่นแหละเผลอๆ ชื่อเดียวกัน
        - Type CNAME: บอกชื่อ เสมือน ชื่อที่แบบว่าพิมพ์แล้วก็เจอผลลัพธ์เดียวกัน Canonical Name
        
        <aside>
        💡 DNS ใช้ UDP เพราะต้องการความเร็วอีกอย่าง packet มีขนาดเล็กต่อให้ loss ก็ re ได้
        
        </aside>
        
- P2P applications
    - File Distribution Time
        - Client Server
            - N = N copy files
            - F = One file
            - Us = Server upload
            - Dmin = Lowest download from client
                
                $Dc-s = max[NF/Us, F/Dmin]$
                
        - P2P
            - (Us + summation (Ui)) = Max upload from server + peer device
                
                $Dp2p = max[F/Us, F/Dmin, NF/(Us + summation(Ui))]$
                
    - BitTorrent
        - คืออะไร: น้องคือ ตัวแชร์ไฟล์ขนาดใหญ่ข้าม Internet โดย BitTorrent จะแบ่งไฟล์ออกเป็นชิ้นเล็กๆ “Chunk” และกระจายข้ามผ่านไปยัง User ต่างๆ
        - ทำงานอย่างไร
            - Torrent File: เป็น file เล็กๆ .torrent เป็นนามสกุลไฟล์ที่จะประกอบไปด้วยข้อมูลของไฟล์ขนาดใหญ่ที่คุณต้องการจะ Download เช่น ชื่อ ขนาด และ list ของ trackers ต่างๆ ทั้งหมดนี้ได้มาจากการติดต่อกับ Server ในช่วงแรกโดยใช้ TCP
            
            <aside>
            💡 Trackers คือ กลุ่มคนที่อยู่ใน list เพราะว่ากลุ่มคนเหล่านี้คือคนที่เขามีไฟล์ที่เราต้องการจะ download และเราก็ต้องไปเอาจากกลุ่มคนเหล่านี้นี่แหละ
            
            </aside>
            
            - Seeding: คือคนที่มี file ที่จะกลายมาเป็นผู้ให้และแชร์ส่วนนั้นไปให้คนอื่นๆ รวมถึงเราด้วย
            - Leeching: คือกลุ่มคนที่มา download ไฟล์จากเราอะ เราเรียกว่า “Leecher” พวกเขาจะ download ชิ้นส่วนไฟล์มาจากคนอื่นๆ และนอกจากนี้ตัวเขาเองก็สามารถเป็น Seeding ได้นะ ถ้าหากว่าเขาโหลด File นั้นเสร็จแล้ว
        - Tit - for - tat
            - เป็นรูปแบบของ BitTorrent เพื่อหาความเหมาะสมในการกระจายไฟล์ระหว่าง peers
            - ทำงานอย่างไร
                - Reciprocity: client จะติดตามอัตราการ upload จาก peers คนอื่นๆ
                - Prioritization: peers ไหนที่สามารถ upload ข้อมูลได้มากกว่ากันให้กับ client คนๆนั้นจะกลายเป็นคนที่มี priority สูงที่สุด เพื่อที่จะได้ให้ client ได้โหลดไฟล์เสร็จที่เร็วขึ้น
            - Tit - for - tat ที่ใช้กับรูปแบบอื่น
                - Optimistic unchoking: ทุกๆเวลาที่กำหนดไว้จะมีการสุ่ม peers คนอื่นๆขึ้นมาเพื่อหา peers ที่มีอัตราการ upload ที่สูงกว่าเมื่อหาเจอแล้วก็ตัด peer ที่มีอัตราการ upload ต่ำที่สุดในที่นี้ออก จะได้ทำให้ client download file ได้เร็วขึ้น
                - Rarest first: ให้ลำดับความสำคัญกับ chunk ที่มีการพบเห็นน้อยที่สุดในกลุ่ม peers นั้นๆก่อน
- Video streaming and content distribution networks
    - Challenge: ทำยังไงถึงจะสามารถส่งข้อมูล Video streaming เป็นล้านๆ คนได้แบบไม่พัง
        - Encode Image
            - Spatial: คือการที่เราจะเก็บ pixel ที่มันซ้ำกันเยอะๆอะ เราจะไม่ส่งข้อมูลของส่วนนั้นไป แต่ว่าเราจะบอกว่า ตั้งแต่ pixel ที่เท่านี้ ถึง เท่านี้อะมีสีนี่นะ ประมาณนี้ จะได้ไม่ตรงส่งทุก pixel
            - Temporal: อันนี้คือ ส่งแค่ pixel ที่มันมีความแตกต่างจากภาพที่แล้วอะ ส่วนอันที่เหมือนกันก็ไม่ส่ง
        - การส่ง video
            - CBR (Constant bit rate): คือการส่งไฟล์ encode ด้วย bit rate ที่คงที่ไม่มีการปรับเปลี่ยนตามขนาดของ bandwidth
            - VBR (Variable bit rate): น้องคนนี้สามารถส่งไฟล์ encode ด้วย bit rate ที่สามารถปรับเปลี่ยนได้ตลอดเวลาตามขนาด bandwidth ที่เปลี่ยนแปลงไปตามแต่ละ devices
        - DASH - Dynamic Adaptive Streaming over HTTP
            - น้องเป็นคนที่สามารถทำให้เราปรับค่า definition ได้ว่าจะเอา High or Low ก็คือน้องสามารถกำกับการส่งได้นั่นแหละ
        - Manifest File: manifest file จะทำให้เราได้รู้ว่า chunks แต่ละ chunk อยู่ที่ไหนโดยน้องจะให้ URL มาแล้วไปตามที่นั้น เพราะแน่นอนว่า Netflix ไม่ได้เก็บไฟล์ไว้ที่เดียวแต่เขาแตกออกไปไว้หลายๆที่ ตาม CDNs ทั่วโลก
- Socket programming with UDP and TCP
    - UDP - User Datagram Protocol: เนื่องจาก UDP ไม่มีการทำ Handshaking ก่อน และไม่มีการจอง path ด้วยทำให้ทุกๆครั้งที่มีการส่ง datagram ไปจะต้องมีการกำหนด IP - Address และ port number ของ process นั้นด้วยๆ เพราะว่าตอนที่ Network Interface Card ได้รับข้อมูลมาตัวของ OS จะเช็คว่าข้อมูลที่เข้ามานี้ process ไหนต้องการโดยเช็คจาก port number และ IP - Address ของ process นั้นๆ นั่นแหละ นอกจากนี้ข้อมูลที่ได้รับอาจมีการสลับลำดับกัน หรือ อาจหายได้ เพราะว่าเราต้องการความเร็วเลยได้ผลลัพธ์แบบนี้ แต่ก็เป็นข้อเสียที่รับได้
    - TCP - Transmission Control Protocol: อันนี้คือ ส่งข้อมูลเป็น Bytes Stream ทุกๆการส่งไม่ต้องมีการส่ง port number กับ IP - Address มาด้วยเพราะว่ามีการทำ Handshaking แล้วเรียบร้อย

# Chapter 3: Transport Layer

- Transport-layer services
    - บทนี้จะอธิบายเกี่ยวกับเรื่องเริ่มต้นของการส่งข้อความ
        - Transport protocols actions in end system
            - sender: จะมีการแยกย่อย message ที่ได้จาก App layer ออกเป็น segment หลังจากนั้นก็ส่งให้กับ Network layer
            - receiver: ก็จะมีการรวบรวม segment เหล่านั้นอะ ให้กลับมาเป็น message แล้วส่งต่อไปยัง App layer โดยจะแยก Header ออกก่อนนะ เอามาแต่ข้อความ เราเรียกว่า Demultiplexes
            - โดย Transport Layer: จะติดต่อสื่อสารกันระหว่าง process และ Network Layer จะติดต่อสื่อสารกันระหว่าง Host ที่อยู่ ณ Devices อื่นๆ
        - 2 ตัวที่ใช้ในหลักการ Internet transport protocols
            - TCP, UDP
- Multiplexing and Demultiplexing
    - Multiplexing: The Sender’s Role
        - ทำการรวมข้อมูลต่างๆ จากหลายๆ Application ให้เหลือแค่ single data stream (bytes steam) เดียวเพื่อที่จะเตรียมส่งออกไปใน Network
        - ทำการใส่ Header เอาไว้แต่ละ segment ที่มีการแยกออกมา โดยจะมีการใส่ source + destination addresses และ port number
        - จากนั้นทำการรวบรวม bytes steam ทั้งหมดแล้วส่งเข้าไปใน Network
    - Demultiplexing: The Receiver’s Role
        - ทำการแยก bytes steam ต่างๆ ออกมาให้เหมือนกับ bytes steam ที่อยู่ฝั่ง Sender ก่อนที่จะถูกรวม
        - ทำการวิเคราะห์ header ว่าข้อมูลของแต่ละ segment นั้น มีปลายทางที่ Application อะไร
        - ส่งข้อมูลที่ผ่านการวิเคราะห์แล้วไปให้กับ process นั้นๆที่ทำงานให้กับ Application นั้นๆอยู่
    - UDP: ทำการ demultiplexing หรือว่าแยกชิ้นส่วนออก โดยใช้แค่ destination port number
    - TCP: ทำการ demultiplexing โดยต้องใช้ถึง 4-tuple ในการ Identified TCP Socket
        - Source IP Address
        - Source port number
        - Dest IP Address
        - Dest port number
- Connectionless transport: UDP
    - UDP - User Datagram Protocol
        - การใช้ connection transport แบบ UDP คือ
            - ไม่มีการทำ Handshaking ก็คือ ไม่มีการจองพื้นที่และ Path ระหว่าง Host & Destination
            - ส่งข้อมูลได้เต็ม Bandwidth เพราะไม่มีการทำ congestion control
            - ช่วยทำให้ RTT ลดลงไม่ต้องมีการทำ Handshaking ก่อน
        - UDP use
            - DNS
            - SNMP - Simple Network Management Protocol
            - HTTP/3
    - Checksum
        
        ![https://cdn.discordapp.com/attachments/1210100621697490965/1273108828178878465/image.jpg?ex=66bd6a7d&is=66bc18fd&hm=564bbfbd5a6a66edebd188518cb1a42a5c4da45f20063d29052f794cba7a5732&](https://cdn.discordapp.com/attachments/1210100621697490965/1273108828178878465/image.jpg?ex=66bd6a7d&is=66bc18fd&hm=564bbfbd5a6a66edebd188518cb1a42a5c4da45f20063d29052f794cba7a5732&)
        
- Principles of reliable data transfer
    - บทนี้จะกล่าวเกี่ยวกับการ Transfer ข้อมูลระหว่าง Sender กับ Receiver ผ่าน Underlying channel (Physical Link) โดย Underlying channel ที่ดีต้องไม่มี bit errors และ loss of packet
    - RDT = Reliable Data Transfer
        - 1.0
            - ยังมีแค่การส่ง และ รับตามปกติไม่มีการเช็คอะไรทั้งสิ้น
        - 2.0
            - เวอร์ชั่นนี้มีการ checksum กันเกิดขึ้นทำให้สามารถรู้ได้ว่าข้อมูลที่ส่งมาเกิด bit flip และยังมีการเช็ค corrupt ด้วย
                - โดยถ้าหากว่าเราเอา Data + Checksum แล้วข้อมูลเป็น 1’s หมดนั่นเท่ากับว่าข้อมูลที่ส่งมาไม่มี bit flip ส่ง ACKs (Acknowledgement) กลับไปได้ เพื่อบอกให้ sender ส่งอันต่อไปมาได้เลย
                - แต่ถ้าหากว่าตรงกันข้ามกับเงื่อนไขบนก็ส่ง NAKs (Negative Acknowledgement) กลับไปเพื่อขอให้ sender ส่งซ้ำอีกรอบหรือที่เรียกว่า retransmission
            - 2.1
                - เวอร์ชั่นนี้จะมีการปรับปรุงตรงที่ว่า ถ้าหาก ACKs || NAKs พังจะทำยังไงน้องคนนี้เลยมีการเพิ่มตัวแปรใหม่นั่นก็คือ sqn (Sequence Number# Packet) นั่นเอง
            - 3.0
                - เวอร์ชั่นนี้จะมีการปรับปรุงทั้งในด้านของ bit error และ packet loss ด้วยการใส่ Timeout เข้ามา โดยถ้าหากว่าไม่มีการตอบกลับอะไรจาก Receiver เมื่อจนหมด Timeout Sender จะทำการ retransmit อีกรอบนึง น้องคือ Stop-and-Wait-Operation
                    
                    $$
                    Usender = (L/R) + RTT + L/R
                    $$
                    
    - Go Back End
        - หมายความว่าถ้าหากว่า packet ที่ sender ส่งไปแล้วถ้ามี packet ไหนที่ receiver ไม่ได้ส่ง ACKs หรืออะไรกลับมาเลย เมื่อ Timeout หมด sender จะมีการส่งย้อนใหม่ทั้งหมดตั้งแต่ตัวที่ไม่ได้รับการยืนยัน ACKs, NAKs จาก receiver ส่วนตัวที่ได้รับการยืนยันก่อนหน้านั้นแล้ว window size จะขยับให้
    - Selective Repeat
        - น้องคนนี้ทำงานเหมือน Go Back End ทุกอย่างๆ แต่ต่างกันตรงที่ว่าน้องคนนี้จะมี Buffer ที่ส่งเอาไว้ให้ทำให้ packet ที่ส่งมาต่อให้เราไม่ได้ต้องการตัวนั้นแต่ receiver ก็จะเก็บตัวนั้นเอาไว้ใน buffer เป็น order ไว้ แล้วพอ timeout หมด ก็ส่งแค่ไอ้ตัวที่มีปัญหาซ้ำกลับมาให้ receiver นั่นเอง ส่วนตัวอื่นๆ ก็จับเอามาเรียงตามปกติเป็น ordered จากนั้นก็ extract แล้วเอา data ไปให้ Application ต่อไป
        - Sequence wraps around: คือปัญหาที่ขนาด window size = ขนาดของ sequence เช่นแบบ window size กว้าง 3 หน่วยในเชิง 1-3 แล้วตัวของ sequence ก็สามหน่วยเหมือนกันในเชิง 0-2 ทำให้เวลา window size จะเลื่อนอะ มันก็จะไปเจอ sequence number ที่มันซ้ำทำให้ตัวของ receiver คิดว่านี่เป็นข้อมูลที่ซ้ำแต่ตัวเองก็ต้องรับอยู่ดีเพราะ receiver กับ sender ไม่ได้คุยกันว่าข้อมูลที่ส่งมามันซ้ำหรือไม่ซ้ำ