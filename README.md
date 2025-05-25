# `ros_pong_semiautomatic` package  
Pong játék ROS 2-ben, Python segítségével, turtlesim vizualizációval.  
[![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

Ez a csomag egy egyszerű **Pong** játékot valósít meg ROS 2 környezetben.  
A labda (`turtle1`) két ütő (teknős) között mozog, és szögekben pattan vissza. A bal ütő (`turtle2`) kézzel irányítható, míg a jobb oldali ütő (`turtle3`) egy mesterséges intelligencia által vezérelt bot, amely próbálja követni a labdát — de verhető. 🏓

---

## 👨‍💻 Készítette:
**Szabó Áron I5EE5T és Kucserka Szabolcs ULB7DX** fejlesztette ezt a projektet tanulási célból.

---

## 🚀 Funkciók

- A labda szögben pattog az ütőkről
- Falról **nem pattan vissza**, csak ütőről
- Győzelem/vereség detektálás, ha a labda elhagyja a pályát
- Jobb oldali ütő követi a labdát, de hibázhat
- Bal oldali ütő `w/s` billentyűkkel vezérelhető

---

## 📦 Használat-  Két terminálba kell megynyitni az egyikbe a kovetkezo kodokkal elinditjuk a játékot a másik terminálba pedig a saját oldalunkat inditjuk el és w,s billentyű bemeneteket érzékeli


### 1.Terminál

```bash
cd ~/ros2_ws/src
git clone https://github.com/sze-info/ros2_py_template.git ros_pong_semiautomatic

 cd ros2_ws/

colcon build --packages-select ros_pong_semiautomatic
 . install/setup.bash
 ros2 launch ros_pong_semiautomatic launch_example1.launch.py
```


### 2.Terminál
```bash
cd ~/ros2_ws/src
git clone https://github.com/sze-info/ros2_py_template.git ros_pong_semiautomatic

 cd ros2_ws/
 colcon build --packages-select ros_pong_semiautomatic
 . install/setup.bash
 ros2 run ros_pong_semiautomatic paddle_node
```

###Játékmenet

<p align="center">
  <img src="img/jatekmenet.png" width="70%">
</p>

###Gyozelem es vereseg kiirasa

<p align="center">
  <img src="img/nyertel.png" width="70%">
</p>
<p align="center">
  <img src="img/vesztes.png" width="70%">
</p>
 
