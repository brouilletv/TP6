import arcade

from game_state import GameState

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

        self.player = None
        self.compy = None
        self.static_list = None

        self.square_list = None

        self.rock = None
        self.paper = None
        self.cissors = None
        self.move_list = None

        """
        self.player_attack_type = {
            AttackType.ROCK: False,
            AttackType.PAPER: False,
            AttackType.SCISSORS: False
        }
        """

    def setup(self):
        self.state = GameState.NOT_STARTED

        self.rpc = arcade.Text("Roche, Papier, ciseaux", 100, 550, arcade.color.RED_DEVIL, 50)
        self.appuyer = arcade.Text(" ", 100, 500, arcade.color.LIGHT_BLUE, 20)
        self.score1 = arcade.Text("pointage du joueur", 100, 500, arcade.color.LIGHT_BLUE, 20)
        self.score2 = arcade.Text("pointage de l'ordinateur", 100, 500, arcade.color.LIGHT_BLUE, 20)

        self.player = arcade.Sprite("assets/assets/faceBeard.png", 0.4, 200, 300)
        self.compy = arcade.Sprite("assets/assets/compy.png", 2, 600, 300)
        self.static_list = arcade.SpriteList()
        self.static_list.append(self.player)
        self.static_list.append(self.compy)

        self.square_list = [[30, 130, 100, 200], [160, 260, 100, 200], [290, 390, 100, 200], [550, 650, 100, 200]]

        self.rock = arcade.Sprite("assets/assets/srock.png", 0.6, 80, 150)
        self.paper = arcade.Sprite("assets/assets/spaper.png", 0.6, 210, 150)
        self.cissors = arcade.Sprite("assets/assets/scissors.png", 0.6, 340, 150)
        self.move_list = arcade.SpriteList()
        self.move_list.append(self.rock)
        self.move_list.append(self.paper)
        self.move_list.append(self.cissors)

    def on_draw(self):
        self.clear()

        self.rpc.draw()
        self.static_list.draw()
        self.score1.draw()
        self.score2.draw()

        for i in self.square_list:
            arcade.draw_lrbt_rectangle_outline(i[0], i[1], i[2], i[3], arcade.color.REDWOOD)

        if self.state == GameState.NOT_STARTED:
            self.appuyer.text = "Appuyer sur 'Espace' pour commencer un nouveau round!"
        elif self.state == GameState.ROUND_ACTIVE:
            self.appuyer.text = "Appuyer sur une image pour faire une attack!"
            self.move_list.draw()
        elif self.state == GameState.ROUND_DONE:
            self.appuyer.text = "Appuyer sur 'Espace' pour commencer un nouveau round!"
        else:
            pass
        self.appuyer.draw()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.state == GameState.NOT_STARTED:
            self.state = GameState.ROUND_ACTIVE


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()