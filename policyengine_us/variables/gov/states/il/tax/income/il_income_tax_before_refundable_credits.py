from policyengine_us.model_api import *


class il_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "IL income tax before nonrefundable credits"
    unit = USD
    definition_period = YEAR

    defined_for = StateCode.IL

    def formula(tax_unit, period, parameters):
        taxbc = tax_unit("il_income_tax_before_nonrefundable_credits", period)
        non_refundable_credits = tax_unit("il_nonrefundable_credits", period)
        return max_(taxbc - non_refundable_credits, 0)
