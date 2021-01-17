from survey import db
from survey.forms import SurveyForm
from survey.models import SurveyModel
from flask import Blueprint, redirect, render_template, url_for

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def render_survey():
    form = SurveyForm()
    if form.validate_on_submit():
        age_range_id = form.age_range.data
        enrollment_range_id = form.enrollment_range.data
        salary_range_id = form.salary_range.data
        reason_range_id = form.reason_range.data

        survey_item = SurveyModel(
            age_range_id=age_range_id,
            enrollment_range_id=enrollment_range_id,
            salary_range_id=salary_range_id,
            reason_range_id=reason_range_id,
        )

        db.session.add(survey_item)
        db.session.commit()
        return redirect(url_for("main.finished"))

    return render_template("survey.html", title="Pesquisa Bem Promotora", form=form)


@main.route("/thanks")
def finished():
    return render_template("thanks.html", title="Obrigado")