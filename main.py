"""
Vincent Brouillet
405
TP6
project rock, papier, cissors sur arcade
"""
import random

import arcade

from game_state import GameState
from attack_animation import AttackType, AttackAnimation

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TP6"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.clear()
        arcade.set_background_color(arcade.color.GRAY)

        self.state = None

        self.rpc = None
        self.appuyer = None
        self.score1 = None
        self.score2 = None
        self.win_lose = None

        self.player = None
        self.compy = None
        self.static_list = None

        self.square_list = None

        self.rock = None
        self.paper = None
        self.cissors = None
        self.rock_list = None
        self.paper_list = None
        self.cissors_list = None

        self.d_rock = None
        self.d_paper = None
        self.d_cissors = None

        self.compy_move = None

        self.pointage_joueur = None
        self.pointage_bot = None

    def setup(self):
        self.state = GameState.NOT_STARTED

        self.pointage_joueur = 0
        self.pointage_bot = 0

        self.rpc = arcade.Text("Roche, Papier, ciseaux", 100, 550, arcade.color.RED_DEVIL, 50)
        self.appuyer = arcade.Text(" ", 100, 500, arcade.color.LIGHT_BLUE, 20)
        self.score1 = arcade.Text(f"pointage du joueur:{self.pointage_joueur}", 100, 50, arcade.color.LIGHT_BLUE, 20)
        self.score2 = arcade.Text(f"pointage de l'ordinateur:{self.pointage_bot}", 500, 50, arcade.color.LIGHT_BLUE, 20)
        self.win_lose = arcade.Text("", 250, 450, arcade.color.LIGHT_BLUE, 20)

        self.player = arcade.Sprite("assets/faceBeard.png", 0.4, 200, 300)
        self.compy = arcade.Sprite("assets/compy.png", 2, 600, 300)
        self.static_list = arcade.SpriteList()
        self.static_list.append(self.player)
        self.static_list.append(self.compy)

        self.square_list = [[30, 130, 100, 200], [160, 260, 100, 200], [290, 390, 100, 200], [550, 650, 100, 200]]

        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.cissors = AttackAnimation(AttackType.CISSORS)
        self.rock_list = arcade.SpriteList()
        self.paper_list = arcade.SpriteList()
        self.cissors_list = arcade.SpriteList()
        self.rock_list.append(self.rock)
        self.paper_list.append(self.paper)
        self.cissors_list.append(self.cissors)

        self.d_rock = True
        self.d_paper = True
        self.d_cissors = True

        self.compy_move = None

    def on_draw(self):
        self.clear()

        for i in self.square_list:
            arcade.draw_lrbt_rectangle_outline(i[0], i[1], i[2], i[3], arcade.color.REDWOOD)

        if self.state == GameState.NOT_STARTED:
            self.appuyer.text = "Appuyer sur 'Espace' pour commencer un nouveau round!"
        elif self.state == GameState.ROUND_ACTIVE:
            self.appuyer.text = "Appuyer sur une image pour faire une attack!"
        elif self.state == GameState.ROUND_DONE:
            self.appuyer.text = "Appuyer sur 'Espace' pour commencer un nouveau round!"
        else:
            pass

        self.classic_object()
        self.compy_move_draw()

    def on_update(self, delta_time):
        self.rock.on_update(delta_time)
        self.paper.on_update(delta_time)
        self.cissors.on_update(delta_time)

        if self.state == GameState.ROUND_ACTIVE:
            if not self.d_rock or not self.d_paper or not self.d_cissors:

                compy_move_list = ["rock", "paper", "cissors"]
                self.compy_move = random.choice(compy_move_list)

                if self.d_rock and self.compy_move == "cissors" or self.d_paper and self.compy_move == "rock" or self.d_cissors and self.compy_move == "paper":
                    self.win_lose.text = "Vous avez gagner le round!"
                    self.pointage_joueur += 1
                elif self.d_rock and self.compy_move == "paper" or self.d_paper and self.compy_move == "cissors" or self.d_cissors and self.compy_move == "rock":
                    self.win_lose.text = "compy a gagner le round!"
                    self.pointage_bot += 1
                else:
                    self.win_lose.text = "égalité"

                self.score1.text = f"pointage du joueur:{self.pointage_joueur}"
                self.score2.text = f"pointage de l'ordinateur:{self.pointage_bot}"

                self.state = GameState.ROUND_DONE

        elif self.state == GameState.GAME_OVER:
            if self.pointage_joueur == 3:
                self.win_lose.text = "Vous avez gagner la partie"
            else:
                self.win_lose.text = "Compy a gagner la partie"

            self.appuyer.text = "Appuyer sur 'Espace' pour commencer une nouvelle partie!"

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == GameState.NOT_STARTED:
            self.state = GameState.ROUND_ACTIVE
        elif key == arcade.key.SPACE and self.state == GameState.ROUND_DONE:
            if self.pointage_joueur == 3 or self.pointage_bot == 3:
                self.state = GameState.GAME_OVER
            else:
                self.d_rock = True
                self.d_paper = True
                self.d_cissors = True
                self.win_lose.text = ""
                self.compy_move = None
                self.state = GameState.ROUND_ACTIVE
        elif key == arcade.key.SPACE and self.state == GameState.GAME_OVER:
            self.pointage_joueur = 0
            self.pointage_bot = 0
            self.d_rock = True
            self.d_paper = True
            self.d_cissors = True
            self.win_lose.text = ""
            self.compy_move = None

            self.score1.text = f"pointage du joueur:{self.pointage_joueur}"
            self.score2.text = f"pointage de l'ordinateur:{self.pointage_bot}"

            self.state = GameState.ROUND_ACTIVE


    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.state == GameState.ROUND_ACTIVE:
            if self.rock.collides_with_point((x, y)):
                self.d_paper = False
                self.d_cissors = False
            elif self.paper.collides_with_point((x, y)):
                self.d_rock = False
                self.d_cissors = False
            elif self.cissors.collides_with_point((x, y)):
                self.d_rock = False
                self.d_paper = False

    def classic_object(self):
        self.rpc.draw()
        self.static_list.draw()
        self.score1.draw()
        self.score2.draw()
        self.appuyer.draw()
        self.win_lose.draw()

        self.rock.center_x = 80
        self.rock.center_y = 150

        self.paper.center_x = 210
        self.paper.center_y = 150

        self.cissors.center_x = 340
        self.cissors.center_y = 150

        if self.d_rock:
            self.rock_list.draw()
        if self.d_paper:
            self.paper_list.draw()
        if self.d_cissors:
            self.cissors_list.draw()

    def compy_move_draw(self):
        if self.compy_move == "rock":
            self.rock.center_x = 600
            self.rock.center_y = 150
            self.rock_list.draw()
        elif self.compy_move == "paper":
            self.paper.center_x = 600
            self.paper.center_y = 150
            self.paper_list.draw()
        elif self.compy_move == "cissors":
            self.cissors.center_x = 600
            self.cissors.center_y = 150
            self.cissors_list.draw()



def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()