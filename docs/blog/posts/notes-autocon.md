---
# draft: true 
date: 2025-07-21
categories:
  - notes
tags:
  - links
  - autocon
---

Нотатки по AutoCon. Пам'ятаю, що було багато ідей, коли дивилася, але вже забула які.
Тому хочу передивитися старі автокони та подивитися останній AutoCon 3.

<!-- more -->


Також можна почитати блог/інформацію на сайті [NAF](https://networkautomation.forum/).

## Random thoughts

### У всіх все автоматизоване

Не стосується напряму автоконів, але слухала нещодавно подкасти мережевих
інженерів, і там обговорювали з чого почати в автоматизації і який відсоток
мереж хоч якось автоматизовані (в подкасті згадували якесь опитування і там
було, що 70% не автоматизовані ніяк). 

Нотатка для себе про те, що якщо послухати умовний автокон чи подібні
подкасти/конференції, то здається, що у всіх вже все автоматизовано і мова йде
не просто про базові скрипти на Python, а про досить високий рівень.

Але, якщо вийти за межі "бульбашки автоматизації", виходить, що багато хто ще
не пішов в цей бік чи тільки починає. І мова тут не про початківців в мережах,
а про людей, які в цій сфері багато років.

> Це, в тому числі, нагадування для себе, що ще є для кого робити контент з основ.

### Автоматизація хаоса

В організації і роботі мережі може бути накопичений великий technical debt.
Інформація про мережу в голові різних людей, в різних місцях (таблиці,
документи тощо).  В такій ситуації складно говорити про source of truth,
"правильну" автоматизацію.  Але все одно може бути актуальним базове знання
Python/Ansible та автоматизація рутини.

# AutoCon

# AutoCon 0

## [AutoCon 0 Day One Keynote: John Willis](https://www.youtube.com/watch?v=S2atmZlASAs&list=PLP6VWb4PEbEo4i47JpOykMCM-qt2SpO9r&index=4)

Багато корисних ідей і додаткових матеріалів.
Варто перечитати/прочитати:

* The Phoenix Project
* Effective DevOps
* The DevOps Handbook, 2nd Edition

І загальна думка "це ж було вже" і, що так само, як колись була фантастичною думка
про 10 deployments в день, зараз може здаватися, що автоматизація неможлива.
Це все дуже спрощено, але схожого багато.

## [Mini Track: The State of Network Automation](https://youtu.be/o41VuaI3_R4?si=cEI0uCWSZy4TlhvX)

Думки схожі з попереднім відео:

* є що взяти в девелоперів і в devops: CI/CD, source of truth, ... 

## [Applying Platform Engineering Principles to On-Premises Network Infrastructure - Kaon Thana](https://youtu.be/nlDrSzzzybE?si=I-ShuOvYbnDktoa3)

Більш наближене до життя мережевих інженерів в невеликих/середніх компаніях.

* Є SoT, але там не вся інформація.
* Є перевірка відповідності конфігу до "golden config", але все ще можливі
  зміни через CLI
* зробили staging area з containerlab, де створюється частка, на якій будуть
  робитися зміни і відпрацьовуються перед deployment в production
* Ansible + Ansible Tower, де можливо, але також є Python скрипти для задач де
  Ansible не підходить

Links:

* [Github Kaon Thana](https://github.com/kaon1/golden-config-engine/tree/main)
* Blog post [Golden Configuration Deployment with Ansible and Netbox](https://kaonbytes.com/p/golden-configuration-deployment-with-ansible-and-netbox/)

## [Mini Track: Challenges to Network Automation Adoption](https://youtu.be/epGa0tMDfrQ?si=t546v7_HnuJFbJAa)

