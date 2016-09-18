from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from level_editor_data import *
class RaceSetup(DirectObject):
    def __init__(self, editor):
        editor.bgr = 0.717794537544
        editor.bgg = 0.918295800686
        editor.bgb = 1.0
        editor.loadTerrain("lavaland/world/lw")
        editor.terrain.setScale(VBase3(8, 8, 8))
        editor.terrain.setZ(0.0)
        editor.alightBrightness = 0.300000011921
        editor.dlightBrightness = 1.0
        editor.ships.append(setupShip(575.0, 393.0, 0, 167.0))
        editor.ships.append(setupShip(556.0, 396.0, 1, 167.0))
        editor.ships.append(setupShip(538.0, 400.0, 2, 167.0))
        editor.ships.append(setupShip(542.0, 415.0, 3, 167.0))
        editor.ships.append(setupShip(559.0, 409.0, 4, 167.0))
        editor.ships.append(setupShip(578.0, 404.0, 5, 167.0))
        editor.checkpoints.append(setupCheckpoint(554.0, -123.0, -182.0, 0, 1))
        editor.checkpoints.append(setupCheckpoint(787.0, -594.0, -150.0, 1, 4))
        editor.checkpoints.append(setupCheckpoint(1288.0, -589.0, -2.0, 2, 9))
        editor.checkpoints.append(setupCheckpoint(1108.0, -425.0, 89.0, 3, 12))
        editor.checkpoints.append(setupCheckpoint(876.0, -78.0, -46.0, 4, 17))
        editor.checkpoints.append(setupCheckpoint(1124.0, 228.0, -90.0, 5, 21))
        editor.checkpoints.append(setupCheckpoint(1318.0, 609.0, 46.0, 6, 27))
        editor.startingline = setupStartingline(549.0, 375.0, -195.0)
        editor.powerups.append(setupPowerup(575.0, 175.0))
        editor.powerups.append(setupPowerup(562.0, 175.0))
        editor.powerups.append(setupPowerup(544.0, 175.0))
        editor.powerups.append(setupPowerup(528.0, 175.0))
        editor.powerups.append(setupPowerup(514.0, 175.0))
        editor.powerups.append(setupPowerup(625.0, -340.0))
        editor.powerups.append(setupPowerup(613.0, -358.0))
        editor.powerups.append(setupPowerup(603.0, -374.0))
        editor.powerups.append(setupPowerup(853.0, -619.0))
        editor.powerups.append(setupPowerup(853.0, -633.0))
        editor.powerups.append(setupPowerup(853.0, -648.0))
        editor.powerups.append(setupPowerup(1119.0, -658.0))
        editor.powerups.append(setupPowerup(1119.0, -672.0))
        editor.powerups.append(setupPowerup(1119.0, -686.0))
        editor.powerups.append(setupPowerup(1205.0, -444.0))
        editor.powerups.append(setupPowerup(1205.0, -425.0))
        editor.powerups.append(setupPowerup(1205.0, -408.0))
        editor.powerups.append(setupPowerup(926.0, -369.0))
        editor.powerups.append(setupPowerup(918.0, -384.0))
        editor.powerups.append(setupPowerup(843.0, -226.0))
        editor.powerups.append(setupPowerup(843.0, -208.0))
        editor.powerups.append(setupPowerup(956.0, 103.0))
        editor.powerups.append(setupPowerup(972.0, 103.0))
        editor.powerups.append(setupPowerup(1188.0, 227.0))
        editor.powerups.append(setupPowerup(1188.0, 216.0))
        editor.powerups.append(setupPowerup(1188.0, 240.0))
        editor.powerups.append(setupPowerup(1402.0, 432.0))
        editor.powerups.append(setupPowerup(1418.0, 432.0))
        editor.powerups.append(setupPowerup(1433.0, 432.0))
        editor.powerups.append(setupPowerup(1116.0, 605.0))
        editor.powerups.append(setupPowerup(1116.0, 621.0))
        editor.powerups.append(setupPowerup(638.0, 517.0))
        editor.powerups.append(setupPowerup(654.0, 510.0))
        editor.powerups.append(setupPowerup(671.0, 504.0))
        editor.powerh.append(setupPowerh(633.0, -320.0))
        editor.powerh.append(setupPowerh(591.0, -389.0))
        editor.powerh.append(setupPowerh(1256.0, -540.0))
        editor.powerh.append(setupPowerh(1278.0, -542.0))
        editor.powerh.append(setupPowerh(1295.0, -543.0))
        editor.powerh.append(setupPowerh(938.0, -354.0))
        editor.powerh.append(setupPowerh(907.0, -399.0))
        editor.powerh.append(setupPowerh(940.0, 103.0))
        editor.powerh.append(setupPowerh(1071.0, 228.0))
        editor.powerh.append(setupPowerh(1071.0, 237.0))
        editor.powerh.append(setupPowerh(1071.0, 217.0))
        editor.powerh.append(setupPowerh(1450.0, 432.0))
        editor.powerh.append(setupPowerh(1116.0, 637.0))
        editor.powerh.append(setupPowerh(627.0, 523.0))
        editor.powerh.append(setupPowerh(685.0, 498.0))
        editor.waypoints.append(setupWaypoint(543.0, 185.0, 0))
        editor.waypoints.append(setupWaypoint(618.0, -365.0, 2))
        editor.waypoints.append(setupWaypoint(706.0, -437.0, 3))
        editor.waypoints.append(setupWaypoint(842.0, -635.0, 5))
        editor.waypoints.append(setupWaypoint(1050.0, -674.0, 6))
        editor.waypoints.append(setupWaypoint(1203.0, -674.0, 7))
        editor.waypoints.append(setupWaypoint(1279.0, -629.0, 8))
        editor.waypoints.append(setupWaypoint(1281.0, -466.0, 10))
        editor.waypoints.append(setupWaypoint(1206.0, -425.0, 11))
        editor.waypoints.append(setupWaypoint(1014.0, -425.0, 13))
        editor.waypoints.append(setupWaypoint(927.0, -369.0, 14))
        editor.waypoints.append(setupWaypoint(842.0, -287.0, 15))
        editor.waypoints.append(setupWaypoint(842.0, -137.0, 16))
        editor.waypoints.append(setupWaypoint(959.0, 29.0, 18))
        editor.waypoints.append(setupWaypoint(959.0, 175.0, 19))
        editor.waypoints.append(setupWaypoint(988.0, 228.0, 20))
        editor.waypoints.append(setupWaypoint(1231.0, 228.0, 22))
        editor.waypoints.append(setupWaypoint(1286.0, 251.0, 23))
        editor.waypoints.append(setupWaypoint(1401.0, 365.0, 24))
        editor.waypoints.append(setupWaypoint(1418.0, 431.0, 25))
        editor.waypoints.append(setupWaypoint(1388.0, 526.0, 26))
        editor.waypoints.append(setupWaypoint(1271.0, 618.0, 28))
        editor.waypoints.append(setupWaypoint(1047.0, 622.0, 29))
        editor.waypoints.append(setupWaypoint(751.0, 575.0, 30))
        editor.waypoints.append(setupWaypoint(571.0, 438.0, 31))
        editor.laps = 3
        editor.winCredits = 750
        editor.minPlace = 1
        editor.setValues()