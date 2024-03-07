hari_kerja = 14 

hari_kerja_perbulan  = 16 

gaji = 3000000 

total_gaji = (hari_kerja / hari_kerja_perbulan) * gaji

formatted_total_gaji = "{:,.2f}".format(total_gaji).rstrip('0').rstrip('.')

print(formatted_total_gaji)
