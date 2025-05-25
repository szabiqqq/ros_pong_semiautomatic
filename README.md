# `ros_pong_semiautomatic` package  
Pong játék ROS 2-ben, Python segítségével, turtlesim vizualizációval.  
[![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

Ez a csomag egy egyszerű **Pong** játékot valósít meg ROS 2 környezetben.  
A labda (`turtle1`) két ütő (teknős) között mozog, és szögekben pattan vissza. A bal ütő (`turtle2`) kézzel irányítható, míg a jobb oldali ütő (`turtle3`) egy mesterséges intelligencia által vezérelt bot, amely próbálja követni a labdát — de verhető. 🏓

---

## 👨‍💻 Készítette:
**Két hallgató közösen** fejlesztette ezt a projektet tanulási célból.

---

## 🚀 Funkciók

- A labda szögben pattog az ütőkről
- Falról **nem pattan vissza**, csak ütőről
- Győzelem/vereség detektálás, ha a labda elhagyja a pályát
- Jobb oldali ütő követi a labdát, de hibázhat
- Bal oldali ütő `w/s` billentyűkkel vezérelhető

---

## 📦 Használat

### 1. Klónozd és fordítsd

```bash
cd ~/ros2_ws/src
git clone https://github.com/sze-info/ros2_py_template.git ros_pong_semiautomatic
