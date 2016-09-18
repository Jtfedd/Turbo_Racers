from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from level_editor_data import *
class RaceSetup(DirectObject):
    def __init__(self, editor):
        editor.bgr = 0.40000000596
        editor.bgg = 0.40000000596
        editor.bgb = 0.40000000596
        editor.loadTerrain("city/world/cw")
        editor.terrain.setScale(VBase3(5.35364, 5.35364, 5.35364))
        editor.terrain.setZ(0.0)
        editor.alightBrightness = 0.300000011921
        editor.dlightBrightness = 1.0
        editor.ships.append(setupShip(-228.0, 493.0, 0, 89.0))
        editor.ships.append(setupShip(-228.0, 476.0, 1, 89.0))
        editor.ships.append(setupShip(-222.0, 485.0, 2, 89.0))
        editor.ships.append(setupShip(-228.0, 508.0, 3, 89.0))
        editor.ships.append(setupShip(-222.0, 501.0, 4, 89.0))
        editor.ships.append(setupShip(-215.0, 493.0, 5, 89.0))
        editor.barriers.append(setupBarrier(-352.0, -71.0, 324.0))
        editor.barriers.append(setupBarrier(-420.0, 41.0, 324.0))
        editor.barriers.append(setupBarrier(384.0, 502.0, 180.0))
        editor.barriers.append(setupBarrier(-395.0, 350.0, 269.0))
        editor.checkpoints.append(setupCheckpoint(-418.0, 295.0, 173.0, 0, 4))
        editor.checkpoints.append(setupCheckpoint(-352.0, -1.0, 176.0, 1, 7))
        editor.checkpoints.append(setupCheckpoint(-7.0, -50.0, 267.0, 2, 10))
        editor.checkpoints.append(setupCheckpoint(205.0, -310.0, 300.0, 3, 15))
        editor.checkpoints.append(setupCheckpoint(385.0, 11.0, 362.0, 4, 16))
        editor.checkpoints.append(setupCheckpoint(256.0, 485.0, 454.0, 5, 19))
        editor.startingline = setupStartingline(-238.0, 484.0, 89.0)
        editor.powerups.append(setupPowerup(-377.0, 473.0))
        editor.powerups.append(setupPowerup(-377.0, 485.0))
        editor.powerups.append(setupPowerup(-377.0, 498.0))
        editor.powerups.append(setupPowerup(-473.0, 421.0))
        editor.powerups.append(setupPowerup(-485.0, 421.0))
        editor.powerups.append(setupPowerup(-496.0, 421.0))
        editor.powerups.append(setupPowerup(-284.0, -51.0))
        editor.powerups.append(setupPowerup(104.0, -135.0))
        editor.powerups.append(setupPowerup(117.0, -135.0))
        editor.powerups.append(setupPowerup(130.0, -135.0))
        editor.powerups.append(setupPowerup(211.0, -147.0))
        editor.powerups.append(setupPowerup(283.0, -147.0))
        editor.powerups.append(setupPowerup(350.0, -147.0))
        editor.powerups.append(setupPowerup(411.0, -147.0))
        editor.powerups.append(setupPowerup(372.0, 234.0))
        editor.powerups.append(setupPowerup(384.0, 234.0))
        editor.powerups.append(setupPowerup(159.0, 472.0))
        editor.powerups.append(setupPowerup(159.0, 485.0))
        editor.powerh.append(setupPowerh(-407.0, 187.0))
        editor.powerh.append(setupPowerh(-418.0, 187.0))
        editor.powerh.append(setupPowerh(-430.0, 187.0))
        editor.powerh.append(setupPowerh(-284.0, -39.0))
        editor.powerh.append(setupPowerh(-284.0, -63.0))
        editor.powerh.append(setupPowerh(245.0, -147.0))
        editor.powerh.append(setupPowerh(319.0, -147.0))
        editor.powerh.append(setupPowerh(379.0, -147.0))
        editor.powerh.append(setupPowerh(398.0, 234.0))
        editor.powerh.append(setupPowerh(159.0, 499.0))
        editor.waypoints.append(setupWaypoint(-448.0, 480.0, 0))
        editor.waypoints.append(setupWaypoint(-477.0, 456.0, 1))
        editor.waypoints.append(setupWaypoint(-376.0, 43.0, 6))
        editor.waypoints.append(setupWaypoint(-342.0, -36.0, 8))
        editor.waypoints.append(setupWaypoint(-265.0, -48.0, 9))
        editor.waypoints.append(setupWaypoint(80.0, -56.0, 11))
        editor.waypoints.append(setupWaypoint(117.0, -91.0, 12))
        editor.waypoints.append(setupWaypoint(123.0, -281.0, 13))
        editor.waypoints.append(setupWaypoint(155.0, -316.0, 14))
        editor.waypoints.append(setupWaypoint(385.0, 455.0, 17))
        editor.waypoints.append(setupWaypoint(350.0, 481.0, 18))
        editor.waypoints.append(setupWaypoint(-216.0, 478.0, 20))
        editor.waypoints.append(setupWaypoint(-452.0, 349.0, 3))
        editor.waypoints.append(setupWaypoint(-479.0, 391.0, 2))
        editor.waypoints.append(setupWaypoint(-418.0, 88.0, 5))
        editor.laps = 3
        editor.winCredits = 600
        editor.minPlace = 1
        editor.setValues()