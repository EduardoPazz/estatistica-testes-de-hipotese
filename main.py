from PDFQuestion import pdf_list
from expected_value import expected_value
from variance import variance
# print(*pdf_list, sep="\n")

total_expected_value = 0.0
total_variance = 0.0

for pdf in pdf_list:
    total_expected_value += expected_value({0, 1}, pdf.apply, 2)
    total_variance += variance({0, 1}, pdf.apply, 2)

print("\nTotal:", total_expected_value, total_variance)
    
