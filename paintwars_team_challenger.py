# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: _________
#  Prénom Nom: _________

import braitenberg_avoider
import braitenberg_hateBot
import braitenberg_hateWall
import braitenberg_loveBot


def get_team_name():
    return "[ team with no name ]" # à compléter (comme vous voulez)

def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors

def step(robotId, sensors):

    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        return braitenberg_hateWall.step(robotId,sensors)
    elif sensors["sensor_front_right"]["distance"] < 1:
        return braitenberg_loveBot.step(robotId,sensors)

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

    return translation, rotation


def step_genetic(robotId, sensors):
    sensors = get_extended_sensors(sensors)
    translation, rotation = genetic_algorithms.step(robotId, sensors)

    translation = 1
    
    if sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1:
        return braitenberg_hateWall.step(robotId,sensors)

    if sensors["sensor_front"]["isSameTeam"] == True or sensors["sensor_front_left"]["isSameTeam"] == True or sensors["sensor_front_right"]["isSameTeam"] == True:
        return braitenberg_hateBot.step(robotId, sensors)


    return translation, rotation

