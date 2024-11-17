from django.contrib import admin

# Register your models here.

from .models import Usuarios
admin.site.register(Usuarios)

from .models import Proveedores
admin.site.register(Proveedores)

from .models import Productos
admin.site.register(Productos)

from .models import Comentarios
admin.site.register(Comentarios)

from .models import Categorias
admin.site.register(Categorias)

from .models import Boleta
admin.site.register(Boleta)

from .models import Descuentos
admin.site.register(Descuentos)

from .models import Envios
admin.site.register(Envios)

from .models import Pedido
admin.site.register(Pedido)

from .models import PedidoDetalle
admin.site.register(PedidoDetalle)

