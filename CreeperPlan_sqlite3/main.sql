/*
 Navicat Premium Data Transfer

 Source Server         : czw
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 05/12/2022 22:19:03
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for ComputerInformationUser_CZW
-- ----------------------------
DROP TABLE IF EXISTS "ComputerInformationUser_CZW";
CREATE TABLE "ComputerInformationUser_CZW" (
  "id" varchar(36) DEFAULT NULL,
  "user" varchar(255) DEFAULT NULL,
  "IP" varchar(255) DEFAULT NULL,
  "computerName" varchar(255) DEFAULT NULL,
  "theUser" varchar(255) DEFAULT NULL,
  "manufactureDate" varchar(255) DEFAULT NULL,
  "mainboardModel" varchar(255) DEFAULT NULL,
  "motherboardSerialNumber" varchar(255) DEFAULT NULL,
  "CPUmodel" varchar(255) DEFAULT NULL,
  "CPUserialNumber" varchar(255) DEFAULT NULL,
  "memoryManufacturer" varchar(255) DEFAULT NULL,
  "memoryModel" varchar(255) DEFAULT NULL,
  "memorySize" varchar(255) DEFAULT NULL,
  "graphicsCardName" varchar(255) DEFAULT NULL,
  "nowTime" datetime DEFAULT NULL
);

-- ----------------------------
-- Table structure for Log_CZW
-- ----------------------------
DROP TABLE IF EXISTS "Log_CZW";
CREATE TABLE "Log_CZW" (
  "id" varchar(36) DEFAULT NULL,
  "user" varchar(255) DEFAULT NULL,
  "type" varchar(255) DEFAULT NULL,
  "userPasswd" varchar(255) DEFAULT NULL,
  "searchKeywords" varchar(255) DEFAULT NULL,
  "captureGJC" varchar(2000) DEFAULT NULL,
  "captureHYGJC" varchar(2000) DEFAULT NULL,
  "captureCleanSaveGJC" varchar(2000) DEFAULT NULL,
  "operationTime" datetime DEFAULT NULL
);

-- ----------------------------
-- Table structure for UserConfigurationKeys_CZW
-- ----------------------------
DROP TABLE IF EXISTS "UserConfigurationKeys_CZW";
CREATE TABLE "UserConfigurationKeys_CZW" (
  "id" varchar(36) NOT NULL,
  "user" varchar(255) NOT NULL,
  "czw_user" varchar(255) DEFAULT NULL,
  "czw_passwd" varchar(255) DEFAULT NULL,
  "filterKeywords" varchar(2000) DEFAULT NULL,
  "filterIndustryKeywords" varchar(2000) DEFAULT NULL,
  "cleanORsaveKeywords" varchar(2000) DEFAULT NULL
);

-- ----------------------------
-- Table structure for User_CZW
-- ----------------------------
DROP TABLE IF EXISTS "User_CZW";
CREATE TABLE "User_CZW" (
  "id" varchar(36) NOT NULL DEFAULT '',
  "user" varchar(255) NOT NULL DEFAULT '',
  "password" varchar(255) DEFAULT '',
  "name" varchar(255) DEFAULT '',
  "phone" varchar(255) DEFAULT '',
  "time" date DEFAULT NULL,
  "activateStatus" varchar(255) DEFAULT '',
  "createTime" datetime DEFAULT NULL,
  "days" varchar(255) DEFAULT ''
);

-- ----------------------------
-- Table structure for VersionSet_CZW
-- ----------------------------
DROP TABLE IF EXISTS "VersionSet_CZW";
CREATE TABLE "VersionSet_CZW" (
  "version" varchar(255) DEFAULT NULL,
  "version_url" varchar(255) DEFAULT NULL
);

-- ----------------------------
-- Table structure for sqlite_user
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_user";
CREATE TABLE "sqlite_user" (
  "uname" TEXT,
  "isAdmin" BOOLEAN,
  "pw" BLOB,
  PRIMARY KEY ("uname")
)
WITHOUT ROWID;

PRAGMA foreign_keys = true;
