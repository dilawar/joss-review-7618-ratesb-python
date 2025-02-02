from ratesb_python import check_model

# Load custom rate law checks
custom_rate_law_file = "custom_rate_law.json"
print(check_model("S1->P1; k1 * S1", custom_rate_law_file))

from ratesb_python import Analyzer

# Load custom rate law checks
custom_rate_law_file = "custom_rate_law.json"
analyzer = Analyzer("S1->P1; k1 * S1", custom_rate_law_file)

# Analyze the model for rate law correctness
analyzer.check_all()
print(analyzer.results)
