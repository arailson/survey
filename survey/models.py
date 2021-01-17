from survey import db


class SurveyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_range_id = db.Column(db.Integer, nullable=False)
    enrollment_range_id = db.Column(db.Integer, nullable=False)
    salary_range_id = db.Column(db.Integer, nullable=False)
    reason_range_id = db.Column(db.Integer, nullable=False)
