
def update_libro_stock(sender, instance, **kwargs):
    ''' actualizador de stock, si se elimina un prestamo '''

    instance.libro.stock += 1
    instance.libro.save()
    