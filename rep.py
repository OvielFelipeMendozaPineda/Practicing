totalFacturaSinIva = float(input("Ingrese el valor de la factura sin iva.\n"))
iva = float(input("Ingrese el iva a aplicar\n"))
def ivaAplicator():
  if iva != 0:
    totalFacturaConIva = totalFacturaSinIva + (totalFacturaSinIva * iva/100)
  else:
     totalFacturaConIva = totalFacturaSinIva + (totalFacturaSinIva * 21/100) 
  return totalFacturaConIva, False
print(f'el valor de la factura despues del iva es {ivaAplicator()}')

