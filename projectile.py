import pyglet
import pymunk
from math import degrees
from constants import Color
from constants import Coll_Type
from constants import Direction
from global_vars import barrel_batch
from global_vars import fg_batch
from global_vars import space
from global_vars import barrel_group
from enum import IntEnum

class Projectile:
    class Ammo_Type(IntEnum):
        REGULAR = 1
        AP = 2
    SCALE = 0.65
    HEIGHT = 34 * SCALE
    WIDTH = 20 * SCALE
    def __init__(self, pos = (0,0), color=Color.RED, idn=0, src_idn = 0, type=Ammo_Type.REGULAR):
        self.idn = idn
        self.src_idn = src_idn
        self.type = type
        self.damage = 10
        self.velocity = 1000
        img = None
        if self.type == Projectile.Ammo_Type.REGULAR:
            img = pyglet.image.load("res/PNG/Bullets/bullet%s_outline.png" % color.value)
        elif self.type == Projectile.Ammo_Type.AP:
            img = pyglet.image.load("res/PNG/Bullets/bullet%sSilver_outline.png" % color.value)
            self.damage = 100
            self.velocity = 1500
        img.anchor_x = img.width // 2 
        img.anchor_y = img.height // 2 
        self.sprite = pyglet.sprite.Sprite(img, x = pos[0], y = pos[1], batch = fg_batch, group=barrel_group)
        self.sprite.scale = Projectile.SCALE
        self.poly = pymunk.Poly.create_box(None, size=(Projectile.HEIGHT,Projectile.WIDTH))
        self.poly.collision_type = Coll_Type.PROJECTILE
        self.poly.idn = self.idn
        self.moment = pymunk.moment_for_poly(25, self.poly.get_vertices())
        self.body = pymunk.Body(25, self.moment, pymunk.Body.DYNAMIC)
        self.poly.body = self.body
        self.body.position = pos
        space.add(self.poly, self.body)

    def update(self,dt):
        self.sprite.position = self.body.position
        self.sprite.rotation = degrees(self.body.angle)

    def destroy(self):
        self.sprite = None
        space.remove(self.poly,self.body)

    def create_from_message(message):
        idn = message.id.value
        src_id = message.src_id.value
        position = message.pos_x.value, message.pos_y.value
        rotation = message.rot.value
        projectile_type = message.type.value
        color = Color.from_int[message.color.value]
        return Projectile(position, color, idn, src_id)

    def update_from_message(self, message):
        self.body.position = message.pos_x.value, message.pos_y.value
        self.body.angle = message.rot.value