from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, FloatField, SelectField, SubmitField


class ConfigForm(FlaskForm):
    SUBSTRATE_TYPE = SelectField('Substrate Type', choices=[('CONTINUOUS_GRADIENTS', 'Continuous Gradients'),
                                                            ('WEDGES', 'Wedges'), ('STRIPE', 'Stripe'), ('GAP', 'Gap')])
    ROWS = IntegerField('Rows', default=100)
    COLS = IntegerField('Cols', default=100)
    GC_COUNT = IntegerField('Growth Cone Count', default=20)
    GC_SIZE = IntegerField('Growth Cone Size', default=5)
    STEP_SIZE = IntegerField('Step Size', default=1)
    STEP_AMOUNT = IntegerField('Step Amount', default=16000)
    X_STEP_POSSIBILITY = FloatField('X Step Possibility', default=0.55)
    Y_STEP_POSSIBILITY = FloatField('Y Step Possibility', default=0.50)
    SIGMOID_GAIN = FloatField('Sigmoid Gain', default=8)
    SIGMOID_SHIFT = FloatField('Sigmoid Shift', default=-4)
    SIGMA = FloatField('Sigma', default=0.12)
    FORCE = BooleanField('Force', default=False)
    FORWARD_SIG = BooleanField('Forward Signal', default=True)
    REVERSE_SIG = BooleanField('Reverse Signal', default=True)
    FF_INTER = BooleanField('Fiber-Fiber Interaction', default=True)
    FT_INTER = BooleanField('Fiber-Target Interaction', default=True)
    ADAPTATION_ENABLED = BooleanField('Adaptation Enabled', default=True)
    ADAPTATION_MU = FloatField('Adaptation Mu', default=0.006)
    ADAPTATION_LAMBDA = FloatField('Adaptation Lambda', default=0.0045)
    ADAPTATION_HISTORY = IntegerField('Adaptation History', default=50)
    submit = SubmitField('Save Configuration')
