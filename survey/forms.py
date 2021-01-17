from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField


class SurveyForm(FlaskForm):
    age_range = RadioField(
        "Qual sua faixa de Idade",
        choices=[
            ("1", "Até 30 Anos"),
            ("2", "De 30 a 50 anos"),
            ("3", "De 50 a 65 anos"),
            ("4", "Acima de 65 anos"),
        ],
    )
    enrollment_range = RadioField(
        "Qual seu convênio",
        choices=[
            ("1", "INSS"),
            ("2", "SIAPE"),
            ("3", "Forças Armadas"),
            ("4", "Outros"),
        ],
    )
    salary_range = RadioField(
        "Qual sua faixa salarial",
        choices=[
            ("1", "Até 2 SM"),
            ("2", "De 2 a 4 SM"),
            ("3", "De 4 a 6 SM"),
            ("4", "Acima de 6 SM"),
        ],
    )
    reason_range = RadioField(
        "Por que você realizou o empréstimo",
        choices=[
            ("1", "Pagar contas"),
            ("2", "Reforma da Casa"),
            ("3", "Compra de Carro"),
            ("4", "Outras"),
        ],
    )

    submit = SubmitField("Update")
