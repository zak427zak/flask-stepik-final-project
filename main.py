from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap

from config import Config
from forms import MoveForm, InitGameWorldForm
from logic import Adventure

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)


# Стартовый экран игры. Здесь происходит инициализация логики приключения (класс Adventure)
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    init_form = InitGameWorldForm()
    if init_form.validate_on_submit() and init_form.submit_init.data:
        Adventure(int(init_form.width.data), int(init_form.height.data), init_form.is_step_counter_on.data)
        return redirect(url_for('adventure'))
    return render_template("index.html", form=init_form)


# Перезапуск приключения (выбранные при инициализации ширина и высота сохраняться)
@app.route("/rerun/<int:width>/<int:height>", methods=["GET"])
def rerun(width, height):
    Adventure(width, height)
    return redirect(url_for('adventure'))


# "Шаг" в приключении и вытекающая из него логика
@app.route("/adventure", methods=["GET", "POST"])
def adventure():
    move_form = MoveForm()
    current_adventure = Adventure()

    if move_form.validate_on_submit() and move_form.submit_move.data:
        answer = current_adventure.make_step(int(move_form.number_steps.data), int(move_form.way.data))
        flash(answer[0])
        return render_template("adventure.html", move_form=move_form, current_adventure=current_adventure,
                               alert_type=answer[1])
    else:
        flash(f'Вчерашний поход к барону явно удался. Сейчас вы в пыльной непонятной комнате '
              f'{current_adventure.current_position[0]}-{current_adventure.current_position[1]}, '
              f'и ваше самочувствие оставляет желать лучшего.\nВы чувствуете, что вам необходимо попасть в комнату '
              f'{current_adventure.final_position[0]}-{current_adventure.final_position[1]}')
        return render_template("adventure.html", move_form=move_form, current_adventure=current_adventure,
                               alert_type="info")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
