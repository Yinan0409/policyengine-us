from openfisca_core.model_api import *
from openfisca_us.entities import *
from openfisca_us.tools.general import *


class snap(Variable):
    value_type = float
    entity = SPMUnit
    label = u"Supplemental Nutrition Assistance Program, benefit amount"
    definition_period = YEAR

    def formula(spm_unit, period, parameters):

        # Params:
        # Income Threshold
        # Max Benefit
        # Phase-out Rate
        # for later, Employment Rules

        # Get vars:
        # net income
        # gross income
        # number of individuals

        # for later, Employment Status

        return standard


class expected_food_contribution(Variable):
    value_type = float
    entity = SPMUnit
    label = u"Supplemental Nutrition Assistance Program, spm unit's expected food contribution"
    definition_period = YEAR

    def formula(spm_unit, period, parameters):

        # Params:
        # Income Threshold
        # Max Benefit
        # Phase-out Rate
        # for later, Employment Rules

        # Get vars:
        # net income
        # gross income
        # number of individuals

        # for later, Employment Status

        return standard
