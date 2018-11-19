#!/bin/bash

wget -P ~/tmp/  https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.42.zip
unzip ~/tmp/mysql-connector-java-5.1.42.zip -d ~/tmp

wget -P ~/tmp/ https://downloads.jboss.org/keycloak/4.5.0.Final/keycloak-4.5.0.Final.zip
unzip ~/tmp/keycloak-4.5.0.Final.zip -d /opt

mkdir -p /opt/keycloak-4.5.0.Final/modules/system/layers/keycloak/com/mysql/main

cp ~/tmp/mysql-connector-java-5.1.42/mysql-connector-java-5.1.42-bin.jar /opt/keycloak-4.5.0.Final/modules/system/layers/keycloak/com/mysql/main