import bpy

'''*********************************************************************'''
'''Funciones comunes útiles para selección/activación/borrado de objetos'''
'''*********************************************************************'''
def seleccionarObjeto(nombreObjeto): # Seleccionar un objeto por su nombre
    bpy.ops.object.select_all(action='DESELECT') # deseleccionamos todos...
    bpy.ops.object.select_pattern(pattern=nombreObjeto,case_sensitive= True, extend=True) # ...excepto el buscado

def activarObjeto(nombreObjeto): # Activar un objeto por su nombre
    bpy.context.scene.objects.active = bpy.data.objects[nombreObjeto]

def borrarObjeto(nombreObjeto): # Borrar un objeto por su nombre
    seleccionarObjeto(nombreObjeto)
    bpy.ops.object.delete(use_global=False)

def borrarObjetos(): # Borrar todos los objetos
    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

'''****************************************************************'''
'''Clase para realizar transformaciones sobre objetos seleccionados'''
'''****************************************************************'''
class Seleccionado:
    def mover(v):
        bpy.ops.transform.translate(
            value=v, constraint_axis=(True, True, True))

    def escalar(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))

    def rotarX(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')

    def rotarY(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')

    def rotarZ(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')

'''**********************************************************'''
'''Clase para realizar transformaciones sobre objetos activos'''
'''**********************************************************'''
class Activo:
    def posicionar(v):
        bpy.context.object.location = v

    def escalar(v):
        bpy.context.object.scale = v

    def rotar(v):
        bpy.context.object.rotation_euler = v

    def renombrar(nombreObjeto):
        bpy.context.object.name = nombreObjeto

'''**************************************************************'''
'''Clase para realizar transformaciones sobre objetos específicos'''
'''**************************************************************'''
class Especifico:
    def escalar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].scale = v

    def posicionar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].location = v

    def rotar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].rotation_euler = v

'''************************'''
'''Clase para crear objetos'''
'''************************'''
class Objeto:
    def crearCubo(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearEsfera(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearCono(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearCilindro(objName):     
        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
        Activo.renombrar(objName)
        
def parte_rueda(ang,xe,ye,ze,xm,ym,zm,nombre):
    Objeto.crearCilindro(nombre)
    Seleccionado.rotarY(ang)
    Seleccionado.escalar((xe, ye, ze))
    Seleccionado.mover((xm, ym, zm))
    
def rueda(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    parte_rueda(3.14 / 2,0.03,0.4,0.4,x1,y1,z1,'Rueda1')
    parte_rueda(3.14 / 2,0.03,0.3,0.3,x2,y2,z2,'Rueda2')
    parte_rueda(3.14 / 2,0.03,0.4,0.4,x3,y3,z3,'Rueda3')
    
def eje_motriz(y):
    Objeto.crearCilindro('Eje')
    Seleccionado.escalar((0.1, 0.1, 0.1))
    Seleccionado.rotarY(3.14/2)
    Seleccionado.escalar((14.1, 1, 1))
    Seleccionado.mover((0.5, y, 0))
    
    
def soporte(x,y):
    Objeto.crearEsfera('Esfera1')
    Seleccionado.escalar((0.2, 0.2, 0.2))
    Seleccionado.mover((x, y, 0.11))
    
    Objeto.crearCubo('Cubo')
    Seleccionado.escalar((0.2, 0.2, 1))
    Seleccionado.mover((x, y, 0.3))
    
def base_robot(xe,ye,ze,xm,ym,zm):
    bpy.ops.object.metaball_add(type='CUBE', radius=1, enter_editmode=False, location=(0, 0, 0))
    Seleccionado.escalar((xe, ye, ze))
    Seleccionado.mover((xm, ym, zm))
    
def eje_robot(xe,ye,ze,xm,ym,zm,ang):
    Objeto.crearCubo('Eje')
    Seleccionado.escalar((xe,ye,ze))
    Seleccionado.mover((xm,ym,zm))
    Seleccionado.rotarX(ang)
    
def link():
    bpy.ops.object.metaball_add(type='BALL', radius=1, enter_editmode=False, location=(0, 0, 0))
    Seleccionado.escalar((0.28, 0.28, 0.28))
    Seleccionado.mover((0.5, 1, 2.35))
    

    
    
    

'''************'''
''' M  A  I  N '''
'''************'''
if __name__ == "__main__":
    borrarObjetos()
 

    rueda(1.94,0,0,2,0,0,2.05,0,0)
    rueda(-0.94,0,0,-1,0,0,-1.05,0,0)
    rueda(1.94,2,0,2,2,0,2.05,2,0)
    rueda(-0.94,2,0,-1,2,0,-1.05,2,0)
    
    eje_motriz(0)
    eje_motriz(2)
    
    soporte(-0.35,0)
    soporte(1.3,0)
    soporte(-0.35,2)
    soporte(1.3,2)
    
    base_robot(0.6, 0.6, 0.08,0.5, 1, 0.65)
    base_robot(0.3, 0.3, 0.06,0.5, 1, 0.93)
    
    eje_robot(0.8, 0.8, 2.8,0.5, 1, 1.75,0)
    link()
    eje_robot(0.7, 0.7, 2.8,0.5, 1.6, 2.8,3.14/3)
    
    
    
    eje_robot(1.6, 0.3, 0.2,0.5, 2, 3,3.14/3)
    eje_robot(0.18, 0.18, 1.6,0.8, 2.4, 3.22,3.14/3)
    eje_robot(0.18, 0.18, 1.6,0.2, 2.4, 3.22,3.14/3)
    eje_robot(1.6, 0.3, 0.2,0.5, 2, 3,3.14)
    Seleccionado.rotarY(3.14/2)
    Seleccionado.rotarZ(3.14/2)
    Seleccionado.rotarX(-3.14/6)
    
    eje_robot(0.18, 0.18, 1.6,0.5, 2.2, 3.46,3.14/3)
    eje_robot(0.18, 0.18, 1.6,0.5, 2.5, 3,3.14/3)
    
    seleccionarObjeto('Rueda1.001')
    #seleccionarObjeto('Rueda2.001')
    #bpy.ops.object.join()
    
 

    
 
    
    
   


