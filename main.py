import arcade

from game_state import GameState

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.clear()
        arcade.set_background_color(arcade.color.GRAY)

        self.state = None
        self.rpc = None
        self.appuyer = None
        self.player = None

        """
        self.player_attack_type = {
            AttackType.ROCK: False,
            AttackType.PAPER: False,
            AttackType.SCISSORS: False
        }
        """

    def setup(self):
        self.state = GameState.NOT_STARTED

        self.player = arcade.Sprite("assets/assets/faceBeard.png", 1, 100, 100)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.GRAY)

        arcade.draw_text("Roche, Papier, ciseaux", 100, 550, arcade.color.RED_DEVIL, 50)
        self.player.draw()

        if self.state == GameState.NOT_STARTED:
            arcade.draw_text("Appuyer sur 'Espace' pour commencer un nouveau round!", 100, 500, arcade.color.LIGHT_BLUE, 20)
        elif self.state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Appuyer sur une image pour faire une attack!", 200, 500, arcade.color.LIGHT_BLUE, 20)
        elif self.state == GameState.ROUND_DONE:
            arcade.draw_text("Appuyer sur 'Espace' pour commencer un nouveau round!", 100, 500, arcade.color.LIGHT_BLUE, 20)
        else:
            pass

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
