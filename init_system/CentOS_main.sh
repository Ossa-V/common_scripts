#!/bin/bash
yum -y update       # Обновить систему, при этом сохранить устаревшие версии пакетов
yum upgrade         # Или обновить все пакеты, старые пакеты будут удалены
yum -y install mc
yum -y install net-tools.x86_64   #ifconfig
yum -y install tcpdump #tcpdump
